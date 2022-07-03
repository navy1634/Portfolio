import wx
import pandas as pd
from Table import mainTable

type_name_list = ["ノーマル", "ほのお", "みず", "でんき", "くさ", "こおり", "かくとう", "どく", "じめん", "ひこう", "エスパー", "むし", "いわ", "ゴースト", "ドラゴン", "あく", "はがね", "フェアリー"]
move_columns = ["技名", "タイプ", "取得条件", "効果"]
type_columns = ["4倍", "2倍", "半減", "1/4減", "無効"]
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

swsh = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 50, 51, 52, 53, 54, 55, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 72, 73, 77, 78, 79, 80, 81, 82, 83, 90, 91, 92, 93, 94, 95, 98, 99, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 163, 164, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 182, 183, 184, 185, 186, 194, 195, 196, 197, 199, 202, 206, 208, 211, 212, 213, 214, 215, 220, 221, 222, 223, 224, 225, 226, 227, 230, 233, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260, 263, 264, 270, 271, 272, 273, 274, 275, 278, 279, 280, 281, 282, 290, 291, 292, 293, 294, 295, 298, 302, 303, 304, 305, 306, 309, 310, 315, 318, 319, 320, 321, 324, 328, 329, 330, 333, 334, 337, 338, 339, 340, 341, 342, 343, 344, 345, 346, 347, 348, 349, 350, 355, 356, 359, 360, 361, 362, 363, 364, 365, 369, 371, 372, 373, 374, 375, 376, 377, 378, 379, 380, 381, 382, 383, 384, 385, 403, 404, 405, 406, 407, 415, 416, 420, 421, 422, 423, 425, 426, 427, 428, 434, 435, 436, 437, 438, 439, 440, 442, 443, 444, 445, 446, 447, 448, 449, 450, 451, 452, 453, 454, 458, 459, 460, 461, 462, 463, 464, 465, 466, 467, 468, 470, 471, 473, 474, 475, 477, 478, 479, 480, 481, 482, 483, 484, 485, 486, 487, 488, 494, 506, 507, 508, 509, 510, 517, 518, 519, 520, 521, 524, 525, 526, 527, 528, 529, 530, 531, 532, 533, 534, 535, 536, 537, 538, 539, 543, 544, 545, 546, 547, 548, 549, 550, 551, 552, 553, 554, 555, 556, 557, 558, 559, 560, 561, 562, 563, 564, 565, 566, 567, 568, 569, 570, 571, 572, 573, 574, 575, 576, 577, 578, 579, 582, 583, 584, 587, 588, 589, 590, 591, 592, 593, 595, 596, 597, 598, 599, 600, 601, 605, 606, 607, 608, 609, 610, 611, 612, 613, 614, 615, 616, 617, 618, 619, 620, 621, 622, 623, 624, 625, 626, 627, 628, 629, 630, 631, 632, 633, 634, 635, 636, 637, 638, 639, 640, 641, 642, 643, 644, 645, 646, 647, 649, 659, 660, 661, 662, 663, 674, 675, 677, 678, 679, 680, 681, 682, 683, 684, 685, 686, 687, 688, 689, 690, 691, 692, 693, 694, 695, 696, 697, 698, 699, 700, 701, 702, 703, 704, 705, 706, 707, 708, 709, 710, 711, 712, 713, 714, 715, 716, 717, 718, 719, 721, 722, 723, 724, 725, 726, 727, 728, 729, 730, 736, 737, 738, 742, 743, 744, 745, 746, 747, 748, 749, 750, 751, 752, 753, 754, 755, 756, 757, 758, 759, 760, 761, 762, 763, 764, 765, 766, 767, 768, 769, 770, 771, 772, 773, 776, 777, 778, 780, 781, 782, 783, 784, 785, 786, 787, 788, 789, 790, 791, 792, 793, 794, 795, 796, 797, 798, 799, 800, 801, 802, 803, 804, 805, 806, 807, 808, 809, 810, 811, 812, 813, 814, 815, 816, 817, 818, 819, 820, 821, 822, 823, 824, 825, 826, 827, 828, 829, 830, 831, 832, 833, 834, 835, 836, 837, 838, 839, 840, 841, 842, 843, 844, 845, 846, 847, 848, 849, 850, 851, 852, 853, 854, 855, 856, 857, 858, 859, 860, 861, 862, 863, 864, 865, 866, 867, 868, 869, 870, 871, 872, 873, 874, 875, 876, 877, 878, 879, 880, 881, 882, 883, 884, 885, 886, 887, 888, 889, 890, 891, 892, 893, 894, 895, 896, 897, 898]
usum = range(1, 721)


class pk_data_Panel(wx.Panel):
    """
    Panel名 : ポケモン図鑑
    """
    def __init__(self, parent, setting):
        super().__init__(parent, -1)
        self.setting = setting
        self.parent = parent
        self.size = parent.size
        self.conn = parent.conn
        self.df_move_all = parent.df_move_all
        self.use_move_json  = parent.use_move_data

        # テーブルの作成
        self.df_type = pd.DataFrame(comp_list, index=type_name_list, columns=type_name_list)
        self.move_list = mainTable(self, size=(370, 470))
        self.type_list = mainTable(self, size=(410, 200))
        self.get_pk_name_list()

        # パネル内のレイアウト
        panel_layout = wx.BoxSizer(wx.VERTICAL)
        panel_layout.Add(wx.StaticText(self, -1, " "))
        panel_layout.Add(wx.StaticText(self, -1, " "))
        panel_layout.Add(self.set_layout(), flag=wx.ALIGN_CENTER)
        self.SetSizer(panel_layout)

        # テーブルに値を追加
        for col, v in enumerate(move_columns):
            self.move_list.InsertColumn(col, v)
        for col, v in enumerate(type_columns):
            self.type_list.InsertColumn(col, v)


    def view_move_list(self) -> None:
        """
        取得技一覧の反映
        """
        pk_move = self.use_move_json[self.name]["Move"]
        self.move_list.DeleteAllItems()
        use_move = list(pk_move.keys())
        use_move.reverse()
        for move in use_move:
            df_move = self.df_move_all[self.df_move_all["名前"]==move.replace("*", "")]
            self.move_list.InsertItem(0, move.replace("*", ""))
            self.move_list.SetItem(0,1, df_move["タイプ"].tolist()[0])
            self.move_list.SetItem(0,2, pk_move[move])
            self.move_list.SetItem(0,3, df_move["効果"].tolist()[0])
        return None

    def view_type_list(self):
        """
        取得したデータの反映
        """
        self.set_type_list()
        self.type_list.DeleteAllItems()
        for i in range(len(self.type_dict[4])-1, -1, -1):
            self.type_list.InsertItem(0, self.type_dict[4][i])
            self.type_list.SetItem(0,1,str(self.type_dict[2][i]))
            self.type_list.SetItem(0,2,str(self.type_dict[0.5][i]))
            self.type_list.SetItem(0,3,str(self.type_dict[0.25][i]))
            self.type_list.SetItem(0,4,str(self.type_dict[0][i]))

    def set_type_list(self):
        """
        タイプ相性表の作成
        """
        self.type_comp()
        keys = self.type_dict.keys()
        if 4 in keys:
            len_ty4 = len(self.type_dict[4])
        else:
            len_ty4 = 0
        if 2 in keys:
            len_ty2 = len(self.type_dict[2])
        else:
            len_ty2 = 0
        if 0.5 in keys:
            len_ty05 = len(self.type_dict[0.5])
        else:
            len_ty05 = 0
        if 0.25 in keys:
            len_ty025 = len(self.type_dict[0.25])
        else:
            len_ty025 = 0
        if 0 in keys:
            len_ty0 = len(self.type_dict[0])
        else:
            len_ty0 = 0

        max_len = max(len_ty4, len_ty2, len_ty05, len_ty025, len_ty0)
        if len_ty4 == 0:
            self.type_dict[4] = [" "] * max_len
        else:
            self.type_dict[4] += [" "] * (max_len - len_ty4)
        if len_ty2 == 0:
            self.type_dict[2] = [" "] * max_len
        else:
            self.type_dict[2] += [" "] * (max_len - len_ty4)
        if len_ty05 == 0:
            self.type_dict[0.5] = [" "] * max_len
        else:
            self.type_dict[0.5] += [" "] * (max_len - len_ty4)
        if len_ty025 == 0:
            self.type_dict[0.25] = [" "] * max_len
        else:
            self.type_dict[0.25] += [" "] * (max_len - len_ty4)
        if len_ty0 == 0:
            self.type_dict[0] = [" "] * max_len
        else:
            self.type_dict[0] += [" "] * (max_len - len_ty4)
        
    def type_comp(self):
        """
        タイプ相性の取得
        """
        self.type_dict = dict()
        for ty in type_name_list:
            if self.type2 in type_name_list:
                rate = self.df_type.loc[ty, self.type1] * self.df_type.loc[ty, self.type2]
            else:
                rate = self.df_type.loc[ty, self.type1]

            if rate not in self.type_dict:
                self.type_dict[rate] = [ty]
            else:
                self.type_dict[rate].append(ty)
            
    def get_pk_use(self, event):
        """
        覚える技の取得
        """
        try:
            toggle = self.series_button.GetValue()
            use_move_list_my = self.use_move_json[self.name]["Move"]
            if toggle == True:
                use_move_list = [move for move,val in use_move_list_my.items()  if val !="過去限定"]
            else:
                use_move_list = list(use_move_list_my.keys())
            self.move_data = self.df_move_all[self.df_move_all["名前"].isin(use_move_list)]
        except:
            self.move_data = pd.DataFrame(["Error"])

    def set_valuses(self, event):
        """
        検索対象のデータの反映
        """
        self.name = self.name_box.GetValue()
        sql = self.Create_SQL(self.name)
        self.pk_data = pd.read_sql_query(sql=sql, con=self.conn)

        folm = self.pk_data["フォルム"].tolist()
        self.folm_box.Clear()
        self.folm_box.SetValue(folm[0])
        for f in folm:
            self.folm_box.Append(f)
        
        self.type1 = self.pk_data["タイプ1"].tolist()[0]
        self.type2 = self.pk_data["タイプ2"].tolist()[0]
        self.type1_box.SetValue(self.type1)
        self.type2_box.SetValue(self.type2)

        abi1 = self.pk_data["特性1"].tolist()[0]
        abi2 = self.pk_data["特性2"].tolist()[0]
        abi3 = self.pk_data["夢特性"].tolist()[0]
        self.abi1_box.SetValue(abi1)
        self.abi2_box.SetValue(abi2)
        self.abi_hide_box.SetValue(abi3)

        # 種族値の取得
        self.status_sum.SetValue(str(self.pk_data["合計値"].tolist()[0]))
        self.status_H.SetValue(str(self.pk_data["H"].tolist()[0]))
        self.status_A.SetValue(str(self.pk_data["A"].tolist()[0]))
        self.status_B.SetValue(str(self.pk_data["B"].tolist()[0]))
        self.status_C.SetValue(str(self.pk_data["C"].tolist()[0]))
        self.status_D.SetValue(str(self.pk_data["D"].tolist()[0]))
        self.status_S.SetValue(str(self.pk_data["S"].tolist()[0]))

        gene = self.pk_data["世代"].tolist()[0]
        class_ = self.pk_data["分類"].tolist()[0]
        self.gene_box.SetValue(str(gene))
        self.class_box.SetValue(class_)
        self.view_type_list()
        self.view_move_list()

    def set_folm_valuses(self, event):
        """
        検索対象のデータの反映
        """
        folm = self.folm_box.GetValue()
        pk_folm_data = self.pk_data[self.pk_data["フォルム"]==folm]
        
        self.type1 = pk_folm_data["タイプ1"].tolist()[0]
        self.type2 = pk_folm_data["タイプ2"].tolist()[0]
        self.type1_box.SetValue(self.type1)
        self.type2_box.SetValue(self.type2)

        abi1 = pk_folm_data["特性1"].tolist()[0]
        abi2 = pk_folm_data["特性2"].tolist()[0]
        abi3 = pk_folm_data["夢特性"].tolist()[0]
        self.abi1_box.SetValue(abi1)
        self.abi2_box.SetValue(abi2)
        self.abi_hide_box.SetValue(abi3)

        # 種族値の取得
        self.status_sum.SetValue(str(pk_folm_data["合計値"].tolist()[0]))
        self.status_H.SetValue(str(pk_folm_data["H"].tolist()[0]))
        self.status_A.SetValue(str(pk_folm_data["A"].tolist()[0]))
        self.status_B.SetValue(str(pk_folm_data["B"].tolist()[0]))
        self.status_C.SetValue(str(pk_folm_data["C"].tolist()[0]))
        self.status_D.SetValue(str(pk_folm_data["D"].tolist()[0]))
        self.status_S.SetValue(str(pk_folm_data["S"].tolist()[0]))

        gene = pk_folm_data["世代"].tolist()[0]
        class_ = pk_folm_data["分類"].tolist()[0]
        self.gene_box.SetValue(str(gene))
        self.class_box.SetValue(class_)
        self.view_type_list()
        self.view_move_list()

    def Create_SQL(self, name):
        """
        ポケモン図鑑データの準備
        """
        sql = '''
            Select pk_nomal.名前, pk_nomal.フォルム, pk_fight.タイプ1, pk_fight.タイプ2, pk_fight.特性1, pk_fight.特性2, pk_fight.夢特性, pk_status.合計値, pk_status.H, pk_status.A, pk_status.B, pk_status.C, pk_status.D, pk_status.S, pk_nomal.世代, pk_nomal.分類
            From pk_status, pk_nomal, pk_fight
            Where pk_status.名前 = pk_nomal.名前 and pk_status.フォルム = pk_nomal.フォルム and pk_status.名前 = pk_nomal.名前
            and pk_status.名前 = pk_fight.名前 and pk_status.フォルム = pk_fight.フォルム and pk_status.名前 = pk_fight.名前
            and pk_status.名前 = '{name}'
        '''.format(name=name)
        return sql

    def get_pk_name_list(self):
        sql = '''
            Select pk_nomal.名前
            From pk_nomal
        '''
        self.pk_name_list = pd.read_sql_query(sql=sql, con=self.conn)
        self.pk_name_list = self.pk_name_list["名前"].values.tolist()

    # レイアウト
    def set_layout(self):
        """
        パーツ全体のレイアウト
        """
        layout = wx.BoxSizer(wx.VERTICAL)
        layout.Add(self.pk_data_layout(), wx.ALIGN_CENTER)
        layout.Add(wx.StaticText(self, -1, " "))
        layout.Add(wx.StaticText(self, -1, " "))
        layout.Add(self.set_option_layout(), flag=wx.ALIGN_CENTER)
        layout.Add(wx.StaticText(self, -1, " "))
        layout.Add(self.type_list, flag=wx.ALIGN_CENTER)

        panel_layout = wx.BoxSizer(wx.HORIZONTAL)
        panel_layout.Add(layout, border=10)
        panel_layout.Add(self.move_list, flag=wx.SHAPED | wx.LEFT, border=20)
        return panel_layout

    def pk_data_layout(self):
        layout = wx.BoxSizer(wx.HORIZONTAL)
        layout.Add(self.search_text_layout())
        layout.Add(self.set_pk_layout())
        layout.Add(self.status_text_layout())
        layout.Add(self.status_layout())
        return layout

    def search_text_layout(self):
        name_text = wx.StaticText(self, -1, "名前", size=self.size)
        type1_text = wx.StaticText(self, -1, "タイプ1", size=self.size)
        type2_text = wx.StaticText(self, -1, "タイプ2", size=self.size)
        abi1_text = wx.StaticText(self, -1, "特性1", size=self.size)
        abi2_text = wx.StaticText(self, -1, "特性2", size=self.size)
        abi_hide_text = wx.StaticText(self, -1, "夢特性", size=self.size)
        class_text = wx.StaticText(self, -1, "分類", size=self.size)
        gene_text = wx.StaticText(self, -1, "世代", size=self.size)

        layout = wx.BoxSizer(wx.VERTICAL)
        layout.Add(name_text)
        layout.Add(type1_text)
        layout.Add(type2_text)
        layout.Add(abi1_text)
        layout.Add(abi2_text)
        layout.Add(abi_hide_text)
        layout.Add(class_text)
        layout.Add(gene_text)
        return layout
    
    def set_pk_layout(self):
        self.name_box = wx.ComboBox(self, -1, "名前", size=self.size, choices=self.pk_name_list)
        self.name_box.Bind(wx.EVT_COMBOBOX, self.set_valuses)
        self.type1_box = wx.TextCtrl(self, -1, "タイプ", size=self.size)
        self.type2_box = wx.TextCtrl(self, -1, "タイプ", size=self.size)
        self.abi1_box = wx.TextCtrl(self, -1, "特性1", size=self.size)
        self.abi2_box = wx.TextCtrl(self, -1, "特性2", size=self.size)
        self.abi_hide_box = wx.TextCtrl(self, -1, "夢特性", size=self.size)
        self.class_box = wx.TextCtrl(self, -1, "分類", size=self.size)
        self.gene_box = wx.TextCtrl(self, -1, "世代", size=self.size)

        layout = wx.BoxSizer(wx.VERTICAL)
        layout.Add(self.name_box)
        layout.Add(self.type1_box)
        layout.Add(self.type2_box)
        layout.Add(self.abi1_box)
        layout.Add(self.abi2_box)
        layout.Add(self.abi_hide_box)
        layout.Add(self.class_box)
        layout.Add(self.gene_box)
        return layout

    def status_text_layout(self):
        status_sum = wx.StaticText(self, -1, "合計値", size=self.size)
        status_H = wx.StaticText(self, -1, "HP", size=self.size)
        status_A = wx.StaticText(self, -1, "攻撃", size=self.size)
        status_B = wx.StaticText(self, -1, "防御", size=self.size)
        status_C = wx.StaticText(self, -1, "特攻", size=self.size)
        status_D = wx.StaticText(self, -1, "特防", size=self.size)
        status_S = wx.StaticText(self, -1, "素早さ", size=self.size)
        folm_text = wx.StaticText(self, -1, "フォルム", size=self.size)
        layout = wx.BoxSizer(wx.VERTICAL)
        layout.Add(folm_text)
        layout.Add(status_sum)
        layout.Add(status_H)
        layout.Add(status_A)
        layout.Add(status_B)
        layout.Add(status_C)
        layout.Add(status_D)
        layout.Add(status_S)
        return layout

    def status_layout(self):
        self.status_sum = wx.TextCtrl(self, -1, "合計値", size=self.size)
        self.status_H = wx.TextCtrl(self, -1, "H", size=self.size)
        self.status_A = wx.TextCtrl(self, -1, "A", size=self.size)
        self.status_B = wx.TextCtrl(self, -1, "B", size=self.size)
        self.status_C = wx.TextCtrl(self, -1, "C", size=self.size)
        self.status_D = wx.TextCtrl(self, -1, "D", size=self.size)
        self.status_S = wx.TextCtrl(self, -1, "S", size=self.size)
        self.folm_box = wx.ComboBox(self, -1, "フォルム", size=self.size)
        self.folm_box.Bind(wx.EVT_COMBOBOX, self.set_folm_valuses)

        layout = wx.BoxSizer(wx.VERTICAL)
        layout.Add(self.folm_box)
        layout.Add(self.status_sum)
        layout.Add(self.status_H)
        layout.Add(self.status_A)
        layout.Add(self.status_B)
        layout.Add(self.status_C)
        layout.Add(self.status_D)
        layout.Add(self.status_S)
        return layout

    def set_option_layout(self):
        self.series_button = wx.ComboBox(self, -1, "世代", size=self.size, choices=["USUM", "SWSH", "SV"])
        self.series_button.Bind(wx.EVT_COMBOBOX, self.get_pk_use)
        close_button = wx.Button(self, -1, "閉じる", size=self.size)
        close_button.Bind(wx.EVT_BUTTON, self.app_close)

        layout = wx.BoxSizer(wx.HORIZONTAL)
        layout.Add(self.series_button)
        layout.Add(close_button)
        return layout

    def app_close(self, event):
        """
        GUIの停止
        """
        self.conn.close()
        wx.Exit()
    
