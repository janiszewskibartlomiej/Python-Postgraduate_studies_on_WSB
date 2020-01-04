# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import os 

os.chdir('D:\\GITHUB\\Python-Postgraduate_studies_on_WSB')


#---- load data ----
flights = pd.read_csv("01_2020\\flights.csv")
weather = pd.read_csv("01_2020\\weather.csv")

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

plt.scatter(x,y)  # łaczy dane
plt.show()  #pokazuje 

## line plot
# line 1

eco1 = pd.DataFrame({'HPI':[80,85,88,85],
                    'Int_rate':[2, 3, 2, 2],
                    'US_GDP_Thousands':[50, 55, 65, 55],
                   'Year' : [2001, 2002, 2003, 2004]})

eco1['Year'] = eco1['Year'].astype(str) 

plt.plot(eco1['Year'], eco1['US_GDP_Thousands'])    # wykres liniowy - plot
plt.show()

# line 2

plt.plot('Year', 'US_GDP_Thousands',
         data= eco1,
         marker = 'o',
         markerfacecolor = 'blue') 
plt.plot('Year', 'HPI',
         data = eco1,
         markerfacecolor = 'red',
         marker = 'x')
plt.legend()
plt.show()




## bar blot 
# histogram
import numpy as np
import matplotlib.pyplot as plt


# the histogram of the data

plt.hist(flights['arr_delay'], bins = 50)
plt.xlabel('min')
plt.ylabel('freq')
plt.title('Histogram of arrival delays')
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

summary_origin.plot.bar(x = 'origin',
                        y = 'mean')


## box plot

import matplotlib.pyplot as plt
 
flights.boxplot(by = 'origin',
                column = 'dep_delay',
                grid = False,
                showfliers = False)

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

p = figure(plot_width = 400,
           plot_height = 400)

# add a circle renderer with a size, color, and alpha
x = flights['dep_delay']
y = flights['arr_delay']

p.scatter(x,y)


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


p2 = figure(plot_width = 400,
           plot_height = 400)

# add a line renderer

p2.line(eco1['Year'],
        eco1['Int_rate'],
        line_width = 2)

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


bar_p = figure(plot_width = 400,
           plot_height = 400,
           x_range = summary_origin['origin'],
           title = 'Bar plot of mean departure delays',
           toolbar_location = None)

bar_p.vbar(x = summary_origin['origin'],
           top = summary_origin['mean'],
           width = 0.5
           )

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


## line plot

# one line

#fig.show()


# two lines 


#line_fig.show()



## bar blot 
# histogram

#fig.show()


# frequency plot (regular bar plot)


## box plot

#box_fig.show()

## maps

# bubble map
#fig.show()

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