from tkinter import * 
import webbrowser,os,subprocess,pickle
index=0
dir_path = os.path.dirname(os.path.realpath(__file__)) #to take File path
dir_path1=dir_path.replace("\\Files","")
print(dir_path)
def save():
    with open(f"{dir_path1}\\Data\\restdata.dat",'wb') as restdata:
        pickle.dump(f"{radiovar.get()},{hourvar.get()}:{minsvar.get()}:{secvar.get()},{hour_len_var.get()}:{mins_len_var.get()}:{sec_len_var.get()},{checkvar1.get()},{checkvar2.get()}",restdata)
    webbrowser.open(f"{dir_path}\\Custom.pyw")
def restbutton():
    pass
def customization():
    webbrowser.open(f"{dir_path}\\Custom.pyw")
def system():
    webbrowser.open(f'{dir_path}\\System.pyw')
root=Tk()
root.geometry("400x450")
root.title("EyeDaemon-Rest your eye")
root.resizable(False,False)
root.config(bg="white")
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
system=Button(root,text="System",font="Helvetica 15 ",fg="#a0a0a0",bg='White',activeforeground="#00aacc",borderwidth=0,command=system).place(x=300,y=70)


#Rest body
#Notifications
radiovar=IntVar()
radiovar.set(1)
a=Label(text="Notify me using",font="Sublime 11 italic underline ",bg='White')
a.place(x=15,y=135)
notify1=Radiobutton(root,text="Fullscreen Notifications",font="Sublime 10 bold",variable=radiovar,value=1,relief=SUNKEN)
notify1.place(x=30,y=160)
notify2=Radiobutton(root,text="Simple Notifications     ",font="Sublime 10 bold",variable=radiovar,value=2,relief=SUNKEN)
notify2.place(x=30,y=187)
#Rest Frequency
hourvar=StringVar()
minsvar=StringVar()
secvar=StringVar()
b=Label(text="Rest Frequency",font="Sublime 11 italic underline ",bg='White')
b.place(x=15,y=230)
hour=Entry(root,width=int(2.5), font="Arial 15",fg="Grey",bg="#e2e2e2",textvariable=hourvar)
hour.place(x=30,y=255)
mins=Entry(root,width=int(2.5), font="Arial 15",fg="Grey",bg="#e2e2e2",textvariable=minsvar)
mins.place(x=60,y=255)
sec=Entry(root,width=int(2.5), font="Arial 15",fg="Grey",bg="#e2e2e2",textvariable=secvar)
sec.place(x=90,y=255)
hourvar.set("00")
minsvar.set("20")
secvar.set("00")
#Rest Lenth
hour_len_var=StringVar()
mins_len_var=StringVar()
sec_len_var=StringVar()
c=Label(text="Rest Lenth",font="Sublime 11 italic underline ",bg='White')
c.place(x=15,y=292)
hour1=Entry(root,width=int(2.5), font="Arial 15",fg="Grey",bg="#e2e2e2",textvariable=hour_len_var)
hour1.place(x=30,y=320)
mins1=Entry(root,width=int(2.5), font="Arial 15",fg="Grey",bg="#e2e2e2",textvariable=mins_len_var)
mins1.place(x=60,y=320)
sec1=Entry(root,width=int(2.5), font="Arial 15",fg="Grey",bg="#e2e2e2",textvariable=sec_len_var)
sec1.place(x=90,y=320)
hour_len_var.set("00")
mins_len_var.set("02")
sec_len_var.set("00")
#Check Buttons 
checkvar1=IntVar()
checkvar2=IntVar()
d=Label(text="Options",font="Sublime 11 italic underline ",bg='White')
d.place(x=15,y=350)
soundcheck=Checkbutton(text="Playsound while starting the rest?",font="Sublime 9 bold",variable=checkvar1)
soundcheck.place(x=30,y=375)
endrestcheck=Checkbutton(text="Allow End Rest?                                  ",font="Sublime 9 bold",variable=checkvar2)
endrestcheck.place(x=30,y=400)
root.mainloop()

