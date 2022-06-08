import wx
from Table import mainTable

columns = ["図鑑番号", "名前", "フォルム",  "タイプ1", "タイプ2", "特性1", "特性2", "夢特性1", "合計値", "H", "A", "B", "C", "D", "S", "分類", "世代"]
type_list = ['タイプ', 'あく', 'いわ', 'かくとう', 'くさ', 'こおり', 'じめん', 'でんき', 'どく', 'はがね', 'ひこう', 'ほのお', 'みず', 'むし', 'エスパー', 'ゴースト', 'ドラゴン', 'ノーマル', 'フェアリー']

# フレームに情報を埋め込むパネルの作成
class pk_Panel(wx.Panel):
    def __init__(self, parent, setting):
        super().__init__(parent, id=-1)
        self.use_list = mainTable(self, size=(900, 380))
        self.setting = setting
        self.size = parent.size
        self.conn = parent.conn
        self.cursor = parent.cursor
        
        self.pk_list = []
        self.name = list()
        self.folm = list()

        panel_layout = wx.BoxSizer(wx.VERTICAL)
        panel_layout.Add(self.layout(), flag=wx.SHAPED | wx.ALIGN_CENTER)
        self.SetSizer(panel_layout)
        self.use_list.Bind(wx.EVT_LIST_ITEM_SELECTED, self.get_name)

        for col, v in enumerate(columns):
            self.use_list.InsertColumn(col, v)

        self.get_pk_data()
        for line, cur in enumerate(self.cursor):
            cur = list(cur)
            self.use_list.InsertItem(line, cur[0])
            for col in range(1, len(cur)):
                data = str(cur[col])
                self.use_list.SetItem(line,col,data)


    # 選択したアイテムの取得
    def get_name(self, event):
        ind = self.use_list.GetFirstSelected()
        if ind >=0:
            self.name.append(self.use_list.GetItem(ind,1).GetText())
        
    def get_calc_pk(self, event):
        self.pk_list.extend(self.name)
        self.name = list()
    
    # 取得したデータの反映
    def view_pk_list(self, event):
        self.get_pk_data()
        self.use_list.DeleteAllItems()
        for line, cur in enumerate(self.cursor):
            cur = list(cur)
            self.use_list.InsertItem(line, cur[0])
            for col in range(1, len(cur)):
                data = str(cur[col])
                self.use_list.SetItem(line,col,data)
    
    # SQl文の作成
    def get_pk_data(self):
        sql = """
            Select pk_nomal.図鑑番号, pk_nomal.名前, pk_nomal.フォルム, pk_fight.タイプ1, pk_fight.タイプ2, pk_fight.特性1, pk_fight.特性2, pk_fight.夢特性, pk_status.合計値, pk_status.H, pk_status.A, pk_status.B, pk_status.C, pk_status.D, pk_status.S, pk_nomal.分類, pk_nomal.世代
            From pk_status left outer join pk_nomal
            on pk_status.図鑑番号 = pk_nomal.図鑑番号 and pk_status.フォルム = pk_nomal.フォルム and pk_status.名前 = pk_nomal.名前
            left outer join pk_fight
            on pk_status.図鑑番号 = pk_fight.図鑑番号 and pk_status.フォルム = pk_fight.フォルム and pk_status.名前 = pk_fight.名前
        """
        sql = sql + self.create_sql()
        self.cursor.execute(sql)

    # 検索条件の取得
    def create_sql(self):
        sql = """   """

        name = self.name_button.GetValue()
        if name != "名前":
            sql += """ and pk_nomal.名前 Like '%{name}%'""".format(name=name)
        type1 = self.type1_button.GetValue()
        if type1 != "タイプ":
            sql += """ and (pk_fight.タイプ1 = '{type1}' or pk_fight.タイプ2 = '{type1}')""".format(type1=type1)
        type2 = self.type2_button.GetValue()
        if type2  != "タイプ":
            sql += """ and (pk_fight.タイプ1 = '{type2}' or pk_fight.タイプ2 = '{type2}')""".format(type2=type2)
        char1 = self.abi_button.GetValue()
        if char1 != "特性1":
            sql += """ and (pk_fight.特性1 = '{char}' or pk_fight.特性2 = '{char}' or pk_fight.夢特性 = '{char}')""".format(char=char1)
        char2 = self.hide_abi_button.GetValue()
        if char2 != "特性2":
            sql += """ and (pk_fight.特性1 = '{char}' or pk_fight.特性2 = '{char}' or pk_fight.夢特性 = '{char}')""".format(char=char2)
        gene = self.gene_button.GetValue()
        if gene != "世代":
            sql += """ and pk_nomal.世代 = {gene}""".format(gene=gene)
        cls = self.class_button.GetValue()
        if cls != "分類":
            sql += """ and pk_nomal.分類 = '{cls}'""".format(cls=cls)

        SUM_m = self.status_SUM_m.GetValue()
        if 0 <= int(SUM_m) <= 255:
            sql += """ and pk_status.合計値 >= {}""".format(int(SUM_m))
        H_m = self.status_H_m.GetValue()
        if 0 <= int(H_m) <= 255:
            sql += """ and pk_status.H >= {}""".format(int(H_m))
        A_m = self.status_A_m.GetValue()
        if 0 <= int(A_m) <= 255:
            sql += """ and pk_status.A >= {}""".format(int(A_m))
        B_m = self.status_A_m.GetValue()
        if 0 <= int(B_m) <= 255:
            sql += """ and pk_status.B >= {}""".format(int(B_m))
        C_m = self.status_A_m.GetValue()
        if 0 <= int(C_m) <= 255:
            sql += """ and pk_status.C >= {}""".format(int(C_m))
        D_m = self.status_A_m.GetValue()
        if 0 <= int(D_m) <= 255:
            sql += """ and pk_status.D >= {}""".format(int(D_m))
        S_m = self.status_A_m.GetValue()
        if 0 <= int(S_m) <= 255:
            sql += """ and pk_status.S >= {}""".format(int(S_m))

        SUM_M = self.status_SUM_M.GetValue()
        if 0 <= int(SUM_M) <= 255:
            sql += """ and pk_status.合計値 <= {}""".format(int(SUM_M))
        H_M = self.status_H_M.GetValue()
        if 0 <= int(H_M) <= 255:
            sql += """ and pk_status.H <= {}""".format(int(H_M))
        A_M = self.status_A_M.GetValue()
        if 0 <= int(A_M) <= 255:
            sql += """ and pk_status.A <= {}""".format(int(A_M))
        B_M = self.status_B_M.GetValue()
        if 0 <= int(B_M) <= 255:
            sql += """ and pk_status.B <= {}""".format(int(B_M))
        C_M = self.status_C_M.GetValue()
        if 0 <= int(C_M) <= 255:
            sql += """ and pk_status.C <= {}""".format(int(C_M))
        D_M = self.status_D_M.GetValue()
        if 0 <= int(D_M) <= 255:
            sql += """ and pk_status.D <= {}""".format(int(D_M))
        S_M = self.status_S_M.GetValue()
        if 0 <= int(S_M) <= 255:
            sql += """ and pk_status.S <= {}""".format(int(S_M))

        return sql.replace(" and", "Where", 1)

    # 以下ボタンのレイアウト
    def layout(self):
        layout = wx.BoxSizer(wx.VERTICAL)
        layout.Add(wx.StaticText(self, -1, ""))
        layout.Add(wx.StaticText(self, -1, ""))
        layout.Add(wx.StaticText(self, -1, ""))
        layout.Add(self.pk_layout(), flag=wx.SHAPED | wx.ALIGN_CENTER)
        layout.Add(wx.StaticText(self, -1, ""))
        layout.Add(self.search_button(), flag=wx.SHAPED | wx.ALIGN_CENTER)
        layout.Add(wx.StaticText(self, -1, ""))
        layout.Add(self.use_list, flag=wx.SHAPED | wx.ALIGN_CENTER)
        return layout

    def pk_layout(self):
        layout = wx.BoxSizer(wx.HORIZONTAL)
        layout.Add(self.search_text_layout())
        layout.Add(self.set_pk_layout())
        layout.Add(self.status_layout())
        return layout

    def search_button(self):
        append_button = wx.Button(self, -1, "追加")
        append_button.Bind(wx.EVT_BUTTON, self.get_calc_pk)
        reset_button = wx.Button(self, -1, "リセット")
        reset_button.Bind(wx.EVT_BUTTON, self.reset_button)
        close_button = wx.Button(self, -1, "終了")
        close_button.Bind(wx.EVT_BUTTON, self.app_close)

        layout = wx.BoxSizer(wx.HORIZONTAL)
        layout.Add(append_button)
        layout.Add(reset_button)
        layout.Add(close_button)
        return layout
    
    def search_text_layout(self):
        name_text = wx.StaticText(self, -1, "名前", size=self.size)
        type1_text = wx.StaticText(self, -1, "タイプ1", size=self.size)
        type2_text = wx.StaticText(self, -1, "タイプ2", size=self.size)
        char_text = wx.StaticText(self, -1, "特性1", size=self.size)
        hide_abi_text = wx.StaticText(self, -1, "特性2", size=self.size)
        gene_text = wx.StaticText(self, -1, "世代", size=self.size)
        class_text = wx.StaticText(self, -1, "分類", size=self.size)

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
        self.name_button = wx.TextCtrl(self, -1, "名前", size=self.size)
        self.name_button.Bind(wx.EVT_TEXT, self.view_pk_list)
        self.name_button.SetMaxLength(10)
        self.type1_button = wx.ComboBox(self, -1, "タイプ", choices=type_list, size=self.size)
        self.type1_button.Bind(wx.EVT_TEXT, self.view_pk_list)
        self.type2_button = wx.ComboBox(self, -1, "タイプ", choices=type_list, size=self.size)
        self.type2_button.Bind(wx.EVT_TEXT, self.view_pk_list)
        self.abi_button = wx.TextCtrl(self, -1, "特性1", size=self.size)
        self.abi_button.Bind(wx.EVT_TEXT, self.view_pk_list)
        self.hide_abi_button = wx.TextCtrl(self, -1, "特性2", size=self.size)
        self.hide_abi_button.Bind(wx.EVT_TEXT, self.view_pk_list)
        self.gene_button = wx.ComboBox(self, -1, "世代", choices=["世代", "1", "2", "3", "4", "5", "6", "7", "8"], size=self.size)
        self.gene_button.Bind(wx.EVT_TEXT, self.view_pk_list)
        self.class_button = wx.ComboBox(self, -1, "分類", choices=["分類", "一般", "準伝説", "伝説", "幻"], size=self.size)
        self.class_button.Bind(wx.EVT_TEXT, self.view_pk_list)

        data_layout = wx.BoxSizer(wx.VERTICAL)
        data_layout.Add(self.name_button)
        data_layout.Add(self.type1_button)
        data_layout.Add(self.type2_button)
        data_layout.Add(self.abi_button)
        data_layout.Add(self.hide_abi_button)
        data_layout.Add(self.gene_button)
        data_layout.Add(self.class_button)
        return data_layout

    def status_layout(self):
        status_SUM = wx.StaticText(self, -1, "合計値", size=self.size)
        status_H = wx.StaticText(self, -1, "HP", size=self.size)
        status_A = wx.StaticText(self, -1, "攻撃", size=self.size)
        status_B = wx.StaticText(self, -1, "防御", size=self.size)
        status_C = wx.StaticText(self, -1, "特攻", size=self.size)
        status_D = wx.StaticText(self, -1, "特防", size=self.size)
        status_S = wx.StaticText(self, -1, "素早さ", size=self.size)

        status_upper_SUM = wx.StaticText(self, -1, "以上", size=(40, 20))
        status_upper_H = wx.StaticText(self, -1, "以上", size=(40, 20))
        status_upper_A = wx.StaticText(self, -1, "以上", size=(40, 20))
        status_upper_B = wx.StaticText(self, -1, "以上", size=(40, 20))
        status_upper_C = wx.StaticText(self, -1, "以上", size=(40, 20))
        status_upper_D = wx.StaticText(self, -1, "以上", size=(40, 20))
        status_upper_S = wx.StaticText(self, -1, "以上", size=(40, 20))

        status_lower_SUM = wx.StaticText(self, -1, "以下", size=(40, 20))    
        status_lower_H = wx.StaticText(self, -1, "以下", size=(40, 20))
        status_lower_A = wx.StaticText(self, -1, "以下", size=(40, 20))
        status_lower_B = wx.StaticText(self, -1, "以下", size=(40, 20))
        status_lower_C = wx.StaticText(self, -1, "以下", size=(40, 20))
        status_lower_D = wx.StaticText(self, -1, "以下", size=(40, 20))
        status_lower_S = wx.StaticText(self, -1, "以下", size=(40, 20))
    
        self.status_SUM_m = wx.TextCtrl(self, -1, "0", size=self.size)
        self.status_SUM_m.Bind(wx.EVT_TEXT, self.view_pk_list)
        self.status_H_m = wx.TextCtrl(self, -1, "0", size=self.size)
        self.status_H_m.Bind(wx.EVT_TEXT, self.view_pk_list)
        self.status_A_m = wx.TextCtrl(self, -1, "0", size=self.size)
        self.status_A_m.Bind(wx.EVT_TEXT, self.view_pk_list)
        self.status_B_m = wx.TextCtrl(self, -1, "0", size=self.size)
        self.status_B_m.Bind(wx.EVT_TEXT, self.view_pk_list)
        self.status_C_m = wx.TextCtrl(self, -1, "0", size=self.size)
        self.status_C_m.Bind(wx.EVT_TEXT, self.view_pk_list)
        self.status_D_m = wx.TextCtrl(self, -1, "0", size=self.size)
        self.status_D_m.Bind(wx.EVT_TEXT, self.view_pk_list)
        self.status_S_m = wx.TextCtrl(self, -1, "0", size=self.size)
        self.status_S_m.Bind(wx.EVT_TEXT, self.view_pk_list)

        self.status_SUM_M = wx.TextCtrl(self, -1, "1530", size=self.size)
        self.status_SUM_M.Bind(wx.EVT_TEXT, self.view_pk_list)
        self.status_H_M = wx.TextCtrl(self, -1, "255", size=self.size)
        self.status_H_M.Bind(wx.EVT_TEXT, self.view_pk_list)
        self.status_A_M = wx.TextCtrl(self, -1, "255", size=self.size)
        self.status_A_M.Bind(wx.EVT_TEXT, self.view_pk_list)
        self.status_B_M = wx.TextCtrl(self, -1, "255", size=self.size)
        self.status_B_M.Bind(wx.EVT_TEXT, self.view_pk_list)
        self.status_C_M = wx.TextCtrl(self, -1, "255", size=self.size)
        self.status_C_M.Bind(wx.EVT_TEXT, self.view_pk_list)
        self.status_D_M = wx.TextCtrl(self, -1, "255", size=self.size)
        self.status_D_M.Bind(wx.EVT_TEXT, self.view_pk_list)
        self.status_S_M = wx.TextCtrl(self, -1, "255", size=self.size)
        self.status_S_M.Bind(wx.EVT_TEXT, self.view_pk_list)

        layout = wx.GridSizer(7, 5, 0, 0)
        layout.Add(status_SUM)
        layout.Add(self.status_SUM_m)
        layout.Add(status_upper_SUM)
        layout.Add(self.status_SUM_M)
        layout.Add(status_lower_SUM)

        layout.Add(status_H)
        layout.Add(self.status_H_m)
        layout.Add(status_upper_H)
        layout.Add(self.status_H_M)
        layout.Add(status_lower_H)

        layout.Add(status_A)
        layout.Add(self.status_A_m)
        layout.Add(status_upper_A)
        layout.Add(self.status_A_M)
        layout.Add(status_lower_A)

        layout.Add(status_B)
        layout.Add(self.status_B_m)
        layout.Add(status_upper_B)
        layout.Add(self.status_B_M)
        layout.Add(status_lower_B)

        layout.Add(status_C)
        layout.Add(self.status_C_m)
        layout.Add(status_upper_C)
        layout.Add(self.status_C_M)
        layout.Add(status_lower_C)
        
        layout.Add(status_D)
        layout.Add(self.status_D_m)
        layout.Add(status_upper_D)
        layout.Add(self.status_D_M)
        layout.Add(status_lower_D)

        layout.Add(status_S)
        layout.Add(self.status_S_m)
        layout.Add(status_upper_S)
        layout.Add(self.status_S_M)
        layout.Add(status_lower_S)

        return layout

    # リセット
    def reset_button(self, event):
        self.name_button.SetValue("名前")
        self.type1_button.SetValue("タイプ")
        self.type2_button.SetValue("タイプ")
        self.abi_button.SetValue("特性1")
        self.hide_abi_button.SetValue("特性2")
        self.gene_button.SetValue("世代")
        self.class_button.SetValue("分類")

        self.status_SUM_m.SetValue("0")
        self.status_H_m.SetValue("0")
        self.status_A_m.SetValue("0")
        self.status_B_m.SetValue("0")
        self.status_C_m.SetValue("0")
        self.status_D_m.SetValue("0")
        self.status_S_m.SetValue("0")

        self.status_SUM_M.SetValue("1530")
        self.status_H_M.SetValue("255")
        self.status_A_M.SetValue("255")
        self.status_B_M.SetValue("255")
        self.status_C_M.SetValue("255")
        self.status_D_M.SetValue("255")
        self.status_S_M.SetValue("255")
        self.view_pk_list(event)

    # GUI停止のボタン作成
    def app_close(self, event):
        self.conn.close()
        wx.Exit()

