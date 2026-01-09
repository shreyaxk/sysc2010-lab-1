#Task 5.1
import matplotlib.pyplot as plt 
import numpy
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
