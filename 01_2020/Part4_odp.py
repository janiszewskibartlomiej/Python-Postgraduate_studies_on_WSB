# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import os 

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


###### PLOTS ######## 

#---- MATPLOTLIB -----#

## scatter plot

import matplotlib.pyplot as plt


x = flights['dep_delay']
y = flights['arr_delay']

plt.scatter(x, y)
plt.show()



## line plot
# line 1

eco1 = pd.DataFrame({'HPI':[80,85,88,85],
                    'Int_rate':[2, 3, 2, 2],
                    'US_GDP_Thousands':[50, 55, 65, 55],
                   'Year' : [2001, 2002, 2003, 2004]})

eco1['Year'] = eco1['Year'].astype(str) 

plt.plot(eco1['Year'], eco1['US_GDP_Thousands'])


# line 2
plt.plot(eco1['Year'], eco1['US_GDP_Thousands'])

plt.plot( 'Year', 'US_GDP_Thousands', data=eco1, marker='o', markerfacecolor='blue', markersize=12, color='skyblue', linewidth=4)
plt.plot( 'Year', 'HPI', data=eco1, marker='', color='olive', linewidth=2)
plt.legend()



## bar blot 
# histogram
import numpy as np
import matplotlib.pyplot as plt


# the histogram of the data
#n, bins, patches = plt.hist(flights['arr_delay'], 50, normed=1, facecolor='g', alpha=0.75)
plt.hist(flights['arr_delay'], 50, facecolor='g')

plt.xlabel('arr_delay')
plt.ylabel('Frequency')
plt.title('Histogram of Arrival Delays')
plt.grid(True)
plt.show()


# frequency plot (regular bar plot)
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

summary_origin = (flights
 .filter(['origin', 'dep_delay'])
 .groupby(['origin'])
 .agg(['mean']))

summary_origin = summary_origin.reset_index()
summary_origin.columns = ['origin', 'mean']

bar_plot = summary_origin.plot.bar(x='origin', y='mean')


## box plot

import matplotlib.pyplot as plt
 
flights.boxplot(by='origin', 
                       column=['dep_delay'], 
                       grid=False,
                       showfliers=False)


## maps

import pandas as pd
import matplotlib
import geopandas


# plot map shape
world = geopandas.read_file(geopandas.datasets.get_path('naturalearth_lowres'))
world.plot()

# fill countries with colors
world = world[(world.pop_est>0) & (world.name!="Antarctica")]
world['gdp_per_cap'] = world.gdp_md_est / world.pop_est
world.plot(column='gdp_per_cap');

# add legend
import matplotlib.pyplot as plt

fig, ax = plt.subplots(1, 1)
world.plot(column='pop_est', ax=ax, legend=True)


# choose colors 
# https://matplotlib.org/users/colormaps.html
world.plot(column='gdp_per_cap', cmap='BuGn');



#----- BOKEH ------#

## scatter plot

from bokeh.plotting import figure, output_file, show

# output to static HTML file
output_file("scatter.html")

# define plot
p = figure(plot_width=400, plot_height=400)

# add a circle renderer with a size, color, and alpha
x = flights['dep_delay']
y = flights['arr_delay']


p.scatter(x, y, color="navy")

# show the results
show(p)



## line plot

from bokeh.plotting import figure, output_file, show

output_file("line1.html")

eco1 = pd.DataFrame({'HPI':[80,85,88,85],
                    'Int_rate':[2, 3, 2, 2],
                    'US_GDP_Thousands':[50, 55, 65, 55],
                   'Year' : [2001, 2002, 2003, 2004]})

eco1['Year'] = eco1['Year'].astype(str)

p2 = figure(plot_width=400, plot_height=400)

# add a line renderer
p2.line(eco1['Year'].astype(str), eco1['Int_rate'], line_width=2)

show(p2)


## bar blot 

# frequency plot (regular bar plot)

from bokeh.plotting import figure, show, output_file

output_file('bar_chart.html')


summary_origin = (flights
 .filter(['origin', 'dep_delay'])
 .groupby(['origin'])
 .agg(['mean']))

summary_origin = summary_origin.reset_index()
summary_origin.columns = ['origin', 'mean']


bar_p = figure(x_range= summary_origin['origin'],
               title="Average Delay",
               toolbar_location=None, 
               tools="", 
               plot_width=400, 
               plot_height=400)

bar_p.vbar(x = summary_origin['origin'], width=0.5, bottom=0,
       top = summary_origin['mean'], color="firebrick")

show(bar_p)



## maps

from bokeh.plotting import figure, show, output_file
from bokeh.tile_providers import get_provider, Vendors

output_file("tile.html")

tile_provider = get_provider(Vendors.CARTODBPOSITRON)

# range bounds supplied in web mercator coordinates
p = figure(x_range=(-18000000, 18000000), 
           y_range=(-800000, 8000000),
           x_axis_type="mercator", y_axis_type="mercator")
p.add_tile(tile_provider)
    
show(p)


#----- PLOTLY ------#
import plotly.express as px

## scatter plot


#iris = px.data.iris()
fig = px.scatter(flights, x="dep_delay", y="arr_delay")
#fig.show()
fig.write_html(file = "scatter_px.html")

## line plot

# one line
gapminder = px.data.gapminder().query("country=='Canada'")

line_fig = px.line(gapminder, 
                   x="year", 
                   y="lifeExp",
                   title='Life expectancy in Canada')
#fig.show()
line_fig.write_html(file = "line_px.html")


# two lines 

gapminder1 = px.data.gapminder().query("continent=='Oceania'")

line1_fig = px.line(gapminder1, x="year", y="lifeExp", color='country')
#line_fig.show()

line1_fig.write_html(file = "line_px1.html")


## bar blot 
# histogram

tips = px.data.tips()
hist_fig = px.histogram(tips, x="total_bill")
#fig.show()

hist_fig.write_html(file = "hist_px.html")

# frequency plot (regular bar plot)

data_canada = px.data.gapminder().query("country == 'Canada'")
freq_fig = px.bar(data_canada, x='year', y='pop')
freq_fig.show()

freq_fig.write_html(file = "freq_fig.html")

## box plot

tips = px.data.tips()
box_fig = px.box(tips, x="time", y="total_bill")
#box_fig.show()
box_fig.write_html(file = "box_fig.html")

## maps

# bubble map
gapminder = px.data.gapminder().query("year==2007")
fig = px.scatter_geo(gapminder, locations="iso_alpha", color="continent",
                     hover_name="country", size="pop",
                     projection="natural earth")
#fig.show()
fig.write_html(file = "map1.html")

# map with lines
import plotly.graph_objects as go

fig = go.Figure(data=go.Scattergeo(
    lat = [40.7127, 51.5072],
    lon = [-74.0059, 0.1275],
    mode = 'lines',
    line = dict(width = 2, color = 'blue'),
))

fig.update_layout(
    title_text = 'London to NYC Great Circle',
    showlegend = False,
    geo = dict(
        resolution = 50,
        showland = True,
        showlakes = True,
        landcolor = 'rgb(204, 204, 204)',
        countrycolor = 'rgb(204, 204, 204)',
        lakecolor = 'rgb(255, 255, 255)',
        projection_type = "equirectangular",
        coastlinewidth = 2,
        lataxis = dict(
            range = [20, 60],
            showgrid = True,
            dtick = 10
        ),
        lonaxis = dict(
            range = [-100, 20],
            showgrid = True,
            dtick = 20
        ),
    )
)

#fig.show()

fig.write_html(file = "map2.html")