from Crawler import Crawler
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class Dell_Perser(Crawler):
    def __init__(self):
        super().__init__()
        self.pc_class_list = list()
        self.pc_href_list = list()

    def get_pc_data(self, name_id):
        self.name_id = name_id
        self.search_data()
        # リストに保存
        for self.pc in range(len(self.pc_names)):
            self.get_pc_class()
            self.get_pc_href()
    
    def search_data(self):
        WebDriverWait(self.browser, 20).until(EC.presence_of_element_located((By.ID, f"{self.name_id}")))
        self.pc_type = self.browser.find_element(By.ID, f"{self.name_id}")
        
        # 製品名の一覧とそのリンクを一括で取得
        self.pc_names = self.pc_type.text.split("\n")
        self.pc_href = self.pc_type.find_elements(By.TAG_NAME, "a")
        
        if len(self.pc_names) == len(self.pc_href):
            self.pc_href = self.pc_href[1:]
        self.pc_names = self.pc_names[1:]
    
    def get_pc_class(self):
        """
        取得する製品名を取得
        """
        target = self.name_id.replace("0", "") + "_" + self.pc_names[self.pc].replace("ノート", "").replace("パソコン", "").replace("デスクトップ", "").replace("サーバー", "").replace("ワークステーション", "").replace("産業グレードの", "産業グレード").replace(" ", "")
        self.pc_class_list.append(target)
    
    def get_pc_href(self):
        """
        取得する製品ページへのリンクを取得
        """
        pc_url = self.pc_href[self.pc].get_attribute('href')
        self.pc_href_list.append(pc_url)
    
    def return_data(self):
        return self.pc_class_list, self.pc_href_list
    
    def prd(self):
        return self.browser.find_elements(By.CLASS_NAME, "stack-system.ps-stack")
    