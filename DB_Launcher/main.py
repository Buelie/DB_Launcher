from ttkbootstrap import Style
#import Beta
import tkinter

#b = Beta.beta_mc()

style = Style(theme="superhero")
MainTK = style.master
# MainTK = tkinter.Tk()

VERMC = ['1.0.0','1.0','1.0.1','1.1.0','1.1','1.2.0','1.2','1.2.1','1.2.2','1.2.3','1.2.4','1.2.5',
         '1.3.0','1.3','1.3.1','1.3.2','1.4.0','1.4','1.4.2','1.4.4','1.4.5','1.4.6','1.4.7','1.5.0','1.5',
         '1.5.1','1.5.2','1.6.0','1.6','1.6.1','1.6.2','1.6.3','1.6.4','1.7.0','1.7','1.7.2','1.7.4','1.7.5','1.7.6',
         '1.7.7','1.7.8','1.7.9','1.7.10','1.8.0','1.8','1.8.1','1.8.2','1.8.3','1.8.4','1.8.5','1.8.6','1.8.7','1.8.8',
         '1.8.9','1.9.0','1.9','1.9.1','1.9.2','1.9.3','1.9.4','1.10.0','1.10','1.10.1','1.10.2','1.11.0','1.11.1',
         '1.11.2','1.12.0','1.12','1.12.1','1.12.2','1.13.0','1.13.1','1.13.2','1.14.0','1.14','1.14.1','1.14.2',
         '1.14.3','1.14.4','1.15.0','1.15','1.15.1','1.15.2','1.16.0','1.16','1.16.1','1.16.2','1.16.3','1.16.4',
         '1.16.5','1.17.0','1.17','1.17.1','1.17.2','1.18.0','1.18','1.18.2','1.19.0','1.19','1.19.1','1.19.2','1.19.3']
MinecraftVer = ['1.8.0']

def addver():
    try:
        if ModApi.get() == 1:
            if AddVer.get() in VERMC:
                MinecraftVer.append(f'Forge-' + AddVer.get())
                rn.config(text="- - -[状态：安装成功]- - -")
            else:
                rn.config(text="- - -[状态：安装失败]- - -")
        elif ModApi.get() == 2:
            if AddVer.get() in VERMC:
                MinecraftVer.append(f'Fabric-' + AddVer.get())
                rn.config(text="- - -[状态：安装成功]- - -")
            else:
                rn.config(text="- - -[状态：安装失败]- - -")
        elif ModApi.get() != 2 or ModApi.get() != 1 or ModApi.get() == "":
            rn.config(text="- - -[状态：安装失败]- - -")
        else:
            rn.config(text="- - -[状态：安装失败]- - -")
        list.insert(0, MinecraftVer[-1])
    except:
        rn.config(text="- - -[状态：安装失败]- - -")

def addverB():
    pass

Bgimg = tkinter.Label(MainTK, text="                     DB启动器                     \n\n", bg="#366ace",font=("楷体",28))
Bgimg.grid(column=10,columnspan=1,ipadx=30,row=1)

AddVer = tkinter.Entry(MainTK,font=("楷体",20))
AddVer.grid(column=10,columnspan=40,ipadx=60,row=2)

rn = tkinter.Label(MainTK,text="- - -[状态：待安装]- - -",fg="#214283",font=("微软雅黑",12))
rn.grid(column=10,columnspan=50,ipadx=60,row=3)

ModApi = tkinter.IntVar()
ModApi.set("Forge")
ApiForge = tkinter.Radiobutton(MainTK,text="Forge",variable=ModApi,value=1)
ApiForge.grid(column=10,columnspan=40,ipadx=60,row=4)
ApiFabric = tkinter.Radiobutton(MainTK,text="Fabric",variable=ModApi,value=2)
ApiFabric.grid(column=10,columnspan=40,ipadx=60,row=5)
AddMCVer = tkinter.Button(MainTK,text=" 安装该版本  ",command=addver)
AddMCVer.grid(column=10,columnspan=10,ipadx=60,row=6)
AddMCVerB = tkinter.Button(MainTK,text="安装其他版本",command=addverB)
AddMCVerB.grid(column=10,columnspan=10,ipadx=60,row=7)

rnter = tkinter.Label(MainTK,text="\n\n")
rnter.grid(column=10,columnspan=50,ipadx=60,row=8)

list = tkinter.Listbox(MainTK,width=20,height=9)
list.grid(column=10,columnspan=40,ipadx=70,row=10)

for item in MinecraftVer:
    list.insert(0,item)

br = tkinter.Label(MainTK,text="------")
br.grid(column=10,columnspan=40,ipadx=60,row=11)

StartGameBtn = tkinter.Button(MainTK,text="启动游戏")
StartGameBtn.grid(column=10,columnspan=40,ipadx=60,row=12)

MainTK.title("DB启动器")
MainTK.geometry("1080x650")
MainTK.mainloop()
