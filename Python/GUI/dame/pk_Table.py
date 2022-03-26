import wx
import wx.lib.mixins.listctrl as listmix

# パネルに反映するリストを定義
class mainTable(wx.ListCtrl, listmix.ListCtrlAutoWidthMixin):
    def __init__(self, panel, size):
        wx.ListCtrl.__init__(self, panel, -1, style=wx.LC_REPORT | wx.SUNKEN_BORDER, size=size, pos=wx.Point(10, 20))
        listmix.ListCtrlAutoWidthMixin.__init__(self)
