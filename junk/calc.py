#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
#
# generated by wxGlade 1.0.1 on Mon Apr 26 17:45:41 2021
#

import wx

# begin wxGlade: dependencies
# end wxGlade

# begin wxGlade: extracode
# end wxGlade


class CalculatorFrame(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: CalculatorFrame.__init__
        kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.SetSize((400, 300))
        self.SetTitle("Calculator")

        self.panel_1 = wx.Panel(self, wx.ID_ANY)

        sizer_1 = wx.BoxSizer(wx.VERTICAL)

        sizer_2 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_1.Add(sizer_2, 0, wx.ALL | wx.EXPAND, 4)

        label_1 = wx.StaticText(self.panel_1, wx.ID_ANY, "value 1")
        sizer_2.Add(label_1, 0, wx.ALIGN_CENTER_VERTICAL, 0)

        self.text_value1 = wx.TextCtrl(self.panel_1, wx.ID_ANY, "")
        sizer_2.Add(self.text_value1, 1, 0, 0)

        sizer_5 = wx.StdDialogButtonSizer()
        sizer_1.Add(sizer_5, 0, wx.EXPAND, 0)

        label_4 = wx.StaticText(self.panel_1, wx.ID_ANY, "Operator")
        sizer_5.Add(label_4, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 4)

        self.radio_box_1 = wx.RadioBox(self.panel_1, wx.ID_ANY, "", choices=["+", "-", "*", "/"], majorDimension=1, style=wx.RA_SPECIFY_ROWS)
        self.radio_box_1.SetSelection(0)
        sizer_5.Add(self.radio_box_1, 0, 0, 0)

        sizer_3 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_1.Add(sizer_3, 0, wx.EXPAND, 0)

        label_2 = wx.StaticText(self.panel_1, wx.ID_ANY, "value 2")
        sizer_3.Add(label_2, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 4)

        self.text_value2 = wx.TextCtrl(self.panel_1, wx.ID_ANY, "")
        sizer_3.Add(self.text_value2, 1, 0, 0)

        static_line_1 = wx.StaticLine(self.panel_1, wx.ID_ANY)
        sizer_1.Add(static_line_1, 0, wx.BOTTOM | wx.EXPAND | wx.TOP, 5)

        sizer_4 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_1.Add(sizer_4, 1, wx.EXPAND, 0)

        label_3 = wx.StaticText(self.panel_1, wx.ID_ANY, "results")
        sizer_4.Add(label_3, 0, 0, 0)

        self.text_result = wx.TextCtrl(self.panel_1, wx.ID_ANY, "", style=wx.TE_MULTILINE | wx.TE_READONLY)
        self.text_result.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_3DDKSHADOW))
        sizer_4.Add(self.text_result, 1, wx.EXPAND, 0)

        sizer_6 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_1.Add(sizer_6, 0, wx.ALIGN_CENTER_HORIZONTAL, 0)

        self.button_execute = wx.Button(self.panel_1, wx.ID_ANY, " Execute")
        self.button_execute.SetDefault()
        sizer_6.Add(self.button_execute, 0, wx.ALL, 5)

        self.button_reset = wx.Button(self.panel_1, wx.ID_ANY, "Reset")
        sizer_6.Add(self.button_reset, 0, wx.ALL, 5)

        sizer_5.Realize()

        self.panel_1.SetSizer(sizer_1)

        self.Layout()
        # end wxGlade

# end of class CalculatorFrame

class MyApp(wx.App):
    def OnInit(self):
        self.frame = CalculatorFrame(None, wx.ID_ANY, "")
        self.SetTopWindow(self.frame)
        self.frame.Show()
        return True

# end of class MyApp

if __name__ == "__main__":
    app = MyApp(0)
    app.MainLoop()
