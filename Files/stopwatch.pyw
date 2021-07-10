import time,os,pickle,webbrowser
index=0
dir_path = os.path.dirname(os.path.realpath(__file__)) #to take File path
dir_path1=dir_path.replace("\\Files","")
with open(f"{dir_path1}\\Data\\restdata.dat",'rb') as rest:
    restdata=pickle.load(rest)
restdata=restdata.split(',')
frequency=restdata[1].split(":")
hour=frequency[0]
mins=frequency[1]
sec=frequency[2]
hour1=int(hour)
mins1=int(mins)
sec1=int(sec)
if hour1>0:
    hour1=hour1*3600
if mins1>0:
    min1=mins1*60
if sec1>0:
    sec1=sec1
total=hour1+min1+sec1
while True:
    print(index,end="\r")
    time.sleep(1)
    index+=1
    if index==total:
        break
webbrowser.open(f"{dir_path}\\EyeDaemon.py")