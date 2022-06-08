import wx
import sqlite3
import json
import pandas as pd
from Panel_Data import pk_data_Panel
from Panel_Party import pk_party_Panel
from Panel_Search import pk_Panel
from Panel_Calc import PK_calc_Panel
from Panel_Move import pk_Move_Panel
from Panel_Setting import pk_setting_Panel


class TabNote(wx.Notebook):
    def __init__(self, parent):
        super().__init__(parent, id=wx.ID_ANY, style=wx.BK_DEFAULT)
        self.get_use_data()
        self.size = wx.Size(80, 20)

        self.setting_Panel = pk_setting_Panel(self)
        self.setting = self.setting_Panel.setting_data

        self.Pic_Panel = pk_Panel(self, self.setting["picture"])
        self.calc_Panel = PK_calc_Panel(self, self.setting["calc"])
        self.move_Panel = pk_Move_Panel(self, self.setting["move"])
        self.data_Panel = pk_data_Panel(self, self.setting["search"])
        self.party_Panel = pk_party_Panel(self, self.setting["party"])

        self.AddPage(self.Pic_Panel, "ポケモン検索")
        self.AddPage(self.data_Panel, "ポケモン図鑑")
        self.AddPage(self.move_Panel, "技一覧")
        self.AddPage(self.calc_Panel, "ダメージ計算")
        self.AddPage(self.party_Panel, "パーティ編成")
        # self.AddPage(self.setting_Panel, "設定")

        self.Bind(wx.EVT_NOTEBOOK_PAGE_CHANGED, self.set_values)
    
    def get_use_data(self):
        self.conn = sqlite3.connect("./Python/GUI/ポケモン_ダメージ計算ツール/use_data/py_db.db")
        self.cursor = self.conn.cursor()
        with open("./Python/GUI/ポケモン_ダメージ計算ツール/use_data/PK_Move.json", encoding="UTF-8") as f:
            text = f.read()
            self.use_move_data = json.loads(text)
            f.close()

        sql2 = """
        Select * 
        From pk_move
        """
        self.df_move_all = pd.read_sql_query(sql=sql2, con=self.conn)

    def set_values(self, event):
        tab_num = event.GetSelection()
        if tab_num == 3 or tab_num == 1:
            pk_list = self.Pic_Panel.pk_list.copy()
            pk_list.sort()
            if pk_list != []:
                name_my = self.calc_Panel.name_box_my.GetValue()
                name_enem = self.calc_Panel.name_box_enem.GetValue()

                self.calc_Panel.name_box_my.Clear()
                self.calc_Panel.name_box_enem.Clear()
                self.calc_Panel.name_box_my.SetValue(name_my)
                self.calc_Panel.name_box_enem.SetValue(name_enem)
                self.calc_Panel.name_box_my.AppendItems(pk_list)
                self.calc_Panel.name_box_enem.AppendItems(pk_list)


