from pprint import pprint
from datetime import date
import pandas as pd
import re
from time import sleep
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

# 名前、別名、図鑑番号、高さ、重さ
def get_pk_nomal_data(data):
    del_list = list()
    for d in data:
        k = re.search(r'(ガラル|ヨロイ島|カンムリ|アローラ)No\.\w*', d)
        if k:
            del_list.append(d)
        if d == "":
            data.remove(d)

    for d in del_list:
        data.remove(d)

    return [data[0], data[1], data[2].replace("全国", "").replace("ぜんこく", "").replace(" ", ""), data[3].replace("高さ ", ""), data[5]]

# タイプ
def get_type(browser):
    typea = browser.find_element(By.CLASS_NAME, "type")
    typeb = typea.find_elements(By.TAG_NAME, "img")
    type_list = list()
    for t in typeb:
        ty = t.get_attribute("alt")
        type_list.append(ty)
    
    if len(type_list) == 1:
        type_list.append("-")
    return type_list

def data_split(data):
    return data.split("  ")[1].split("(")[0]

def del_friend(data):
    for d in data:
        if re.match(r'仲間呼びやすさ\w*', d):
            data.remove(d)
    return data

# タマゴグループ
def get_egg(data):
    egg_data = data[32].replace("タマゴグループ ", "").split(" / ")
    if len(egg_data) == 1:
        egg_data.append("-")
    return egg_data

def char_split(data):
    return data.split(" ")[0].replace("*", "")

# 特性
def get_char(data):
    data = data[1:]
    index = data.index("◆")
    data1 = data[:index]
    data2 = data[index+1]

    if len(data1) == 1:
        data1.append("-")
    if data2 == "なし":
        data2 = "-"
    return data1 + [data2]

# 世代
def get_gene(num):
    num = int(num.split(".")[1])
    if num <= 151:
        return 1
    elif num <= 251:
        return 2
    elif num <= 386:
        return 3
    elif num <= 493:
        return 4
    elif num <= 649:
        return 5
    elif num <= 721:
        return 6
    elif num <= 809:
        return 7
    else:
        return 8

def get_Pokemon(browser):
    pk_data_all = list()
    df_char_list = list()
    # 名前・別名・タイプ
    WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.ID, "base_anchor")))
    pk_data1 = browser.find_element(By.ID, "base_anchor")
    pk_data1 = pk_data1.text.split("\n")
    nomal_data = get_pk_nomal_data(pk_data1)
    type_data = get_type(browser)

    # 種族値・タマゴグループ・特性
    WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.ID, "stats_anchor")))
    pk_data2 = browser.find_element(By.ID, "stats_anchor")
    pk_data2 = pk_data2.text.split("\n")
    pk_data2 = del_friend(pk_data2)

    Race_value = list(map(data_split, pk_data2[1:8]))
    Race_value[6] = Race_value[6].split(" / ")[1]
    Egg_type = get_egg(pk_data2)
    char_list = list(map(char_split, pk_data2[33:39]))
    char_list = get_char(char_list)

    df_char = list(map(lambda x: x.replace("*", "").split(" "), pk_data2[33:39]))
    df_char_list.append(df_char[1])
    df_char_list.append(df_char[3])

    sleep(1)
    pk_data_all.extend(nomal_data)
    pk_data_all.extend(type_data)
    pk_data_all.extend(Race_value)
    pk_data_all.extend(Egg_type)
    pk_data_all.extend(char_list)
    pk_data_all.append(get_gene(nomal_data[2]))

    return pk_data_all, df_char_list


options = webdriver.ChromeOptions()
options.add_argument('--headless')

columns = ["名前", "別名", "図鑑番号", "高さ", "重さ", "タイプ1", "タイプ2",  "H", "A", "B", "C", "D", "S", "合計値", "タマゴ1", "タマゴ2", "特性1", "特性2", "夢特性", "世代"]
Pokemon_Picture_book = list()
df_char_list = list()
error_list = list()

# ブラウザの立ち上げ
browser = webdriver.Chrome(ChromeDriverManager().install(), options=options)

for i in range(807):
    try:
        print(i+1, "匹目")
        sleep(1)
        url = f"https://yakkun.com/sm/zukan/n{i+1}"
        browser.get(url)
        sleep(1)
        pk_data_all = get_Pokemon(browser)[0]
        df_char_list.extend(get_Pokemon(browser)[1])
        Pokemon_Picture_book.append(pk_data_all)
    except:
        error_list.append(i+1)


for i in range(807, 898):
    try:
        print(i+1, "匹目")
        sleep(1)
        url = f"https://yakkun.com/swsh/zukan/n{i+1}"
        browser.get(url)
        sleep(1)
        pk_data_all = get_Pokemon(browser)[0]
        df_char_list.extend(get_Pokemon(browser)[1])
        Pokemon_Picture_book.append(pk_data_all)
    except:
        error_list.append(i+1)

browser.quit()


df_pokemon = pd.DataFrame(Pokemon_Picture_book, columns=columns)
df_pokemon = df_pokemon.set_index("図鑑番号")
df_pokemon = df_pokemon[["名前", "別名", "世代", "タイプ1", "タイプ2", "特性1", "特性2", "夢特性", "H", "A", "B", "C", "D", "S", "合計値", "高さ", "重さ", "タマゴ1", "タマゴ2"]]
df_pokemon.to_csv("pokemon_picturebook.csv", encoding="cp932")

df_char_list_ = pd.DataFrame(df_char_list)
df_char_list_ = df_char_list_.rename(columns={0: "特性", 1: "効果"})
df_char_list_ = df_char_list_[(df_char_list_["特性"]!="◆")&(df_char_list_["特性"]!="なし")].sort_values("特性", ascending=True)
df_char_all = df_char_list_[["特性", "効果"]][~df_char_list_[["特性", "効果"]].duplicated()].reset_index(drop=True)
df_char_all.to_csv("pokemon_character.csv", encoding="cp932")
