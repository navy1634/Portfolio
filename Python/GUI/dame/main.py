import wx
from pk_Frame import MainFrame

def main():
    application = wx.App()
    frame = MainFrame()
    frame.SetMaxSize(wx.Size(1000,700))
    frame.SetMinSize(wx.Size(1000,700))
    frame.Show()
    application.MainLoop()

main()


# - バフデバフ(複数選択可)
# - 持ち物(戦闘用のみ) -> 持ち物一覧の取得

# - タイプ相性
# - 性格補正

# - 覚える技一覧 -> 現在の未完のものを改良

# - 出力のコピー

# - 検索保存機能
# - オプション機能(配置)
# - menuバー
