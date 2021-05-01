import wx
from MapoMaticUI22 import MainFrame


class Myframe(MainFrame):
    def __init__(self, *args, **kwds):
        MainFrame.__init__(self, *args, **kwds)

    def on_button_pressed(self, event):  # wxGlade: MyFrame.<event_handler>
        print("Event handler 'on_button_pressed' not implemented!")
        event.Skip()

class MyApp(wx.App):
    def OnInit(self):
        self.frame = MainFrame(None, wx.ID_ANY, "")
        self.SetTopWindow(self.frame)
        self.frame.Show()
        return True


if __name__ == "__main__":
    app = MyApp(0)
    app.MainLoop()