# -*- coding: utf-8 -*-

#######################
# exercises 4 answers #
#######################
import os 
import pandas as pd 
os.chdir('D:\\Python_learning\\Python_WSB')

#---- load data ----
flights = pd.read_csv("SampleFiles\\Flights\\flights.csv")
weather = pd.read_csv("SampleFiles\\Flights\\weather.csv")

#----- prepare data ------

#---- time series ----

flights['YMD'] = flights['year'].apply(str) + '-' + flights['month'].apply(str) + '-' +  flights['day'].apply(str)
flights['YMD1'] = pd.to_datetime(flights.YMD)
flights['MDY'] = flights['YMD1'].dt.strftime('%m/%d/%Y')

weather.dtypes
weather[['month', 'day']] = weather[['month', 'day']].fillna(0.0).astype(int)
weather = weather.query("month > 0 and day > 0")
weather['YMD'] = weather['year'].apply(str) + '-' + weather['month'].apply(str) + '-' +  weather['day'].apply(str)
weather['YMD1'] = pd.to_datetime(weather.YMD)
weather['MDY'] = weather['YMD1'].dt.strftime('%m/%d/%Y')

weather_summary1 = (weather
 .filter(['YMD', 'temp'])
 .groupby(['YMD'])
 .agg(['mean', 'median', 'size']))

weather_summary1 = weather_summary1.reset_index()
weather_summary1.columns = ['YMD', 'mean', 'median', 'size']



#---- ex 1 -------
# check if there is a linear realtion between temperature and humidity at NY airports.
# sprawdz czy jest relacja liniowa miedzy danymi pogodowymi na lotniskach w NY miedzy temperatura a wilgotnoscia. 

import matplotlib.pyplot as plt

x = weather['temp']
y = weather['humid']

plt.scatter(x, y)
plt.show()


#---- ex 2 -------
# add 3rd line to the below plot with Int_rate
# dodaj 3 linie z Int_rate


eco1 = pd.DataFrame({'HPI':[80,85,88,85],
                    'Int_rate':[2, 3, 2, 2],
                    'US_GDP_Thousands':[50, 55, 65, 55],
                   'Year' : [2001, 2002, 2003, 2004]})

eco1['Year'] = eco1['Year'].astype(str) 


plt.plot( 'Year', 'US_GDP_Thousands', data=eco1, marker='o', markerfacecolor='blue', markersize=12, color='skyblue', linewidth=4)
plt.plot( 'Year', 'HPI', data=eco1, marker='', color='olive', linewidth=2)
plt.plot( 'Year', 'Int_rate', data=eco1, marker='x', color='black', linewidth=2)

plt.legend()


#----- ex 3 ------
# show legend from ex2 on the top left side
# pokaz legende dla powyzszego wykresu u gory wykresu po lewej stronie

plt.plot( 'Year', 'US_GDP_Thousands', data=eco1, marker='o', markerfacecolor='blue', markersize=12, color='skyblue', linewidth=4)
plt.plot( 'Year', 'HPI', data=eco1, marker='', color='olive', linewidth=2)
plt.plot( 'Year', 'Int_rate', data=eco1, marker='x', color='black', linewidth=2)

plt.legend(loc = 'upper left')


#---- ex 4 --------------------------
# change below plot to have two lines (HPI, Int_rate)
# zmien wykres ponizej aby wyswietlic 2 linie HPI, Int_rate

from bokeh.plotting import figure, output_file, show

output_file("line4.html")

eco1 = pd.DataFrame({'HPI':[80,85,88,85],
                    'Int_rate':[2, 3, 2, 2],
                    'US_GDP_Thousands':[50, 55, 65, 55],
                   'Year' : [2001, 2002, 2003, 2004]})

eco1['Year'] = eco1['Year'].astype(str)

p = figure(plot_width=400, plot_height=400)

# add a line renderer

p.line(eco1['Year'].astype(str), eco1['Int_rate'], line_width=2)

show(p)


###
output_file("line4.html")
p4 = figure(plot_width=400, plot_height=400)
p4.line(eco1['Year'].astype(str), eco1['Int_rate'], line_width=2)
p4.line(eco1['Year'].astype(str), eco1['HPI'], line_width=2)

show(p4)


#----- ex 5 ------
# Add legend to plot from ex 4. Change position to bottom right
# Dodaj legende do wykresow z zadania 4. Pokaz legende po prawej stronie w dolny rogu wykresu.

output_file("line5.html")
p5 = figure(plot_width=400, plot_height=400)
p5.line(eco1['Year'].astype(str), eco1['Int_rate'], line_width=2, legend = 'Int_rate')
p5.line(eco1['Year'].astype(str), eco1['HPI'], line_width=2, legend = 'HPI')
p5.legend.location = 'bottom_right'

show(p5)


