# Creates a task-bar icon with balloon tip.  Run from Python.exe to see the
# messages printed.  Right click for balloon tip.  Double click to exit.
# original version of this demo available at http://www.itamarst.org/software/
import win32api, win32con, win32gui

class Taskbar:
    def __init__(self):
        self.visible = 0
        message_map = {
            win32con.WM_DESTROY: self.onDestroy,
            win32con.WM_USER+20 : self.onTaskbarNotify,
        }
        # Register the Window class.
        wc = win32gui.WNDCLASS()
        hinst = wc.hInstance = win32api.GetModuleHandle(None)
        wc.lpszClassName = "PythonTaskbarDemo"
        wc.style = win32con.CS_VREDRAW | win32con.CS_HREDRAW;
        wc.hCursor = win32gui.LoadCursor( 0, win32con.IDC_ARROW )
        wc.hbrBackground = win32con.COLOR_WINDOW
        wc.lpfnWndProc = message_map # could also specify a wndproc.
        classAtom = win32gui.RegisterClass(wc)
        # Create the Window.
        style = win32con.WS_OVERLAPPED | win32con.WS_SYSMENU
        self.hwnd = win32gui.CreateWindow( classAtom, "Taskbar Demo", style, \
                    0, 0, win32con.CW_USEDEFAULT, win32con.CW_USEDEFAULT, \
                    0, 0, hinst, None)
        win32gui.UpdateWindow(self.hwnd)

    def setIcon(self, hicon, tooltip=None):
        self.hicon = hicon
        self.tooltip = tooltip
        
    def show(self):
        """Display the taskbar icon"""
        flags = win32gui.NIF_ICON | win32gui.NIF_MESSAGE
        if self.tooltip is not None:
            flags |= win32gui.NIF_TIP
            nid = (self.hwnd, 0, flags, win32con.WM_USER+20, self.hicon, self.tooltip)
        else:
            nid = (self.hwnd, 0, flags, win32con.WM_USER+20, self.hicon)
        if self.visible:
            self.hide()
        win32gui.Shell_NotifyIcon(win32gui.NIM_ADD, nid)
        self.visible = 1

    def hide(self):
        """Hide the taskbar icon"""
        if self.visible:
            nid = (self.hwnd, 0)
            win32gui.Shell_NotifyIcon(win32gui.NIM_DELETE, nid)
        self.visible = 0
        
    def onDestroy(self, hwnd, msg, wparam, lparam):
        self.hide()
        win32gui.PostQuitMessage(0) # Terminate the app.

    def onTaskbarNotify(self, hwnd, msg, wparam, lparam):
        if lparam == win32con.WM_LBUTTONUP:
            self.onClick()
        elif lparam == win32con.WM_LBUTTONDBLCLK:
            self.onDoubleClick()
        elif lparam ==  win32con.WM_RBUTTONUP:
            self.onRightClick()
        return 1

    def onClick(self):
        """Override in subclassess"""
        pass

    def onDoubleClick(self):
        """Override in subclassess"""
        pass
    def onRightClick(self):
        """Override in subclasses"""
        pass

if __name__=='__main__':
    class DemoTaskbar(Taskbar):

        def __init__(self):
            Taskbar.__init__(self)
            icon = win32gui.LoadIcon(0, win32con.IDI_APPLICATION)
            self.setIcon(icon)
            self.show()
            
        def onClick(self):
            print "you clicked"

        def onDoubleClick(self):
            print "you double clicked, bye!"
            win32gui.PostQuitMessage(0)

        def onRightClick(self):
            #NIF_INFO flag below enables balloony stuff
            flags = win32gui.NIF_ICON | win32gui.NIF_MESSAGE | win32gui.NIF_INFO
            #define the icon properties (see http://msdn.microsoft.com/library/default.asp?url=/library/en-us/shellcc/platform/shell/reference/structures/notifyicondata.asp)
            nid = (self.hwnd, 0, flags, win32con.WM_USER+20, self.hicon, "", "Balloon Message", 10, "Balloon", win32gui.NIIF_INFO)
            #change our already present icon ...
            win32gui.Shell_NotifyIcon(win32gui.NIM_MODIFY, nid)
            
            
    t = DemoTaskbar()
    win32gui.PumpMessages() # start demo