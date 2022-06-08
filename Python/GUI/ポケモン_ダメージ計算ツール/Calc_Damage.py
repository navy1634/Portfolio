import pandas as pd
from math import floor, ceil

type_list = ["ノーマル", "ほのお", "みず", "でんき", "くさ", "こおり", "かくとう", "どく", "じめん", "ひこう", "エスパー", "むし", "いわ", "ゴースト", "ドラゴン", "あく", "はがね", "フェアリー"]
char_list = ["さみしがり", "いじっぱり", "やんちゃ", "ゆうかん", "ずぶとい", "わんぱく", "のうてんき", "のんき", "ひかえめ", "おっとり", "うっかりや", "れいせい", "おだやか", "おとなしい", "しんちょう", "なまいき	", "おくびょう", "せっかち", "ようき", "むじゃき", "がんばりや",  "てれや", "すなお", "きまぐれ",  "まじめ"]
field_ = ["エレキ", "グラス", "ミスト", "サイコ"]
ex = ["光の壁", "リフレクター", "オーロラベール"]
invent_list = []
comp_list = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0.5, 0, 1, 1, 0.5, 1], 
    [1, 0.5, 0.5, 1, 2, 2, 1, 1, 1, 1, 1, 2, 0.5, 1, 0.5, 1, 2, 1], 
    [1, 2, 0.5, 1, 0.5, 1, 1, 1, 2, 1, 1, 1, 2, 1, 0.5, 1, 1, 1], 
    [1, 1, 2, 0.5, 0.5, 1, 1, 1, 0, 2, 1, 1, 1, 1, 0.5, 1, 1, 1], 
    [1, 0.5, 2, 1, 0.5, 1, 1, 0.5, 2, 0.5, 1, 0.5, 2, 1, 0.5, 1, 0.5, 1], 
    [1, 0.5, 0.5, 1, 2, 0.5, 1, 1, 2, 2, 1, 1, 1, 1, 2, 1, 0.5, 1], 
    [2, 1, 1, 1, 1, 2, 1, 0.5, 1, 0.5, 0.5, 0.5, 2, 0, 1, 2, 2, 0.5], 
    [1, 1, 1, 1, 2, 1, 1, 0.5, 0.5, 1, 1, 1, 0.5, 0.5, 1, 1, 0, 2], 
    [1, 2, 1, 2, 0.5, 1, 1, 2, 1, 0, 1, 0.5, 2, 1, 1, 1, 2, 1], 
    [1, 1, 1, 0.5, 2, 1, 2, 1, 1, 1, 1, 2, 0.5, 1, 1, 1, 0.5, 1], 
    [1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 0.5, 1, 1, 1, 1, 2, 0.5, 1], 
    [1, 0.5, 1, 1, 2, 1, 0.5, 0.5, 1, 0.5, 2, 1, 1, 0.5, 1, 2, 0.5, 0.5], 
    [1, 2, 1, 1, 1, 2, 0.5, 1, 0.5, 2, 1, 2, 1, 1, 1, 1, 0.5, 1], 
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 0.5, 1, 1], 
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 0.5, 0], 
    [1, 1, 1, 1, 1, 1, 0.5, 1, 1, 1, 2, 1, 1, 2, 1, 0.5, 1, 0.5], 
    [1, 0.5, 0.5, 0.5, 1, 2, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 0.5, 2], 
    [1, 0.5, 1, 1, 1, 1, 2, 0.5, 1, 1, 1, 1, 1, 1, 2, 2, 0.5, 1]]

class Calc_Damage():
    def __init__(self, pk_data, df_pk, df_move):
        self.df_pk = df_pk
        self.df_move = df_move
        self.pk_data = pk_data
        self.df_type = pd.DataFrame(comp_list, index=type_list, columns=type_list)

    # ダメージ計算用のデータ取得
    def get_move_info(self):
        # 攻撃側
        pk_name_my = self.pk_data[0][0]
        pk_folm_my = self.pk_data[0][1]
        self.df_pk_my = self.df_pk[(self.df_pk["名前"]==pk_name_my)&(self.df_pk["フォルム"]==pk_folm_my)]
        self.pk_type_my = self.df_pk_my[["タイプ1", "タイプ2"]].to_numpy().tolist()[0]
        self.pk_level_my = self.pk_data[0][2]
        self.pk_abi_my = self.pk_data[0][3]
        self.pk_invent_my = self.pk_data[0][4]
        self.pk_condi_my = self.pk_data[0][5]
        self.pk_big_my = self.pk_data[0][6]

        # 防御側
        pk_name_enem = self.pk_data[1][0]
        pk_folm_enem = self.pk_data[1][1]
        self.df_pk_enem = self.df_pk[(self.df_pk["名前"]==pk_name_enem)&(self.df_pk["フォルム"]==pk_folm_enem)]
        self.pk_type_enem = self.df_pk_enem[["タイプ1", "タイプ2"]].to_numpy().tolist()[0]
        self.pk_level_enem = self.pk_data[1][2]
        self.pk_abi_enem = self.pk_data[1][3]
        self.pk_invent_enem = self.pk_data[1][4]
        self.pk_big_enem = self.pk_data[1][5]

        # 技
        self.move_name = self.pk_data[2][0]
        df_use_move = self.df_move[self.df_move["名前"]==self.move_name]
        self.move_type = df_use_move["タイプ"].tolist()[0]
        self.move_class = df_use_move["分類"].tolist()[0]
        if self.pk_big_my == "あり":
            self.move_damage = df_use_move["ダイマックス"].astype(int).tolist()[0]
        else:
            self.move_damage = df_use_move["威力"].astype(int).tolist()[0]

        # 各種補正
        self.weather = self.pk_data[2][1]
        self.field = self.pk_data[2][2]
        self.critical = self.pk_data[2][3]

        # ステータス
        self.H_correct = self.pk_data[3][0]
        self.S_correct = self.pk_data[3][1]
        self.S_correct = self.pk_data[3][2]
        self.AC = self.pk_data[3][3]
        self.BD = self.pk_data[3][4]

    # ダメージ計算
    def get_damage(self, rand):
        self.get_move_info()
        damage = floor(floor(floor(self.pk_level_my * 2 / 5 + 2) * self.move_damage * self.AC / self.BD) / 50 + 2)
        #天候補正
        damage = self.round_056(damage * self.get_weather(move_type=self.move_type))

        #急所
        if self.critical == "あり":
            damage = self.round_056(damage * 1.5)

        #乱数
        damage = damage * rand // 1

        #タイプ一致補正
        if self.pk_abi_my=="てきおうりょく":
            damage = self.round_056(damage * 1.5)
        elif self.move_type in self.pk_type_my:     #タイプ一致補正
            damage = self.round_056(damage * 1.5)

        #タイプ相性補正
        for ty in self.pk_type_enem:
            if ty != "-":
                damage = self.round_056(damage * self.type_comp(self.move_type, ty))

        #状態異常補正(火傷)
        if self.pk_condi_my == "火傷":
            damage = self.round_056(damage * 0.5)

        #フィールド補正
        damage = self.round_056(damage * self.get_field(field=self.field, move_type=self.move_type, move_name=self.move_name))
        return damage

    # タイプ相性補正
    def type_comp(self, move_type, enem_type):
        return self.df_type.loc[move_type, enem_type]

    # 天候補正
    def get_weather(self, move_type):
        """
        晴      : 炎技 1.5倍、水技 0.5倍
        雨      : 炎技 0.5倍、水技 1.5倍
        砂嵐    : 岩特防 1.5倍
        """
        if self.weather == "晴":
            if move_type == "ほのお":
                return 1.5
            elif move_type == "みず":
                return 0.5
        elif self.weather == "雨":
            if move_type == "ほのお":
                return 0.5
            elif move_type == "みず":
                return 1.5
        return 1

    # フィールド補正
    def get_field(self, field, move_type, move_name):
        """
        エレキフィールド : 電気技 1.3倍
        グラスフィールド : 草技 1.3倍
        ミストフィールド : ドラゴン技 半減
        サイコフィールド : エスパー技 1.3倍
        """
        if field == "エレキ":
            if move_type == "でんき":
                return 1.3
        elif field == "グラス":
            if move_type == "くさ":
                return 1.3
            if move_name == "じしん" or move_name == "じならし":
                return 0.5
        elif field == "ミスト":
            if move_type == "ドラゴン":
                return 0.5
        elif field == "サイコ":
            if move_type == "エスパー":
                return 1.3
        return 1

    # 五捨五超入用の関数(小数用)
    def round_056(self, num):
        if num % 1 <= 5:
            return floor(num)
        return ceil(num)

