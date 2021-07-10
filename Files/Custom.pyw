from tkinter import *
import pickle
import webbrowser,os
dir_path = os.path.dirname(os.path.realpath(__file__)) #to take File path
root=Tk()
root.geometry("400x450")
root.title("EyeDaemon-Rest your eye")
root.resizable(False,False)
root.config(bg="white")
dir_path1=dir_path.replace("\\Files","")
print(dir_path)
def save():
    with open(f"{dir_path1}\\Data\\customdata.dat",'wb') as customdata:
        pickle.dump(f"{rest_title_var.get()},{rest_msg_var.get()}",customdata)
    webbrowser.open(f"{dir_path}\\System.pyw")
def restbutton():
    webbrowser.open(f"{dir_path}\\Rest_Settings.pyw")
def customization():
    pass
def system():
    webbrowser.open(f"{dir_path}\\System.pyw")
# mycolor = '#3889c7'

#Frame
f1=Frame(bg="#00aacc",height=50)
f1.pack(fill=X)
#Labels
#Top Layout
SettingLabel=Label(root,font="Helvetica 17 bold",text="Setup",fg="#dfdfdf",bg="#00aacc").place(x=5,y=10)
SaveButton=Button(root,font="Helvetica 10 bold",text="Save",bg="#0059ff",fg="#dfdfdf",border=2,borderwidth=1,command=save).place(x=340,y=15)
#Body
rest=Button(root,text="Rest Settings",font="Helvetica 15 ",fg="#a0a0a0",bg='White',activeforeground="#00aacc",borderwidth=0,takefocus=2,command=restbutton).place(x=20,y=70)
custom=Button(root,text="Customiztion",font="Helvetica 15 ",fg="#a0a0a0",bg='White',activeforeground="#00aacc",borderwidth=0,command=customization).place(x=160,y=70)
system=Button(root,text="System",font="Helvetica 15 ",fg="#a0a0a0",bg='White',activeforeground="#00aacc",borderwidth=0).place(x=300,y=70)

rest_title_var=StringVar()
resttitle=Label(root,text="Rest Title",font="Sublime 11 italic underline ",bg='White')
resttitle.place(x=15,y=135)
rest_title=Entry(root,width=20,font="Arial 15",fg="Grey",bg="#e2e2e2",textvariable=rest_title_var)
rest_title_var.set("Have Some Rest!")
rest_title.place(x=30,y=160)

rest_msg_var=StringVar()
restmsg=Label(root,text="Rest Message",font="Sublime 11 italic underline ",bg='White')
restmsg.place(x=15,y=190)
rest_msg=Entry(root,width=30,font="Arial 15",fg="Grey",bg="#e2e2e2",textvariable=rest_msg_var)
rest_msg_var.set("Rest your eyes and grab some water!")
rest_msg.place(x=30,y=215)


root.mainloop()