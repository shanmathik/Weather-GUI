
import pyowm
import json
import requests
from tkinter import *
import tkinter.messagebox
from PIL import ImageTk,Image

# Required Details
root = tkinter.Tk()
root.geometry("1250x650")
root.title("Weather App")
#root.configure(bg='white')

# for images

img = ImageTk.PhotoImage(Image.open('green-bg.jpg'))
panel = Label(root,image=img)
panel.place(x=11,y=11)

lable_0 = Label(root,text="  WEATHER NOW  ",anchor='e',font=("comic sans",48,"bold",),bg='lawn green',fg='black',bd=7,relief='raised')
lable_0.place(x=400,y=30)

city_names = StringVar()
entry_1 = Entry(root,font=("arial",23),bg='pale green',textvariable=city_names,width=24)
entry_1.place(x=700,y=160)

lable_7 = Label(root,text="Enter the city name ",width = 20,font=("comic sans",23,"bold"),bg='green2',fg='grey2',borderwidth=3,relief="raised")
lable_7.place(x=200,y=160)

lable_1 = Label(root,text=" Minimum Temperature : ",width = 20,font=("comic sans",17),fg='light yellow',bg='dark green',borderwidth=3,relief="raised")
lable_1.place(x=110,y=310)


lable_6 = Label(root,text="Maximum Temperature : ",width = 20,font=("comic sans",17),fg='light yellow',bg='dark green',borderwidth=3,relief="raised")
lable_6.place(x=110,y=380)

lable_2 = Label(root,text="Temperature : ",width = 20,font=("comic sans",17),fg='light yellow',bg='dark green',borderwidth=3,relief="raised")
lable_2.place(x=110,y=450)

lable_3 = Label(root,text="Wind Speed : ",width = 20,font=("comic sans",17),fg='light yellow',bg='dark green',borderwidth=3,relief="raised")
lable_3.place(x=750,y=310)

lable_5 = Label(root,text="Humidity : ",width = 20,font=("comic sans",17),fg='light yellow',bg='dark green',borderwidth=3,relief="raised")
lable_5.place(x=750,y=380)

lable_8 = Label(root,text="Pressure : ",width = 20,font=("comic sans",17),fg='light yellow',bg='dark green',borderwidth=3,relief="raised")
lable_8.place(x=750,y=450)

lable_9= Label(root,text=" Description :",width = 20,font=("comic sans",17),fg='light yellow',bg='dark green',borderwidth=3,relief="raised")
lable_9.place(x=320,y=540)

lable_mintemp = Label(root,text="...",width = 7,bg='white',font=("bold",25),fg='black')
lable_mintemp.place(x=460,y=310)

lable_maxtemp = Label(root,text="...",width = 7,bg='white',font=("bold",25),fg='black')
lable_maxtemp.place(x=460,y=380)

lable_temp = Label(root,text="...",width = 7,bg='white',font=("bold",25),fg='black')
lable_temp.place(x=460,y=450)

lable_speed = Label(root,text="...",width = 7,bg='white',font=("bold",25),fg='black')
lable_speed.place(x=1030,y=310)

lable_humid = Label(root,text="...",width = 7,bg='white',font=("bold",25),fg='black')
lable_humid.place(x=1030,y=380)

lable_pressure = Label(root,text="...",width = 15,bg='white',font=("bold",17),fg='black')
lable_pressure.place(x=1030,y=450)

lable_desc = Label(root,text="...",width = 24,bg='white',font=("bold",17),fg='black')
lable_desc.place(x=693,y=540)





# api config
def getTemp():

    
    owm = pyowm.OWM('0b3f36d3680df22d44911dd9f5268626')
    city_name = entry_1.get()
    reg=owm.city_id_registry()
    exist=reg.ids_for(city_name)
    if(exist):
        observation = owm.weather_at_place(city_name)
        w = observation.get_weather()
        temperature = w.get_temperature('celsius')
        description=w.get_detailed_status()
        tomorrow = pyowm.timeutils.tomorrow()
        wind= w.get_wind()
        we=str(w)
        wf=we.split(",")
        #rain= w.get_rain()
        current_temperature = int(temperature['temp'])
        current_mintemp=int( temperature['temp_min'])
        current_maxtemp= int(temperature['temp_max'])
        current_speed =int(wind['speed'])
        weather_description=description.upper()
        humidity=w.get_humidity()
        pressure=w.get_pressure()

        lable_mintemp.configure(text=str(current_mintemp)+chr(176)+"C")
        lable_maxtemp.configure(text=str(current_maxtemp)+chr(176)+"C")
        lable_speed.configure(text=str(current_speed)+" kmph")
        lable_temp.configure(text=str(current_temperature)+chr(176)+"C")
        lable_desc.configure(text=weather_description)
        lable_humid.configure(text=str(humidity)+"%")
        lable_pressure.configure(text=str(pressure['press'])+"hpa")
       # print(city_name ,rain['3h'])
    else:
        tkinter.messagebox.showinfo("Error","City not found")
        
    


Button(root,text="SUBMIT",width=15,font=("comic sans",13),bg='maroon',fg='white',bd=9,command=getTemp).place(x=590,y=235)

mainloop()
