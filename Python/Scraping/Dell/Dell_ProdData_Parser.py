from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from datetime import date
from Crawler import Crawler
import pandas as pd

class Dell_Index_Perser(Crawler):
    def __init__(self):
        self.pc_data_list = list()
    
    def set_target(self, target):
        self.target = target

    def get_pc_data(self, prod) -> list:
        self.prod = prod
        # target : {PCの種類}_{製品の種類}
        # 例     : Laptops_Alienware
        pc_data = self.target.split("_")
        pc_name = self.get_PC_name()
        pc_data.append(pc_name)
        pc_price = self.get_PC_price()
        pc_data.append(pc_price)
        pc_pros = self.get_PC_pros()
        pc_data.append(pc_pros)
        pc_os = self.get_PC_os()
        pc_data.append(pc_os)
        pc_gpu = self.get_PC_gpu()
        pc_data.append(pc_gpu)
        pc_mem = self.get_PC_mem()
        pc_data.append(pc_mem)
        pc_hdd = self.get_PC_hdd()
        pc_data.append(pc_hdd)
        pc_camp = self.get_PC_camp()
        pc_data.extend(pc_camp)
        self.pc_data_list.append(pc_data)

    def get_PC_name(self):
        """
        製品名
        """
        WebDriverWait(self.prod, 20).until(EC.presence_of_element_located((By.CLASS_NAME, "ps-title")))
        pc_name = self.prod.find_element(By.CLASS_NAME, "ps-title")
        if pc_name != None:
            return pc_name.text.replace("\n", "")
        return "-"

    def get_PC_price(self):
        """
        価格情報
        """
        WebDriverWait(self.prod, 20).until(EC.presence_of_element_located((By.CLASS_NAME, "ps-dell-price.ps-simplified")))
        pc_price = self.prod.find_element(By.CLASS_NAME, "ps-dell-price.ps-simplified")
        if pc_price != None:
            return pc_price.text.replace("\n", "").replace("販売価格", "")
        return "-"

    def get_PC_pros(self):
        """
        CPU, プロセッサ
        """
        WebDriverWait(self.prod, 20).until(EC.presence_of_element_located((By.CLASS_NAME, "short-specs.ps-dds-font-icon.dds_processor")))
        pc_pros = self.prod.find_element(By.CLASS_NAME, "short-specs.ps-dds-font-icon.dds_processor")
        if pc_pros != None:
            return pc_pros.text.replace("\n", "").replace(" ", "")
        return "-"

    def get_PC_os(self):
        """
        OS, Windows
        """
        WebDriverWait(self.prod, 20).until(EC.presence_of_element_located((By.CLASS_NAME, "short-specs.ps-dds-font-icon.dds_disc-system")))
        pc_win = self.prod.find_element(By.CLASS_NAME, "short-specs.ps-dds-font-icon.dds_disc-system")
        if pc_win != None:
            return pc_win.text.replace("\n", "").replace(" ", "")
        return "-"

    def get_PC_gpu(self):
        """
        GPU, グラフィックボード
        """
        WebDriverWait(self.prod, 20).until(EC.presence_of_element_located((By.CLASS_NAME, "short-specs.ps-dds-font-icon.dds_video-card")))
        pc_gpu = self.prod.find_element(By.CLASS_NAME, "short-specs.ps-dds-font-icon.dds_video-card")
        if pc_gpu != None:
            return pc_gpu.text.replace("\n", "").replace(" ", "")
        return "-"

    def get_PC_mem(self):
        """
        メモリ
        """
        WebDriverWait(self.prod, 20).until(EC.presence_of_element_located((By.CLASS_NAME, "short-specs.ps-dds-font-icon.dds_memory")))
        pc_mem = self.prod.find_element(By.CLASS_NAME, "short-specs.ps-dds-font-icon.dds_memory")
        if pc_mem != None:
            return pc_mem.text.replace("\n", "").replace(" ", "")
        return "-"

    def get_PC_hdd(self):
        """
        SSD / HDD
        """
        WebDriverWait(self.prod, 20).until(EC.presence_of_element_located((By.CLASS_NAME, "short-specs.ps-dds-font-icon.dds_hard-drive")))
        pc_hdd = self.prod.find_element(By.CLASS_NAME, "short-specs.ps-dds-font-icon.dds_hard-drive")
        if pc_hdd != None:
            return pc_hdd.text.replace("\n", "").replace(" ", "")
        return "-"

    def get_PC_camp(self):
        """
        クーポン等キャンペーン
        """
        camp_list = list()
        pc_camp = self.prod.find_elements(By.CLASS_NAME, "ps-special-offers-expanded-link")
        for i in range(len(pc_camp)):
            camp_list.append(pc_camp[i].text.replace("\n", "").replace(" ", "").replace("\u200b", ""))
        while len(camp_list)!=2:
            camp_list.append("-")
        return camp_list[:2]

    def return_pc(self):
        """
        取得したデータをリストとして出力
        """
        return self.pc_data_list

    def save_csv(self):
        """
        取得結果を csv に保存
        """
        today = date.today()
        df_pc = pd.DataFrame(self.pc_data_list, columns=["分類", "種類", "品名", "販売価格", "CPU", "OS", "GPU", "RAM", "SSD/HDD", "クーポン1", "クーポン2"])
        df_pc.to_csv(f"Dell_PC_{today}.csv", encoding="utf-8", index=False)
    