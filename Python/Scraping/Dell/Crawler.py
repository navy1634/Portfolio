from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

class Crawler():
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        self.browser = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    
    def page_change(self, url):
        self.browser.get(url)
    
    def Close(self):
        self.browser.close()
        self.browser.quit()


    def get_next_page(self):
        # 次のページへ
        next_page = self.browser.find_elements(By.CLASS_NAME, "system-result-btn.page.pagination-btn.prev-next-btn")

        # 次のぺージが無い場合
        if next_page == []:
            return False
        if next_page[1].get_attribute('data-disabled') == "True":
            return False
        next_page[1].click()
        return True
        