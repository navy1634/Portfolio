import wx
import pandas as pd
from pk_Table import mainTable

type_list = ['タイプ', 'あく', 'いわ', 'かくとう', 'くさ', 'こおり', 'じめん', 'でんき', 'どく', 'はがね', 'ひこう', 'ほのお', 'みず', 'むし', 'エスパー', 'ゴースト', 'ドラゴン', 'ノーマル', 'フェアリー']
move_class_list = ["分類", '物理', '特殊', '変化', 'Z技', "ダイマックス"]
move_target_list = ["対象", '自分', '味方1体', '1体', '自分か味方', '味方全体', '相手全体', '全体', 'ランダム1体', '自分以外', '味方の場', '相手の場', '全体の場', '不定']

# フレームに情報を埋め込むパネルの作成
class pk_Move_Panel(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent, id=-1)
        self.size = (70, 20)
        self.conn = parent.conn
        self.df_move_all = parent.df_move_all
        self.use_move_data  = parent.use_move_data
        self.output_list = mainTable(self, size=(900, 210))

        panel_layout = wx.BoxSizer(wx.VERTICAL)
        panel_layout.Add(self.set_panel(), flag=wx.SHAPED | wx.ALIGN_CENTER)
        self.SetSizer(panel_layout)

        # 初期配置
        for col, v in enumerate(self.df_move_all.columns):
            self.output_list.InsertColumn(col, v)
        
        self.set_output(self.df_move_all)


    # 検索
    def get_move_data(self, event):
        pk_move_name = self.move_name.GetValue()
        pk_move_type = self.move_type.GetValue()
        pk_move_class = self.move_class.GetValue()
        pk_move_power_m = self.move_power_m.GetValue()
        pk_move_power_M = self.move_power_M.GetValue()
        pk_move_big_m = self.move_power_big_m.GetValue()
        pk_move_big_M = self.move_power_big_M.GetValue()
        pk_move_hit_m = self.move_hit_m.GetValue()
        pk_move_hit_M = self.move_hit_M.GetValue()
        pk_move_pp_m = self.move_pp_m.GetValue()
        pk_move_pp_M = self.move_pp_M.GetValue()
        pk_move_way = self.move_way.GetValue()
        pk_move_target = self.move_target.GetValue()

        df_move = self.df_move_all.copy()
        if pk_move_name != "技名":
            df_move = df_move[df_move["名前"]==pk_move_name]
        if pk_move_type in type_list and pk_move_type != "タイプ":
            df_move = df_move[df_move["タイプ"]==pk_move_type]
        if pk_move_class in move_class_list and pk_move_class != "分類":
            df_move = df_move[df_move["分類"]==pk_move_class]

        # df_move = df_move[df_move["威力"]>=move_power_m]
        # df_move = df_move[df_move["威力"]<=move_power_M]
        # df_move = df_move[df_move["ダイマックス"]>=move_big_m]
        # df_move = df_move[df_move["ダイマックス"]<=move_big_M]
        # df_move = df_move[df_move["命中"]>=move_hit_m]
        # df_move = df_move[df_move["命中"]<=move_hit_M]
        # df_move = df_move[df_move["PP"]>=move_pp_m]
        # df_move = df_move[df_move["PP"]<=move_pp_M]

        if pk_move_way != "攻撃方法":
            df_move = df_move[df_move["攻撃方法"]==pk_move_way]
        if pk_move_target in move_target_list and pk_move_target != "対象":
            df_move = df_move[df_move["対象"]==pk_move_target]
        self.set_output(df_move)

    # 取得したデータの反映
    def set_output(self, df):
        self.output_list.DeleteAllItems()
        for line, cur in enumerate(df.itertuples()):
            self.output_list.InsertItem(line, str(cur[1]))
            for col in range(1, len(cur)):
                self.output_list.SetItem(line,col-1,str(cur[col]))

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

    # 以下ボタンのレイアウト
    def set_pk_button(self):
        move_name_text = wx.StaticText(self, -1, "ポケモン名", size=self.size)
        self.name_box = wx.ComboBox(self, -1, "ポケモン", size=self.size)
        self.name_box.Bind(wx.EVT_COMBOBOX, self.get_pk_use)
        move_folm_text = wx.StaticText(self, -1, "フォルム", size=self.size)
        self.folm_box = wx.ComboBox(self, -1, "フォルム", size=self.size)
        self.series_button = wx.ToggleButton(self, -1, "過去作", size=self.size)
        self.series_button.Bind(wx.EVT_TOGGLEBUTTON, self.get_pk_use)
        reset_button = wx.Button(self, -1, "リセット", size=self.size)
        reset_button.Bind(wx.EVT_BUTTON, self.reset_data)
        close_button = wx.Button(self, -1, "終了", size=self.size)
        close_button.Bind(wx.EVT_BUTTON, self.app_close)
        layout = wx.GridSizer(2, 4, 0, 0)
        layout.Add(move_name_text)
        layout.Add(self.name_box)
        layout.Add(self.series_button)
        layout.Add(reset_button)
        layout.Add(move_folm_text)
        layout.Add(self.folm_box)
        layout.Add(wx.StaticText(self, -1, "", size=self.size))
        layout.Add(close_button)
        return layout

    def set_panel(self):
        layout = wx.BoxSizer(wx.VERTICAL)
        layout.Add(wx.StaticText(self, -1, "", size=self.size))
        layout.Add(wx.StaticText(self, -1, "", size=self.size))
        layout.Add(self.set_move_layout(), flag=wx.SHAPED | wx.ALIGN_CENTER)
        layout.Add(wx.StaticText(self, -1, "", size=self.size))
        layout.Add(self.set_pk_button(), flag=wx.SHAPED | wx.ALIGN_CENTER)
        layout.Add(wx.StaticText(self, -1, "", size=self.size))
        layout.Add(self.output_list, flag=wx.SHAPED | wx.ALIGN_CENTER)
        return layout

    def set_move_layout(self):
        move_name_text = wx.StaticText(self, -1, "技名", size=self.size)
        move_type_text = wx.StaticText(self, -1, "タイプ", size=self.size)
        move_class_text = wx.StaticText(self, -1, "分類", size=self.size)
        move_power_text = wx.StaticText(self, -1, "威力", size=self.size)
        move_power_big_text = wx.StaticText(self, -1, "ダイマックス時", size=self.size)
        move_hit_text = wx.StaticText(self, -1, "命中率", size=self.size)
        move_pp_text = wx.StaticText(self, -1, "PP", size=self.size)
        move_way_text = wx.StaticText(self, -1, "攻撃方法", size=self.size)
        move_target_text = wx.StaticText(self, -1, "攻撃対象", size=self.size)

        self.move_name = wx.ComboBox(self, -1, "技名", size=self.size, choices=["技名"])
        self.move_name.Bind(wx.EVT_COMBOBOX, self.get_move_data)
        self.move_type = wx.ComboBox(self, -1, "タイプ", size=self.size, choices=type_list)
        self.move_type.Bind(wx.EVT_COMBOBOX, self.get_move_data)
        self.move_class = wx.ComboBox(self, -1, "分類", size=self.size, choices=move_class_list)
        self.move_class.Bind(wx.EVT_COMBOBOX, self.get_move_data)
        self.move_power_m = wx.SpinCtrlDouble(self, -1, "0", size=self.size, min=0, max=300, inc=5)
        self.move_power_m.Bind(wx.EVT_COMBOBOX, self.get_move_data)
        self.move_power_M = wx.SpinCtrlDouble(self, -1, "255", size=self.size, min=0, max=300, inc=5)
        self.move_power_M.Bind(wx.EVT_COMBOBOX, self.get_move_data)
        self.move_power_big_m = wx.SpinCtrlDouble(self, -1, "0", size=self.size, min=0, max=300, inc=5)
        self.move_power_big_m.Bind(wx.EVT_COMBOBOX, self.get_move_data)
        self.move_power_big_M = wx.SpinCtrlDouble(self, -1, "255", size=self.size, min=0, max=300, inc=5)
        self.move_power_big_M.Bind(wx.EVT_COMBOBOX, self.get_move_data)
        self.move_hit_m = wx.SpinCtrlDouble(self, -1, "0", size=self.size, min=0, max=100, inc=5)
        self.move_hit_m.Bind(wx.EVT_COMBOBOX, self.get_move_data)
        self.move_hit_M = wx.SpinCtrlDouble(self, -1, "100", size=self.size, min=0, max=100, inc=5)
        self.move_hit_M.Bind(wx.EVT_COMBOBOX, self.get_move_data)
        self.move_pp_m = wx.SpinCtrl(self, -1, "0", size=self.size, min=0, max=50)
        self.move_pp_m.Bind(wx.EVT_COMBOBOX, self.get_move_data)
        self.move_pp_M = wx.SpinCtrl(self, -1, "50", size=self.size, min=0, max=50)
        self.move_pp_M.Bind(wx.EVT_COMBOBOX, self.get_move_data)
        self.move_way = wx.ComboBox(self, -1, "攻撃方法", size=self.size, choices=["攻撃方法", "接触", "非接触"])
        self.move_way.Bind(wx.EVT_COMBOBOX, self.get_move_data)
        self.move_target = wx.ComboBox(self, -1, "攻撃対象", size=self.size, choices=move_target_list)
        self.move_target.Bind(wx.EVT_COMBOBOX, self.get_move_data)

        layout = wx.GridSizer(5, 7, 0, 0)
        layout.Add(move_name_text)
        layout.Add(self.move_name)
        layout.Add(move_power_text)
        layout.Add(self.move_power_m)
        layout.Add(wx.StaticText(self, -1, "以上", size=self.size))
        layout.Add(self.move_power_M)
        layout.Add(wx.StaticText(self, -1, "以下", size=self.size))
        layout.Add(move_type_text)
        layout.Add(self.move_type)
        layout.Add(move_power_big_text)
        layout.Add(self.move_power_big_m)
        layout.Add(wx.StaticText(self, -1, "以上", size=self.size))
        layout.Add(self.move_power_big_M)
        layout.Add(wx.StaticText(self, -1, "以下", size=self.size))
        layout.Add(move_class_text)
        layout.Add(self.move_class)
        layout.Add(move_pp_text)
        layout.Add(self.move_pp_m)
        layout.Add(wx.StaticText(self, -1, "以上", size=self.size))
        layout.Add(self.move_pp_M)
        layout.Add(wx.StaticText(self, -1, "以下", size=self.size))
        layout.Add(move_way_text)
        layout.Add(self.move_way)
        layout.Add(move_hit_text)
        layout.Add(self.move_hit_m)
        layout.Add(wx.StaticText(self, -1, "以上", size=self.size))
        layout.Add(self.move_hit_M)
        layout.Add(wx.StaticText(self, -1, "以下", size=self.size))
        layout.Add(move_target_text)
        layout.Add(self.move_target)
        layout.Add(wx.StaticText(self, -1, "", size=self.size))
        layout.Add(wx.StaticText(self, -1, "", size=self.size))
        layout.Add(wx.StaticText(self, -1, "", size=self.size))
        layout.Add(wx.StaticText(self, -1, "", size=self.size))
        layout.Add(wx.StaticText(self, -1, "", size=self.size))
        return layout

    # リセットボタン
    def reset_data(self, event):
        self.move_name.SetValue("名前")
        self.move_type.SetValue("タイプ")
        self.move_class.SetValue("分類")
        self.move_power_m.SetValue("0")
        self.move_power_M.SetValue("255")
        self.move_power_big_m.SetValue("0")
        self.move_power_big_M.SetValue("255")
        self.move_hit_m.SetValue("0")
        self.move_hit_M.SetValue("100")
        self.move_pp_m.SetValue("0")
        self.move_pp_M.SetValue("50")
        self.move_way.SetValue("攻撃方法")
        self.move_target.SetValue("攻撃対象")

    # GUI停止のボタン作成
    def app_close(self, event):
        self.conn.close()
        wx.Exit()

