from ttkbootstrap import Style
import main
import tkinter

#b = Beta.beta_mc()

class window:
    def ins_wind(self = None):
        style = Style(theme="yeti")
        MainTKT = style.master
        # MainTK = tkinter.Tk()

        MainTKT.title("DB启动器 - 安装其他版本")
        MainTKT.geometry("1080x650")
        MainTKT.mainloop()
#MainTKT.mainloop()
