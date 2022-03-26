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