# -*- coding: utf-8 -*-

####################
# PART 1 exercises #
####################


#--- Exercise 1 -----
# a) Utwórz zmienną x i przypisz do niej wartość 3.
# b) Utwórz zmienną y i przypisz do niej wartość 4.0.
# c) Dodaj obie liczby. Jaki wynik otrzymasz? Jaki jest typ zmiennej wynikowej?

x = 3
y = 4.0

xy = x + y
xy
type(xy)

#--- Exercise 2 -----
# a) Utwórz zmienną x i przypisz do niej wartość 10.0
# b) Utwórz zmienną y i przypisz do niej wartość 4.0
# c) Odejmij od zmiennej x zmienną y. Jaki wynik otrzymasz? Jaki jest typ zmiennej wynikowej?


x = 10.0
y = 4.0

xy = x - y
xy
type(xy)


#--- Exercise 3 -----
# a) x = 3.0
# b) Zmień typ zmiennej x na int.

x = 3.0
type(x)

x1 = int(x)
type(x1)

#--- Exercise 4 -----
# a) x = 3
# b) zmień type zmiennej na str
# c) Wydrukuj. Co otrzymasz?
 
x = 3
type(x)
x1 = str(x)

type(x1)
x1


#--- Exercise 5 -----
# a. Utwórz zmienną x i przypisz do niej wartość 3.
# b. Utwórz zmienną y i przypisz do niej wartość 3.0.
# c. Co wydrukuje x==y?
# d. Co wydrukuje x==y==True? Dlaczego?
# e. Co wydrukuje x==y==False? Dlaczego?

x = 3
y = 3.0

x==y
x==y==True
x==y==False


#--- Exercise 6 -----
# a. Utwórz zmienną x i przypisz do niej wartość 3.
# b. Utwórz zmienną y i przypisz do niej wartość 3.
# c. Utwórz zmienną z i przypisz do niej wartość wyniku operatora porównania zmiennej x i y.
# d. Używając operatora porównania porównaj z oraz True.

x = 3
y = 3
z = x + y

z == True

#--- Exercise 7 -----
# a. Utwórz zmienną x i przypisz do niej tekst ”3”
# b. Utwórz zmienną y i przypisz do niej tekst ”4”
# c. Co wydrukuje x+y?

x = '3'
y = '4'
z = x + y

type(z)

#--- Exercise 8 -----
# a. Utwórz zmienną x i przypisz do niej tekst ”3”
# b. Utwórz zmienną y i przypisz do niej tekst ”4”
# c. Dodaj x i y tak, by otrzymać wynik 7 i typ int.

x = '3'
y = '4'
z = int(x) + int(y)
type(z)



#--- Exercise 8 -----
# a. utwórz funkcję, która wydrukuje bilet poprzez połączenie imienia poniższych zmiennych. 
name = "Jan"
surname = "Kowalski"

def drukuj_bilet(imie, nazwisko, obywatelstwo=''): 
    return imie + " " + nazwisko + ", " + str(obywatelstwo)

drukuj_bilet(name, surname)


#--- Exercise 9 -----
# Utwórz listę o nazwie my_list i dodaj do nie następujące elementy: 1, 3.1, ”a”, False.
my_list = [1, 3.1, "a", False]
my_list

#--- Exercise 10 -----
# Wydrukuj drugi element listy.
my_list2 = [1,2,3,4,5]

my_list2[1]

#--- Exercise 11 -----
#Wydrukuj liczbę elementów w liście my list2.

len(my_list2)

#--- Exercise 12 -----
# Wydrukuj pierwsze 3 elementy listy my_list2

my_list2[:3]


#--- Exercise 13 -----
# Dołącz do list1 liste nr 2

list1 = [1,2,3]
list2 = [4,5,6]

list1 += list2
print(list1)


#--- Exercise 14 -----
# Ile elementów posiada lista?

mylist3 = [[1,2], [3,4], [4,5]]

len(mylist3)

#--- Exercise 15 -----
# Policz sumę wartosci w pierwszej kolumnie 

input = [
[1,'asdf'],
[3, 'dsf'],
[5, 'dsf'],
[4, 'dsf'],
[9, 'dsf'],
[33, 'dsf'],
[23, 'dsf']]

## method 1 - with numpy
import numpy as np

input1 = np.array(input)
input1

input2 = input1[: , 0]

np.sum(input2.astype(int))



## method 2 - basic method
suma_kolumny_pierwszej = 0
for el in input:
    #print(el)
    suma_kolumny_pierwszej += el[0]
print(suma_kolumny_pierwszej)



############################

import pandas as pd 
data_shops = [['Gdynia',100, 'Biedronka'], ['Gdansk',120, 'Biedronka'], ['Sopot',130, 'Lidl'], ['Gdynia',90, 'Lidl'], ['Gdansk',150, 'Kaufland'], ['Sopot', 200, 'Kaufland'], ['Gdansk', 160, 'Lidl'] ]
df_shops = pd.DataFrame(data_shops, columns=['City','Sales', 'Shops'])


#--- Exercise 16 -----
# Wybierz sklepy Lidl z ramki danych df_shops.
# Choose Lidl show from df_shops data frame.

df_shops[df_shops['Shops'] == 'Lidl']

#--- Exercise 17 -----
# Sprawdz gdzie sprzedaz byla wieksza niz 150 (df_shops).
# Check where sales is higher than 150 (df_shops).

df_shops[df_shops['Sales'] > 150]

#--- Exercise 18 -----
# Sprawdz w ktorych sklepach w Gdansku i Sopocie sprzedaz przewyzszyla kwote 140. (df_shops)
# Check in what shops in Gdansk and Sopot sales is higher than 140.
 
df_shops[ (df_shops['Sales'] > 150) & (df_shops['City'].isin(['Gdansk','Sopot']))]

#--- Exercise 19 -----
# Wybierz wszystkie sklepy oprocz sopockich.
# Choose all shops except Sopot.

df_shops[ -df_shops['City'].isin(['Sopot'])]


#--- Exercise 20 -----
# Wybierz wszystkie sklepy Lidl w Gdansku i Sopocie, w ktorych sprzedaz byla wieksza niz 100 oraz mniejsza niz 210
# Choose all Lidl shops in Gdansk and Sopot where sales is higher than 100 and lower than 210.

df_shops[ (df_shops['Sales'] > 100) & (df_shops['Sales'] < 210) & (df_shops['City'].isin(['Gdansk','Sopot'])) & (df_shops['Shops'].isin(['Lidl'])) ]
