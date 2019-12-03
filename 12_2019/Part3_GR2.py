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




# string / dates formating:
# https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior


#---- column \ row selection ----

# row selection

# column selection 



#---- introduction to dfply / pandas -----
# https://github.com/kieferk/dfply
# https://towardsdatascience.com/dplyr-style-data-manipulation-with-pipes-in-python-380dcb137000

# data transform / column operations  



## data aggregation

# count mean


# complex data wrangling



## gather / melt
df1 = pd.DataFrame({'first' : ['Adam', 'John'],
'last' : ['Kowalski', 'Doe'],
'height' : [5.5, 6.0],
'weight' : [130, 150]})



## spread / pivot
#df2.pivot(index = ['first','last'], values = 'value', columns = 'variable')



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


import numpy as np



# https://pandas.pydata.org/pandas-docs/stable/user_guide/timedeltas.html


#---- regular expressions (regex) ----
#https://www.geeksforgeeks.org/split-a-string-into-columns-using-regex-in-pandas-dataframe/


flights['test'] = flights['carrier'].apply(str) + flights['tailnum'].apply(str) 




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






#----- working with NA / None values -----
# fill up with 0 or missing


# calculate average

# delete not needed row / column
