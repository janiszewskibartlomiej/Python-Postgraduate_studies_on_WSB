import pandas as pd


### Pytanie 1 

#Jaką funkcję należy użyc aby załadować plik csv do ramki danych? 

pd.read_csv()


### Pytanie 2

# bibliotekę służącą do operacji na ramkach danych oraz przekształcania danych (data wrangling).

#pandas

### Pytanie 3 

#Jaki będzie rezultat wywołania poniższej funkcji? 

 def SampleFunction(a, b):
    a = 3
    c = a + b
    return(c)
    
    SampleFunction(a = 2, b = 3)
    
    # 6
    

### Pytanie 4 

#Która z poniższych bibliotek nie służy do wykonywania wykresów? 
1. matplotlib
2. plotly
3. numpy  <--
4. Żadna z powyższych.

# numpy
    

### Pytanie 5

#Co będzie rezultatem wykonania poniższej lini kodu? 
    
    
x = ["a", "b", "c", "d"]
y = ["w", "x", "y", "z"]


x + y

#Out[7]: ['a', 'b', 'c', 'd', 'w', 'x', 'y', 'z']


### Pytanie 6 

#Jaki kod należy wpisać aby wybrać rekord z 2giego wiersza i 3ciej kolumny z poniższej ramki danych?


import pandas as pd


data1 = [['Gdansk', 10, 100], ['Sopot',12, 345], ['Gdynia', 20, 500]]
SampleDF = pd.DataFrame(data1, columns=['City', 'Sales', 'Income'])

SampleDF.iloc[1,2]



### Pytanie 7 

#Jaki rodzaj wykresu będzie rezultatem poniższego kodu? 

import matplotlib.pyplot as plt

eco1 = pd.DataFrame({'HPI':[80,85,88,85],
                    'Int_rate':[2, 3, 2, 2],
                    'US_GDP_Thousands':[50, 55, 65, 55],
                   'Year' : [2001, 2002, 2003, 2004]})

eco1['Year'] = eco1['Year'].astype(str) 

plt.plot(eco1['Year'], eco1['US_GDP_Thousands'])

#  line


### Pytanie 8 

#Jaki typ(y) danych będzie / będą zapisane w poniższym wektorze? 

SampleVec = [1, "bla", True]

type(SampleVec)
type(SampleVec[0])
type(SampleVec[1])
type(SampleVec[2])

#numeric, character, logical


### Pytanie 9

#Jaka jest różnica miedzy metodą "loc" a "iloc" w ramkach danych?


 #iloc słóży do wyboru elementów na podstawie indeksów wierszy/kolumn, a loc na podstawie nazw wierszy/kolumn. 

# .loc - locates by name   name location
# .iloc- locates by numerical index index location

SampleDF.loc[:,'City']
SampleDF.iloc[:,[0,1]]

### Pytanie 10 

#Która z poniższych lini kodu wybierze rekord(y) gdzie sprzedaż jest większa od 200 i mniejsza od 400. 


SampleDF10 = pd.DataFrame({'City':["Gdansk", "Gdynia", "Sopot", "Gdansk", "Gdynia", "Sopot", "Sopot", "Gdansk"],
                    'Sales':[500, 400, 200, 400, 200, 250, 200, 100],
                    'Employees':[6, 4, 1, 6, 4, 1, 2, 3]})
SampleDF10
SampleDF10.drop('Employees', axis=1)    
SampleDF10.query("Sales > 200 & Sales < 400")

# pytanie 11

#Jaki będzie rezultat poniższej lini kodu:


x = [1,2,3]
a,b,c = x
a
b
c
# do obiektów a, b, c zostaną odpowiednio przypisane wartości 1,2,3

# pytanie 12

#Jeżeli w ramce danych są dostępne następujące kolumny: 
"name", "year", "month", "day", "hour" 

#Co wywoła poniższy kod?


import pandas as pd


date1 = pd.Series(pd.date_range('2012-1-1 12:00:00', periods=7, freq='M'))
date2 = pd.Series(pd.date_range('2013-3-11 21:45:00', periods=7, freq='W'))
 
dates_df = pd.DataFrame(dict(Start_date = date1, End_date = date2))


dates_df['YM'] = dates_df['Start_date'].map(lambda x: x.month).apply(str) + "-" + dates_df['Start_date'].map(lambda x: x.year).apply(str) 

dates_df

1. Zostaną wybrane wiersze, które są w formacie "m-yyyy".
2. Zastąpi obecna kolumnę "Start_date", która będzie składać się roku orazmiesiąca.
3. Utworzy nową kolumnę "YM", która będzie składać się roku, miesiąca oraz dnia.
4. Żadne z powyższych.  <--

#Żadne z powyższych.

# pytanie 13


#Jeżeli dzisiaj jest 13 grudnia 2018, to co będzie wynikiem wywałania poniższej lini kodu? 

import pandas as pd 

t = pd.datetime.now()
t

tmoje = pd.datetime.strptime('2018-12-13', "%Y-%m-%d")
tmoje
t1 = pd.datetime.strptime('2018-11-10', "%Y-%m-%d")
t1
t2 = tmoje - t1
t2.days // 30

1. -33
2. 33
3. -1
4. 1   <--

#1

### Pytanie 14 

#Co bedzię rezultatem wywołania poniższych lini kodu?
import pandas as pd

day = [1, 1, 2, 2, 3, 3]
hour = [8, 16, 8, 16, 8, 16]
profit = [100, 200, 50, 60, None, None]


shopData = pd.DataFrame(list(zip(day, hour, profit)), columns = ["day", "hour", "profit"])
shopData

shopData['profit']= shopData.profit.fillna(shopData.profit.median())

#Rekordy NA będą zastąpione madianą wartości całej kolumny profit.


### Pytanie 15 

#Co wywołają poniższe linie kodu? 

import pandas as pd
import matplotlib.pyplot as plt

day = [1, 1, 2, 2, 3, 3]
hour = [8, 16, 8, 16, 8, 16]
profit = [100, 200, 50, 60, None, None]

shopData = pd.DataFrame(list(zip(day, hour, profit)), columns = ["day", "hour", "profit"])

shopData

x = shopData['hour']
y = shopData['profit']

plt.scatter(x, y)

#W zakładce plot pojawi się kompletny wykres (tło ze skalą, wykres punktowy oraz podpisane osie).

### Pytanie 16

#Co pojawi się na ekranie (w konsoli) po wywyłaniu poniższej lini kodu: 


y = list(range(9))
y

for i in y:
  print(i)

#10 pojedynczych elementów (wektorów jednoelementowych) z wartościami od 0 do 8.

### Pytanie 17 

#Która z poniższych metod służy do ładowania plików xlsx do ramki danych? 

1. pd.read_xlsx
2. pd.read_excel  <--
3. excel.read
4. xlsx_read

#pd.read_excel


### Pytanie 18

Jaką funkcje należy wstawić w "__" aby usunąć z ramki danych kolumny "month" i "carrier".


flights_s1 = flights.__([ 'month', 'carrier'], axis = 1)

1. drop  <--
2. remove
3. purge
4. pop

#drop



### Pytanie 19 

#Jakich funkcji / kroków użyjesz aby zbudować podsumowanie (agregacje) dla poszczególnych miast z poniższej ramki danych?



data3 = [['Gdynia',100],['Gdansk',120],['Sopot',130], ['Gdynia',90], ['Gdansk',100]]

df3 = pd.DataFrame(data3, columns=['City','Sales'])


1. df3.groupby(['City']).agg(['mean', 'size', 'sum'])  <--
2. df3.agg(['mean', 'size', 'sum'].groupby(['City']))
3. mydf.groupby(['City']).agg(['mean', 'size', 'sum'])
4. df3.agg(['mean', 'size', 'sum'])

#df3.groupby(['City']).agg(['mean', 'size', 'sum'])


### Pytanie 20 

#Który z poniższy kodów zwróci błąd (error)? 
import os

os.chdir('D:\\GITHUB\\Python-Postgraduate_studies_on_WSB')


#---- load data ----
flights = pd.read_csv("01_2020\\flights.csv")


1. flights.query("year == 2013 and month == 1 and day == 1")
2. flights.query("year == 2013 & month == 1 & day == 1")
3. flights.query(" year == 2013 | month == 1 | day == 1 ")
4. flights.query(" year = 2013 | month = 1 | day = 1 ")  <--

#4. flights.query(" year = 2013 | month = 1 | day = 1 ")
