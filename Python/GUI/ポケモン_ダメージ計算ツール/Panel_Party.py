import wx
from concurrent.futures import ThreadPoolExecutor

class pk_party_Panel(wx.Panel):
    def __init__(self, parent, setting):
        super().__init__(parent, -1)
        self.setting = setting
        self.parent = parent
        self.size = parent.size
        self.conn = parent.conn
        self.df_move_all = parent.df_move_all
        self.use_move_data  = parent.use_move_data

        self.set_sc_button()
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.SetSizer(self.sizer)
        self.set_screen(self=self, panel=pk_view_party_Panel, sizer=self.sizer, rbox=self.rbox)


    def set_sc_button(self):
        self.rbox = wx.RadioBox(self, -1, "ページ構成", choices=['確認', '編成'])
        self.rbox.Bind(wx.EVT_RADIOBOX, self.check)

    @staticmethod
    def set_screen(self, panel, sizer: wx.BoxSizer, rbox: wx.RadioBox):
        sizer.Clear(False)
        self.DestroyChildren()

        self.set_sc_button()
        # sizer.Add(rbox)
        sizer.Add(panel(self), flag=wx.ALIGN_CENTER)
        sizer.Layout()

    def check(self, event):
        num = self.rbox.GetSelection()

        with ThreadPoolExecutor(max_workers=4) as exec:
            if num == 0:
                exec.submit(self.set_screen, pk_view_party_Panel, self.sizer, self.rbox)
                self.rbox.SetSelection(0)
                print(0)
            else:
                exec.submit(self.set_screen, pk_set_party_Panel, self.sizer, self.rbox)
                self.rbox.SetSelection(1)
                print(1)


class pk_view_party_Panel(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent, -1)
        self.setting = parent.setting
        self.parent = parent
        self.size = parent.size
        self.conn = parent.conn
        self.df_move_all = parent.df_move_all
        self.use_move_data  = parent.use_move_data

        panel_layout = wx.BoxSizer(wx.VERTICAL)
        panel_layout.Add(self.set_party(), flag=wx.ALIGN_CENTER)
        self.SetSizer(panel_layout)


    def set_party(self):
        layout = wx.FlexGridSizer(3, 2, 70, 60)
        layout.Add(self.party1())
        layout.Add(self.party2())
        layout.Add(self.party3())
        layout.Add(self.party4())
        layout.Add(self.party5())
        layout.Add(self.party6())
        return layout
    
    def party1(self):
        self.pk1_name = wx.TextCtrl(self, -1, "名前", size=self.size)
        self.pk1_status = wx.TextCtrl(self, -1, "努力値配分")
        self.pk1_type1 = wx.TextCtrl(self, -1, "タイプ1", size=self.size)
        self.pk1_type2 = wx.TextCtrl(self, -1, "タイプ2", size=self.size)
        self.pk1_char = wx.TextCtrl(self, -1, "性格", size=self.size)
        self.pk1_abi = wx.TextCtrl(self, -1, "特性", size=self.size)
        self.pk1_move1 = wx.TextCtrl(self, -1, "技1", size=self.size)
        self.pk1_move2 = wx.TextCtrl(self, -1, "技2", size=self.size)
        self.pk1_move3 = wx.TextCtrl(self, -1, "技3", size=self.size)
        self.pk1_move4 = wx.TextCtrl(self, -1, "技4", size=self.size)
        self.pk1_invent = wx.TextCtrl(self, -1, "持ち物", size=self.size)
        
        layout_left = wx.BoxSizer(wx.VERTICAL)
        layout_left.Add(self.pk1_name)
        layout_left.Add(self.pk1_type1)
        layout_left.Add(self.pk1_type2)
        layout_left.Add(self.pk1_char)
        layout_left.Add(self.pk1_invent)

        layout_right = wx.BoxSizer(wx.VERTICAL)
        layout_right.Add(self.pk1_abi)
        layout_right.Add(self.pk1_move1)
        layout_right.Add(self.pk1_move2)
        layout_right.Add(self.pk1_move3)
        layout_right.Add(self.pk1_move4)

        layout_party = wx.BoxSizer(wx.HORIZONTAL)
        layout_party.Add(self.party_text_left())
        layout_party.Add(layout_left)
        layout_party.Add(self.party_text_right())
        layout_party.Add(layout_right)

        layout_status = wx.BoxSizer(wx.HORIZONTAL)
        pk_status_text = wx.StaticText(self, -1, "努力値配分", size=self.size)
        layout_status.Add(pk_status_text)
        layout_status.Add(self.pk1_status, flag=wx.EXPAND)

        layout = wx.BoxSizer(wx.VERTICAL)
        layout.Add(layout_party)
        layout.Add(layout_status, flag=wx.EXPAND)
        return layout

    def party2(self):
        self.pk2_name = wx.TextCtrl(self, -1, "名前", size=self.size)
        self.pk2_status = wx.TextCtrl(self, -1, "努力値配分")
        self.pk2_type1 = wx.TextCtrl(self, -1, "タイプ1", size=self.size)
        self.pk2_type2 = wx.TextCtrl(self, -1, "タイプ2", size=self.size)
        self.pk2_char = wx.TextCtrl(self, -1, "性格", size=self.size)
        self.pk2_abi = wx.TextCtrl(self, -1, "特性", size=self.size)
        self.pk2_move1 = wx.TextCtrl(self, -1, "技1", size=self.size)
        self.pk2_move2 = wx.TextCtrl(self, -1, "技2", size=self.size)
        self.pk2_move3 = wx.TextCtrl(self, -1, "技3", size=self.size)
        self.pk2_move4 = wx.TextCtrl(self, -1, "技4", size=self.size)
        self.pk2_invent = wx.TextCtrl(self, -1, "持ち物", size=self.size)
        
        layout_left = wx.BoxSizer(wx.VERTICAL)
        layout_left.Add(self.pk2_name)
        layout_left.Add(self.pk2_type1)
        layout_left.Add(self.pk2_type2)
        layout_left.Add(self.pk2_char)
        layout_left.Add(self.pk2_invent)

        layout_right = wx.BoxSizer(wx.VERTICAL)
        layout_right.Add(self.pk2_abi)
        layout_right.Add(self.pk2_move1)
        layout_right.Add(self.pk2_move2)
        layout_right.Add(self.pk2_move3)
        layout_right.Add(self.pk2_move4)

        layout_party = wx.BoxSizer(wx.HORIZONTAL)
        layout_party.Add(self.party_text_left())
        layout_party.Add(layout_left)
        layout_party.Add(self.party_text_right())
        layout_party.Add(layout_right)

        layout_status = wx.BoxSizer(wx.HORIZONTAL)
        pk_status_text = wx.StaticText(self, -1, "努力値配分", size=self.size)
        layout_status.Add(pk_status_text)
        layout_status.Add(self.pk2_status, flag=wx.EXPAND)

        layout = wx.BoxSizer(wx.VERTICAL)
        layout.Add(layout_party)
        layout.Add(layout_status, flag=wx.EXPAND)
        return layout

    def party3(self):
        self.pk3_name = wx.TextCtrl(self, -1, "名前", size=self.size)
        self.pk3_status = wx.TextCtrl(self, -1, "努力値配分")
        self.pk3_type1 = wx.TextCtrl(self, -1, "タイプ1", size=self.size)
        self.pk3_type2 = wx.TextCtrl(self, -1, "タイプ2", size=self.size)
        self.pk3_char = wx.TextCtrl(self, -1, "性格", size=self.size)
        self.pk3_abi = wx.TextCtrl(self, -1, "特性", size=self.size)
        self.pk3_move1 = wx.TextCtrl(self, -1, "技1", size=self.size)
        self.pk3_move2 = wx.TextCtrl(self, -1, "技2", size=self.size)
        self.pk3_move3 = wx.TextCtrl(self, -1, "技3", size=self.size)
        self.pk3_move4 = wx.TextCtrl(self, -1, "技4", size=self.size)
        self.pk3_invent = wx.TextCtrl(self, -1, "持ち物", size=self.size)
        
        layout_left = wx.BoxSizer(wx.VERTICAL)
        layout_left.Add(self.pk3_name)
        layout_left.Add(self.pk3_type1)
        layout_left.Add(self.pk3_type2)
        layout_left.Add(self.pk3_char)
        layout_left.Add(self.pk3_invent)

        layout_right = wx.BoxSizer(wx.VERTICAL)
        layout_right.Add(self.pk3_abi)
        layout_right.Add(self.pk3_move1)
        layout_right.Add(self.pk3_move2)
        layout_right.Add(self.pk3_move3)
        layout_right.Add(self.pk3_move4)

        layout_party = wx.BoxSizer(wx.HORIZONTAL)
        layout_party.Add(self.party_text_left())
        layout_party.Add(layout_left)
        layout_party.Add(self.party_text_right())
        layout_party.Add(layout_right)

        layout_status = wx.BoxSizer(wx.HORIZONTAL)
        pk_status_text = wx.StaticText(self, -1, "努力値配分", size=self.size)
        layout_status.Add(pk_status_text)
        layout_status.Add(self.pk3_status, flag=wx.EXPAND)

        layout = wx.BoxSizer(wx.VERTICAL)
        layout.Add(layout_party)
        layout.Add(layout_status, flag=wx.EXPAND)
        return layout

    def party4(self):
        self.pk4_name = wx.TextCtrl(self, -1, "名前", size=self.size)
        self.pk4_status = wx.TextCtrl(self, -1, "努力値配分")
        self.pk4_type1 = wx.TextCtrl(self, -1, "タイプ1", size=self.size)
        self.pk4_type2 = wx.TextCtrl(self, -1, "タイプ2", size=self.size)
        self.pk4_char = wx.TextCtrl(self, -1, "性格", size=self.size)
        self.pk4_abi = wx.TextCtrl(self, -1, "特性", size=self.size)
        self.pk4_move1 = wx.TextCtrl(self, -1, "技1", size=self.size)
        self.pk4_move2 = wx.TextCtrl(self, -1, "技2", size=self.size)
        self.pk4_move3 = wx.TextCtrl(self, -1, "技3", size=self.size)
        self.pk4_move4 = wx.TextCtrl(self, -1, "技4", size=self.size)
        self.pk4_invent = wx.TextCtrl(self, -1, "持ち物", size=self.size)
        
        layout_left = wx.BoxSizer(wx.VERTICAL)
        layout_left.Add(self.pk4_name)
        layout_left.Add(self.pk4_type1)
        layout_left.Add(self.pk4_type2)
        layout_left.Add(self.pk4_char)
        layout_left.Add(self.pk4_invent)

        layout_right = wx.BoxSizer(wx.VERTICAL)
        layout_right.Add(self.pk4_abi)
        layout_right.Add(self.pk4_move1)
        layout_right.Add(self.pk4_move2)
        layout_right.Add(self.pk4_move3)
        layout_right.Add(self.pk4_move4)

        layout_party = wx.BoxSizer(wx.HORIZONTAL)
        layout_party.Add(self.party_text_left())
        layout_party.Add(layout_left)
        layout_party.Add(self.party_text_right())
        layout_party.Add(layout_right)

        layout_status = wx.BoxSizer(wx.HORIZONTAL)
        pk_status_text = wx.StaticText(self, -1, "努力値配分", size=self.size)
        layout_status.Add(pk_status_text)
        layout_status.Add(self.pk4_status, flag=wx.EXPAND)

        layout = wx.BoxSizer(wx.VERTICAL)
        layout.Add(layout_party)
        layout.Add(layout_status, flag=wx.EXPAND)
        return layout

    def party5(self):
        self.pk5_name = wx.TextCtrl(self, -1, "名前", size=self.size)
        self.pk5_status = wx.TextCtrl(self, -1, "努力値配分")
        self.pk5_type1 = wx.TextCtrl(self, -1, "タイプ1", size=self.size)
        self.pk5_type2 = wx.TextCtrl(self, -1, "タイプ2", size=self.size)
        self.pk5_char = wx.TextCtrl(self, -1, "性格", size=self.size)
        self.pk5_abi = wx.TextCtrl(self, -1, "特性", size=self.size)
        self.pk5_move1 = wx.TextCtrl(self, -1, "技1", size=self.size)
        self.pk5_move2 = wx.TextCtrl(self, -1, "技2", size=self.size)
        self.pk5_move3 = wx.TextCtrl(self, -1, "技3", size=self.size)
        self.pk5_move4 = wx.TextCtrl(self, -1, "技4", size=self.size)
        self.pk5_invent = wx.TextCtrl(self, -1, "持ち物", size=self.size)
        
        layout_left = wx.BoxSizer(wx.VERTICAL)
        layout_left.Add(self.pk5_name)
        layout_left.Add(self.pk5_type1)
        layout_left.Add(self.pk5_type2)
        layout_left.Add(self.pk5_char)
        layout_left.Add(self.pk5_invent)

        layout_right = wx.BoxSizer(wx.VERTICAL)
        layout_right.Add(self.pk5_abi)
        layout_right.Add(self.pk5_move1)
        layout_right.Add(self.pk5_move2)
        layout_right.Add(self.pk5_move3)
        layout_right.Add(self.pk5_move4)

        layout_party = wx.BoxSizer(wx.HORIZONTAL)
        layout_party.Add(self.party_text_left())
        layout_party.Add(layout_left)
        layout_party.Add(self.party_text_right())
        layout_party.Add(layout_right)

        layout_status = wx.BoxSizer(wx.HORIZONTAL)
        pk_status_text = wx.StaticText(self, -1, "努力値配分", size=self.size)
        layout_status.Add(pk_status_text)
        layout_status.Add(self.pk5_status, flag=wx.EXPAND)

        layout = wx.BoxSizer(wx.VERTICAL)
        layout.Add(layout_party)
        layout.Add(layout_status, flag=wx.EXPAND)
        return layout

    def party6(self):
        self.pk6_name = wx.TextCtrl(self, -1, "名前", size=self.size)
        self.pk6_status = wx.TextCtrl(self, -1, "努力値配分")
        self.pk6_type1 = wx.TextCtrl(self, -1, "タイプ1", size=self.size)
        self.pk6_type2 = wx.TextCtrl(self, -1, "タイプ2", size=self.size)
        self.pk6_char = wx.TextCtrl(self, -1, "性格", size=self.size)
        self.pk6_abi = wx.TextCtrl(self, -1, "特性", size=self.size)
        self.pk6_move1 = wx.TextCtrl(self, -1, "技1", size=self.size)
        self.pk6_move2 = wx.TextCtrl(self, -1, "技2", size=self.size)
        self.pk6_move3 = wx.TextCtrl(self, -1, "技3", size=self.size)
        self.pk6_move4 = wx.TextCtrl(self, -1, "技4", size=self.size)
        self.pk6_invent = wx.TextCtrl(self, -1, "持ち物", size=self.size)
        
        layout_left = wx.BoxSizer(wx.VERTICAL)
        layout_left.Add(self.pk6_name)
        layout_left.Add(self.pk6_type1)
        layout_left.Add(self.pk6_type2)
        layout_left.Add(self.pk6_char)
        layout_left.Add(self.pk6_invent)

        layout_right = wx.BoxSizer(wx.VERTICAL)
        layout_right.Add(self.pk6_abi)
        layout_right.Add(self.pk6_move1)
        layout_right.Add(self.pk6_move2)
        layout_right.Add(self.pk6_move3)
        layout_right.Add(self.pk6_move4)

        layout_party = wx.BoxSizer(wx.HORIZONTAL)
        layout_party.Add(self.party_text_left())
        layout_party.Add(layout_left)
        layout_party.Add(self.party_text_right())
        layout_party.Add(layout_right)

        layout_status = wx.BoxSizer(wx.HORIZONTAL)
        pk_status_text = wx.StaticText(self, -1, "努力値配分", size=self.size)
        layout_status.Add(pk_status_text)
        layout_status.Add(self.pk6_status, flag=wx.EXPAND)

        layout = wx.BoxSizer(wx.VERTICAL)
        layout.Add(layout_party)
        layout.Add(layout_status, flag=wx.EXPAND)
        return layout

    def party_text_left(self):
        pk_name_text = wx.StaticText(self, -1, "名前", size=self.size)
        pk_type1_text = wx.StaticText(self, -1, "タイプ1", size=self.size)
        pk_type2_text = wx.StaticText(self, -1, "タイプ2", size=self.size)
        pk_char_text = wx.StaticText(self, -1, "性格", size=self.size)
        pk_invent_text = wx.StaticText(self, -1, "持ち物", size=self.size)
        
        text_layout_left = wx.BoxSizer(wx.VERTICAL)
        text_layout_left.Add(pk_name_text)
        text_layout_left.Add(pk_type1_text)
        text_layout_left.Add(pk_type2_text)
        text_layout_left.Add(pk_char_text)
        text_layout_left.Add(pk_invent_text)
        return text_layout_left

    def party_text_right(self):
        pk_abi_text = wx.StaticText(self, -1, "特性", size=self.size)
        pk_move1_text = wx.StaticText(self, -1, "技1", size=self.size)
        pk_move2_text = wx.StaticText(self, -1, "技2", size=self.size)
        pk_move3_text = wx.StaticText(self, -1, "技3", size=self.size)
        pk_move4_text = wx.StaticText(self, -1, "技4", size=self.size)
        
        text_layout_right = wx.BoxSizer(wx.VERTICAL)
        text_layout_right.Add(pk_abi_text)
        text_layout_right.Add(pk_move1_text)
        text_layout_right.Add(pk_move2_text)
        text_layout_right.Add(pk_move3_text)
        text_layout_right.Add(pk_move4_text)

        return text_layout_right


class pk_set_party_Panel(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent, -1)
        self.parent = parent
        self.setting = parent.setting
        self.size = parent.size
        self.conn = parent.conn
        self.df_move_all = parent.df_move_all
        self.use_move_data  = parent.use_move_data

        panel_layout = wx.BoxSizer(wx.VERTICAL)
        panel_layout.Add(self.set_party(), flag=wx.ALIGN_CENTER)
        self.SetSizer(panel_layout)


    def set_party(self):
        layout = wx.FlexGridSizer(3, 2, 70, 60)
        layout.Add(self.party1())
        layout.Add(self.party2())
        layout.Add(self.party3())
        layout.Add(self.party4())
        layout.Add(self.party5())
        layout.Add(self.party6())
        return layout
    
    def party1(self):
        self.pk1_name = wx.ComboCtrl(self, -1, "名前", size=self.size)
        self.pk1_status = wx.TextCtrl(self, -1, "努力値配分")
        self.pk1_type1 = wx.TextCtrl(self, -1, "タイプ1", size=self.size)
        self.pk1_type2 = wx.TextCtrl(self, -1, "タイプ2", size=self.size)
        self.pk1_char = wx.ComboCtrl(self, -1, "性格", size=self.size)
        self.pk1_abi = wx.ComboCtrl(self, -1, "特性", size=self.size)
        self.pk1_move1 = wx.ComboCtrl(self, -1, "技1", size=self.size)
        self.pk1_move2 = wx.ComboCtrl(self, -1, "技2", size=self.size)
        self.pk1_move3 = wx.ComboCtrl(self, -1, "技3", size=self.size)
        self.pk1_move4 = wx.ComboCtrl(self, -1, "技4", size=self.size)
        self.pk1_invent = wx.ComboCtrl(self, -1, "持ち物", size=self.size)
        
        layout_left = wx.BoxSizer(wx.VERTICAL)
        layout_left.Add(self.pk1_name)
        layout_left.Add(self.pk1_type1)
        layout_left.Add(self.pk1_type2)
        layout_left.Add(self.pk1_char)
        layout_left.Add(self.pk1_invent)

        layout_right = wx.BoxSizer(wx.VERTICAL)
        layout_right.Add(self.pk1_abi)
        layout_right.Add(self.pk1_move1)
        layout_right.Add(self.pk1_move2)
        layout_right.Add(self.pk1_move3)
        layout_right.Add(self.pk1_move4)

        layout_party = wx.BoxSizer(wx.HORIZONTAL)
        layout_party.Add(self.party_text_left())
        layout_party.Add(layout_left)
        layout_party.Add(self.party_text_right())
        layout_party.Add(layout_right)

        layout_status = wx.BoxSizer(wx.HORIZONTAL)
        pk_status_text = wx.StaticText(self, -1, "努力値配分", size=self.size)
        layout_status.Add(pk_status_text)
        layout_status.Add(self.pk1_status, flag=wx.EXPAND)

        layout = wx.BoxSizer(wx.VERTICAL)
        layout.Add(layout_party)
        layout.Add(layout_status, flag=wx.EXPAND)
        return layout

    def party2(self):
        self.pk2_name = wx.ComboCtrl(self, -1, "名前", size=self.size)
        self.pk2_status = wx.TextCtrl(self, -1, "努力値配分")
        self.pk2_type1 = wx.TextCtrl(self, -1, "タイプ1", size=self.size)
        self.pk2_type2 = wx.TextCtrl(self, -1, "タイプ2", size=self.size)
        self.pk2_char = wx.ComboCtrl(self, -1, "性格", size=self.size)
        self.pk2_abi = wx.ComboCtrl(self, -1, "特性", size=self.size)
        self.pk2_move1 = wx.ComboCtrl(self, -1, "技1", size=self.size)
        self.pk2_move2 = wx.ComboCtrl(self, -1, "技2", size=self.size)
        self.pk2_move3 = wx.ComboCtrl(self, -1, "技3", size=self.size)
        self.pk2_move4 = wx.ComboCtrl(self, -1, "技4", size=self.size)
        self.pk2_invent = wx.ComboCtrl(self, -1, "持ち物", size=self.size)
        
        layout_left = wx.BoxSizer(wx.VERTICAL)
        layout_left.Add(self.pk2_name)
        layout_left.Add(self.pk2_type1)
        layout_left.Add(self.pk2_type2)
        layout_left.Add(self.pk2_char)
        layout_left.Add(self.pk2_invent)

        layout_right = wx.BoxSizer(wx.VERTICAL)
        layout_right.Add(self.pk2_abi)
        layout_right.Add(self.pk2_move1)
        layout_right.Add(self.pk2_move2)
        layout_right.Add(self.pk2_move3)
        layout_right.Add(self.pk2_move4)

        layout_party = wx.BoxSizer(wx.HORIZONTAL)
        layout_party.Add(self.party_text_left())
        layout_party.Add(layout_left)
        layout_party.Add(self.party_text_right())
        layout_party.Add(layout_right)

        layout_status = wx.BoxSizer(wx.HORIZONTAL)
        pk_status_text = wx.StaticText(self, -1, "努力値配分", size=self.size)
        layout_status.Add(pk_status_text)
        layout_status.Add(self.pk2_status, flag=wx.EXPAND)

        layout = wx.BoxSizer(wx.VERTICAL)
        layout.Add(layout_party)
        layout.Add(layout_status, flag=wx.EXPAND)
        return layout

    def party3(self):
        self.pk3_name = wx.ComboCtrl(self, -1, "名前", size=self.size)
        self.pk3_status = wx.TextCtrl(self, -1, "努力値配分")
        self.pk3_type1 = wx.TextCtrl(self, -1, "タイプ1", size=self.size)
        self.pk3_type2 = wx.TextCtrl(self, -1, "タイプ2", size=self.size)
        self.pk3_char = wx.ComboCtrl(self, -1, "性格", size=self.size)
        self.pk3_abi = wx.ComboCtrl(self, -1, "特性", size=self.size)
        self.pk3_move1 = wx.ComboCtrl(self, -1, "技1", size=self.size)
        self.pk3_move2 = wx.ComboCtrl(self, -1, "技2", size=self.size)
        self.pk3_move3 = wx.ComboCtrl(self, -1, "技3", size=self.size)
        self.pk3_move4 = wx.ComboCtrl(self, -1, "技4", size=self.size)
        self.pk3_invent = wx.ComboCtrl(self, -1, "持ち物", size=self.size)
        
        layout_left = wx.BoxSizer(wx.VERTICAL)
        layout_left.Add(self.pk3_name)
        layout_left.Add(self.pk3_type1)
        layout_left.Add(self.pk3_type2)
        layout_left.Add(self.pk3_char)
        layout_left.Add(self.pk3_invent)

        layout_right = wx.BoxSizer(wx.VERTICAL)
        layout_right.Add(self.pk3_abi)
        layout_right.Add(self.pk3_move1)
        layout_right.Add(self.pk3_move2)
        layout_right.Add(self.pk3_move3)
        layout_right.Add(self.pk3_move4)

        layout_party = wx.BoxSizer(wx.HORIZONTAL)
        layout_party.Add(self.party_text_left())
        layout_party.Add(layout_left)
        layout_party.Add(self.party_text_right())
        layout_party.Add(layout_right)

        layout_status = wx.BoxSizer(wx.HORIZONTAL)
        pk_status_text = wx.StaticText(self, -1, "努力値配分", size=self.size)
        layout_status.Add(pk_status_text)
        layout_status.Add(self.pk3_status, flag=wx.EXPAND)

        layout = wx.BoxSizer(wx.VERTICAL)
        layout.Add(layout_party)
        layout.Add(layout_status, flag=wx.EXPAND)
        return layout

    def party4(self):
        self.pk4_name = wx.ComboCtrl(self, -1, "名前", size=self.size)
        self.pk4_status = wx.TextCtrl(self, -1, "努力値配分")
        self.pk4_type1 = wx.TextCtrl(self, -1, "タイプ1", size=self.size)
        self.pk4_type2 = wx.TextCtrl(self, -1, "タイプ2", size=self.size)
        self.pk4_char = wx.ComboCtrl(self, -1, "性格", size=self.size)
        self.pk4_abi = wx.ComboCtrl(self, -1, "特性", size=self.size)
        self.pk4_move1 = wx.ComboCtrl(self, -1, "技1", size=self.size)
        self.pk4_move2 = wx.ComboCtrl(self, -1, "技2", size=self.size)
        self.pk4_move3 = wx.ComboCtrl(self, -1, "技3", size=self.size)
        self.pk4_move4 = wx.ComboCtrl(self, -1, "技4", size=self.size)
        self.pk4_invent = wx.ComboCtrl(self, -1, "持ち物", size=self.size)

        layout_left = wx.BoxSizer(wx.VERTICAL)
        layout_left.Add(self.pk4_name)
        layout_left.Add(self.pk4_type1)
        layout_left.Add(self.pk4_type2)
        layout_left.Add(self.pk4_char)
        layout_left.Add(self.pk4_invent)

        layout_right = wx.BoxSizer(wx.VERTICAL)
        layout_right.Add(self.pk4_abi)
        layout_right.Add(self.pk4_move1)
        layout_right.Add(self.pk4_move2)
        layout_right.Add(self.pk4_move3)
        layout_right.Add(self.pk4_move4)

        layout_party = wx.BoxSizer(wx.HORIZONTAL)
        layout_party.Add(self.party_text_left())
        layout_party.Add(layout_left)
        layout_party.Add(self.party_text_right())
        layout_party.Add(layout_right)

        layout_status = wx.BoxSizer(wx.HORIZONTAL)
        pk_status_text = wx.StaticText(self, -1, "努力値配分", size=self.size)
        layout_status.Add(pk_status_text)
        layout_status.Add(self.pk4_status, flag=wx.EXPAND)

        layout = wx.BoxSizer(wx.VERTICAL)
        layout.Add(layout_party)
        layout.Add(layout_status, flag=wx.EXPAND)
        return layout

    def party5(self):
        self.pk5_name = wx.ComboCtrl(self, -1, "名前", size=self.size)
        self.pk5_status = wx.TextCtrl(self, -1, "努力値配分")
        self.pk5_type1 = wx.TextCtrl(self, -1, "タイプ1", size=self.size)
        self.pk5_type2 = wx.TextCtrl(self, -1, "タイプ2", size=self.size)
        self.pk5_char = wx.ComboCtrl(self, -1, "性格", size=self.size)
        self.pk5_abi = wx.ComboCtrl(self, -1, "特性", size=self.size)
        self.pk5_move1 = wx.ComboCtrl(self, -1, "技1", size=self.size)
        self.pk5_move2 = wx.ComboCtrl(self, -1, "技2", size=self.size)
        self.pk5_move3 = wx.ComboCtrl(self, -1, "技3", size=self.size)
        self.pk5_move4 = wx.ComboCtrl(self, -1, "技4", size=self.size)
        self.pk5_invent = wx.ComboCtrl(self, -1, "持ち物", size=self.size)
        
        layout_left = wx.BoxSizer(wx.VERTICAL)
        layout_left.Add(self.pk5_name)
        layout_left.Add(self.pk5_type1)
        layout_left.Add(self.pk5_type2)
        layout_left.Add(self.pk5_char)
        layout_left.Add(self.pk5_invent)

        layout_right = wx.BoxSizer(wx.VERTICAL)
        layout_right.Add(self.pk5_abi)
        layout_right.Add(self.pk5_move1)
        layout_right.Add(self.pk5_move2)
        layout_right.Add(self.pk5_move3)
        layout_right.Add(self.pk5_move4)

        layout_party = wx.BoxSizer(wx.HORIZONTAL)
        layout_party.Add(self.party_text_left())
        layout_party.Add(layout_left)
        layout_party.Add(self.party_text_right())
        layout_party.Add(layout_right)

        layout_status = wx.BoxSizer(wx.HORIZONTAL)
        pk_status_text = wx.StaticText(self, -1, "努力値配分", size=self.size)
        layout_status.Add(pk_status_text)
        layout_status.Add(self.pk5_status, flag=wx.EXPAND)

        layout = wx.BoxSizer(wx.VERTICAL)
        layout.Add(layout_party)
        layout.Add(layout_status, flag=wx.EXPAND)
        return layout

    def party6(self):
        self.pk6_name = wx.ComboCtrl(self, -1, "名前", size=self.size)
        self.pk6_status = wx.TextCtrl(self, -1, "努力値配分")
        self.pk6_type1 = wx.TextCtrl(self, -1, "タイプ1", size=self.size)
        self.pk6_type2 = wx.TextCtrl(self, -1, "タイプ2", size=self.size)
        self.pk6_char = wx.ComboCtrl(self, -1, "性格", size=self.size)
        self.pk6_abi = wx.ComboCtrl(self, -1, "特性", size=self.size)
        self.pk6_move1 = wx.ComboCtrl(self, -1, "技1", size=self.size)
        self.pk6_move2 = wx.ComboCtrl(self, -1, "技2", size=self.size)
        self.pk6_move3 = wx.ComboCtrl(self, -1, "技3", size=self.size)
        self.pk6_move4 = wx.ComboCtrl(self, -1, "技4", size=self.size)
        self.pk6_invent = wx.ComboCtrl(self, -1, "持ち物", size=self.size)

        layout_left = wx.BoxSizer(wx.VERTICAL)
        layout_left.Add(self.pk6_name)
        layout_left.Add(self.pk6_type1)
        layout_left.Add(self.pk6_type2)
        layout_left.Add(self.pk6_char)
        layout_left.Add(self.pk6_invent)

        layout_right = wx.BoxSizer(wx.VERTICAL)
        layout_right.Add(self.pk6_abi)
        layout_right.Add(self.pk6_move1)
        layout_right.Add(self.pk6_move2)
        layout_right.Add(self.pk6_move3)
        layout_right.Add(self.pk6_move4)

        layout_party = wx.BoxSizer(wx.HORIZONTAL)
        layout_party.Add(self.party_text_left())
        layout_party.Add(layout_left)
        layout_party.Add(self.party_text_right())
        layout_party.Add(layout_right)

        layout_status = wx.BoxSizer(wx.HORIZONTAL)
        pk_status_text = wx.StaticText(self, -1, "努力値配分", size=self.size)
        layout_status.Add(pk_status_text)
        layout_status.Add(self.pk6_status, flag=wx.EXPAND)

        layout = wx.BoxSizer(wx.VERTICAL)
        layout.Add(layout_party)
        layout.Add(layout_status, flag=wx.EXPAND)
        return layout

    def party_text_left(self):
        pk_name_text = wx.StaticText(self, -1, "名前", size=self.size)
        pk_type1_text = wx.StaticText(self, -1, "タイプ1", size=self.size)
        pk_type2_text = wx.StaticText(self, -1, "タイプ2", size=self.size)
        pk_char_text = wx.StaticText(self, -1, "性格", size=self.size)
        pk_invent_text = wx.StaticText(self, -1, "持ち物", size=self.size)
        
        text_layout_left = wx.BoxSizer(wx.VERTICAL)
        text_layout_left.Add(pk_name_text)
        text_layout_left.Add(pk_type1_text)
        text_layout_left.Add(pk_type2_text)
        text_layout_left.Add(pk_char_text)
        text_layout_left.Add(pk_invent_text)
        return text_layout_left

    def party_text_right(self):
        pk_abi_text = wx.StaticText(self, -1, "特性", size=self.size)
        pk_move1_text = wx.StaticText(self, -1, "技1", size=self.size)
        pk_move2_text = wx.StaticText(self, -1, "技2", size=self.size)
        pk_move3_text = wx.StaticText(self, -1, "技3", size=self.size)
        pk_move4_text = wx.StaticText(self, -1, "技4", size=self.size)
        
        text_layout_right = wx.BoxSizer(wx.VERTICAL)
        text_layout_right.Add(pk_abi_text)
        text_layout_right.Add(pk_move1_text)
        text_layout_right.Add(pk_move2_text)
        text_layout_right.Add(pk_move3_text)
        text_layout_right.Add(pk_move4_text)

        return text_layout_right

    def set_option_button(self):
        self.save_button = wx.Button(self, -1, "保存")
        self.party_list = wx.ComboCtrl(self, -1, "パーティ名", choices=[])

    def save_party(self):
        name = self.party_list.GetValue()
        

