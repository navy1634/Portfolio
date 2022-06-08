import wx
from Frame import MainFrame

def main():
    application = wx.App()
    frame = MainFrame()
    frame.SetMaxSize(wx.Size(1000,700))
    frame.SetMinSize(wx.Size(1000,700))
    frame.Show()
    application.MainLoop()

main()

