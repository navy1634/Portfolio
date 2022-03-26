import wx

class Menu_bar(wx.MenuBar):
    def __init__(self, parent):
        super().__init__(parent, -1)

        fileMenu = wx.Menu()
        save = fileMenu.Append(-1, 'Save')
        exit = fileMenu.Append(-1, 'Exit')
        self.Bind(wx.EVT_MENU, self.OnSave, save)
        self.Bind(wx.EVT_MENU, self.OnExit, exit)

        # Create a menu bar.
        menuBar = wx.MenuBar()
        menuBar.Append(fileMenu, 'File')
        parent.SetMenuBar(menuBar)

    def OnSave(self, event):
        wx.MessageBox('OnSave')

    def OnExit(self, event):
        self.Close()