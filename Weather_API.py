import tkinter as tk
import requests

api_key = '30d4741c779ba94c470ca1f63045390a'

window= tk.Tk()
window.title('Weather')

window.columnconfigure(0, weight=1, minsize = 75)
window.columnconfigure(1, weight=5, minsize = 300)
window.rowconfigure([0,1,2,3,4], weight=1, minsize = 20)


label_city = tk.Label(window, text='Enter City: ')
label_city.grid(row=0, column=0)
entry_city = tk.Entry(window)
entry_city.grid(row=0, column=1, sticky='we')



label_weather = tk.Label(window, text='Weather: ')
label_weather.grid(row=2, column=0)
weather_output = tk.Label(window, text='')
weather_output.grid(row=2, column=1, sticky='w')

label_temp = tk.Label(window, text='Temperature: ')
label_temp.grid(row=3, column=0)
temp_output = tk.Label(window, text='')
temp_output.grid(row=3, column=1, sticky='w')

label_humid = tk.Label(window, text='Humidity: ')
label_humid.grid(row=4, column=0)
humid_output = tk.Label(window, text='')
humid_output.grid(row=4, column=1, sticky='w')


def handler_clear():
    entry_city.delete(0, tk.END)
    weather_output['text'] = ''
    temp_output['text'] = ''
    humid_output['text'] = ''
    

def handler_submit():
    str_city = entry_city.get()
    weather_data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={str_city}&units=imperial&APPID={api_key}")
    print(weather_data.json())
    if str_city == '':
        weather_output['text'] = "No City Found"
    elif weather_data.json()['cod'] == '404':
        weather_output['text'] = "No City Found"
    else:
        city = weather_data.json()['name']
        entry_city.delete(0, tk.END)
        entry_city.insert(0,city)
        weather = weather_data.json()['weather'][0]['description']
        temp = round(weather_data.json()['main']['temp'])
        humid = weather_data.json()['main']['humidity']
        weather_output['text'] = weather
        temp_output['text'] = f'{temp} ºF'
        humid_output['text'] = f'{humid}%'
    
    

frame= tk.Frame(window)

button_submit = tk.Button(frame, text='Submit', command=handler_submit)
button_submit.pack(side=tk.LEFT)

button_clear = tk.Button(frame, text='Clear', command=handler_clear)
button_clear.pack(side=tk.LEFT)



frame.grid(row=1, column=1, sticky='enws')




window.mainloop()