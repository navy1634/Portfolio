import wx
from Notebook import TabNote

class MainFrame(wx.Frame):
    def __init__(self):
        super().__init__(None, wx.ID_ANY, "ポケモン図鑑", size=(1000,700))
        panel = wx.Panel(self, -1)
        self.notebook = TabNote(panel)
        self.set_menubar()

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.notebook, 1, wx.ALL|wx.EXPAND, 5)
        panel.SetSizer(sizer)

        self.SetMenuBar(self.menubar)
        self.Layout()
    

    # メニューバーの設定
    def set_menubar(self):
        self.menubar = wx.MenuBar()
        fileMenu = wx.Menu()
        optionsItem = fileMenu.Append(wx.NewId(), "Options", "Show an Options Dialog")
        exitMenuItem = fileMenu.Append(wx.NewId(), "Exit", "Exit the application")
        self.Bind(wx.EVT_MENU, self.app_close, exitMenuItem)

        editmenu = wx.Menu()
        copy_menu = editmenu.Append(wx.NewId(), "Copy", "コピー")

        self.menubar.Append(fileMenu, "&File")
        self.menubar.Append(editmenu, "編集")

    # GUI停止
    def app_close(self, event):
        self.notebook.conn.close()
        wx.Exit()
