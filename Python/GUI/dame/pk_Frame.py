import wx
from pk_Menu import Menu_bar
from pk_Notebook import TabNote

class MainFrame(wx.Frame):
    def __init__(self):
        super().__init__(None, wx.ID_ANY, "ポケモン図鑑", size=(1000,700))
        panel = wx.Panel(self)
        notebook = TabNote(panel)

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(notebook, 1, wx.ALL|wx.EXPAND, 5)
        panel.SetSizer(sizer)
        self.Layout()
