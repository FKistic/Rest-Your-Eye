from tkinter import *
import webbrowser,os,pickle
dir_path = os.path.dirname(os.path.realpath(__file__)) #to take File path
dir_path1=dir_path.replace("\\Files","")
root=Tk()
root.geometry("400x450")
root.wm_attributes("-topmost", 1)
root.title("EyeDaemon-Rest your eye")
root.resizable(False,False)
root.config(bg="white")
# mycolor = '#3889c7'
#Frame
f1=Frame(bg="#00aacc",height=50)
f1.pack(fill=X)
def save():
    with open(f"{dir_path1}\\Data\\sysdata.dat",'wb') as sysdata:
        pickle.dump(f"{checkvar.get()}",sysdata)
        webbrowser.open(f"{dir_path}\\stopwatch.pyw")
def restbutton():
    webbrowser.open(f"{dir_path}\\Rest_Settings.pyw")
def customization():
    webbrowser.open(f"{dir_path}\\Custom.pyw")
def system():
    pass
SettingLabel=Label(root,font="Helvetica 17 bold",text="Setup",fg="#dfdfdf",bg="#00aacc").place(x=5,y=10)
SaveButton=Button(root,font="Helvetica 10 bold",text="Save",bg="#0059ff",fg="#dfdfdf",border=2,borderwidth=1,command=save).place(x=340,y=15)
#Body
rest=Button(root,text="Rest Settings",font="Helvetica 15 ",fg="#a0a0a0",bg='White',activeforeground="#00aacc",borderwidth=0,takefocus=2,command=restbutton).place(x=20,y=70)
custom=Button(root,text="Customiztion",font="Helvetica 15 ",fg="#a0a0a0",bg='White',activeforeground="#00aacc",borderwidth=0,command=customization).place(x=160,y=70)
system=Button(root,text="System",font="Helvetica 15 ",fg="#a0a0a0",bg='White',activeforeground="#00aacc",borderwidth=0,command=system).place(x=300,y=70)
checkvar=IntVar()
runatboot=Checkbutton(root,text="Run on boot",font="Sublime 11 italic underline ",variable=checkvar)
runatboot.place(x=15,y=135)
root.mainloop()

