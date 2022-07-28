from datetime import date
import pandas as pd
from Parser import Dell_Perser
from Dell_ProdData_Parser import Dell_Index_Perser

def main():
    prod_type_name_id = ["Laptops0", "Desktops0", "gaming", "Workstations0", "Servers0"]
    url = "https://www.dell.com/ja-jp/shop?~ck=bt"

    print("【 ブラウザの立ち上げ 】\n")
    browser = Dell_Perser()
    browser.page_change(url)
    for name_id in prod_type_name_id:
        browser.get_pc_data(name_id)

    pc_class_list, pc_href_list = browser.return_data()

    pc_data = Dell_Index_Perser()
    print("【 取得開始 】\n")

    for i in range(len(pc_href_list)):
        target = pc_class_list[i]
        browser.page_change(pc_href_list[i])
        print("\n～ " + target + " ～")
        pc_data.set_target(target)

        k = 1
        while True:
            print(f"{k}ページ目")
            pc_prod = browser.prd()
            for prod in pc_prod:
                pc_data.get_pc_data(prod)
            
            next_page = browser.get_next_page()
            if next_page == False:
                break
            k += 1

    print("\n【 取得完了 】\n")
    pc_data.save_csv()
    print("\n【 データの保存 】\n")
    browser.Close()
    print("\n【 終了 】\n")

if __name__ == "__main__":
    main()
