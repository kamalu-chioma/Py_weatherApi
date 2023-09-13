# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 08:48:30 2023

@author: kamalu-chioma
"""

import tkinter as tk
from tkinter import messagebox
import requests

def get_weather():
    city = city_entry.get()
    if not city:
        messagebox.showerror("Error", "Please enter a city name.")
        return

    try:
        api_key = '5da1ad4dec68a984c595ed9378e42dc5'
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
        response = requests.get(url)
        data = response.json()

        if data['cod'] == 200:
            weather_info = f"Weather in {city}:\n"
            weather_info += f"Temperature: {data['main']['temp']}°C\n"
            weather_info += f"Description: {data['weather'][0]['description']}"
            result_label.config(text=weather_info)
        else:
            messagebox.showerror("Error", "City not found.")
    except Exception:
        messagebox.showerror("Error", "An error occurred while fetching weather data.")

# Create the main window
root = tk.Tk()
root.title("Weather App")

# Create GUI elements
label = tk.Label(root, text="Enter a city:")
city_entry = tk.Entry(root)
get_weather_button = tk.Button(root, text="Get Weather", command=get_weather)
result_label = tk.Label(root, text="", wraplength=300)

# Place GUI elements on the window
label.pack()
city_entry.pack()
get_weather_button.pack()
result_label.pack()

root.mainloop()
