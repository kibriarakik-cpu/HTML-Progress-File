city=str(input("Enter your city name: "))
temperature=float(input("Enter the temperature in Celsius: "))
print("The temperature in", city, "is", temperature, "°C.")
wind_speed=int(input("Enter the wind speed in km/h: "))
print("The wind speed in", city, "is", wind_speed, "km/h.")
print("City:", city)
print("Temperature:", temperature, "°C")
print("Wind Speed:", wind_speed, "km/h")
if temperature > 30:
    print("Warning: It's a hot day in", city, "!")
if temperature > 35:
    print("Warning: It's a very hot day in", city, "!")
else:
    print("The weather in", city, "is cold.")
if temperature > 40:
    print("Warning: It's an extremely hot day in", city, "!")
elif temperature < 10:
    print("Warning: It's a cold day in", city, "!")
elif temperature >= 10 and temperature <= 30:
    print("The weather in", city, "is tolerable.")
else:
    print("The weather in", city, "is cold.")
import datetime
import calendar
now = datetime.datetime.now()
print("city:", city )
print("Time:", now.strftime("%H:%M:%S"))
print("Current date and time:", now)
print(calendar.calendar(now.year))