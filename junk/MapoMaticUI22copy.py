#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
#
# generated by wxGlade 1.0.1 on Tue Apr 27 15:34:59 2021
#

import wx
import gmplot
from cefpython3 import cefpython as cef
import sys
import platform
import os
from wx.core import HORIZONTAL, PRINTBIN_USER, TE_PROCESS_ENTER
import Route_generator1 
# import test 

# builder = Route_generator1.RouteBuilder()
# Route_generator1.RouteDirector(builder.setMid("Nigh University Center", "MaxCHambers Library", False))
# test.cb = test.CarBuilderImpl()
# test.poop = test.CarBuildDirector(test.cb)
# print(test.poop.construct())


WINDOWS = (platform.system() == "Windows")
LINUX = (platform.system() == "Linux")
MAC = (platform.system() == "Darwin")

startLocation =''
endLocation=''

choices = ['Nigh University Center','Communications Building','Max Chambers Library','Math and Computer Science']

ucoBuildings = {
    'Nigh University Center' : (35.65572618535371, -97.47124943368546),
    "Communications Building": (35.657162786958885, -97.47134177810977),
    "Max Chambers Library" : (35.657965312633785, -97.47373031501483),
    "Math and Computer Science": (35.653997083277126, -97.47312997269954)

}


WIDTH = 900
HEIGHT = 640


# begin wxGlade: dependencies
# end wxGlade

# begin wxGlade: extracode
# end wxGlade
apikey = 'AIzaSyDrGcqQdFJDsBWBEPkT7NoXFnTccHlTJ2U' # (your API key here)

def main():
    check_versions()
    sys.excepthook = cef.ExceptHook  # To shutdown all CEF processes on error
    settings = {}
    cef.DpiAware.EnableHighDpiSupport()
    cef.Initialize(settings=settings)
    app = CefApp(False)
    app.MainLoop()
    del app  # Must destroy before calling Shutdown

    cef.Shutdown()


def check_versions():
    print("[wxpython.py] CEF Python {ver}".format(ver=cef.__version__))
    print("[wxpython.py] Python {ver} {arch}".format(
            ver=platform.python_version(), arch=platform.architecture()[0]))
    print("[wxpython.py] wxPython {ver}".format(ver=wx.version()))
    # CEF Python version requirement
    assert cef.__version__ >= "66.0", "CEF Python v66.0+ required to run this"


def scale_window_size_for_high_dpi(width, height):
    """Scale window size for high DPI devices. This func can be
    called on all operating systems, but scales only for Windows.
    If scaled value is bigger than the work area on the display
    then it will be reduced."""
    if not WINDOWS:
        return width, height
    (_, _, max_width, max_height) = wx.GetClientDisplayRect().Get()
    # noinspection PyUnresolvedReferences
    (width, height) = cef.DpiAware.Scale((width, height))
    if width > max_width:
        width = max_width
    if height > max_height:
        height = max_height
    return width, height

class MainFrame(wx.Frame):
    def __init__(self):
        
        # begin wxGlade: MyFrame.__init__
        # startLocation =''
        # endLocation=''
        self.wheelChair=False
        
        if WINDOWS:
            # noinspection PyUnresolvedReferences, PyArgumentList
            print("[wxpython.py] System DPI settings: %s"
                  % str(cef.DpiAware.GetSystemDpi()))
        if hasattr(wx, "GetDisplayPPI"):
            print("[wxpython.py] wx.GetDisplayPPI = %s" % wx.GetDisplayPPI())
        print("[wxpython.py] wx.GetDisplaySize = %s" % wx.GetDisplaySize())

        print("[wxpython.py] MainFrame declared size: %s"
              % str((WIDTH, HEIGHT)))
        size = scale_window_size_for_high_dpi(WIDTH, HEIGHT)
        print("[wxpython.py] MainFrame DPI scaled size: %s" % str(size))
        




        wx.Frame.__init__(self,parent=None, id=wx.ID_ANY,title='wxPython example', size=size)
        print("[wxpython.py] MainFrame actual size: %s" % self.GetSize())
        self.Bind(wx.EVT_CLOSE, self.OnClose)

        self.SetSize((1000, 500))
        self.SetTitle("Mapomatic")

        self.panel_1 = wx.Panel(self, wx.ID_ANY)

        sizer_1 = wx.BoxSizer(wx.HORIZONTAL)

        sizer_2 = wx.BoxSizer(wx.VERTICAL)
        sizer_1.Add(sizer_2, 1, wx.EXPAND, 0)

        label_1 = wx.StaticText(self.panel_1, wx.ID_ANY, "Start Location")
        sizer_2.Add(label_1, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.BOTTOM | wx.TOP, 10)

        self.text_ctrl_ = wx.SearchCtrl(self.panel_1,style=wx.TE_PROCESS_ENTER)
        self.text_ctrl_.ShowCancelButton(True)
        self.text_ctrl_.AutoComplete(choices)
        self.Bind(wx.EVT_SEARCHCTRL_SEARCH_BTN, self.on_enter, self.text_ctrl_)
        
        
        sizer_2.Add(self.text_ctrl_, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.BOTTOM, 10)

        label_2 = wx.StaticText(self.panel_1, wx.ID_ANY, "End location\n")
        sizer_2.Add(label_2, 0, wx.ALIGN_CENTER_HORIZONTAL, 0)

        self.text_ctrl_2 = wx.SearchCtrl(self.panel_1, wx.ID_ANY, "")
        self.text_ctrl_2.ShowCancelButton(True)
        self.text_ctrl_2.AutoComplete(choices)
        self.Bind(wx.EVT_SEARCHCTRL_SEARCH_BTN, self.on_enter, self.text_ctrl_2)
        

        sizer_2.Add(self.text_ctrl_2, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.BOTTOM, 10)

        

        self.checkbox_1 = wx.CheckBox(self.panel_1, wx.ID_ANY, "Wheel Chair Access")
        sizer_2.Add(self.checkbox_1, 0, 0, 0)
        self.Bind(wx.EVT_CHECKBOX, self.on_checked, self.checkbox_1)


        self.button_Submit = wx.Button(self.panel_1, wx.ID_ANY, "Submit")
        self.Bind(wx.EVT_BUTTON, self.on_button_pressed, self.button_Submit)
        sizer_2.Add(self.button_Submit, 0, wx.ALIGN_CENTER_HORIZONTAL, 0)
        
        self.browser_panel = wx.Panel(self.panel_1, wx.ID_ANY, style=wx.BORDER_SIMPLE)
        self.browser_panel.SetMinSize((1000, 400))
        # self.browser_panel.Bind(wx.EVT_SET_FOCUS, self.OnSetFocus)
        # self.browser_panel.Bind(wx.EVT_SIZE, self.OnSize)
         
    
        sizer_1.Add(self.browser_panel, 1, wx.EXPAND, 0)

        
        self.panel_1.SetSizer(sizer_1)
        
        

        
       
        
        self.Show()
        self.Layout()
        # end wxGlade

    def on_button_pressed(self, event):  # wxGlade: MyFrame.<event_handler>
        # print("Event handler 'on_button_pressed' not implemented!")
        # self.set_Start(self.text_ctrl_.GetValue())
        # self.set_End(self.text_ctrl_2.GetValue())
        # start= self.get_Start()
        # end=self.get_End()
 
       
        
        # if start in ucoBuildings:
        #     print(start)
        #     print(ucoBuildings[start])
        
        # if end in ucoBuildings:
        #     print(end)
        #     print(ucoBuildings[end])

            

        # self.embed_browser(ucoBuildings[start][0],ucoBuildings[end][0],ucoBuildings[start][1],ucoBuildings[end][1])
        
        builder = Route_generator1.RouteBuilder()
        Route_generator1.RouteDirector(builder.setMid("Nigh University Center", "MaxCHambers Library", False))
        event.Skip()


    def on_checked(self, event):  # wxGlade: MyFrame.<event_handler>
        print("Wheel Chair Access")
        self.wheelChair= True


        event.Skip()
   
    def on_enter(self, event):  # wxGlade: MyFrame.<event_handler>
        
        
    
 
       
        
    #    """ if start in ucoBuildings:
    #         print(start)
    #         print(ucoBuildings[start])
        
    #     if end in ucoBuildings:
    #         print(end)
    #         print(ucoBuildings[end])

    #       """  

        
        self.embed_browser(ucoBuildings[start][0],ucoBuildings[end][0],ucoBuildings[start][1],ucoBuildings[end][1])
        

        event.Skip()

    #----browser stuff-----------------------------------------------------------------------------------------------------------
    def embed_browser(self, startPoint, midPoint, endPoint):
        

        #Gmplot
        if self.wheelChair is False:
            print('wheel chair = false')
        else:
            print('wheel chair = true')

        print(startPoint)
        print(midPoint)
        print(endPoint)

        

        gmap = gmplot.GoogleMapPlotter.from_geocode('100 N University Dr, Edmond, OK 73034',16, apikey=apikey)
        gmap.scatter(startPoint,endPoint,color=['blue', 'orange'])
        gmap.plot(*midPoint,edge_width=7)
        gmap.draw("map.html")
        
        window_info = cef.WindowInfo()
        (width, height) = self.browser_panel.GetClientSize().Get()
        assert self.browser_panel.GetHandle(), "Window handle not available"
        window_info.SetAsChild(self.browser_panel.GetHandle(),
                               [0, 0, width, height])
        self.browser = cef.CreateBrowserSync(window_info,
                                             url="file:///C:/Users/ninte/Documents/School/Software%20I/Project/map.html")
        self.browser.SetClientHandler(FocusHandler())


    def get_Start(self):
        return self.startLocation
    def set_Start(self,x):
        self.startLocation = x
    def get_End(self):
        return self.endLocation
    def set_End(self,x):
        self.endLocation = x
    
    
    


    def OnSetFocus(self, _):
        
        cef.WindowUtils.OnSetFocus(self.browser_panel.GetHandle(),
                                       0, 0, 0)
        self.browser.SetFocus(True)
     

    def OnSize(self, _):
        cef.WindowUtils.OnSize(self.browser_panel.GetHandle(),
                                   0, 0, 0)
    
        self.browser.NotifyMoveOrResizeStarted()

    def OnClose(self, event):
        print("[wxpython.py] OnClose called")
        
        self.browser.ParentWindowWillClose()
        event.Skip()
        self.clear_browser_references()



    def OnClose(self, event):
        print("[wxpython.py] OnClose called")
        if not self.browser:
            # May already be closing, may be called multiple times on Mac
            return
        self.browser.ParentWindowWillClose()
        event.Skip()
        self.clear_browser_references()
    def clear_browser_references(self):
        # Clear browser references that you keep anywhere in your
        # code. All references must be cleared for CEF to shutdown cleanly.
        self.browser = None

# end of class MyFrame
class FocusHandler(object):
    def OnGotFocus(self, browser, **_):
        # Temporary fix for focus issues on Linux (Issue #284).
        if LINUX:
            print("[wxpython.py] FocusHandler.OnGotFocus:"
                  " keyboard focus fix (Issue #284)")
            browser.SetFocus(True)
class MyApp(wx.App):
    def OnInit(self):
        self.frame = MainFrame(None, wx.ID_ANY, "")
        self.SetTopWindow(self.frame)
        self.frame.Show()
        return True
class CefApp(wx.App):

    def __init__(self, redirect):
        self.timer = None
        self.timer_id = 1
        self.is_initialized = False
        super(CefApp, self).__init__(redirect=redirect)

    def OnPreInit(self):
        super(CefApp, self).OnPreInit()
        # On Mac with wxPython 4.0 the OnInit() event never gets
        # called. Doing wx window creation in OnPreInit() seems to
        # resolve the problem (Issue #350).
        if MAC and wx.version().startswith("4."):
            print("[wxpython.py] OnPreInit: initialize here"
                  " (wxPython 4.0 fix)")
            self.initialize()

    def OnInit(self):
        self.initialize()
        return True

    def initialize(self):
        if self.is_initialized:
            return
        self.is_initialized = True
        self.create_timer()
        frame = MainFrame()
        self.SetTopWindow(frame)
        frame.Show()

    def create_timer(self):
        # See also "Making a render loop":
        # http://wiki.wxwidgets.org/Making_a_render_loop
        # Another way would be to use EVT_IDLE in MainFrame.
        self.timer = wx.Timer(self, self.timer_id)
        self.Bind(wx.EVT_TIMER, self.on_timer, self.timer)
        self.timer.Start(10)  # 10ms timer

    def on_timer(self, _):
        cef.MessageLoopWork()

    def OnExit(self):
        self.timer.Stop()
        return 0
# end of class MyApp

if __name__ == "__main__":
    main()

