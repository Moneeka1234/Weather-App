from tkinter import *
from tkinter import ttk
import requests
import time
from configparser import ConfigParser

#extract api key from another file
api_file="weather.key"
file_a=ConfigParser()
file_a.read(api_file)
api_key=file_a['api_key']['key']

#function return weather details
def getweather():

    city=city_name.get()
    data=requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}").json()
    print(data)
    condition=data["weather"][0]["description"]
    temp=int(data['main']['temp']-273.15)
    pressure=data['main']['pressure']
    humidity=data['main']['humidity']
    wind=data['wind']['speed']
    latitude=data["coord"]['lon']
    longitude=data["coord"]['lat']
    sunrise=time.strftime("%I:%M:%S", time.gmtime(data['sys']['sunrise']+19800))
    sunset=time.strftime("%I:%M:%S", time.gmtime(data['sys']['sunset']+19800))

    final_info = "Condition : " + str(condition) + "\n" + " Temperature : " + str(temp) + " °C" + "\n" + " Longitude : " + str(longitude) + "\n" + " Latitude : " +  str(latitude) + "\n" + "Sunrise : " + str(sunrise) + "\n" + "Sunset : " + str(sunset) + "\n" + "Pressure : " + str(pressure) + "\n" + "Humidity : " +  str(humidity) + "\n" + "Wind : " +  str(wind) 
    label1.config(text = final_info)

#define window
win=Tk()
win.title("App")
win.config(bg="sky blue")
win.geometry("500x450")

#define title
title=Label(win,text="Weather App",font=("Helvetica",30,"italic"),bg="white")
title.place(x=25,y=30,height=50,width=450)

#define drop down imput
city_name=StringVar()
city_list=["Andhra Pradesh","Arunachal Pradesh ","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal","Andaman and Nicobar Islands","Chandigarh","Dadra and Nagar Haveli","Daman and Diu","Lakshadweep","National Capital Territory of Delhi","Puducherry"]
com=ttk.Combobox(win,font=("Georgia",15,),values=city_list,textvariable=city_name,justify="center")
com.place(x=50,y=100,height=35,width=400)

#define button
done_btn=Button(win,font=("Georgia",12),text="Check Weather",bg="#008080",fg="#FFFFF0",borderwidth="0",command=getweather)
done_btn.place(x=180,y=150,height=30,width=150)

#display weather info
label1=Label(win,font=("Georgia",14),bg="sky blue")
label1.place(x=50,y=200,height=220,width=400)

win.mainloop()
