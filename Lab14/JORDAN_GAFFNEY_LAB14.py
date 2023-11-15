import matplotlib.pyplot as plt
from numpy import size
import pandas as pd
WeatherData = pd.read_csv(r"C:\Users\Jordan\OneDrive\Documents\Python\CS1302\Lab14\atlanta_weather.csv")

# Print the DataFrame
print(WeatherData)

# Assuming you want to plot the second column for the first two rows
High = WeatherData.High
Low = WeatherData.Low
HighGraph = plt.plot(WeatherData.Month, High,'b--o')
LowGraph = plt.plot(WeatherData.Month, Low,'g:^')
Title = plt.title('Atlanta – Monthly Temperature', fontsize=20)
Xlabel = plt.xlabel('Temperature (Fahrenheit)',fontsize=16)
Ylabel = plt.ylabel('Month',fontsize=16)
PlotLegend = plt.legend(fontsize=20)
plt.annotate('Highest Temperature of the Year', arrowprops=dict(facecolor='black'), xy=('Jul',89), xytext=('Apr',75))

plt.show()
plt.savefig('atlanta_weather_plot.jpg')