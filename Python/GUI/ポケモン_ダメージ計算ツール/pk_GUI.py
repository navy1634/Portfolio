import wx
from pk_Frame import MainFrame

def main():
    application = wx.App()
    frame = MainFrame()
    frame.SetMaxSize(wx.Size(1100,720))
    frame.SetMinSize(wx.Size(1100,720))
    frame.Show()
    application.MainLoop()

main()
