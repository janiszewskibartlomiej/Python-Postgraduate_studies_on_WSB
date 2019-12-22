# -*- coding: utf-8 -*-

##########
# PART 3 #
##########
import pandas as pd
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

# string / dates formating:
# https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior


#---- column \ row selection ----

# row selection
flightsJan = flights[(flights.month == 1)]

flightsJan = flights.query("month == 1")


flightsJan1 = flights[(flights.year == 2013) 
	& (flights.month == 1 )  
    & (flights.day== 1 )]

flightsJan1 = flights.query(" year == 2013 and month == 1 and day == 1 ")


flights_c = flights[flights.carrier.isin(["UA", "AA"])]
flights_c = flights.query("carrier in ['UA', 'AA']")

# column selection 

flights_s = flights[['year', 'month', 'carrier']]
flights_s1 = flights.drop(['year', 'month', 'carrier'], axis = 1)



#---- introduction to dfply / pandas -----
# https://github.com/kieferk/dfply
# https://towardsdatascience.com/dplyr-style-data-manipulation-with-pipes-in-python-380dcb137000

# data transform / column operations  
weather['wind_speed_10times'] = weather['wind_speed'].apply(lambda x: x*10)
weather['wind_speed_10times'] = weather['wind_speed_10times'].apply(lambda x: x/10)

## data aggregation

# count mean
weather_summary = weather.groupby('month').mean()
weather_summary_wind = weather.groupby('month').wind_speed.mean()

weather_summary_wind = weather_summary_wind.rename("mean_wind_speed")

# complex data wrangling

weather_summary1 = (weather
 .filter(['month', 'wind_speed'])
 .query('month in [1, 2, 3, 4, 5, 6]')
 .groupby(['month'])
 .agg(['mean', 'size']))
# .sort_values(by=('month'), ascending=True,)
# .head())


## gather / melt
df1 = pd.DataFrame({'first' : ['Adam', 'John'],
'last' : ['Kowalski', 'Doe'],
'height' : [5.5, 6.0],
'weight' : [130, 150]})

df2 = df1.melt(id_vars = ['first', 'last'])


## spread / pivot
#df2.pivot(index = ['first','last'], values = 'value', columns = 'variable')
df3 = df2.pivot_table(index = ['first','last'], values = 'value', columns = 'variable')

#---- working with dates -----
flights.dtypes

t = pd.datetime.now()
t

t.day
t.month
t.year
t.hour
t.minute
t.second

t.timestamp()
t.weekday()


# diffs

date1 = pd.Series(pd.date_range('2012-1-1 12:00:00', periods=7, freq='M'))
date2 = pd.Series(pd.date_range('2013-3-11 21:45:00', periods=7, freq='W'))
 
dates_df = pd.DataFrame(dict(Start_date = date1, End_date = date2))
dates_df

import numpy as np

dates_df['diff_days'] = dates_df['End_date'] - dates_df['Start_date']
dates_df['diff_days1'] = dates_df['diff_days'] / np.timedelta64(1,'D')

dates_df.iloc[0, 2].total_seconds()

dates_df['diff_weeks'] = dates_df['diff_days'] / np.timedelta64(1,'W')


# https://pandas.pydata.org/pandas-docs/stable/user_guide/timedeltas.html


#---- regular expressions (regex) ----
#https://www.geeksforgeeks.org/split-a-string-into-columns-using-regex-in-pandas-dataframe/


flights['test'] = flights['carrier'].apply(str) + flights['tailnum'].apply(str) 


flights['extract_carrier'] = flights['test'].str.extract('^([A-Z0-9]{2})', expand = False)

flights.filter(regex='carrier$', axis=1)
flights.filter(regex='^[0-9]$', axis=0)


#----- join tables -----
eco1 = pd.DataFrame({'HPI':[80,85,88,85],
                    'Int_rate':[2, 3, 2, 2],
                    'US_GDP_Thousands':[50, 55, 65, 55],
                   'Year' : [2001, 2002, 2003, 2004]})

eco2 = pd.DataFrame({'HPI':[80,85,88,85],
                    'Int_rate':[2, 3, 2, 2],
                    'US_GDP_Thousands':[50, 55, 65, 55],
                   'Year' : [2005, 2006, 2007, 2008]})

eco3 = pd.DataFrame({'HPI':[80,85,88,85],
                    'Unemployment':[7, 8, 9, 6],
                    'Low_tier_HPI':[50, 52, 50, 53],
                   'Year': [2002, 2003, 2004, 2005]})


merged = pd.merge(eco1, eco3, how= 'inner', on='Year')
merged1 = pd.merge(eco1, eco3, how= 'left', on='Year')
merged2 = pd.merge(eco1, eco3, how= 'outer', on='Year')
merged3 = pd.merge(eco1, eco3, how= 'right', on='Year')



#----- working with NA / None values -----
# fill up with 0 or missing
sample1 = merged2.fillna(0)
sample2 = merged2.fillna('missing')

# calculate average
sample3 = merged2.fillna(merged2.mean())

# delete not needed row / column
merged2.dropna(axis=0)
merged2.dropna(axis=1)
