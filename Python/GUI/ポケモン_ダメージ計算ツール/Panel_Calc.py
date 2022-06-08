import wx
import pandas as pd
from Table import mainTable
from Calc_Damage import Calc_Damage
from math import floor, ceil

columns = ["味方", "相手", "技名", "最低ダメージ", "最高ダメージ", "最低ダメージ割合", "最高ダメージ割合", "味方レベル", "味方特性", "味方攻撃実数値", "味方性格", "味方持ち物", "味方ダイマックス", "相手レベル", "相手特性", "相手HP実数値", "相手性格", "相手持ち物", "相手ダイマックス"]
char_list = ["さみしがり", "いじっぱり", "やんちゃ", "ゆうかん", "ずぶとい", "わんぱく", "のうてんき", "のんき", "ひかえめ", "おっとり", "うっかりや", "れいせい", "おだやか", "おとなしい", "しんちょう", "なまいき	", "おくびょう", "せっかち", "ようき", "むじゃき", "がんばりや",  "てれや", "すなお", "きまぐれ",  "まじめ"]
field_ = ["エレキ", "グラス", "ミスト", "サイコ"]
ex = ["光の壁", "リフレクター", "オーロラベール"]
invent_list = []

class PK_calc_Panel(wx.Panel):
    def __init__(self, parent, setting):
        super().__init__(parent=parent, id=wx.ID_ANY)
        self.setting = setting
        self.size = parent.size
        self.parent = parent

        # データの出力先
        self.output = mainTable(self, size=wx.Size(900, 180))

        # SQL接続
        self.conn = parent.conn
        self.cursor = parent.cursor

        # 覚える技リストの取得
        self.use_move_data = parent.use_move_data

        # 使用するデータ
        self.get_target_data()
        self.df_move_all = parent.df_move_all
        self.use_data = list()

        # 図鑑で追加したポケモンのリスト
        self.pk_list = self.pk_name_list

        # 出力パネルのレイアウト
        button_layout = self.set_add_button()
        panel_layout = wx.BoxSizer(wx.VERTICAL)
        panel_layout.Add(wx.StaticText(self, -1, " "))
        panel_layout.Add(self.get_panel_layout(), flag=wx.SHAPED | wx.ALIGN_CENTER)
        panel_layout.Add(wx.StaticText(self, -1, " "))
        panel_layout.Add(button_layout, flag=wx.SHAPED | wx.ALIGN_CENTER)
        panel_layout.Add(wx.StaticText(self, -1, " "))
        panel_layout.Add(self.output, flag=wx.SHAPED | wx.ALIGN_CENTER)
        self.SetSizer(panel_layout)

        self.pk_list == []

        # 出力用テーブルのカラム
        for col, v in enumerate(columns):
            self.output.InsertColumn(col, v)


    # 取得したデータの反映
    def view_pk_list(self, event):
        self.set_output_data()
        self.output.InsertItem(0, self.output_data[0])
        for col in range(1, len(self.output_data)):
            self.output.SetItem(0,col,str(self.output_data[col]))

    # 出力データの成形
    def set_output_data(self):
        pk_data = self.get_move_info()
        damage = Calc_Damage(pk_data=pk_data, df_move=self.df_move_all, df_pk=self.df_pk)
        self.damage_m = damage.get_damage(0.85)
        self.damage_M = damage.get_damage(1)
        self.output_data = list()
        self.output_data.append(self.pk_name_my)
        self.output_data.append(self.pk_name_enem)
        self.output_data.append(self.move_name)
        self.output_data.append(self.damage_m)
        self.output_data.append(self.damage_M)
        self.output_data.append(str(round(self.damage_m / self.H_correct_enem * 100, 2)) + "%")
        self.output_data.append(str(round(self.damage_M / self.H_correct_enem * 100, 2)) + "%")
        self.output_data.append(self.pk_level_my)
        self.output_data.append(self.pk_abi_my)
        self.output_data.append(self.AC)
        self.output_data.append(self.char_box_my.GetValue())
        self.output_data.append(self.pk_invent_my)
        self.output_data.append(self.pk_big_my)
        self.output_data.append(self.pk_level_enem)
        self.output_data.append(self.pk_abi_enem)
        self.output_data.append(self.H_correct_enem)
        self.output_data.append(self.char_box_enem.GetValue())
        self.output_data.append(self.pk_invent_enem)
        self.output_data.append(self.pk_big_enem)

    # ダメージ計算用のデータ取得
    def get_move_info(self):
        # 攻撃側
        self.pk_name_my = self.name_box_my.GetValue()
        self.pk_folm_my = self.folm_box_my.GetValue()
        self.pk_level_my = self.level_box_my.GetValue()
        self.pk_abi_my = self.ability_box_my.GetValue()
        self.pk_invent_my = self.invent_box_my.GetValue()
        pk_condi_my = self.condi_box_my.GetValue()
        self.pk_big_my = self.big_box_my.GetValue()

        # 防御側
        self.pk_name_enem = self.name_box_enem.GetValue()
        pk_folm_enem = self.folm_box_enem.GetValue()
        self.pk_level_enem = self.level_box_enem.GetValue()
        self.pk_abi_enem = self.ability_box_enem.GetValue()
        self.pk_invent_enem = self.invent_box_enem.GetValue()
        self.pk_big_enem = self.big_box_enem.GetValue()

        # 技
        self.move_name = self.move_box.GetValue()
        df_use_move = self.df_move_all[self.df_move_all["名前"]==self.move_name]
        move_class = df_use_move["分類"].tolist()[0]

        # 各種補正
        weather = self.weather_box.GetValue()
        field = self.field_box.GetValue()
        critical = self.critical_box.GetValue()

        # ステータス
        self.H_correct_enem = int(self.H_real_correct_enem.GetValue())
        self.S_correct_my = int(self.S_real_correct_my.GetValue())
        self.S_correct_enem = int(self.S_real_correct_enem.GetValue())
        if move_class == "物理":
            self.AC = int(self.A_real_correct_my.GetValue())
            self.BD = int(self.B_real_correct_enem.GetValue())
        elif move_class == "特殊":
            self.AC = int(self.C_real_correct_my.GetValue())
            self.BD = int(self.D_real_correct_enem.GetValue())
        else:
            self.AC = 0
            self.BD = 0

        # 計算用データ
        for_move_list = list()
        pk_list_my = [self.pk_name_my, self.pk_folm_my, self.pk_level_my, self.pk_abi_my, self.pk_invent_my, pk_condi_my, self.pk_big_my]
        pk_list_enem = [self.pk_name_enem, pk_folm_enem, self.pk_level_enem, self.pk_abi_enem, self.pk_invent_enem, self.pk_big_enem]
        move_data = [self.move_name, weather, field, critical]
        status_data = [self.H_correct_enem, self.S_correct_my, self.S_correct_enem, self.AC, self.BD]

        for_move_list.append(pk_list_my)
        for_move_list.append(pk_list_enem)
        for_move_list.append(move_data)
        for_move_list.append(status_data)
        return for_move_list

    # ポケモン図鑑データの準備
    def get_target_data(self):
        sql = """
            Select pk_nomal.名前, pk_nomal.フォルム, pk_fight.タイプ1, pk_fight.タイプ2, pk_fight.特性1, pk_fight.特性2, pk_fight.夢特性, pk_status.合計値, pk_status.H, pk_status.A, pk_status.B, pk_status.C, pk_status.D, pk_status.S
            From pk_status, pk_nomal, pk_fight
            Where pk_status.名前 = pk_nomal.名前 and pk_status.フォルム = pk_nomal.フォルム and pk_status.名前 = pk_nomal.名前
            and pk_status.名前 = pk_fight.名前 and pk_status.フォルム = pk_fight.フォルム and pk_status.名前 = pk_fight.名前
        """
        self.df_pk = pd.read_sql_query(sql=sql, con=self.conn)
        self.pk_name_list = list(self.df_pk["名前"].unique())
        self.pk_name_list.sort()
        
    # 覚える技の取得
    def pk_use_move_list(self, event):
        toggle = self.series_button.GetValue()
        use_move_list_my = self.use_move_data[self.name]["Move"]
        use_move_list = list(use_move_list_my.keys())
        use_move_list.sort()
        self.move_box.Clear()
        self.move_box.SetValue(use_move_list[0])
        for move in use_move_list:
            if "*" not in move:
                self.move_box.Append(move)

    # 実数値の計算式
    def calc_status(self, targ, st, indi, effort, level):
        if targ == "H":
            HP = self.round_056((st*2+indi+effort//4) * (level/100)) + (10+level)
            return HP
        return self.round_056((st*2+indi+effort//4) * (level/100)) + 5

    # ランク補正
    def rank_rate(self, rank):
        rate = (2 + abs(rank)) / 2
        if rank < 0:
            rate **= -1
        return rate

    # 性格補正の計算
    def calc_char(self, st, char):
        if st == "A":
            if char == "さみしがり":
                return 1.1

            elif char == "いじっぱり":
                return 1.1
                
            elif char == "やんちゃ":
                return 1.1
                
            elif char == "ゆうかん":
                return 1.1
                
            elif char == "ずぶとい":
                return 0.9
                
            elif char == "ひかえめ":
                return 0.9
                
            elif char == "おだやか":
                return 0.9
                
            elif char == "おくびょう":
                return 0.9
            return 1

        elif st == "B":
            if char == "さみしがり":
                return 0.9

            elif char == "ずぶとい":
                return 1.1
                
            elif char == "わんぱく":
                return 1.1
                
            elif char == "のうてんき":
                return 1.1
                
            elif char == "のんき":
                return 1.1

            elif char == "おっとり":
                return 0.9
                
            elif char == "おとなしい":
                return 0.9

            elif char == "せっかち":
                return 0.9
            return 1

        elif st == "C":
            if char == "いじっぱり":
                return 0.9

            elif char == "わんぱく":
                return 0.9

            elif char == "ひかえめ":
                return 1.1
                
            elif char == "おっとり":
                return 1.1
                
            elif char == "うっかりや":
                return 1.1
                
            elif char == "れいせい":
                return 1.1

            elif char == "しんちょう":
                return 0.9

            elif char == "ようき":
                return 0.9
            return 1

        elif st == "D":
            if char == "やんちゃ":
                return 0.9

            elif char == "のうてんき":
                return 0.9
            
            elif char == "うっかりや":
                return 0.9
            
            elif char == "おだやか":
                return 1.1
                
            elif char == "おとなしい":
                return 1.1
                
            elif char == "しんちょう":
                return 1.1
                
            elif char == "なまいき":
                return 1.1
                        
            elif char == "むじゃき":
                return 0.9
            return 1
            
        elif st == "S":
            if char == "ゆうかん":
                return 0.9

            elif char == "のんき":
                return 0.9

            elif char == "れいせい":
                return 0.9

            elif char == "なまいき":
                return 0.9
                        
            elif char == "おくびょう":
                return 1.1

            elif char == "せっかち":
                return 1.1
                
            elif char == "ようき":
                return 1.1
                    
            elif char == "むじゃき":
                return 1.1
            return 1

    # 五捨五超入用の関数(小数用)
    def round_056(self, num):
        if num % 1 <= 5:
            return floor(num)
        return ceil(num)

    # 実数値の計算
    def calc_status_my(self, event):
        name_my = self.name_box_my.GetValue()
        folm_my = self.folm_box_my.GetValue()
        self.df_pk_my = self.df_pk[(self.df_pk["名前"]==name_my)&(self.df_pk["フォルム"]==folm_my)]
        self.pk_level_my = self.level_box_my.GetValue()
        self.char = self.char_box_my.GetValue()
        self.calc_H_status_my(event)
        self.calc_A_status_my(event)
        self.calc_B_status_my(event)
        self.calc_C_status_my(event)
        self.calc_D_status_my(event)
        self.calc_S_status_my(event)

    def calc_H_status_my(self, event):
        H_indi_my = self.H_indivi_my.GetValue()
        H_effort_my = self.H_effort_my.GetValue()
        if (0 <= H_indi_my <= 31) and (0 <= H_effort_my <=  255) and (self.sum_effort_my.GetValue() != "Error"):
            self.H_real_value_my = self.calc_status(targ="H", st=self.df_pk_my["H"].tolist()[0], indi=H_indi_my, effort=H_effort_my, level=self.pk_level_my)
            self.H_correct_my = self.H_real_value_my
            if self.big_box_my.GetValue() == "あり":
                self.H_correct_my = self.H_real_value_my * 2
            self.H_real_my.SetValue(str(self.H_real_value_my))
            self.H_real_correct_my.SetValue(str(self.H_correct_my))
        else:
            self.H_real_my.SetValue("Error")
            self.H_real_correct_my.SetValue("Error")

    def calc_A_status_my(self, event):
        A_indi_my = self.A_indivi_my.GetValue()
        A_effort_my = self.A_effort_my.GetValue()
        A_rank_my = self.A_rank_my.GetValue()
        if (0 <= A_indi_my <= 31) and (0 <= A_effort_my <=  255) and (self.sum_effort_my.GetValue() != "Error"):
            self.A_real_value_my = self.calc_status(targ="A", st=self.df_pk_my["A"].to_list()[0], indi=A_indi_my, effort=A_effort_my, level=self.pk_level_my)
            self.A_correct_my = floor(floor(self.A_real_value_my * self.calc_char(st="A", char=self.char)) * self.rank_rate(A_rank_my))
            self.A_real_my.SetValue(str(self.A_real_value_my))
            self.A_real_correct_my.SetValue(str(self.A_correct_my))
        else:
            self.A_real_my.SetValue("Error")
            self.A_real_correct_my.SetValue("Error")

    def calc_B_status_my(self, event):
        B_indi_my = self.B_indivi_my.GetValue()
        B_effort_my = self.B_effort_my.GetValue()
        B_rank_my = self.B_rank_my.GetValue()
        if (0 <= B_indi_my <= 31) and (0 <= B_effort_my <=  255) and (self.sum_effort_my.GetValue() != "Error"):
            self.B_real_value_my = self.calc_status(targ="B", st=self.df_pk_my["B"].to_list()[0], indi=B_indi_my, effort=B_effort_my, level=self.pk_level_my)
            self.B_correct_my = floor(floor(self.B_real_value_my * self.calc_char(st="B", char=self.char)) * self.rank_rate(B_rank_my))
            self.B_real_my.SetValue(str(self.B_real_value_my))
            self.B_real_correct_my.SetValue(str(self.B_correct_my))
        else:
            self.B_real_my.SetValue("Error")
            self.B_real_correct_my.SetValue("Error")

    def calc_C_status_my(self, event):
        C_indi_my = self.C_indivi_my.GetValue()
        C_effort_my = self.C_effort_my.GetValue()
        C_rank_my = self.C_rank_my.GetValue()
        if (0 <= C_indi_my <= 31) and (0 <= C_effort_my <=  255) and (self.sum_effort_my.GetValue() != "Error"):
            self.C_real_value_my = self.calc_status(targ="C", st=self.df_pk_my["C"].to_list()[0], indi=C_indi_my, effort=C_effort_my, level=self.pk_level_my)
            self.C_correct_my = floor(floor(self.C_real_value_my * self.calc_char(st="C", char=self.char)) * self.rank_rate(C_rank_my))
            self.C_real_my.SetValue(str(self.C_real_value_my))
            self.C_real_correct_my.SetValue(str(self.C_correct_my))
        else:
            self.C_real_my.SetValue("Error")
            self.C_real_correct_my.SetValue("Error")

    def calc_D_status_my(self, event):
        D_indi_my = self.D_indivi_my.GetValue()
        D_effort_my = self.D_effort_my.GetValue()
        D_rank_my = self.D_rank_my.GetValue()
        if (0 <= D_indi_my <= 31) and (0 <= D_effort_my <=  255) and (self.sum_effort_my.GetValue() != "Error"):
            self.D_real_value_my = self.calc_status(targ="D", st=self.df_pk_my["D"].to_list()[0], indi=D_indi_my, effort=D_effort_my, level=self.pk_level_my)
            self.D_correct_my = floor(floor(self.D_real_value_my * self.calc_char(st="D", char=self.char)) * self.rank_rate(D_rank_my))
            self.D_real_my.SetValue(str(self.D_real_value_my))
            self.D_real_correct_my.SetValue(str(self.D_correct_my))
        else:
            self.D_real_my.SetValue("Error")
            self.D_real_correct_my.SetValue("Error")

    def calc_S_status_my(self, event):
        S_indi_my = self.S_indivi_my.GetValue()
        S_effort_my = self.S_effort_my.GetValue()
        S_rank_my = self.S_rank_my.GetValue()
        if (0 <= S_indi_my <= 31) and (0 <= S_effort_my <=  255) and (self.sum_effort_my.GetValue() != "Error"):
            self.S_real_value_my = self.calc_status(targ="S", st=self.df_pk_my["S"].to_list()[0], indi=S_indi_my, effort=S_effort_my, level=self.pk_level_my)
            self.S_correct_my = floor(floor(self.S_real_value_my * self.calc_char(st="S", char=self.char)) * self.rank_rate(S_rank_my))
            self.S_real_my.SetValue(str(self.S_real_value_my))
            self.S_real_correct_my.SetValue(str(self.S_correct_my))
        else:
            self.S_real_my.SetValue("Error")
            self.S_real_correct_my.SetValue("Error")

    def calc_status_enem(self, event):
        name_enem = self.name_box_enem.GetValue()
        folm_enem = self.folm_box_enem.GetValue()
        self.df_pk_enem = self.df_pk[(self.df_pk["名前"]==name_enem)&(self.df_pk["フォルム"]==folm_enem)]
        self.pk_level_enem = self.level_box_enem.GetValue()
        self.char = self.char_box_enem.GetValue()
        self.calc_H_status_enem(event)
        self.calc_A_status_enem(event)
        self.calc_B_status_enem(event)
        self.calc_C_status_enem(event)
        self.calc_D_status_enem(event)
        self.calc_S_status_enem(event)

    def calc_H_status_enem(self, event):
        H_indi_enem = self.H_indivi_enem.GetValue()
        H_effort_enem = self.H_effort_enem.GetValue()
        if (0 <= H_indi_enem <= 31) and (0 <= H_effort_enem <=  255) and (self.sum_effort_enem.GetValue() != "Error"):
            self.H_real_value_enem = self.calc_status(targ="H", st=self.df_pk_enem["H"].tolist()[0], indi=H_indi_enem, effort=H_effort_enem, level=self.pk_level_enem)
            self.H_correct_enem = self.H_real_value_enem
            if self.big_box_enem.GetValue() == "あり":
                self.H_correct_enem = self.H_real_value_enem * 2
            self.H_real_enem.SetValue(str(self.H_real_value_enem))
            self.H_real_correct_enem.SetValue(str(self.H_correct_enem))
        else:
            self.H_real_enem.SetValue("Error")
            self.H_real_correct_enem.SetValue("Error")

    def calc_A_status_enem(self, event):
        A_indi_enem = self.A_indivi_enem.GetValue()
        A_effort_enem = self.A_effort_enem.GetValue()
        A_rank_enem = self.A_rank_enem.GetValue()
        if (0 <= A_indi_enem <= 31) and (0 <= A_effort_enem <=  255) and (self.sum_effort_enem.GetValue() != "Error"):
            self.A_real_value_enem = self.calc_status(targ="A", st=self.df_pk_enem["A"].to_list()[0], indi=A_indi_enem, effort=A_effort_enem, level=self.pk_level_enem)
            self.A_correct_enem = floor(floor(self.A_real_value_enem * self.calc_char(st="A", char=self.char)) * self.rank_rate(A_rank_enem))
            self.A_real_enem.SetValue(str(self.A_real_value_enem))
            self.A_real_correct_enem.SetValue(str(self.A_correct_enem))
        else:
            self.A_real_enem.SetValue("Error")
            self.A_real_correct_enem.SetValue("Error")

    def calc_B_status_enem(self, event):
        B_indi_enem = self.B_indivi_enem.GetValue()
        B_effort_enem = self.B_effort_enem.GetValue()
        B_rank_enem = self.B_rank_enem.GetValue()
        if (0 <= B_indi_enem <= 31) and (0 <= B_effort_enem <=  255) and (self.sum_effort_enem.GetValue() != "Error"):
            self.B_real_value_enem = self.calc_status(targ="B", st=self.df_pk_enem["B"].to_list()[0], indi=B_indi_enem, effort=B_effort_enem, level=self.pk_level_enem)
            self.B_correct_enem = floor(floor(self.B_real_value_enem * self.calc_char(st="B", char=self.char)) * self.rank_rate(B_rank_enem))
            self.B_real_enem.SetValue(str(self.B_real_value_enem))
            self.B_real_correct_enem.SetValue(str(self.B_correct_enem))
        else:
            self.B_real_enem.SetValue("Error")
            self.B_real_correct_enem.SetValue("Error")

    def calc_C_status_enem(self, event):
        C_indi_enem = self.C_indivi_enem.GetValue()
        C_effort_enem = self.C_effort_enem.GetValue()
        C_rank_enem = self.C_rank_enem.GetValue()
        if (0 <= C_indi_enem <= 31) and (0 <= C_effort_enem <=  255) and (self.sum_effort_enem.GetValue() != "Error"):
            self.C_real_value_enem = self.calc_status(targ="C", st=self.df_pk_enem["C"].to_list()[0], indi=C_indi_enem, effort=C_effort_enem, level=self.pk_level_enem)
            self.C_correct_enem = floor(floor(self.C_real_value_enem * self.calc_char(st="C", char=self.char)) * self.rank_rate(C_rank_enem))
            self.C_real_enem.SetValue(str(self.C_real_value_enem))
            self.C_real_correct_enem.SetValue(str(self.C_correct_enem))
        else:
            self.C_real_enem.SetValue("Error")
            self.C_real_correct_enem.SetValue("Error")

    def calc_D_status_enem(self, event):
        D_indi_enem = self.D_indivi_enem.GetValue()
        D_effort_enem = self.D_effort_enem.GetValue()
        D_rank_enem = self.D_rank_enem.GetValue()
        if (0 <= D_indi_enem <= 31) and (0 <= D_effort_enem <=  255) and (self.sum_effort_enem.GetValue() != "Error"):
            self.D_real_value_enem = self.calc_status(targ="D", st=self.df_pk_enem["D"].to_list()[0], indi=D_indi_enem, effort=D_effort_enem, level=self.pk_level_enem)
            self.D_correct_enem = floor(floor(self.D_real_value_enem * self.calc_char(st="D", char=self.char)) * self.rank_rate(D_rank_enem))
            self.D_real_enem.SetValue(str(self.D_real_value_enem))
            self.D_real_correct_enem.SetValue(str(self.D_correct_enem))
        else:
            self.D_real_enem.SetValue("Error")
            self.D_real_correct_enem.SetValue("Error")

    def calc_S_status_enem(self, event):
        S_indi_enem = self.S_indivi_enem.GetValue()
        S_effort_enem = self.S_effort_enem.GetValue()
        S_rank_enem = self.S_rank_enem.GetValue()
        if (0 <= S_indi_enem <= 31) and (0 <= S_effort_enem <=  255) and (self.sum_effort_enem.GetValue() != "Error"):
            self.S_real_value_enem = self.calc_status(targ="S", st=self.df_pk_enem["S"].to_list()[0], indi=S_indi_enem, effort=S_effort_enem, level=self.pk_level_enem)
            self.S_correct_enem = floor(floor(self.S_real_value_enem * self.calc_char(st="S", char=self.char)) * self.rank_rate(S_rank_enem))
            self.S_real_enem.SetValue(str(self.S_real_value_enem))
            self.S_real_correct_enem.SetValue(str(self.S_correct_enem))
        else:
            self.S_real_enem.SetValue("Error")
            self.S_real_correct_enem.SetValue("Error")

    # 名前変更時
    def set_valuses_my(self, event):
        self.name = self.name_box_my.GetValue()
        pk_data = self.df_pk[self.df_pk["名前"]==self.name]

        self.folm_box_my.Clear()
        folm = pk_data["フォルム"].tolist()
        self.folm_box_my.SetValue(folm[0])
        for f in folm:
            self.folm_box_my.Append(f)

        abi1 = pk_data["特性1"].tolist()[0]
        abi2 = pk_data["特性2"].tolist()[0]
        abi3 = pk_data["夢特性"].tolist()[0]
        self.ability_box_my.Clear()
        self.ability_box_my.Append(abi1)
        self.ability_box_my.SetValue(abi1)
        if abi2 != "-":
            self.ability_box_my.AppendItems(abi2)        
        if abi3 != "-":
            self.ability_box_my.AppendItems(abi3)

        self.H_race_my.SetValue(str(pk_data["H"].tolist()[0]))
        self.A_race_my.SetValue(str(pk_data["A"].tolist()[0]))
        self.B_race_my.SetValue(str(pk_data["B"].tolist()[0]))
        self.C_race_my.SetValue(str(pk_data["C"].tolist()[0]))
        self.D_race_my.SetValue(str(pk_data["D"].tolist()[0]))
        self.S_race_my.SetValue(str(pk_data["S"].tolist()[0]))
        self.sum_race_my.SetValue(str(pk_data["合計値"].tolist()[0]))
        self.calc_status_my(event)
        self.pk_use_move_list(event)

    def set_valuses_enem(self, event):
        name = self.name_box_enem.GetValue()
        pk_data = self.df_pk[self.df_pk["名前"]==name]

        self.folm_box_enem.Clear()
        folm = pk_data["フォルム"].tolist()
        self.folm_box_enem.SetValue(folm[0])
        for f in folm:
            self.folm_box_enem.Append(f)

        abi1 = pk_data["特性1"].tolist()[0]
        abi2 = pk_data["特性2"].tolist()[0]
        abi3 = pk_data["夢特性"].tolist()[0]
        self.ability_box_enem.Clear()
        self.ability_box_enem.Append(abi1)
        self.ability_box_enem.SetValue(abi1)
        if abi2 != "-":
            self.ability_box_enem.AppendItems(abi2)        
        if abi3 != "-":
            self.ability_box_enem.AppendItems(abi3)
        
        self.H_race_enem.SetValue(str(pk_data["H"].tolist()[0]))
        self.A_race_enem.SetValue(str(pk_data["A"].tolist()[0]))
        self.B_race_enem.SetValue(str(pk_data["B"].tolist()[0]))
        self.C_race_enem.SetValue(str(pk_data["C"].tolist()[0]))
        self.D_race_enem.SetValue(str(pk_data["D"].tolist()[0]))
        self.S_race_enem.SetValue(str(pk_data["S"].tolist()[0]))
        self.sum_race_enem.SetValue(str(pk_data["合計値"].tolist()[0]))
        self.calc_status_enem(event)

    # フォルム変更時
    def set_values_folm_my(self, event):
        pk_data = self.df_pk[(self.df_pk["名前"]==self.name_box_my.GetValue()) & (self.df_pk["フォルム"]==self.folm_box_my.GetValue())]
        self.H_race_my.SetValue(str(pk_data["H"].tolist()[0]))
        self.A_race_my.SetValue(str(pk_data["A"].tolist()[0]))
        self.B_race_my.SetValue(str(pk_data["B"].tolist()[0]))
        self.C_race_my.SetValue(str(pk_data["C"].tolist()[0]))
        self.D_race_my.SetValue(str(pk_data["D"].tolist()[0]))
        self.S_race_my.SetValue(str(pk_data["S"].tolist()[0]))
        self.sum_race_my.SetValue(str(pk_data["合計値"].tolist()[0]))
        self.calc_status_my(event)

    def set_values_folm_enem(self, event):
        pk_data = self.df_pk[(self.df_pk["名前"]==self.name_box_enem.GetValue()) & (self.df_pk["フォルム"]==self.folm_box_enem.GetValue())]
        self.H_race_enem.SetValue(str(pk_data["H"].tolist()[0]))
        self.A_race_enem.SetValue(str(pk_data["A"].tolist()[0]))
        self.B_race_enem.SetValue(str(pk_data["B"].tolist()[0]))
        self.C_race_enem.SetValue(str(pk_data["C"].tolist()[0]))
        self.D_race_enem.SetValue(str(pk_data["D"].tolist()[0]))
        self.S_race_enem.SetValue(str(pk_data["S"].tolist()[0]))
        self.sum_race_enem.SetValue(str(pk_data["合計値"].tolist()[0]))
        self.calc_status_enem(event)
    
    # 努力値配分の設定
    def set_effort_my(self, event):
        count = int(self.H_effort_my.GetValue()) + int(self.A_effort_my.GetValue()) + int(self.B_effort_my.GetValue()) + int(self.C_effort_my.GetValue()) + int(self.D_effort_my.GetValue()) + int(self.S_effort_my.GetValue())
        if count > 510:
            count = "Error"
        self.sum_effort_my.SetValue(str(count))
        self.calc_status_my(event)

    def set_effort_enem(self, event):
        count = int(self.H_effort_enem.GetValue()) + int(self.A_effort_enem.GetValue()) + int(self.B_effort_enem.GetValue()) + int(self.C_effort_enem.GetValue()) + int(self.D_effort_enem.GetValue()) + int(self.S_effort_enem.GetValue())
        if count > 510:
            count = "Error"
        self.sum_effort_enem.SetValue(str(count))
        self.calc_status_enem(event)

    # 各種パーツの作成、レイアウト
    def set_add_button(self):
        move = wx.StaticText(self, -1, "技", size=self.size)
        self.move_box = wx.ComboBox(self, -1, "技", size=self.size, choices=[])
        critical = wx.StaticText(self, -1, "急所", size=self.size)
        self.critical_box = wx.ComboBox(self, -1, "急所", size=self.size, choices=["あり", "なし"])
        weather = wx.StaticText(self, -1, "天候", size=self.size)
        self.weather_box = wx.ComboBox(self, -1, "天候", size=self.size, choices=["晴", "雨", "砂嵐", "霰", "旱", "大雨", "乱気流"])
        pfield = wx.StaticText(self, -1, "フィールド", size=self.size)
        self.field_box = wx.ComboBox(self, -1, "フィールド", size=self.size, choices=field_)
        search_button = wx.Button(self, -1, "計算", size=self.size)
        search_button.Bind(wx.EVT_BUTTON, self.view_pk_list)
        reset_button = wx.Button(self, -1, "リセット", size=self.size)
        reset_button.Bind(wx.EVT_BUTTON, self.reset_info)
        close_button = wx.Button(self, -1, "停止", size=self.size)
        close_button.Bind(wx.EVT_BUTTON, self.app_close)
        self.series_button = wx.ToggleButton(self, -1, "過去作", size=self.size)
        self.series_button.Bind(wx.EVT_TOGGLEBUTTON, self.pk_use_move_list)

        button_layout = wx.GridSizer(2, 6, 0, 0)
        button_layout.Add(move)
        button_layout.Add(self.move_box)
        button_layout.Add(critical)
        button_layout.Add(self.critical_box)
        button_layout.Add(search_button)
        button_layout.Add(reset_button)
        button_layout.Add(weather)
        button_layout.Add(self.weather_box)
        button_layout.Add(pfield)
        button_layout.Add(self.field_box)
        button_layout.Add(self.series_button)
        button_layout.Add(close_button)
        return button_layout

    def get_panel_layout(self):
        my_pk_layout = wx.BoxSizer(wx.HORIZONTAL)
        my_pk_layout.Add(self.pk_layout_text("my"))
        my_pk_layout.Add(self.pk_layout_my())
        my_pk_layout.Add(self.status_layout_my())
        my_pk_layout.Add(wx.StaticText(self, -1, "->", size=self.size, style=wx.TE_CENTER), flag=wx.ALIGN_CENTER)
        my_pk_layout.Add(self.effort_layout_my())

        enem_pk_layout = wx.BoxSizer(wx.HORIZONTAL)
        enem_pk_layout.Add(self.pk_layout_text("enem"))
        enem_pk_layout.Add(self.pk_layout_enem())
        enem_pk_layout.Add(self.status_layout_enem())
        enem_pk_layout.Add(wx.StaticText(self, -1, "->", size=self.size, style=wx.TE_CENTER), flag=wx.ALIGN_CENTER)
        enem_pk_layout.Add(self.effort_layout_enem())

        space = wx.StaticText(self, -1, "", size=self.size)
        panel_layout = wx.BoxSizer(wx.VERTICAL)
        panel_layout.Add(wx.StaticText(self, -1, "攻撃側", size=self.size))
        panel_layout.Add(my_pk_layout)
        panel_layout.Add(space)
        panel_layout.Add(wx.StaticText(self, -1, "防御側", size=self.size))
        panel_layout.Add(enem_pk_layout)
        return panel_layout

    def effort_layout_my(self):
        real = wx.StaticText(self, -1, "実数値", size=self.size)
        self.H_real_my = wx.TextCtrl(self, -1, "", size=self.size)
        self.A_real_my = wx.TextCtrl(self, -1, "", size=self.size)
        self.B_real_my = wx.TextCtrl(self, -1, "", size=self.size)
        self.C_real_my = wx.TextCtrl(self, -1, "", size=self.size)
        self.D_real_my = wx.TextCtrl(self, -1, "", size=self.size)
        self.S_real_my = wx.TextCtrl(self, -1, "", size=self.size)
        real_correct = wx.StaticText(self, -1, "補正込実数値", size=(75, 20))
        self.H_real_correct_my = wx.TextCtrl(self, -1, "", size=self.size)
        self.A_real_correct_my = wx.TextCtrl(self, -1, "", size=self.size)
        self.B_real_correct_my = wx.TextCtrl(self, -1, "", size=self.size)
        self.C_real_correct_my = wx.TextCtrl(self, -1, "", size=self.size)
        self.D_real_correct_my = wx.TextCtrl(self, -1, "", size=self.size)
        self.S_real_correct_my = wx.TextCtrl(self, -1, "", size=self.size)
        layout = wx.GridSizer(7, 2, 0, 0)
        layout.Add(real)
        layout.Add(real_correct)
        layout.Add(self.H_real_my)
        layout.Add(self.H_real_correct_my)
        layout.Add(self.A_real_my)
        layout.Add(self.A_real_correct_my)
        layout.Add(self.B_real_my)
        layout.Add(self.B_real_correct_my)
        layout.Add(self.C_real_my)
        layout.Add(self.C_real_correct_my)
        layout.Add(self.D_real_my)
        layout.Add(self.D_real_correct_my)
        layout.Add(self.S_real_my)
        layout.Add(self.S_real_correct_my)
        return layout

    def effort_layout_enem(self):
        real = wx.StaticText(self, -1, "実数値", size=self.size)
        self.H_real_enem = wx.TextCtrl(self, -1, "", size=self.size)
        self.A_real_enem = wx.TextCtrl(self, -1, "", size=self.size)
        self.B_real_enem = wx.TextCtrl(self, -1, "", size=self.size)
        self.C_real_enem = wx.TextCtrl(self, -1, "", size=self.size)
        self.D_real_enem = wx.TextCtrl(self, -1, "", size=self.size)
        self.S_real_enem = wx.TextCtrl(self, -1, "", size=self.size)
        real_correct = wx.StaticText(self, -1, "補正込実数値", size=(75, 20))
        self.H_real_correct_enem = wx.TextCtrl(self, -1, "", size=self.size)
        self.A_real_correct_enem = wx.TextCtrl(self, -1, "", size=self.size)
        self.B_real_correct_enem = wx.TextCtrl(self, -1, "", size=self.size)
        self.C_real_correct_enem = wx.TextCtrl(self, -1, "", size=self.size)
        self.D_real_correct_enem = wx.TextCtrl(self, -1, "", size=self.size)
        self.S_real_correct_enem = wx.TextCtrl(self, -1, "", size=self.size)
        layout = wx.GridSizer(7, 2, 0, 0)
        layout.Add(real)
        layout.Add(real_correct)
        layout.Add(self.H_real_enem)
        layout.Add(self.H_real_correct_enem)
        layout.Add(self.A_real_enem)
        layout.Add(self.A_real_correct_enem)
        layout.Add(self.B_real_enem)
        layout.Add(self.B_real_correct_enem)
        layout.Add(self.C_real_enem)
        layout.Add(self.C_real_correct_enem)
        layout.Add(self.D_real_enem)
        layout.Add(self.D_real_correct_enem)
        layout.Add(self.S_real_enem)
        layout.Add(self.S_real_correct_enem)
        return layout

    def pk_layout_text(self, lab):
        name = wx.StaticText(self, -1, "名前", size=self.size) 
        folm = wx.StaticText(self, -1, "フォルム", size=self.size)
        level = wx.StaticText(self, -1, "レベル", size=self.size)
        char = wx.StaticText(self, -1, "性格", size=self.size)
        ability = wx.StaticText(self, -1, "特性", size=self.size)
        invent = wx.StaticText(self, -1, "持ち物", size=self.size)
            
        layout = wx.BoxSizer(wx.VERTICAL)
        layout.Add(name)
        layout.Add(folm)
        layout.Add(level)
        layout.Add(char)
        layout.Add(ability)
        layout.Add(invent)

        if lab == "my":
            condi = wx.StaticText(self, -1, "状態異常", size=self.size)
            layout.Add(condi)
        big = wx.StaticText(self, -1, "ダイマックス", size=self.size)
        layout.Add(big)
        if lab == "enem":
            buff = wx.StaticText(self, -1, "その他", size=self.size)
            layout.Add(buff)
        return layout

    def pk_layout_my(self):
        self.name_box_my = wx.ComboBox(self, -1, "名前", size=self.size, choices=self.pk_list)
        self.name_box_my.Bind(wx.EVT_COMBOBOX, self.set_valuses_my)
        self.folm_box_my = wx.ComboBox(self, -1, "フォルム", size=self.size)
        self.folm_box_my.Bind(wx.EVT_COMBOBOX, self.set_values_folm_my)
        self.level_box_my = wx.SpinCtrl(self, -1, value="50", size=self.size, min=0, max=100)
        self.level_box_my.Bind(wx.EVT_SPINCTRL, self.calc_status_my) 
        self.char_box_my = wx.ComboBox(self, -1, "性格", size=self.size, choices=char_list)
        self.char_box_my.Bind(wx.EVT_COMBOBOX, self.calc_status_my)
        self.ability_box_my = wx.ComboBox(self, -1, "特性", size=self.size)
        self.ability_box_my.Bind(wx.EVT_COMBOBOX, self.calc_status_my)
        self.invent_box_my = wx.ComboBox(self, -1, "持ち物", size=self.size, choices=invent_list)
        self.invent_box_my.Bind(wx.EVT_COMBOBOX, self.calc_status_my)
        self.condi_box_my = wx.ComboBox(self, -1, "状態異常", size=self.size, choices=["火傷", "麻痺", "眠り", "毒", "混乱"])
        self.condi_box_my.Bind(wx.EVT_COMBOBOX, self.calc_status_my)
        self.big_box_my = wx.ComboBox(self, -1, "ダイマックス", size=self.size, choices=["あり", "なし"])
        self.big_box_my.Bind(wx.EVT_COMBOBOX, self.calc_H_status_my)
        layout = wx.BoxSizer(wx.VERTICAL)
        layout.Add(self.name_box_my)
        layout.Add(self.folm_box_my)
        layout.Add(self.level_box_my)
        layout.Add(self.char_box_my)
        layout.Add(self.ability_box_my)
        layout.Add(self.invent_box_my)
        layout.Add(self.condi_box_my)
        layout.Add(self.big_box_my)

        return layout

    def pk_layout_enem(self):
        self.name_box_enem = wx.ComboBox(self, -1, "名前", size=self.size, choices=self.pk_list)
        self.name_box_enem.Bind(wx.EVT_COMBOBOX, self.set_valuses_enem)
        self.folm_box_enem = wx.ComboBox(self, -1, "フォルム", size=self.size)
        self.folm_box_enem.Bind(wx.EVT_COMBOBOX, self.set_values_folm_enem)
        self.level_box_enem = wx.SpinCtrl(self, -1, value="50", size=self.size, min=0, max=100)
        self.level_box_enem.Bind(wx.EVT_SPINCTRL, self.calc_status_enem)
        self.char_box_enem = wx.ComboBox(self, -1, "性格", size=self.size, choices=char_list)
        self.char_box_enem.Bind(wx.EVT_COMBOBOX, self.calc_status_enem)
        self.ability_box_enem = wx.ComboBox(self, -1, "特性", size=self.size)
        self.ability_box_enem.Bind(wx.EVT_COMBOBOX, self.calc_status_enem)
        self.invent_box_enem = wx.ComboBox(self, -1, "持ち物", size=self.size, choices=invent_list)
        self.invent_box_enem.Bind(wx.EVT_COMBOBOX, self.calc_status_enem)
        self.big_box_enem = wx.ComboBox(self, -1, "ダイマックス", size=self.size, choices=["あり", "なし"])
        self.big_box_enem.Bind(wx.EVT_COMBOBOX, self.calc_H_status_enem)
        self.buff_box_enem = wx.ComboBox(self, -1, "その他", size=self.size, choices=ex)
        self.buff_box_enem.Bind(wx.EVT_COMBOBOX, self.calc_status_enem)
        
        layout = wx.BoxSizer(wx.VERTICAL)
        layout.Add(self.name_box_enem)
        layout.Add(self.folm_box_enem)
        layout.Add(self.level_box_enem)
        layout.Add(self.char_box_enem)
        layout.Add(self.ability_box_enem)
        layout.Add(self.invent_box_enem)
        layout.Add(self.big_box_enem)
        layout.Add(self.buff_box_enem)
        return layout

    def status_layout_my(self):
        space = wx.StaticText(self, -1, "", size=self.size)
        H_status = wx.StaticText(self, -1, "HP", size=self.size)
        A_status = wx.StaticText(self, -1, "攻撃", size=self.size)
        B_status = wx.StaticText(self, -1, "防御", size=self.size)
        C_status = wx.StaticText(self, -1, "特攻", size=self.size)
        D_status = wx.StaticText(self, -1, "特防", size=self.size)
        S_status = wx.StaticText(self, -1, "素早さ", size=self.size)

        race = wx.StaticText(self, -1, "種族値", size=self.size)
        self.H_race_my = wx.TextCtrl(self, -1, "0", size=self.size)
        self.A_race_my = wx.TextCtrl(self, -1, "0", size=self.size)
        self.B_race_my = wx.TextCtrl(self, -1, "0", size=self.size)
        self.C_race_my = wx.TextCtrl(self, -1, "0", size=self.size)
        self.D_race_my = wx.TextCtrl(self, -1, "0", size=self.size)
        self.S_race_my = wx.TextCtrl(self, -1, "0", size=self.size)

        effort = wx.StaticText(self, -1, "努力値", size=self.size)
        self.H_effort_my = wx.SpinCtrlDouble(self, -1, size=self.size, min=0, max=255, inc=4)
        self.H_effort_my.Bind(wx.EVT_SPINCTRLDOUBLE, self.set_effort_my)
        self.A_effort_my = wx.SpinCtrlDouble(self, -1, size=self.size, min=0, max=255, inc=4)
        self.A_effort_my.Bind(wx.EVT_SPINCTRLDOUBLE, self.set_effort_my)
        self.B_effort_my = wx.SpinCtrlDouble(self, -1, size=self.size, min=0, max=255, inc=4)
        self.B_effort_my.Bind(wx.EVT_SPINCTRLDOUBLE, self.set_effort_my)
        self.C_effort_my = wx.SpinCtrlDouble(self, -1, size=self.size, min=0, max=255, inc=4)
        self.C_effort_my.Bind(wx.EVT_SPINCTRLDOUBLE, self.set_effort_my)
        self.D_effort_my = wx.SpinCtrlDouble(self, -1, size=self.size, min=0, max=255, inc=4)
        self.D_effort_my.Bind(wx.EVT_SPINCTRLDOUBLE, self.set_effort_my)
        self.S_effort_my = wx.SpinCtrlDouble(self, -1, size=self.size, min=0, max=255, inc=4)
        self.S_effort_my.Bind(wx.EVT_SPINCTRLDOUBLE, self.set_effort_my)

        individual = wx.StaticText(self, -1, "個体値", size=self.size)
        self.H_indivi_my = wx.SpinCtrlDouble(self, -1, value="31", size=self.size,min=0, max=31)
        self.H_indivi_my.Bind(wx.EVT_SPINCTRLDOUBLE, self.calc_H_status_my)
        self.A_indivi_my = wx.SpinCtrlDouble(self, -1, value="31", size=self.size,min=0, max=31)
        self.A_indivi_my.Bind(wx.EVT_SPINCTRLDOUBLE, self.calc_A_status_my)
        self.B_indivi_my = wx.SpinCtrlDouble(self, -1, value="31", size=self.size,min=0, max=31)
        self.B_indivi_my.Bind(wx.EVT_SPINCTRLDOUBLE, self.calc_B_status_my)
        self.C_indivi_my = wx.SpinCtrlDouble(self, -1, value="31", size=self.size,min=0, max=31)
        self.C_indivi_my.Bind(wx.EVT_SPINCTRLDOUBLE, self.calc_C_status_my)
        self.D_indivi_my = wx.SpinCtrlDouble(self, -1, value="31", size=self.size,min=0, max=31)
        self.D_indivi_my.Bind(wx.EVT_SPINCTRLDOUBLE, self.calc_D_status_my)
        self.S_indivi_my = wx.SpinCtrlDouble(self, -1, value="31", size=self.size,min=0, max=31)
        self.S_indivi_my.Bind(wx.EVT_SPINCTRLDOUBLE, self.calc_S_status_my)

        rank = wx.StaticText(self, -1, "ランク", size=self.size)
        self.H_rank_my = wx.StaticText(self, -1, "-", size=self.size, style=wx.TE_CENTER)
        self.A_rank_my = wx.SpinCtrlDouble(self, -1, size=self.size, min=-6, max=6)
        self.A_rank_my.Bind(wx.EVT_SPINCTRLDOUBLE, self.calc_A_status_my)
        self.B_rank_my = wx.SpinCtrlDouble(self, -1, size=self.size, min=-6, max=6)
        self.B_rank_my.Bind(wx.EVT_SPINCTRLDOUBLE, self.calc_B_status_my)
        self.C_rank_my = wx.SpinCtrlDouble(self, -1, size=self.size, min=-6, max=6)
        self.C_rank_my.Bind(wx.EVT_SPINCTRLDOUBLE, self.calc_C_status_my)
        self.D_rank_my = wx.SpinCtrlDouble(self, -1, size=self.size, min=-6, max=6)
        self.D_rank_my.Bind(wx.EVT_SPINCTRLDOUBLE, self.calc_D_status_my)
        self.S_rank_my = wx.SpinCtrlDouble(self, -1, size=self.size, min=-6, max=6)
        self.S_rank_my.Bind(wx.EVT_SPINCTRLDOUBLE, self.calc_S_status_my)

        status_layout = wx.GridSizer(7, 5, 0, 0)
        status_layout.Add(space)
        status_layout.Add(race)
        status_layout.Add(effort)
        status_layout.Add(individual)
        status_layout.Add(rank)

        status_layout.Add(H_status)
        status_layout.Add(self.H_race_my)
        status_layout.Add(self.H_effort_my)
        status_layout.Add(self.H_indivi_my)
        status_layout.Add(self.H_rank_my)

        status_layout.Add(A_status)
        status_layout.Add(self.A_race_my)
        status_layout.Add(self.A_effort_my)
        status_layout.Add(self.A_indivi_my)
        status_layout.Add(self.A_rank_my)

        status_layout.Add(B_status)
        status_layout.Add(self.B_race_my)
        status_layout.Add(self.B_effort_my)
        status_layout.Add(self.B_indivi_my)
        status_layout.Add(self.B_rank_my)

        status_layout.Add(C_status)
        status_layout.Add(self.C_race_my)
        status_layout.Add(self.C_effort_my)
        status_layout.Add(self.C_indivi_my)
        status_layout.Add(self.C_rank_my)

        status_layout.Add(D_status)
        status_layout.Add(self.D_race_my)
        status_layout.Add(self.D_effort_my)
        status_layout.Add(self.D_indivi_my)
        status_layout.Add(self.D_rank_my)

        status_layout.Add(S_status)
        status_layout.Add(self.S_race_my)
        status_layout.Add(self.S_effort_my)
        status_layout.Add(self.S_indivi_my)
        status_layout.Add(self.S_rank_my)

        space_ = wx.StaticText(self, -1, "合計値", size=self.size)
        self.sum_race_my = wx.TextCtrl(self, -1, "0", size=self.size)
        self.sum_effort_my = wx.TextCtrl(self, -1, "0", size=self.size)
        set_indi_my = wx.Button(self, -1, "リセット", size=self.size)
        set_indi_my.Bind(wx.EVT_BUTTON, self.reset_indi_my)
        set_rank_my = wx.Button(self, -1, "リセット", size=self.size)
        set_rank_my.Bind(wx.EVT_BUTTON, self.reset_rank_my)
        add_layout = wx.BoxSizer(wx.HORIZONTAL)
        add_layout.Add(space_)
        add_layout.Add(self.sum_race_my)
        add_layout.Add(self.sum_effort_my)
        add_layout.Add(set_indi_my)
        add_layout.Add(set_rank_my)

        layout = wx.BoxSizer(wx.VERTICAL)
        layout.Add(status_layout)
        layout.Add(add_layout)
        return layout

    def status_layout_enem(self):
        space = wx.StaticText(self, -1, "", size=self.size)
        H_status = wx.StaticText(self, -1, "HP", size=self.size)
        A_status = wx.StaticText(self, -1, "攻撃", size=self.size)
        B_status = wx.StaticText(self, -1, "防御", size=self.size)
        C_status = wx.StaticText(self, -1, "特攻", size=self.size)
        D_status = wx.StaticText(self, -1, "特防", size=self.size)
        S_status = wx.StaticText(self, -1, "素早さ", size=self.size)

        race = wx.StaticText(self, -1, "種族値", size=self.size)
        self.H_race_enem = wx.TextCtrl(self, -1, "0", size=self.size)
        self.A_race_enem = wx.TextCtrl(self, -1, "0", size=self.size)
        self.B_race_enem = wx.TextCtrl(self, -1, "0", size=self.size)
        self.C_race_enem = wx.TextCtrl(self, -1, "0", size=self.size)
        self.D_race_enem = wx.TextCtrl(self, -1, "0", size=self.size)
        self.S_race_enem = wx.TextCtrl(self, -1, "0", size=self.size)

        effort = wx.StaticText(self, -1, "努力値", size=self.size)
        self.H_effort_enem = wx.SpinCtrlDouble(self, -1, size=self.size, min=0, max=255, inc=4)
        self.H_effort_enem.Bind(wx.EVT_SPINCTRLDOUBLE, self.set_effort_enem)
        self.A_effort_enem = wx.SpinCtrlDouble(self, -1, size=self.size, min=0, max=255, inc=4)
        self.A_effort_enem.Bind(wx.EVT_SPINCTRLDOUBLE, self.set_effort_enem)
        self.B_effort_enem = wx.SpinCtrlDouble(self, -1, size=self.size, min=0, max=255, inc=4)
        self.B_effort_enem.Bind(wx.EVT_SPINCTRLDOUBLE, self.set_effort_enem)
        self.C_effort_enem = wx.SpinCtrlDouble(self, -1, size=self.size, min=0, max=255, inc=4)
        self.C_effort_enem.Bind(wx.EVT_SPINCTRLDOUBLE, self.set_effort_enem)
        self.D_effort_enem = wx.SpinCtrlDouble(self, -1, size=self.size, min=0, max=255, inc=4)
        self.D_effort_enem.Bind(wx.EVT_SPINCTRLDOUBLE, self.set_effort_enem)
        self.S_effort_enem = wx.SpinCtrlDouble(self, -1, size=self.size, min=0, max=255, inc=4)
        self.S_effort_enem.Bind(wx.EVT_SPINCTRLDOUBLE, self.set_effort_enem)

        individual = wx.StaticText(self, -1, "個体値", size=self.size)
        self.H_indivi_enem = wx.SpinCtrlDouble(self, -1, value="31", size=self.size,min=0, max=31)
        self.H_indivi_enem.Bind(wx.EVT_SPINCTRLDOUBLE, self.calc_H_status_enem)
        self.A_indivi_enem = wx.SpinCtrlDouble(self, -1, value="31", size=self.size,min=0, max=31)
        self.A_indivi_enem.Bind(wx.EVT_SPINCTRLDOUBLE, self.calc_A_status_enem)
        self.B_indivi_enem = wx.SpinCtrlDouble(self, -1, value="31", size=self.size,min=0, max=31)
        self.B_indivi_enem.Bind(wx.EVT_SPINCTRLDOUBLE, self.calc_B_status_enem)
        self.C_indivi_enem = wx.SpinCtrlDouble(self, -1, value="31", size=self.size,min=0, max=31)
        self.C_indivi_enem.Bind(wx.EVT_SPINCTRLDOUBLE, self.calc_C_status_enem)
        self.D_indivi_enem = wx.SpinCtrlDouble(self, -1, value="31", size=self.size,min=0, max=31)
        self.D_indivi_enem.Bind(wx.EVT_SPINCTRLDOUBLE, self.calc_D_status_enem)
        self.S_indivi_enem = wx.SpinCtrlDouble(self, -1, value="31", size=self.size,min=0, max=31)
        self.S_indivi_enem.Bind(wx.EVT_SPINCTRLDOUBLE, self.calc_S_status_enem)

        rank = wx.StaticText(self, -1, "ランク", size=self.size)
        self.H_rank_enem = wx.StaticText(self, -1, "-", size=self.size, style=wx.TE_CENTER)
        self.A_rank_enem = wx.SpinCtrlDouble(self, -1, size=self.size, min=-6, max=6)
        self.A_rank_enem.Bind(wx.EVT_SPINCTRLDOUBLE, self.calc_A_status_enem)
        self.B_rank_enem = wx.SpinCtrlDouble(self, -1, size=self.size, min=-6, max=6)
        self.B_rank_enem.Bind(wx.EVT_SPINCTRLDOUBLE, self.calc_B_status_enem)
        self.C_rank_enem = wx.SpinCtrlDouble(self, -1, size=self.size, min=-6, max=6)
        self.C_rank_enem.Bind(wx.EVT_SPINCTRLDOUBLE, self.calc_C_status_enem)
        self.D_rank_enem = wx.SpinCtrlDouble(self, -1, size=self.size, min=-6, max=6)
        self.D_rank_enem.Bind(wx.EVT_SPINCTRLDOUBLE, self.calc_D_status_enem)
        self.S_rank_enem = wx.SpinCtrlDouble(self, -1, size=self.size, min=-6, max=6)
        self.S_rank_enem.Bind(wx.EVT_SPINCTRLDOUBLE, self.calc_S_status_enem)

        status_layout = wx.GridSizer(7, 5, 0, 0)
        status_layout.Add(space)
        status_layout.Add(race)
        status_layout.Add(effort)
        status_layout.Add(individual)
        status_layout.Add(rank)

        status_layout.Add(H_status)
        status_layout.Add(self.H_race_enem)
        status_layout.Add(self.H_effort_enem)
        status_layout.Add(self.H_indivi_enem)
        status_layout.Add(self.H_rank_enem)

        status_layout.Add(A_status)
        status_layout.Add(self.A_race_enem)
        status_layout.Add(self.A_effort_enem)
        status_layout.Add(self.A_indivi_enem)
        status_layout.Add(self.A_rank_enem)

        status_layout.Add(B_status)
        status_layout.Add(self.B_race_enem)
        status_layout.Add(self.B_effort_enem)
        status_layout.Add(self.B_indivi_enem)
        status_layout.Add(self.B_rank_enem)

        status_layout.Add(C_status)
        status_layout.Add(self.C_race_enem)
        status_layout.Add(self.C_effort_enem)
        status_layout.Add(self.C_indivi_enem)
        status_layout.Add(self.C_rank_enem)

        status_layout.Add(D_status)
        status_layout.Add(self.D_race_enem)
        status_layout.Add(self.D_effort_enem)
        status_layout.Add(self.D_indivi_enem)
        status_layout.Add(self.D_rank_enem)

        status_layout.Add(S_status)
        status_layout.Add(self.S_race_enem)
        status_layout.Add(self.S_effort_enem)
        status_layout.Add(self.S_indivi_enem)
        status_layout.Add(self.S_rank_enem)
        
        space_ = wx.StaticText(self, -1, "合計値", size=self.size)
        self.sum_race_enem = wx.TextCtrl(self, -1, "0", size=self.size)
        self.sum_effort_enem = wx.TextCtrl(self, -1, "0", size=self.size)
        set_indi_enem = wx.Button(self, -1, "リセット", size=self.size)
        set_indi_enem.Bind(wx.EVT_BUTTON, self.reset_indi_enem)
        set_rank_enem = wx.Button(self, -1, "リセット", size=self.size)
        set_rank_enem.Bind(wx.EVT_BUTTON, self.reset_rank_enem)
        add_layout = wx.BoxSizer(wx.HORIZONTAL)
        add_layout.Add(space_)
        add_layout.Add(self.sum_race_enem)
        add_layout.Add(self.sum_effort_enem)
        add_layout.Add(set_indi_enem)
        add_layout.Add(set_rank_enem)

        layout = wx.BoxSizer(wx.VERTICAL)
        layout.Add(status_layout)
        layout.Add(add_layout)
        return layout

    # リセット用の関数
    def reset_indi_my(self, event):
        self.H_indivi_my.SetValue("31")
        self.A_indivi_my.SetValue("31")
        self.B_indivi_my.SetValue("31")
        self.C_indivi_my.SetValue("31")
        self.D_indivi_my.SetValue("31")
        self.S_indivi_my.SetValue("31")

    def reset_rank_my(self, event):
        self.A_rank_my.SetValue("0")
        self.B_rank_my.SetValue("0")
        self.C_rank_my.SetValue("0")
        self.D_rank_my.SetValue("0")
        self.S_rank_my.SetValue("0")

    def reset_indi_enem(self, event):
        self.H_indivi_enem.SetValue("31")
        self.A_indivi_enem.SetValue("31")
        self.B_indivi_enem.SetValue("31")
        self.C_indivi_enem.SetValue("31")
        self.D_indivi_enem.SetValue("31")
        self.S_indivi_enem.SetValue("31")

    def reset_rank_enem(self, event):
        self.A_rank_enem.SetValue("0")
        self.B_rank_enem.SetValue("0")
        self.C_rank_enem.SetValue("0")
        self.D_rank_enem.SetValue("0")
        self.S_rank_enem.SetValue("0")    

    def reset_info(self, event):
        """
        盤面の初期化
        """
        self.reset_my()
        self.reset_enem()
        self.name_box_my.AppendItems(self.pk_name_list)
        self.name_box_enem.AppendItems(self.pk_name_list)
        self.parent.Pic_Panel.pk_list = []
    
    def reset_my(self):
        self.output.DeleteAllItems()
        self.move_box.SetValue("技")
        self.critical_box.SetValue("急所")
        self.weather_box.SetValue("天候")
        self.field_box.SetValue("フィールド")

        self.name_box_my.Clear()
        self.folm_box_my.Clear()
        self.ability_box_my.Clear()
        self.name_box_my.SetValue("名前")
        self.folm_box_my.SetValue("フォルム")
        self.level_box_my.SetValue("50")
        self.char_box_my.SetValue("性格")
        self.ability_box_my.SetValue("特性")
        self.invent_box_my.SetValue("持ち物")
        self.condi_box_my.SetValue("状態異常")
        self.H_race_my.SetValue("0")
        self.A_race_my.SetValue("0")
        self.B_race_my.SetValue("0")
        self.C_race_my.SetValue("0")
        self.D_race_my.SetValue("0")
        self.S_race_my.SetValue("0")
        self.sum_race_my.SetValue("0")
        self.H_effort_my.SetValue("0")
        self.A_effort_my.SetValue("0")
        self.B_effort_my.SetValue("0")
        self.C_effort_my.SetValue("0")
        self.D_effort_my.SetValue("0")
        self.S_effort_my.SetValue("0")
        self.sum_effort_my.SetValue("0")
        self.H_indivi_my.SetValue("31")
        self.A_indivi_my.SetValue("31")
        self.B_indivi_my.SetValue("31")
        self.C_indivi_my.SetValue("31")
        self.D_indivi_my.SetValue("31")
        self.S_indivi_my.SetValue("31")
        self.A_rank_my.SetValue("0")
        self.B_rank_my.SetValue("0")
        self.C_rank_my.SetValue("0")
        self.D_rank_my.SetValue("0")
        self.S_rank_my.SetValue("0")
    
    def reset_enem(self):
        self.name_box_enem.Clear()
        self.folm_box_enem.Clear()
        self.ability_box_enem.Clear()
        self.name_box_enem.SetValue("名前")
        self.folm_box_enem.SetValue("フォルム")
        self.level_box_enem.SetValue("50")
        self.char_box_enem.SetValue("性格")
        self.ability_box_enem.SetValue("特性")
        self.invent_box_enem.SetValue("持ち物")
        self.big_box_enem.SetValue("ダイマックス")
        self.buff_box_enem.SetValue("その他")
        self.H_race_enem.SetValue("0")
        self.A_race_enem.SetValue("0")
        self.B_race_enem.SetValue("0")
        self.C_race_enem.SetValue("0")
        self.D_race_enem.SetValue("0")
        self.S_race_enem.SetValue("0")
        self.sum_race_enem.SetValue("0")
        self.H_effort_enem.SetValue("0")
        self.A_effort_enem.SetValue("0")
        self.B_effort_enem.SetValue("0")
        self.C_effort_enem.SetValue("0")
        self.D_effort_enem.SetValue("0")
        self.S_effort_enem.SetValue("0")
        self.sum_effort_enem.SetValue("0")
        self.H_indivi_enem.SetValue("31")
        self.A_indivi_enem.SetValue("31")
        self.B_indivi_enem.SetValue("31")
        self.C_indivi_enem.SetValue("31")
        self.D_indivi_enem.SetValue("31")
        self.S_indivi_enem.SetValue("31")
        self.A_rank_enem.SetValue("0")
        self.B_rank_enem.SetValue("0")
        self.C_rank_enem.SetValue("0")
        self.D_rank_enem.SetValue("0")
        self.S_rank_enem.SetValue("0")

    def app_close(self, event):
        """
        GUIの停止
        """
        self.conn.close()
        wx.Exit()
