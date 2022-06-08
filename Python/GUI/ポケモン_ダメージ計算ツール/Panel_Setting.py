import wx
import json
import pandas as pd

class pk_setting_Panel(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent, -1)
        with open("use_data\pk_setting.json", encoding="CP932") as js:
            setting = js.read()
            self.setting_data = json.loads(setting)
            js.close()
        
        panel_layout = wx.BoxSizer(wx.VERTICAL)
        panel_layout.Add(wx.StaticText(self, -1, " "))
        panel_layout.Add(wx.StaticText(self, -1, " "))
        panel_layout.Add(self.layout(), flag=wx.SHAPED | wx.ALIGN_CENTER)
        panel_layout.Add(wx.StaticText(self, -1, " "))
        self.SetSizer(panel_layout)

    def layout(self):
        set1 = wx.TextCtrl(self, -1, "設定1")
        set2 = wx.ComboBox(self, -1, "初期表示", choices=["番号順", "名前順"])
        set3 = wx.TextCtrl(self, -1, "設定3")
        set4 = wx.TextCtrl(self, -1, "設定4")
        set5 = wx.TextCtrl(self, -1, "設定5")
        set6 = wx.TextCtrl(self, -1, "設定6")

        layout = wx.BoxSizer(wx.VERTICAL)
        layout.Add(set1)
        layout.Add(set2)
        layout.Add(set3)
        layout.Add(set4)
        layout.Add(set5)
        layout.Add(set6)
        return layout

    def Save(self, event):
        with open("use_data\pk_setting.json", "w", encoding="CP932") as js:
            json.dump(self.setting_data, js, ensure_ascii=False, sort_keys=True)

    def reset_save(self, event):
        """
        設定を規定値に戻す
        """
        return 
    
    def reset_log(self ,event):
        """
        保存データのリセット
        """