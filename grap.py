# import the library 
import matplotlib.pyplot as plt


# Creation of Data 
x1 = ['06', '07', '08', '09', '10', '11']
y1 = [0, 5, 3, 0, 1]
y2 = [1, 2, 2, 2, 0]

# Plotting the Data 
plt.plot(x1, y1, label='I dag')
plt.plot(x1, y2, label='Trend')

plt.xlabel('subjects')
plt.ylabel('marks')
plt.title("marks obtained in 2010")

plt.plot(y1, 'o:g', linestyle='--', linewidth='8')
plt.plot(y2, 'o:g', linestyle=':', linewidth='8')

plt.legend()
