# -*- coding: utf-8 -*-

#######################
# exercises 3 answers #
#######################
import pandas as pd
import os 

os.chdir('D:\\GITHUB\\Python-Postgraduate_studies_on_WSB\\12_2019')


#------ ex 1 -------
# from weather data select vacation time (July-August) and select only EWR origin.
# z danych pogodowyc wybierz okres wakacyjny obserwacji i wybierz dane tylko dla EWR (Newark) 

weather = pd.read_csv("SampleFiles\\weather.csv")

df1 = weather.query("month in [7,8] AND origin == 'EWR'")



#------ ex 2 -------
# from wether data list top 5 days with the strongest wind and lowest visibility. List days.
# z danych pogodowych wylistuj top 5 dni kiedy wiatr byl najsilniejszy i widocznosc byla namniejsza. Podaj dni.


#------ ex 3 -------
# check average  delay for each carrier.
# policz srednie  opoznienie samolotow dla poszczegolnych przewoznikow.
flights = pd.read_csv("SampleFiles\\flights.csv")

ex3 = (flights
       .filter(['carrier', 'arr_delay'])
       .groupby('carrier')
       .mean())

#------ ex 4 -------
# join metadata and obseravations tables (from part 2)
# polacz tablice metadane i obserwacje (z cwiczen nr 2)  



#------ ex 5 -------
# fill up NA / None value with average. 
# zamien wartosci NA / None na srednia. 

shop_data = pd.DataFrame({'day':[1, 1, 2, 2, 3, 3],
                    'hour':[8, 16, 8, 16, 8, 16],
                    'profit':[100, 200, 50, 60, None, None]})



#------ ex 6 -------
# fill up NA value with hour average 
# zamien wartosci NA na srednia z poszczegolnych godzin. 

shop_data = pd.DataFrame({'day':[1, 1, 2, 2, 3, 3],
                    'hour':[8, 16, 8, 16, 8, 16],
                    'profit':[100, 200, 50, 60, None, None]})



#------ ex 7 -------
# [*] count income rates for stock idexes (stocks - EuStockMarkets)
# [*] policz miesieczne stopy zwrotu dla indeksow gieldowych (zbior stocks - EuStockMarkets)

import statsmodels.api as sm
dataset_stocks= sm.datasets.get_rdataset(dataname='EuStockMarkets', package='datasets')
stocks = dataset_stocks.data




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




#------ ex 9 -------
# Use weather data to check if in particular month the Precipitation distribution differs. 
# w danych pogodowych sprawdz czy dla poszczegolnych miesiecy rozklad opadow rozni sie od siebie. 




#------ ex 10 -------

# in below data frame select only rows where sales occured in working days (MO - FR)
# dla ponizszej ramki danych wybierz wiersze gdzie sprzedaz wystapila w ciagu tygodnia pracy (PN - PT)
df = pd.DataFrame({ 'sales_date': ["1/01/2019", "02/02/2019", "11/12/2019", "30/5/2019"],
                 'price': [1000, 2000, 900, 700] 
})





#------ ex 11 -------

# check what was the intervals between sales in data frame from ex 10
# sprawdz co ile dni wystepowala sprzedaz w przykladzie z cwiczenia 10

import numpy as np



#------ ex 12 -------

# join data from folder flights (flights, weather, planes, airports, airlines). 
# polacz dane z folderu flights.
# https://cran.r-project.org/web/packages/nycflights13/nycflights13.pdf


flights = pd.read_csv('SampleFiles\\Flights\\all\\flights.csv')
weather = pd.read_csv('SampleFiles\\Flights\\all\\weather.csv')
planes = pd.read_csv('SampleFiles\\Flights\\all\\planes.csv')
#airports = pd.read_csv('SampleFiles\\Flights\\all\\airports.csv')
airlines = pd.read_csv('SampleFiles\\Flights\\all\\airlines.csv')




#------ ex 13 -------

# Extract particular information into seperate columns (street, name & surname, postal_code, city). 
# Przeksztalc ponizsza ramke danych tak aby uzyskac ulice, imie i nazwisko, kod pocztowy oraz miasto w osobnych kolumnach, 

df13 = pd.DataFrame({'Address': [ " 12358 ul. Armii Krajowej 47, 00-252 Warszawa; Jan Kowalski", 
                                " 98786 AL. Jana Pawla II 456, 80-987 Gdansk; Anna Nowak" ,
                                "13258 Plac wyzwolenia 950, 12-547 Wroclaw; Jan Maria Tomaszewski"] })

df13['kod pocztowy'] = df13['Address'].str.extract('([0-9]{2}-[0-9]{3})', expand = False)

df13['imie i nazwisko'] = df13['Address'].str.extract('([A-Za-z ]*)$', expand = False)

df13['ulica_tmp'] = df13['Address'].str.replace('([0-9]+)', '' )

df13['ulica'] = df13['ulica_tmp'].str.replace('(,.+$)','')


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



#------ ex 15 -------

# write a function based on some_txt from above to remove tags with any text and leave only needed information
# napisz funkcje, ktora usunie z wyznaczonego tekstu tagi xml oraz pozostawi jedynie niezbedne informacje. 




#------ ex 16 -------
# From metadane file extract Country from Description column and check if it is the same as Country column.
# Z pliku metadane sprawdz czy kraj w kolumnie Description jest taki sam jak w kolumnie Country. 

Metadane = pd.read_csv('SampleFiles\\Metadane1.csv')



#------ ex 17 -------
# Transform LifeCycleSavings into 3 columns (country, key, value)
# Przeksztalc zbior LifeCycleSavings do 3 kolumn tak aby uzyskac nastepujace kolumny (kraj, klucz, wartosc)

import statsmodels.api as sm
dataset_LCS= sm.datasets.get_rdataset(dataname='LifeCycleSavings', package='datasets')
LCS = dataset_LCS.data



#------ ex 18 -------
# Import WorldPhones and measure what is average and median usage in each decade.
# Zaladuj dane WorldPhones i policz jaki bylo srednie uzycie telefonow w poszczegolnych dekadach. 

import statsmodels.api as sm
dataset_WP= sm.datasets.get_rdataset(dataname='WorldPhones', package='datasets')
WP = dataset_WP.data




#------ ex 19 --------
# from file Obs and Metadane1 find: "Poland, Production, Passenger cars" and create data frame in which years will be in rows na months in columns. 
# dla pliku Obs and Metadane znajdz: "Poland, Production, Passenger cars" oraz dokonaj transformacji danych tak aby w wierszach byly lata, a w kolumnach miesiace. 

Meta = pd.read_csv('SampleFiles\\Metadane1.csv')
Obs = pd.read_csv('SampleFiles\\Obs1.csv')

MetaObs = pd.merge(Meta, Obs, left_on = 'ID', right_on = 'EconomicIndicatorId', how = 'inner')

MetaObs.dtypes
