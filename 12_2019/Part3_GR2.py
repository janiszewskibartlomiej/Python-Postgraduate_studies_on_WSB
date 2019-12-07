# -*- coding: utf-8 -*-

##########
# PART 3 #
##########
import pandas as pd
import os 

os.chdir('D:\\GITHUB\Python-Postgraduate_studies_on_WSB\\12_2019')

#---- load data ----
flights = pd.read_csv("SampleFiles\\flights.csv")
weather = pd.read_csv("SampleFiles\\weather.csv")

#----- prepare data ------


#---- time series ----


flights['DMY'] = flights['day'].apply(str) + "-" + flights['month'].apply(str) + "-" + flights['year'].apply(str)

flights['day']

flights.dtypes


# string / dates formating:
# https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior

flights['DMY1'] = pd.to_datetime(flights['DMY'])

flights['DMY2'] = flights['DMY1'].dt.strftime('%d-%m-%Y')

#---- column \ row selection ----

df1 = flights.loc[flights['month'] == 1,]    # loc po nazwach kolumn  a iloc po indexach

df2 = flights.query("month == 1")

# row selection

df1 = flights.loc[(flights['month'] == 1) | (flights['month'] == 2,)]    # loc po nazwach kolumn  a iloc po indexach

df2 = flights.query("(month == 1) OR (month == 2)")

df1 = flights.loc[(flights['month'].isin([1,2,3])) ,]
df2 = flights.query("month in [1,2,3]")

# column selection 

df3 = flights[['month', 'day', 'dep_time']]

df4 = flights.drop(['arr_time', 'carrier'], axis = 1)  # axis 1 po kolumnach  axis 0 po wierszach

#---- introduction to dfply / pandas -----
# https://github.com/kieferk/dfply
# https://towardsdatascience.com/dplyr-style-data-manipulation-with-pipes-in-python-380dcb137000

# data transform / column operations  

weather['tst1'] = weather['wind_speed'].apply(lambda x: x * 10)   # x w lamda to co jest rezulatatem z x * 10 zz kolumny wind_speed

## data aggregation

# count mean

weather_summary = weather.groupby(['month']).mean().temp
weather_summary = weather.groupby(['month']).temp.mean()

# complex data wrangling

weather_summary2 = (weather
                    .filter(['month', 'temp'])
                    .groupby(['month'])
                    .agg(['mean', 'size'])
                    .sort_values(by=('temp', 'mean'), ascending=True)
                    )

## gather / melt
df1 = pd.DataFrame({'first' : ['Adam', 'John'],
'last' : ['Kowalski', 'Doe'],
'height' : [5.5, 6.0],
'weight' : [130, 150]})

df11 = df1.melt(id_vars=['first', 'last'])  # pakujemy w kolumny klucz:wartosc wzgledem first and last

## spread / pivot  to jest odwrotnosc df11

df22 = df11.pivot_table(index = ['first','last'], 
                        values = 'value', 
                        columns = 'variable')

df22 = df22.reset_index()

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

t.timestamp()   # zapis cyfrowy daty
t.weekday()


# diffs


import numpy as np

Date1 = pd.Series(pd.date_range('2018-12-12',
          periods = 7,
          freq = 'M'))

Date2 = pd.Series(pd.date_range('2018-12-12',
          periods = 7,
          freq = 'W'))

MyDates = pd.DataFrame(dict(StartDate = Date1,
                  EndDate = Date2))

# https://pandas.pydata.org/pandas-docs/stable/user_guide/timedeltas.html

MyDates['diff_weeks1'] = MyDates['StartDate'] - MyDates['EndDate'] 


MyDates['diff_weeks2'] = MyDates['diff_weeks1'] / np.timedelta64(1,'D') 

#---- regular expressions (regex) ----
#https://www.geeksforgeeks.org/split-a-string-into-columns-using-regex-in-pandas-dataframe/


flights['test'] = flights['carrier'].apply(str) + flights['tailnum'].apply(str) 

flights['test_extract'] = flights['test'].str.extract('(^[0-9A-Z]{2})', expand = False)  #  expand rozbija kolumny na czesci


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

df5 = eco1.merge(eco3, how='inner', on = 'Year')


df6 = eco1.merge(eco3, how='left', on = 'Year')


df7 = eco1.merge(eco3, how='right', on = 'Year')


df8 = eco1.merge(eco3, how='outer', on = 'Year')


#----- working with NA / None values -----
# fill up with 0 or missing

df9 = df8.fillna('')

# calculate average

df10 = df8.fillna(df8.mean())  #domyslnie indexowanie po kolumnach


# delete not needed row / column

df11 = df8.dropna(axis = 0)  # dla 0 pozbylismy sie wiersza

df12 = df8.dropna(axis = 1)   # dla 1  kolumn

