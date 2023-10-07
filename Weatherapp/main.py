from tkinter import *
import tkinter as tk

import pandas.core.computation.ops
from geopy.geocoders import Nominatim
from tkinter import ttk, messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import pytz
import requests

def about():
    messagebox.showinfo("About", "Weather App \nDeveloped using Python and Tkinter By ' SHUBHAM KUMAR '")

root = Tk()
root.title("Weather App")
root.geometry("900x500+300+200")
menu = Menu(root)
root.config(menu=menu)
helpmenu = Menu(menu)
menu.add_cascade(label='Help', menu=helpmenu)
helpmenu.add_command(label='About', command=about)

def getw():
    try:
        city = textfield.get()
        
        geolocator = Nominatim(user_agent = "geoapiExcercises")
        location = geolocator.geocode(city)
        obj = TimezoneFinder()
        result = obj.timezone_at(lng =location.longitude, lat = location.latitude)
        
        home = pytz.timezone(result)
        local_time = datetime.now(home)
        current_time = local_time.strftime("%I:%M:%p")
        clock.config(text = "CURRENT WEATHER")
        
        api_key = "YOUR_API_KEY_HERE"
        api = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
        json_data = requests.get(api).json()
        
        if json_data["cod"] != 200:
            raise Exception("City not found")
        
        condition = json_data['weather'][0]['main']
        description = json_data['weather'][0]['description']
        temp = int(json_data['main']['temp'] - 273.15)
        wind = json_data['wind']['speed']
        humidity = json_data['main']['humidity']
        
        t.config(text = f"{temp}°C")
        c.config(text = f"{condition} | FEELS LIKE {temp}°C")
        w.config(text = wind)
        h.config(text = humidity)
        d.config(text = description.capitalize())
        name.config(text = city.upper())
    except Exception as e:
        messagebox.showerror("Weather APP", str(e))
    
    
    
search_image = PhotoImage(file ="")
myimage =Label(image = search_image)
myimage.place(x=20, y=20)

textfield = tk.Entry(root, justify="center", width=17, font =("poppins",25,"bold"), border=0, bg="#404040", fg="white")
textfield.place(x=290, y=20)
textfield.focus()

search_icon = PhotoImage(file="")
myimage_icon = Button(image = search_icon, borderwidth = 0, cursor = "hand2", bg="#404040", command = getw)
myimage_icon.place(x=400,y=34)

logo_image =PhotoImage(file="pngwing.com.png")
logo = Label(image = logo_image)
logo.place(x=150, y=60)


frame_image = PhotoImage(file="")
frame_myimage = Label(image = frame_image)
frame_myimage.pack(padx=5,pady=5,side=BOTTOM)

name = Label(root, font =("helvetica", 15, 'bold'))
name.place(x=30, y=100)
clock = Label(root,font =("helvetica", 25))
clock.place(x=30, y=130)

label1 = Label(root, text="WIND", font=("helvetica", 15, 'bold'), fg="white", bg="#333333")
label1.place(x=120, y=400)

label2 = Label(root, text="HUMIDITY", font=("helvetica", 15, 'bold'), fg="white", bg="#333333")
label2.place(x=250, y=400)

label3 = Label(root, text="DESCRIPTION", font=("helvetica", 15, 'bold'), fg="white", bg="#333333")
label3.place(x=430, y=400)

label4 = Label(root, text="PRESSURE", font=("helvetica", 15, 'bold'), fg="white", bg="#333333")
label4.place(x=650, y=400)

t = Label(font="aerial")
t.place(x=400,y=150)

c = Label(font="aerial")
c.place(x=400,y=250)

w = Label(text=". . .")
w.place(x=120,y=430)
h = Label(text=". . .")
h.place(x=120,y=430)
d = Label(text=". . .")
d.place(x=120,y=430)

root.mainloop()

