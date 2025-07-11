from sense_hat import SenseHat
import time
import matplotlib.pyplot as plt

sense = SenseHat()

temperature_readings = []
humidity_readings = []
pressure_readings = []
time_reading = []

actual_temp = 13.1
actual_humidity = 65
actual_pressure = 1016

for i in range(1, 	11):
	print(f"iteration {i}")
	temp = sense.get_temperature()
	humidity = sense.get_humidity()
	pressure = sense.get_pressure()
	
	sense.show_message(f"Temp : {temp: .1f}C",scroll_speed = 0.08, text_colour=(255,160,122))
	print(f"Temp : {temp: .1f}C")
	temperature_readings.append(temp)
	
	sense.show_message(f"Hum. : {humidity: .1f}%",scroll_speed = 0.08, text_colour=(64,224,208))
	print(f"Hum. : {humidity: .1f}%")
	humidity_readings.append(humidity)
	
	sense.show_message(f"Press. : {pressure: .1f}HPa",scroll_speed = 0.08, text_colour=(182,12,47))
	print(f"Press. : {pressure: .1f}HPa")
	pressure_readings.append(pressure)
	
	time_reading.append(i)
	time.sleep(1)	

avg_temp = sum(temperature_readings) / len(temperature_readings)
avg_humidity = sum(humidity_readings) / len(humidity_readings)
avg_pressure = sum(pressure_readings) / len(pressure_readings)

print(f"\nCalculated Temp: {avg_temp: .1f}C \t Actual Temp: {actual_temp: .1f}C")
print(f"Calculated Humidity: {avg_humidity: .1f}% \t Actual Humidity: {actual_humidity: .1f}%")
print(f"Calculated Pressure: {avg_pressure: .1f}hPa \t Actual Pressure {actual_pressure: .1f}hPa")

print("\nAccuracy Comparison")
print(f"Temp Sensor: {actual_temp - avg_temp:+.1f}C")
print(f"Pressure Sensor: {actual_pressure - avg_pressure:+.1f}hPa")
print(f"Humidity Sensor: {actual_humidity - avg_humidity:+.1f}%")

plt.figure(figsize=(15,10))

plt.subplot(3,1,1)
plt.plot(time_reading, temperature_readings, marker='o', label="Measured Temperature",color="blue")
plt.axhline(y=actual_temp, color = "red", linestyle = '--', label="Actual Temperature")
plt.title("Temperature Readings over Time")
plt.xlabel("Time (sec)")
plt.ylabel("Temperature (C Degree)")
plt.xticks(time_reading)
plt.legend()
plt.grid()

plt.subplot(3,1,2)
plt.plot(time_reading, humidity_readings, marker='o', label="Measured Humidity",color="blue")
plt.axhline(y=actual_humidity, color = "red", linestyle = '--', label="Actual Humidity")
plt.title("Humidity Readings over Time")
plt.xlabel("Time (sec)")
plt.ylabel("Humiduty (%)")
plt.xticks(time_reading)
plt.legend()
plt.grid()

plt.subplot(3,1,3)
plt.plot(time_reading, pressure_readings, marker='o', label="Measured Pressure",color="blue")
plt.axhline(y=actual_pressure, color = "red", linestyle = '--', label="Actual Pressure")
plt.title("Pressure Readings over Time")
plt.xlabel("Time (sec)")
plt.ylabel("Pressure (hPa)")
plt.xticks(time_reading)
plt.legend()
plt.grid()

plt.tight_layout()
plt.show()

