import wx
import pandas as pd
from pk_Table import mainTable

columns = ["図鑑番号", "名前", "フォルム",  "タイプ1", "タイプ2", "特性1", "特性2", "夢特性1", "合計値", "H", "A", "B", "C", "D", "S", "分類", "世代"]
type_list = ['タイプ', 'あく', 'いわ', 'かくとう', 'くさ', 'こおり', 'じめん', 'でんき', 'どく', 'はがね', 'ひこう', 'ほのお', 'みず', 'むし', 'エスパー', 'ゴースト', 'ドラゴン', 'ノーマル', 'フェアリー']


class pk_data_Panel(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent, -1)

        self.size = (70, 20)
        self.conn = parent.conn
        self.df_move_all = parent.df_move_all
        self.use_move_data  = parent.use_move_data
        self.output_list = mainTable(self, size=(900, 210))

        panel_layout = wx.BoxSizer(wx.VERTICAL)
        panel_layout.Add(self.layout(), flag=wx.SHAPED | wx.ALIGN_CENTER)
        panel_layout.Add(self.output_list, flag=wx.SHAPED | wx.ALIGN_CENTER)
        self.SetSizer(panel_layout)
        

    def layout(self):
        layout = wx.BoxSizer(wx.HORIZONTAL)
        layout.Add(self.search_text_layout())
        layout.Add(self.set_pk_layout())
        layout.Add(self.status_layout())
        return layout

    def search_text_layout(self):
        name_text = wx.StaticText(self, -1, "名前", size=(70, 20))
        type1_text = wx.StaticText(self, -1, "タイプ1", size=(70, 20))
        type2_text = wx.StaticText(self, -1, "タイプ2", size=(70, 20))
        char_text = wx.StaticText(self, -1, "特性1", size=(70, 20))
        hide_abi_text = wx.StaticText(self, -1, "特性2", size=(70, 20))
        gene_text = wx.StaticText(self, -1, "世代", size=(70, 20))
        class_text = wx.StaticText(self, -1, "分類", size=(70, 20))

        layout = wx.BoxSizer(wx.VERTICAL)
        layout.Add(name_text)
        layout.Add(type1_text)
        layout.Add(type2_text)
        layout.Add(char_text)
        layout.Add(hide_abi_text)
        layout.Add(gene_text)
        layout.Add(class_text)
        return layout
    
    def set_pk_layout(self):
        self.name_button = wx.TextCtrl(self, -1, "名前", size=(70, 20))
        self.type1_button = wx.ComboBox(self, -1, "タイプ", choices=type_list, size=(70, 20))
        self.type2_button = wx.ComboBox(self, -1, "タイプ", choices=type_list, size=(70, 20))
        self.char_button = wx.TextCtrl(self, -1, "特性1", size=(70, 20))
        self.hide_abi_button = wx.TextCtrl(self, -1, "特性2", size=(70, 20))
        self.gene_button = wx.ComboBox(self, -1, "世代", choices=["世代", "1", "2", "3", "4", "5", "6", "7", "8"], size=(70, 20))
        self.class_button = wx.ComboBox(self, -1, "分類", choices=["分類", "一般", "準伝説", "伝説", "幻"], size=(70, 20))

        data_layout = wx.BoxSizer(wx.VERTICAL)
        data_layout.Add(self.name_button)
        data_layout.Add(self.type1_button)
        data_layout.Add(self.type2_button)
        data_layout.Add(self.char_button)
        data_layout.Add(self.hide_abi_button)
        data_layout.Add(self.gene_button)
        data_layout.Add(self.class_button)
        return data_layout

    def status_layout(self):
        status_SUM = wx.StaticText(self, -1, "合計値", size=(70, 20))
        status_H = wx.StaticText(self, -1, "HP", size=(70, 20))
        status_A = wx.StaticText(self, -1, "攻撃", size=(70, 20))
        status_B = wx.StaticText(self, -1, "防御", size=(70, 20))
        status_C = wx.StaticText(self, -1, "特攻", size=(70, 20))
        status_D = wx.StaticText(self, -1, "特防", size=(70, 20))
        status_S = wx.StaticText(self, -1, "素早さ", size=(70, 20))

        self.status_SUM = wx.TextCtrl(self, -1, size=(70, 20))
        self.status_H = wx.TextCtrl(self, -1, size=(70, 20))
        self.status_A = wx.TextCtrl(self, -1, size=(70, 20))
        self.status_B = wx.TextCtrl(self, -1, size=(70, 20))
        self.status_C = wx.TextCtrl(self, -1, size=(70, 20))
        self.status_D = wx.TextCtrl(self, -1, size=(70, 20))
        self.status_S = wx.TextCtrl(self, -1, size=(70, 20))

        layout = wx.GridSizer(7, 2, 0, 0)
        layout.Add(status_SUM)
        layout.Add(self.status_SUM)
        layout.Add(status_H)
        layout.Add(self.status_H)
        layout.Add(status_A)
        layout.Add(self.status_A)
        layout.Add(status_B)
        layout.Add(self.status_B)
        layout.Add(status_C)
        layout.Add(self.status_C)
        layout.Add(status_D)
        layout.Add(self.status_D)
        layout.Add(status_S)
        layout.Add(self.status_S)

        return layout

    # GUI停止のボタン作成
    def app_close(self, event):
        self.conn.close()
        wx.Exit()
    
    def ge(self):
        self.series_button = wx.ToggleButton(self, -1, "過去作", size=self.size)
        self.series_button.Bind(wx.EVT_TOGGLEBUTTON, self.get_pk_use)

    # 覚える技の取得
    def get_pk_use(self, event):
        name = self.name_box.GetValue()
        try:
            toggle = self.series_button.GetValue()
            use_move_list_my = self.use_move_data[name]["Move"]
            if toggle == True:
                use_move_list = [move for move,val in use_move_list_my.items()  if val !="過去限定"]
            else:
                use_move_list = list(use_move_list_my.keys())
            df_move = self.df_move_all[self.df_move_all["名前"].isin(use_move_list)]
            self.set_output(df_move)
        except:
            df_move = pd.DataFrame(["Error"])
