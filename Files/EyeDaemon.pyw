from tkinter import *
import time,pickle,os,shutil,webbrowser,getpass,threading,pyautogui
pass_index=0
user=getpass.getuser()
start=r"C:\Users\use\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup"
start=start.replace("use",user)
dir_path = os.path.dirname(os.path.realpath(__file__)) #to take File path
dir_path1=dir_path.replace("\\Files","")
with open(f"{dir_path1}\\Data\\sysdata.dat",'rb') as sys:
    sysdata=pickle.load(sys)
with open(f"{dir_path1}\\Data\\customdata.dat",'rb') as custom:
    customdata=pickle.load(custom)
with open(f"{dir_path1}\\Data\\restdata.dat",'rb') as rest:
    restdata=pickle.load(rest)
sysdata=sysdata.split(',')
customdata=customdata.split(',')
restdata=restdata.split(',')
timer=restdata[2]
timer=timer.split(":")
title=customdata[0]
def finder(filepath,startpath):
    a=os.listdir(startpath)
    a=list(a)
    b=0

    index=0
    for i in a:
        if ".lnk" in a[index]:
            b+=1
        index+=1
    if b==0:
        try:
            shutil.copy(filepath,startpath)    
            print("D)")
        except Exception as e:
            print(e)
msg=customdata[1]
class EyeDaemon():
    @staticmethod
    def eye_daemon_full_with_end_no_sound():
        global pass_index
        root=Tk()
        root.title("Rest_Your_Eye")
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        root.resizable(False,False)
        mycolor = '#d3d3d3'
        root.configure(background=mycolor)
        root.wm_attributes("-topmost", 1)
        root.attributes("-fullscreen", True)
        def disable_event():
            pass
        hour=StringVar()
        minute=StringVar()
        second=StringVar()
        hour.set(timer[0])
        minute.set(timer[1])
        second.set(timer[2])
        root.protocol("WM_DELETE_WINDOW", disable_event)

        Button(text="Click here to quit",command=root.destroy,padx=10,pady=10,bg="#f4f5f0", font="sublime 20 bold italic").place(x=525,y=450)
        Label(root,text=title, font="Sublime 70 bold",bg="#d3d3d3").place(x=300,y=150)
        Label(root,text=msg,bg="#d3d3d3", font="Sublime 20 bold").place(x=415,y=250)
        hourEntry= Entry(root, width=2, font="Arial 80",bg="#f4f5f0",textvariable=hour)
        hourEntry.place(x=450,y=300)
        minuteEntry= Entry(root, width=2, font="Arial 80",bg="#f4f5f0",textvariable=minute)
        minuteEntry.place(x=600,y=300)
        
        secondEntry= Entry(root, width=2, font="Arial 80",fg="White",bg="#3b2e1e",textvariable=second)
        secondEntry.place(x=750,y=300)

        
        try:
            # the input provided by the user is
            # stored in here :temp
            temp = int(hour.get())*3600 + int(minute.get())*60 + int(second.get())
        except:
            print("Please input the right value")
        while temp >-1:
            # divmod(firstvalue = temp//60, secondvalue = temp%60)
            mins,secs = divmod(temp,60)

            # Converting the input entered in mins or secs to hours,
            # mins ,secs(input = 110 min --> 120*60 = 6600 => 1hr :
            # 50min: 0sec)
            hours=0
            if mins >60:
                
                # divmod(firstvalue = temp//60, secondvalue
                # = temp%60)
                hours, mins = divmod(mins, 60)
            
            # using format () method to store the value up to
            # two decimal places
            hour.set("{0:2d}".format(hours))
            minute.set("{0:2d}".format(mins))
            second.set("{0:2d}".format(secs))

            # updating the GUI window after decrementing the
            # temp value every time
            root.update()
            time.sleep(1)

            # when temp value = 0; then a messagebox pop's up
            # with a message:"Time's up"
            if (temp == 0):
                time.sleep(2)
                root.destroy()
            
            # after every one sec the value of temp will be decremented
            # by one
            temp -= 1
        root.mainloop()
        pass_index=1
    def eye_daemon_full_no_end_no_sound():
        global pass_index
        root=Tk()
        root.title("Rest_Your_Eye")
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        root.resizable(False,False)
        mycolor = '#d3d3d3'
        root.configure(background=mycolor)
        root.wm_attributes("-topmost", 1)
        root.attributes("-fullscreen", True)
        def disable_event():
            pass
        hour=StringVar()
        minute=StringVar()
        second=StringVar()
        hour.set(timer[0])
        minute.set(timer[1])
        second.set(timer[2])
        # root.protocol("WM_DELETE_WINDOW", disable_event)

        Label(root,text=title, font="Sublime 70 bold",bg="#d3d3d3").place(x=300,y=150)
        Label(root,text=msg,bg="#d3d3d3", font="Sublime 20 bold").place(x=415,y=250)
        hourEntry= Entry(root, width=2, font="Arial 80",bg="#f4f5f0",textvariable=hour)
        hourEntry.place(x=450,y=300)
        minuteEntry= Entry(root, width=2, font="Arial 80",bg="#f4f5f0",textvariable=minute)
        minuteEntry.place(x=600,y=300)
        
        secondEntry= Entry(root, width=2, font="Arial 80",fg="White",bg="#3b2e1e",textvariable=second)
        secondEntry.place(x=750,y=300)

        
        try:
            # the input provided by the user is
            # stored in here :temp
            temp = int(hour.get())*3600 + int(minute.get())*60 + int(second.get())
        except:
            print("Please input the right value")
        while temp >-1:
            # divmod(firstvalue = temp//60, secondvalue = temp%60)
            mins,secs = divmod(temp,60)

            # Converting the input entered in mins or secs to hours,
            # mins ,secs(input = 110 min --> 120*60 = 6600 => 1hr :
            # 50min: 0sec)
            hours=0
            if mins >60:
                
                # divmod(firstvalue = temp//60, secondvalue
                # = temp%60)
                hours, mins = divmod(mins, 60)
            
            # using format () method to store the value up to
            # two decimal places
            hour.set("{0:2d}".format(hours))
            minute.set("{0:2d}".format(mins))
            second.set("{0:2d}".format(secs))

            # updating the GUI window after decrementing the
            # temp value every time
            root.update()
            time.sleep(1)

            # when temp value = 0; then a messagebox pop's up
            # with a message:"Time's up"
            if (temp == 0):
                time.sleep(2)
                root.destroy()
            
            # after every one sec the value of temp will be decremented
            # by one
            temp -= 1
        root.mainloop()
        pass_index=1
    def eye_daemon_full_with_end_sound():
        global pass_index
        from playsound import playsound
        playsound(f"{dir_path1}\\Audio\\1.mp3",False)
        time.sleep(2)
        root=Tk()
        root.title("Rest_Your_Eye")
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        root.resizable(False,False)
        mycolor = '#d3d3d3'
        root.configure(background=mycolor)
        root.wm_attributes("-topmost", 1)
        root.attributes("-fullscreen", True)
        def disable_event():
            pass
        hour=StringVar()
        minute=StringVar()
        second=StringVar()
        hour.set(timer[0])
        minute.set(timer[1])
        second.set(timer[2])
        root.protocol("WM_DELETE_WINDOW", disable_event)

        Button(text="Click here to quit",command=root.destroy,padx=10,pady=10,bg="#f4f5f0", font="sublime 20 bold italic").place(x=525,y=450)
        Label(root,text=title, font="Sublime 70 bold",bg="#d3d3d3").place(x=300,y=150)
        Label(root,text=msg,bg="#d3d3d3", font="Sublime 20 bold").place(x=415,y=250)
        hourEntry= Entry(root, width=2, font="Arial 80",bg="#f4f5f0",textvariable=hour)
        hourEntry.place(x=450,y=300)
        minuteEntry= Entry(root, width=2, font="Arial 80",bg="#f4f5f0",textvariable=minute)
        minuteEntry.place(x=600,y=300)
        
        secondEntry= Entry(root, width=2, font="Arial 80",fg="White",bg="#3b2e1e",textvariable=second)
        secondEntry.place(x=750,y=300)

        
        try:
            # the input provided by the user is
            # stored in here :temp
            temp = int(hour.get())*3600 + int(minute.get())*60 + int(second.get())
        except:
            print("Please input the right value")
        while temp >-1:
            # divmod(firstvalue = temp//60, secondvalue = temp%60)
            mins,secs = divmod(temp,60)

            # Converting the input entered in mins or secs to hours,
            # mins ,secs(input = 110 min --> 120*60 = 6600 => 1hr :
            # 50min: 0sec)
            hours=0
            if mins >60:
                
                # divmod(firstvalue = temp//60, secondvalue
                # = temp%60)
                hours, mins = divmod(mins, 60)
            
            # using format () method to store the value up to
            # two decimal places
            hour.set("{0:2d}".format(hours))
            minute.set("{0:2d}".format(mins))
            second.set("{0:2d}".format(secs))

            # updating the GUI window after decrementing the
            # temp value every time
            root.update()
            time.sleep(1)

            # when temp value = 0; then a messagebox pop's up
            # with a message:"Time's up"
            if (temp == 0):
                time.sleep(2)
                root.destroy()
            
            # after every one sec the value of temp will be decremented
            # by one
            temp -= 1
        root.mainloop()
        pass_index=1
    def eye_daemon_full_no_end_sound():
        global pass_index
        from playsound import playsound
        playsound(f"{dir_path1}\\Audio\\1.mp3",False)
        time.sleep(2)
        root=Tk()
        root.title("Rest_Your_Eye")
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        root.resizable(False,False)
        mycolor = '#d3d3d3'
        root.configure(background=mycolor)
        root.wm_attributes("-topmost", 1)
        root.attributes("-fullscreen", True)
        def disable_event():
            pass
        hour=StringVar()
        minute=StringVar()
        second=StringVar()
        hour.set(timer[0])
        minute.set(timer[1])
        second.set(timer[2])
        root.protocol("WM_DELETE_WINDOW", disable_event)

        Label(root,text=title, font="Sublime 70 bold",bg="#d3d3d3").place(x=300,y=150)
        Label(root,text=msg,bg="#d3d3d3", font="Sublime 20 bold").place(x=415,y=250)
        hourEntry= Entry(root, width=2, font="Arial 80",bg="#f4f5f0",textvariable=hour)
        hourEntry.place(x=450,y=300)
        minuteEntry= Entry(root, width=2, font="Arial 80",bg="#f4f5f0",textvariable=minute)
        minuteEntry.place(x=600,y=300)
        
        secondEntry= Entry(root, width=2, font="Arial 80",fg="White",bg="#3b2e1e",textvariable=second)
        secondEntry.place(x=750,y=300)

        
        try:
            # the input provided by the user is
            # stored in here :temp
            temp = int(hour.get())*3600 + int(minute.get())*60 + int(second.get())
        except:
            print("Please input the right value")
        while temp >-1:
            # divmod(firstvalue = temp//60, secondvalue = temp%60)
            mins,secs = divmod(temp,60)

            # Converting the input entered in mins or secs to hours,
            # mins ,secs(input = 110 min --> 120*60 = 6600 => 1hr :
            # 50min: 0sec)
            hours=0
            if mins >60:
                
                # divmod(firstvalue = temp//60, secondvalue
                # = temp%60)
                hours, mins = divmod(mins, 60)
            
            # using format () method to store the value up to
            # two decimal places
            hour.set("{0:2d}".format(hours))
            minute.set("{0:2d}".format(mins))
            second.set("{0:2d}".format(secs))

            # updating the GUI window after decrementing the
            # temp value every time
            root.update()
            time.sleep(1)

            # when temp value = 0; then a messagebox pop's up
            # with a message:"Time's up"
            if (temp == 0):
                time.sleep(2)
                root.destroy()
            
            # after every one sec the value of temp will be decremented
            # by one
            temp -= 1
        root.mainloop()
        pass_index=1
    def simple_noti():
        global pass_index
        from plyer import notification
        notification.notify(
            title = title,
            message=msg,
            app_name="Rest_Your_Eyes",
            # displaying time
            timeout=10)
        index=1
    def b():
        from pywinauto import application
        app2 = application.Application().connect(title='Rest_Your_Eye')
        try:
            while pass_index<1: 
                app2.Rest_Your_Eye.set_focus()
        except Exception as e:
            pass
    def c():
        if pass_index==0:
            print("as")
            pyautogui.keyDown('shift')
        else:
            print('keyUp')
            pyautogui.keyUp('shift')

        



finder(start,dir_path)
a=EyeDaemon

if restdata[0] and restdata[3] and restdata[4]=='1':
    try:
        threading.Thread(target=a.c).start()
        threading.Thread(target=a.eye_daemon_full_with_end_sound).start()
        threading.Thread(target=a.b).start()
    except Exception as e:
        print(e)
if restdata[0]=='1' and restdata[3]=='0' and restdata[4]=='0':
    print("A")
    try:
        threading.Thread(target=a.c).start()
        threading.Thread(target=a.eye_daemon_full_no_end_no_sound).start()
        threading.Thread(target=a.b).start()
    except Exception as e:
        print(e)
if restdata[0]=='2':
    print("b")
    try:
        a.simple_noti()
    except Exception as e:
        print(e)
if restdata[0]=='1' and restdata[3]=='1' and restdata[4]=='0':
    print("c")
    try:
        threading.Thread(target=a.c).start()
        threading.Thread(target=a.eye_daemon_full_no_end_sound).start()
        threading.Thread(target=a.b).start()

    except Exception as e:
        print(e)
if restdata[0]=='1' and restdata[3]=='0' and restdata[4]=='1':
    print("d")
    try:
        threading.Thread(target=a.c).start()
        threading.Thread(target=a.eye_daemon_full_no_end_sound).start()
        threading.Thread(target=a.b).start()
    except Exception as e:
        print(e)
webbrowser.open(f"{dir_path}\\stopwatch.pyw")