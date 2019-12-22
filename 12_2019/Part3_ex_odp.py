# -*- coding: utf-8 -*-

#######################
# exercises 3 answers #
#######################
import pandas as pd
import os 

os.chdir('D:\\Python_learning\\Python_WSB')


#------ ex 1 -------
# from weather data select vacation time (July-August) and select only EWR origin.
# z danych pogodowyc wybierz okres wakacyjny obserwacji i wybierz dane tylko dla EWR (Newark) 

ex1 = weather.query("year == 2013 and month in (7,8) and origin == 'EWR' ")

#------ ex 2 -------
# from wether data list top 5 days with the strongest wind and lowest visibility. List days.
# z danych pogodowych wylistuj top 5 dni kiedy wiatr byl najsilniejszy i widocznosc byla namniejsza. Podaj dni.

weather_summary2 = (weather
 .filter(['day', 'wind_speed', 'visib'])
 .groupby(['day'])
 .agg(['mean'])
 .sort_values(by=[('wind_speed', 'mean'), ('visib', 'mean')] , ascending=[True, False])
 .tail(5))


#------ ex 3 -------
# check average  delay for each carrier.
# policz srednie  opoznienie samolotow dla poszczegolnych przewoznikow.

flight_summary3 = (flights
 .filter(['carrier', 'arr_delay'])
 .groupby(['carrier'])
 .agg(['mean']))


#------ ex 4 -------
# join metadata and obseravations tables (from part 2)
# polacz tablice metadane i obserwacje (z cwiczen nr 2)  

Meta = pd.read_csv("SampleFiles\\Metadane1.csv")


Obs = pd.read_excel("SampleFiles\\Obs2.xlsx", sheet_name = "Observations2", header = None )
Obs.columns = ['ID', 'ObsDate', 'Value']

MetaObs = pd.merge(Meta, Obs, on = 'ID', how = 'inner')


#------ ex 5 -------
# fill up NA / None value with average. 
# zamien wartosci NA / None na srednia. 

shop_data = pd.DataFrame({'day':[1, 1, 2, 2, 3, 3],
                    'hour':[8, 16, 8, 16, 8, 16],
                    'profit':[100, 200, 50, 60, None, None]})


shop_data['profit'] = shop_data['profit'].fillna(shop_data['profit'].mean())

#------ ex 6 -------
# fill up NA value with hour average 
# zamien wartosci NA na srednia z poszczegolnych godzin. 

shop_data = pd.DataFrame({'day':[1, 1, 2, 2, 3, 3],
                    'hour':[8, 16, 8, 16, 8, 16],
                    'profit':[100, 200, 50, 60, None, None]})


sample6 = shop_data.groupby("hour").transform(lambda x: x.fillna(x.mean()))


#------ ex 7 -------
# [*] count income rates for stock idexes (stocks - EuStockMarkets)
# [*] policz miesieczne stopy zwrotu dla indeksow gieldowych (zbior stocks - EuStockMarkets)

import statsmodels.api as sm
dataset_stocks= sm.datasets.get_rdataset(dataname='EuStockMarkets', package='datasets')
stocks = dataset_stocks.data

stocks['DAX_lag'] = stocks['DAX'].shift(1)
stocks['SMI_lag'] = stocks['SMI'].shift(1)
stocks['CAC_lag'] = stocks['CAC'].shift(1)
stocks['FTSE_lag'] = stocks['FTSE'].shift(1)


stocks['DAX_interest'] = ((stocks['DAX'] - stocks['DAX_lag']) / stocks['DAX'])  * 100 
stocks['SMI_interest'] = ((stocks['SMI'] - stocks['SMI_lag']) / stocks['SMI'])  * 100
stocks['CAC_interest'] = ((stocks['CAC'] - stocks['CAC_lag']) / stocks['CAC'])  * 100
stocks['FTSE_interest'] = ((stocks['FTSE'] - stocks['FTSE_lag']) / stocks['FTSE'])  * 100



#------ ex 8 -------
# below data frames represent 2 tables for demand and supply in particular shops. Check what is the balance between supply and demand in particular shops. 
# ponizsze ramki danych przedstawiaja popyt i podaz na produkty w sklepach. Policz bilans popytu i podazy w danych sklepach. 


df_1 = pd.DataFrame({
  'dates': ["2018-07-01", "2018-06-01", "2018-06-01", "2018-05-01", "2018-07-01", "2018-06-01", "2018-06-01", "2018-05-01"],
  'demand': [10, 11, 12, 13, 10, 11, 12, 13],
  'shop': ["Tesco", "Brico", "Lidl", "Aldo", "Tesco", "Brico", "Lidl", "Aldo"]
})

df_2 = pd.DataFrame({
  'dates': ["2018-07-01", "2018-06-01", "2018-05-01", "2018-04-01", "2018-07-01", "2018-06-01", "2018-05-01", "2018-04-01"],
  'supply': [20, 21, 22, 23, 20, 21, 22, 23],
  'shop': ["P&P", "Alma", "Kaufland", "Auchan", "Tesco", "Brico", "Lidl", "Aldo"]
})


df8 = pd.merge(df_1, df_2, how = 'inner', on = ['dates', 'shop'])
df8['balance'] = df8['supply'] - df8['demand']


#------ ex 9 -------
# Use weather data to check if in particular month the Precipitation distribution differs. 
# w danych pogodowych sprawdz czy dla poszczegolnych miesiecy rozklad opadow rozni sie od siebie. 

weather_summary9 = (weather
                   .filter(['month', 'precip'])
                   .groupby('month')
                   .agg('mean'))

#------ ex 10 -------

# in below data frame select only rows where sales occured in working days (MO - FR)
# dla ponizszej ramki danych wybierz wiersze gdzie sprzedaz wystapila w ciagu tygodnia pracy (PN - PT)
df = pd.DataFrame({ 'sales_date': ["1/01/2019", "02/02/2019", "11/12/2019", "30/5/2019"],
                 'price': [1000, 2000, 900, 700] 
})


df['sales_date'] = pd.to_datetime(df.sales_date)
df.dtypes

df['week_day'] = df['sales_date'].dt.weekday

df.query('week_day >= 1 and week_day <=5')


#------ ex 11 -------

# check what was the intervals between sales in data frame from ex 10
# sprawdz co ile dni wystepowala sprzedaz w przykladzie z cwiczenia 10

import numpy as np


df = df.sort_values(by ='sales_date' )
 

df['sales_date_lag'] = df['sales_date'].shift(1)
df['date_diff'] = df['sales_date'] - df['sales_date_lag']
df['date_diff1'] = df['date_diff'] / np.timedelta64(1,'D')


#------ ex 12 -------

# join data from folder flights (flights, weather, planes, airports, airlines). 
# polacz dane z folderu flights.
# https://cran.r-project.org/web/packages/nycflights13/nycflights13.pdf


flights = pd.read_csv('SampleFiles\\Flights\\all\\flights.csv')
weather = pd.read_csv('SampleFiles\\Flights\\all\\weather.csv')
planes = pd.read_csv('SampleFiles\\Flights\\all\\planes.csv')
#airports = pd.read_csv('SampleFiles\\Flights\\all\\airports.csv')
airlines = pd.read_csv('SampleFiles\\Flights\\all\\airlines.csv')

data_all = flights.merge(weather,on='time_hour').merge(planes,on='tailnum').merge(airlines, on = 'carrier')



#------ ex 13 -------

# Extract particular information into seperate columns (street, name & surname, postal_code, city). 
# Przeksztalc ponizsza ramke danych tak aby uzyskac ulice, imie i nazwisko, kod pocztowy oraz miasto w osobnych kolumnach, 

df13 = pd.DataFrame({'Address': [ " 12358 ul. Armii Krajowej 47, 00-252 Warszawa; Jan Kowalski", 
                                " 98786 AL. Jana Pawla II 456, 80-987 Gdansk; Anna Nowak" ,
                                "13258 Plac wyzwolenia 950, 12-547 Wroclaw; Jan Maria Tomaszewski"] })


df13['postal_code'] =  df13['Address'].str.extract('([0-9]{2}-[0-9]{3})', expand = False)
df13['Name_Surname'] =  df13['Address'].str.extract('([A-Za-z ]*$)', expand = False)
df13['Street1'] =  df13['Address'].str.replace('(^[ 0-9]+)', '')
df13['Street2'] =  df13['Street1'].str.replace('(,\s[0-9]{2}-[0-9]{3}.+$)', '')
df13['City1'] =  df13['Street1'].str.extract('([0-9]{2}-[0-9]{3}\s[A-Za-z]+)', expand = False)
df13['City2'] =  df13['City1'].str.replace('([0-9]{2}-[0-9]{3}\s)', '')



#------ ex 14 -------

# extract title and author to data frame
# napisz takie wyrazenie aby zapisac w ramce danych tytul oraz autora 

some_txt = """
<bookstore>
  <book category='cooking'>
    <title>Everyday Italian</title>
    <author>Giada De Laurentiis</author>
    <year>2005</year>
    <price>30.00</price>
  </book>
  <book>
    <title>Harry Potter</title>
    <author>J K. Rowling</author>
    <year>2005</year>
    <price>29.99</price>
  </book>
  <book>
    <title>Learning XML</title>
    <author>Erik T. Ray</author>
    <year>2003</year>
    <price>39.95</price>
  </book>
</bookstore> """

import re

title = re.findall('(<title.+title>)', some_txt)
author = re.findall('(<author.+author>)', some_txt)

result_df = pd.DataFrame({ 
        'Title': title,
        'Author': author
        })

result_df['Title'] =  result_df['Title'].str.replace('(<title>|<\/title>)', '')
result_df['Author'] =  result_df['Author'].str.replace('(<author>|<\/author>)', '')


#------ ex 15 -------

# write a function based on some_txt from above to remove tags with any text and leave only needed information
# napisz funkcje, ktora usunie z wyznaczonego tekstu tagi xml oraz pozostawi jedynie niezbedne informacje. 

def remove_txt(old_txt, tags):
    tags_regex = "(<" + tags + ">|<\/" + tags + ">)"
    new_txt = str(re.sub(tags_regex, "", old_txt))
    
    return(new_txt)

some_new_txt = remove_txt(some_txt, "author")

#------ ex 16 -------
# From metadane file extract Country from Description column and check if it is the same as Country column.
# Z pliku metadane sprawdz czy kraj w kolumnie Description jest taki sam jak w kolumnie Country. 

Metadane = pd.read_csv('SampleFiles\\Metadane1.csv')

Metadane['Country_extract'] = Metadane['Description'].str.extract("(^[A-Za-z]+)", expand = False)

Metadane.loc[(Metadane.Country == Metadane.Country_extract) , 'check_match'] = True  


#------ ex 17 -------
# Transform LifeCycleSavings into 3 columns (country, key, value)
# Przeksztalc zbior LifeCycleSavings do 3 kolumn tak aby uzyskac nastepujace kolumny (kraj, klucz, wartosc)

import statsmodels.api as sm
dataset_LCS= sm.datasets.get_rdataset(dataname='LifeCycleSavings', package='datasets')
LCS = dataset_LCS.data

    
LCS_new = LCS.reset_index()
LCS_melt = LCS_new.melt(id_vars = ['index'])


#------ ex 18 -------
# Import WorldPhones and measure what is average and median usage in each decade.
# Zaladuj dane WorldPhones i policz jaki bylo srednie uzycie telefonow w poszczegolnych dekadach. 

import statsmodels.api as sm
dataset_WP= sm.datasets.get_rdataset(dataname='WorldPhones', package='datasets')
WP = dataset_WP.data

WP_new = WP.reset_index()

WP_pivot = WP_new.melt(id_vars = ['index'])
WP_pivot['Decade'] = WP_pivot['index'].astype(str).str.extract("([0-9]{2}$)", expand = False)
WP_pivot['Decade'] = WP_pivot['Decade'].str.extract("(^[0-9]{1})", expand = False)

WP_summary = (WP_pivot
              .filter(['Decade', 'value'])
              .groupby('Decade')
              .agg('mean'))

#------ ex 19 --------
# from file Obs and Metadane1 find: "Poland, Production, Passenger cars" and create data frame in which years will be in rows na months in columns. 
# dla pliku Obs and Metadane znajdz: "Poland, Production, Passenger cars" oraz dokonaj transformacji danych tak aby w wierszach byly lata, a w kolumnach miesiace. 

Meta = pd.read_csv('SampleFiles\\Metadane1.csv')
Obs = pd.read_csv('SampleFiles\\Obs1.csv')

MetaObs = pd.merge(Meta, Obs, left_on = 'ID', right_on = 'EconomicIndicatorId', how = 'inner')

MetaObs.dtypes

MetaObs['ObsDate'] = pd.to_datetime(MetaObs['ObsDate'])
MetaObs['month'] = MetaObs['ObsDate'].dt.month
MetaObs['year'] = MetaObs['ObsDate'].dt.year

MetaObs1 = (MetaObs
            .query("Description == 'Poland, Production, Passenger cars'")
            .filter(['month', 'year', 'Value'])
            .pivot_table(index = ['year'], values = 'Value', columns = 'month'))

