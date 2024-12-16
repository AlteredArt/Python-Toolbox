import tkinter as tk
import requests

from tkinter import messagebox
from PIL import Image, ImageTk

import ttkbootstrap

# GET WEATHER FROM WEATHER API
def get_weather(city):
    API_Key = 'b6a61e5b7a18005040feaa658d3a6eed'
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_Key}&units=imperial'
    res = requests.get(url)

    if res.status_code == 404:
        messagebox.showerror("Error", "City not found")
        return None

    weather = res.json()
    icon_id = weather['weather'][0]['icon']
    # temperature = weather['main']['temp'] - 273.15
    temperature = weather['main']['temp']

    description = weather['weather'][0]['description']
    city = weather['name']
    country = weather['sys']['country']

    icon_url = f"http://openweathermap.org/img/wn/{icon_id}@2x.png"
    return (icon_url, temperature, description, city, country)

# SEARCH METHOD
def search():
    city = city_entry.get()
    result = get_weather(city)
    if result is None:
        return 
    # IF THE CITY IS FOUND UNPACK THE WEATHER INFORMATION
    icon_url, temperature, description, city, country = result
    location_label.configure(text=f"{city}, {country}")

    image = Image.open(requests.get(icon_url, stream=True).raw)
    icon = ImageTk.PhotoImage(image)
    icon_label.configure(image=icon)
    icon_label.image = icon

    temperature_label.configure(text=f"Temperature: {temperature:.1f}\u00B0F")
    description_label.configure(text=f"Description: {description}")




# SET THE ROOT TITLE AND SIZE OF THE PROJECT
root = ttkbootstrap.Window(themename="darkly")
root.title("Weather Application")
root.geometry("600x600")

# HEADER / TITLE
header_label = tk.Label(root, text="Weather", font="Helvetica, 20")
header_label.pack(fill="x", pady=10)

# INTRO DESCRIPTION
info_label = tk.Label(root, text="Enter a city name to see the current weather status", font="Helvetica, 14")
info_label.pack(fill="x", pady=10)

# SELECT A CITY
city_entry = ttkbootstrap.Entry(root, font="Helvetica, 18")
city_entry.pack(pady=30)

# SEARCH BUTTON
search_button = ttkbootstrap.Button(root, text="Search", command=search, bootstyle="info")   
search_button.pack(pady=20)

# LOCATION DISPLAYED
location_label= tk.Label(root, font="Helvetica, 28")
location_label.pack(pady=20)

# WEATHER ICON
icon_label = tk.Label(root)
icon_label.pack()

# TEMPERATURE DISPLAYED
temperature_label = tk.Label(root, font="Helvetica, 20")
temperature_label.pack()


# WEATHER DESCRIPTION
description_label = tk.Label(root, font="Helvetica, 20")
description_label.pack()

# RUN MAIN APP LOOP
root.mainloop()

