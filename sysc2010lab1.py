import matplotlib.pyplot as plt 
import numpy
import random
import pandas as pd
#Task 5.1
A = 5
f=10
fs= 500 #sampling frequency
t= numpy.arange (0,1,1/fs) #where the format for numpy.arange is (start,stop,step)
x = A*numpy.sin(2*numpy.pi*f*t) 
plt.xlabel("Time(s)")
plt.ylabel("Amplitude") 
plt.title("Task 5.1 Synthetic sinusoid")
plt.plot(t,x)
plt.show()

#Task 5.2
numpy.random.randn(500)
mu = 5
sigma = 2
magnitude = mu + sigma*numpy.random.randn(500)
y = 0.25*magnitude
A = 5
f=10
fs= 500 #sampling frequency
t= numpy.arange (0,1,1/fs) #where the format for numpy.arange is (start,stop,step)
x = A*numpy.sin(2*numpy.pi*f*t) 
z=y+x
plt.xlabel("Time(s)")
plt.ylabel("Amplitude") 
plt.title("Task 5.2 Synthetic sinusoid with noise")
plt.plot(t,z)
plt.show()

#Task 5.3
time = [i * 60 for i in range(120)]               
temperature = [36 + random.uniform(-0.5, 0.5) for i in range(120)]  

data = {
    "Time (s)": time,
    "Temperature (°C)": temperature
}

df = pd.DataFrame(data)
df.to_csv("sensor_readings.csv", index=False)

print("CSV file 'sensor_readings.csv' has been created!")

df = pd.read_csv("sensor_readings.csv")
subset = df.iloc[41:81]

a = subset["Time (s)"]
b = subset["Temperature (°C)"]

plt.plot(a, b)
plt.xlabel("Time (s)")
plt.ylabel("Temperature (°C)")
plt.title("Sensor Readings from Sample 41 to 80")
plt.show()
