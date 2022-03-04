import pandas as pd
from os import environ
import MySQLdb
from sqlalchemy import column, create_engine
import wx
import wx.lib.mixins.listctrl as listmix

# 未完成

columns = ["図鑑番号", "名前", "タイプ1", "タイプ2", "特性1", "特性2", "合計値", "H", "A", "B", "C", "D", "S"]

class mainTable(wx.ListCtrl, listmix.ListCtrlAutoWidthMixin):
    def __init__(self, panel, style):
        wx.ListCtrl.__init__(self, panel, -1, style=wx.LC_REPORT | wx.SUNKEN_BORDER,size=wx.Size(395, 467), pos=wx.Point(10, 20))
        listmix.ListCtrlAutoWidthMixin.__init__(self)
    

class MainFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, id=-1, title="ポケモン図鑑", size=(750,900))

        self.panel1 = Panel_1(self)
        self.panel1.SetBackgroundColour('#d8d8d8')

        panel_layout = wx.BoxSizer(wx.VERTICAL)
        panel_layout.Add(self.panel1, 1, wx.EXPAND)
        self.SetSizer(panel_layout)


class Panel_1(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent, id=-1)
        self.use_list = mainTable(self, style=wx.LC_REPORT)
        self.conn = MySQLdb.connect(host="localhost",user="navy", passwd=environ.get("SQL_NAVY_PASS"), db="Pokemon")
        self.cursor = self.conn.cursor()

        self.panel_layout = wx.BoxSizer(wx.VERTICAL)
        self.panel_layout.Add(wx.StaticText(self, -1, ""), flag=wx.SHAPED | wx.ALIGN_CENTER)
        self.panel_layout.Add(wx.StaticText(self, -1, "ポケモン検索"), flag=wx.SHAPED | wx.ALIGN_LEFT)
        self.panel_layout.Add(wx.StaticText(self, -1, ""), flag=wx.SHAPED | wx.ALIGN_CENTER)
        self.panel_layout.Add(wx.StaticText(self, -1, ""), flag=wx.SHAPED | wx.ALIGN_CENTER)
        self.panel_layout.Add(self.layout(), flag=wx.SHAPED | wx.ALIGN_CENTER)
        self.panel_layout.Add(wx.StaticText(self, -1, ""), flag=wx.SHAPED | wx.ALIGN_CENTER)
        self.panel_layout.Add(self.search_button(), flag=wx.SHAPED | wx.ALIGN_CENTER)
        self.panel_layout.Add(wx.StaticText(self, -1, ""), flag=wx.SHAPED | wx.ALIGN_CENTER)
        self.panel_layout.Add(self.use_list, flag=wx.SHAPED | wx.ALIGN_CENTER)
        self.SetSizer(self.panel_layout)


    def view_pk_list(self, event):
        self.get_pk_data()
        for col, v in enumerate(columns):
            self.use_list.InsertColumn(col, v)

        for line, cur in enumerate(self.cursor):
            self.use_list.InsertStringItem(line, cur[0])
            for col in enumerate(cur):
                self.use_list.SetStringItem(line,col,cur)

    def get_pk_data(self):
        sql = """
            Select pk_nomal.図鑑番号, pk_nomal.名前, pk_fight.タイプ1, pk_fight.タイプ2, pk_fight.特性1, pk_fight.特性2, pk_status.合計値, pk_status.H, pk_status.A, pk_status.B, pk_status.C, pk_status.D, pk_status.S
            From pk_status left outer join pk_nomal
            on pk_status.図鑑番号 = pk_nomal.図鑑番号 and pk_status.フォルム = pk_nomal.フォルム
            left outer join pk_fight
            on pk_status.図鑑番号 = pk_fight.図鑑番号 and pk_status.フォルム = pk_fight.フォルム
        """

        sql = sql + self.create_sql()
        self.cursor.execute(sql)

    def create_sql(self):
        sql = """
        """

        name = self.name_button.GetValue()
        if name != "名前":
            sql += """ and pk_nomal.名前 = {name}""".format(name=name)
        type1 = self.type1_button.GetValue()
        if type1 != "タイプ1":
            sql += """ and pk_fight_data.タイプ1 = {type1}""".format(type1=type1)
        type2 = self.type2_button.GetValue()
        if type2  != "タイプ2":
            sql += """ and pk_fight_data.タイプ2 = {type2}""".format(type2=type1)
        char = self.char_button.GetValue()
        if char != "特性":
            sql += """ and pk_fight_data.特性 = {char}""".format(char=char)
        gene = self.gene_button.GetValue()
        if gene != "世代":
            sql += """ and pk_nomal.世代 = {gene}""".format(gene=gene)
        cls = self.class_button.GetValue()
        if cls != "分類":
            sql += """ and pk_nomal.分類 = {cls}""".format(cls=cls)

        H_m = self.status_H_m.GetValue()
        if H_m:
            sql += """ and pk_status.H <= {}""".format(H_m)
        A_m = self.status_A_m.GetValue()
        if A_m:
            sql += """ and pk_status.A <= {}""".format(A_m)
        B_m = self.status_A_m.GetValue()
        if B_m:
            sql += """ and pk_status.B >= {}""".format(B_m)
        C_m = self.status_A_m.GetValue()
        if C_m:
            sql += """ and pk_status.C >= {}""".format(C_m)
        D_m = self.status_A_m.GetValue()
        if D_m:
            sql += """ and pk_status.D >= {}""".format(D_m)
        S_m = self.status_A_m.GetValue()
        if S_m:
            sql += """ and pk_status.S >= {}""".format(S_m)

        H_M = self.status_H_M.GetValue()
        if H_M:
            sql += """ and pk_status.H <= {}""".format(H_M)
        A_M = self.status_A_M.GetValue()
        if A_M:
            sql += """ and pk_status.A <= {}""".format(A_M)
        B_M = self.status_B_M.GetValue()
        if B_M:
            sql += """ and pk_status.B <= {}""".format(B_M)
        C_M = self.status_C_M.GetValue()
        if C_M:
            sql += """ and pk_status.C <= {}""".format(C_M)
        D_M = self.status_D_M.GetValue()
        if D_M:
            sql += """ and pk_status.D <= {}""".format(D_M)
        S_M = self.status_S_M.GetValue()
        if S_M:
            sql += """ and pk_status.S <= {}""".format(S_M)

        return sql.replace(" and", "Where", 1)


    def search_button(self):
        search_button = wx.Button(self, -1, "検索")
        search_button.Bind(wx.EVT_BUTTON, self.view_pk_list)
        close_button = wx.Button(self, -1, "終了")
        close_button.Bind(wx.EVT_BUTTON, self.app_close)

        layout = wx.BoxSizer(wx.HORIZONTAL)
        layout.Add(search_button)
        layout.Add(wx.StaticText(self, -1, ""))
        layout.Add(close_button)
        return layout
    
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
        char_text = wx.StaticText(self, -1, "特性", size=(70, 20))
        gene_text = wx.StaticText(self, -1, "世代", size=(70, 20))
        class_text = wx.StaticText(self, -1, "分類", size=(70, 20))

        layout = wx.BoxSizer(wx.VERTICAL)
        layout.Add(name_text)
        layout.Add(type1_text)
        layout.Add(type2_text)
        layout.Add(char_text)
        layout.Add(gene_text)
        layout.Add(class_text)
        return layout
    
    def set_pk_layout(self):
        self.name_button = wx.TextCtrl(self, -1, "名前", size=(70, 20))
        self.type1_button = wx.ComboBox(self, -1, "タイプ1", choices=["A", "B"], size=(70, 20))
        self.type2_button = wx.ComboBox(self, -1, "タイプ2", choices=["A", "B"], size=(70, 20))
        self.char_button = wx.TextCtrl(self, -1, "特性", size=(70, 20))
        self.gene_button = wx.ComboBox(self, -1, "世代", choices=["1", "2", "3", "4", "5", "6", "7", "8"], size=(70, 20))
        self.class_button = wx.ComboBox(self, -1, "分類", choices=["一般", "準伝説", "伝説", "幻"], size=(70, 20))

        data_layout = wx.BoxSizer(wx.VERTICAL)
        data_layout.Add(self.name_button)
        data_layout.Add(self.type1_button)
        data_layout.Add(self.type2_button)
        data_layout.Add(self.char_button)
        data_layout.Add(self.gene_button)
        data_layout.Add(self.class_button)
        return data_layout

    def status_layout(self):
        status_H = wx.StaticText(self, -1, "HP", size=(70, 20))
        status_A = wx.StaticText(self, -1, "攻撃", size=(70, 20))
        status_B = wx.StaticText(self, -1, "防御", size=(70, 20))
        status_C = wx.StaticText(self, -1, "特攻", size=(70, 20))
        status_D = wx.StaticText(self, -1, "特防", size=(70, 20))
        status_S = wx.StaticText(self, -1, "素早さ", size=(70, 20))

        status_upper_H = wx.StaticText(self, -1, "以上", size=(40, 20))
        status_upper_A = wx.StaticText(self, -1, "以上", size=(40, 20))
        status_upper_B = wx.StaticText(self, -1, "以上", size=(40, 20))
        status_upper_C = wx.StaticText(self, -1, "以上", size=(40, 20))
        status_upper_D = wx.StaticText(self, -1, "以上", size=(40, 20))
        status_upper_S = wx.StaticText(self, -1, "以上", size=(40, 20))
    
        status_lower_H = wx.StaticText(self, -1, "以下", size=(40, 20))
        status_lower_A = wx.StaticText(self, -1, "以下", size=(40, 20))
        status_lower_B = wx.StaticText(self, -1, "以下", size=(40, 20))
        status_lower_C = wx.StaticText(self, -1, "以下", size=(40, 20))
        status_lower_D = wx.StaticText(self, -1, "以下", size=(40, 20))
        status_lower_S = wx.StaticText(self, -1, "以下", size=(40, 20))
    
        self.status_H_m = wx.TextCtrl(self, -1, size=(70, 20))
        self.status_A_m = wx.TextCtrl(self, -1, size=(70, 20))
        self.status_B_m = wx.TextCtrl(self, -1, size=(70, 20))
        self.status_C_m = wx.TextCtrl(self, -1, size=(70, 20))
        self.status_D_m = wx.TextCtrl(self, -1, size=(70, 20))
        self.status_S_m = wx.TextCtrl(self, -1, size=(70, 20))

        self.status_H_M = wx.TextCtrl(self, -1, size=(70, 20))
        self.status_A_M = wx.TextCtrl(self, -1, size=(70, 20))
        self.status_B_M = wx.TextCtrl(self, -1, size=(70, 20))
        self.status_C_M = wx.TextCtrl(self, -1, size=(70, 20))
        self.status_D_M = wx.TextCtrl(self, -1, size=(70, 20))
        self.status_S_M = wx.TextCtrl(self, -1, size=(70, 20))


        layout = wx.GridSizer(6, 5, 0, 0)
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


    def app_close(self, event):
        self.conn.close()
        wx.Exit()


application = wx.App()
frame = MainFrame()
frame.SetMinSize(wx.Size(520,700))
frame.Show()
application.MainLoop()
