from datetime import date
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


options = webdriver.ChromeOptions()
options.add_argument('--headless')

pc_dict = {"デスクトップパソコン": "Desktop", "ノートパソコンと2-in-1 PC": "Laptop", "ゲーミングデスクトップ": "Gaming Desktop", "ゲーミングノート": "Gaming Laptop", "モニター・アクセサリー・その他周辺機器": "Peripheral"}
today = date.today()
today = str(today)


def get_pc_data(pc_prod, target):
    pc_data_list = list()

    for pc in pc_prod:
        pc_name = pc.find_element(By.CLASS_NAME, "ps-title")
        pc_price = pc.find_element(By.CLASS_NAME, "ps-dell-price.ps-simplified")
        pc_pros = pc.find_element(By.CLASS_NAME, "short-specs.ps-dds-font-icon.dds_processor")
        pc_win = pc.find_element(By.CLASS_NAME, "short-specs.ps-dds-font-icon.dds_disc-system")
        pc_gpu = pc.find_element(By.CLASS_NAME, "short-specs.ps-dds-font-icon.dds_video-card")
        pc_mem = pc.find_element(By.CLASS_NAME, "short-specs.ps-dds-font-icon.dds_memory")
        pc_hdd = pc.find_element(By.CLASS_NAME, "short-specs.ps-dds-font-icon.dds_hard-drive")
        pc_camp = pc.find_elements(By.CLASS_NAME, "ps-special-offers-expanded-link")


        # リストに保存
        pc_data = target.split("_")
        pc_data.append(pc_name.text.replace("\n", ""))
        pc_data.append(pc_price.text.replace("\n", "").replace("販売価格", ""))
        if pc_gpu != None:
            pc_data.append(pc_pros.text.replace("\n", "").replace(" ", ""))
        else:
            pc_data.append("-")

        if pc_win != None:
            pc_data.append(pc_win.text.replace("\n", "").replace(" ", ""))
        else:
            pc_data.append("-")

        if pc_gpu != None:
            pc_data.append(pc_gpu.text.replace("\n", "").replace(" ", ""))
        else:
            pc_data.append("-")

        if pc_gpu != None:
            pc_data.append(pc_mem.text.replace("\n", "").replace(" ", ""))
        else:
            pc_data.append("-")

        if pc_hdd != None:
            pc_data.append(pc_hdd.text.replace("\n", "").replace(" ", ""))
        else:
            pc_data.append("-")

        for i in range(len(pc_camp)):
            pc_data.append(pc_camp[i].text.replace("\n", "").replace(" ", "").replace("\u200b", ""))

        pc_data_list.append(pc_data)
    return pc_data_list


# ブラウザの立ち上げ
browser = webdriver.Chrome(ChromeDriverManager().install(), options=options)
url = "https://www.dell.com/ja-jp/shop?~ck=bt"
browser.get(url)

pc_class_list = list()
pc_href_list = list()

WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.CLASS_NAME, "category-text-margin.col-lg-6.col-md-6.col-sm-6")))
pc_type = browser.find_elements(By.CLASS_NAME, "category-text-margin.col-lg-6.col-md-6.col-sm-6")
for i in range(1, 6):
    # TOPよりPCの種類を取得
    WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.TAG_NAME, "h5")))
    pc_types = pc_type[i].find_element(By.TAG_NAME, "h5")
    WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.CLASS_NAME, "sub-category.unstyled")))
    pc_names = pc_type[i].find_elements(By.CLASS_NAME, "sub-category.unstyled")
    pc_name = pc_names[0].text.split("\n")

    # 各製品への遷移先のURLの取得
    pc_href = pc_names[0].find_elements(By.TAG_NAME, "a")

    pc_url_list = list()
    pc_type_list = list()

    # リストに保存
    for pc in range(len(pc_name)):
        target = pc_dict[pc_types.text] + "_" + pc_name[pc].replace("ノート・2-in-1", "")
        pc_class_list.append(target)
        pc_url = pc_href[pc].get_attribute('href')
        pc_href_list.append(pc_url)

pc_class_list = pc_class_list[:-1]
pc_href_list = pc_href_list[:-1]

print("【要素の取得中】")
pc_data_list = list()

for i in range(len(pc_href_list)):
    target = pc_class_list[i]
    browser.get(pc_href_list[i])
    print("\n～ " + target + " ～")

    k = 1
    while True:
        print(f"{k}ページ目")
        
        pc_prod = browser.find_elements(By.CLASS_NAME, "stack-system.ps-stack")
        pc_data = get_pc_data(pc_prod, target)
        pc_data_list.extend(pc_data)
        
        # 次のページへ
        next_page = browser.find_elements(By.CLASS_NAME, "system-result-btn.page.pagination-btn.prev-next-btn")

        # 次のぺージが無い場合
        if next_page == []:
            break
        if next_page[1].get_attribute('data-disabled') == "True":
            break

        next_page[1].click()
        k += 1

print("\n【取得完了】")

# ブラウザを閉じる
browser.close()

# データフレーム化してcsvに保存
df_pc = pd.DataFrame(pc_data_list, columns=["分類", "種類", "品名", "販売価格", "CPU", "OS", "GPU", "RAM", "SSD/HDD", "クーポン1", "クーポン2"])

df_pc.to_csv(f"Dell_PC_{today}.csv", encoding="utf-8", index=False)

