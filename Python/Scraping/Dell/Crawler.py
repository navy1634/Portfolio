from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class Crawler():
    def __init__(self):
        options = webdriver.ChromeOptions()
        # コメントアウトをすると、ブラウザが立ち上がる
        options.add_argument('--headless')
        self.browser = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    
    def page_change(self, url):
        """
        ページ遷移用の関数
        """
        self.browser.get(url)
    
    def Close(self):
        """
        ブラウザを閉じる関数
        最後に絶対に実行すること
        """
        self.browser.close()
        self.browser.quit()


    def get_next_page(self):
        """
        ページ内の項目の移動に用いる
        """
        # 次のページへ
        next_page = self.browser.find_elements(By.CLASS_NAME, "system-result-btn.page.pagination-btn.prev-next-btn")

        # 次のぺージが無い場合
        if next_page == []:
            return False
        if next_page[1].get_attribute('data-disabled') == "True":
            return False
        next_page[1].click()
        return True
        