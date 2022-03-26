import wx
import sqlite3
import json
import pandas as pd
from pk_data_Panel import pk_data_Panel
from pk_panel import pk_Panel
from Calc_Panel import PK_calc_Panel
from pk_Move_data import pk_Move_Panel
from pk_setting import pk_setting_Panel


class TabNote(wx.Notebook):
    def __init__(self, parent):
        super().__init__(parent, id=wx.ID_ANY, style=wx.BK_DEFAULT)
        self.get_use_data()

        self.setting_Panel = pk_setting_Panel(self)
        self.Pic_Panel = pk_Panel(self)
        self.calc_Panel = PK_calc_Panel(self)
        self.move_Panel = pk_Move_Panel(self)
        self.data_Panel = pk_data_Panel(self)

        self.AddPage(self.Pic_Panel, "ポケモン検索")
        self.AddPage(self.data_Panel, "ポケモン図鑑")
        self.AddPage(self.move_Panel, "技一覧")
        self.AddPage(self.calc_Panel, "ダメージ計算")
        self.AddPage(self.setting_Panel, "設定")

        self.Bind(wx.EVT_NOTEBOOK_PAGE_CHANGED, self.set_values)
    
    def get_use_data(self):
        self.conn = sqlite3.connect("py_db.db")
        self.cursor = self.conn.cursor()
        with open("use_data\PK_Move.json", encoding="UTF-8") as f:
            text = f.read()
            self.use_move_data = json.loads(text)
            f.close()
        sql2 = """
        Select * 
        From pk_move
        """.format(name=self)
        self.df_move_all = pd.read_sql_query(sql=sql2, con=self.conn)

    def set_values(self, event):
        tab_num = event.GetSelection()
        if tab_num == 3:
            pk_list = self.Pic_Panel.pk_list
            for name in pk_list:
                if name not in self.calc_Panel.name_box_my.Items:
                    self.calc_Panel.name_box_my.AppendItems(name)
                    self.calc_Panel.name_box_enem.AppendItems(name)
            self.Pic_Panel.pk_list = []
    