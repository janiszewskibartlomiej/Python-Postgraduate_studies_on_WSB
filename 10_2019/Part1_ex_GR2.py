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

z = x+y

#otrzymam float 7.0

type(z)


#--- Exercise 2 -----
# a) Utwórz zmienną x i przypisz do niej wartość 10.0
# b) Utwórz zmienną y i przypisz do niej wartość 4.0
# c) Odejmij od zmiennej x zmienną y. Jaki wynik otrzymasz? Jaki jest typ zmiennej wynikowej?


x = 10.0

y = 4.0

z = x - y

#otrzymam float 6.0

type(z)


#--- Exercise 3 -----
# a) x = 3.0
# b) Zmień typ zmiennej x na int.


x = 3.0

x = int(x)

print(x, type(x))



#--- Exercise 4 -----
# a) x = 3
# b) zmień type zmiennej na str
# c) Wydrukuj. Co otrzymasz?
 
x = 3

x = str(x)

print(x, type(x))





#--- Exercise 5 -----
# a. Utwórz zmienną x i przypisz do niej wartość 3.
# b. Utwórz zmienną y i przypisz do niej wartość 3.0.
# c. Co wydrukuje x==y?
# d. Co wydrukuje x==y==True? Dlaczego?
# e. Co wydrukuje x==y==False? Dlaczego?


x = 3
y = 3.0

print(x==y)
print(x==y==True)
print(x==y==False)


#--- Exercise 6 -----
# a. Utwórz zmienną x i przypisz do niej wartość 3.
# b. Utwórz zmienną y i przypisz do niej wartość 3.
# c. Utwórz zmienną z i przypisz do niej wartość wyniku operatora porównania zmiennej x i y.
# d. Używając operatora porównania porównaj z oraz True.


x = 3
y = 3
z = x==y

print(z==True)



#--- Exercise 7 -----
# a. Utwórz zmienną x i przypisz do niej tekst ”3”
# b. Utwórz zmienną y i przypisz do niej tekst ”4”
# c. Co wydrukuje x+y?

x = "3"
y = "4"

print(x+y, type(x+y))


#--- Exercise 8 -----
# a. Utwórz zmienną x i przypisz do niej tekst ”3”
# b. Utwórz zmienną y i przypisz do niej tekst ”4”
# c. Dodaj x i y tak, by otrzymać wynik 7 i typ int.

x = "3"

y = "4"

x, y = int(x), int(y)

z = x + y

print(z, type(z))

#--- Exercise 8 -----
# a. utwórz funkcję, która wydrukuje bilet poprzez połączenie imienia poniższych zmiennych. 

name = "Jan"
surname = "Kowalski"

def bilet():
    x = print(name, surname)
    return x

bilet()


def moj(name, surname, sep = " "):
    bilet = name + sep + surname
    return bilet

bilet(name=name, syrname = surname)

#--- Exercise 9 -----
# Utwórz listę o nazwie my_list i dodaj do niej następujące elementy: 1, 3.1, ”a”, False.

my_list = []

my_list = [1, 3.1, "a", False]
 
dane = (1, 3.1, "a", False)

for x in dane:
    my_list.append(x)
    
    
print(my_list)


#--- Exercise 10 -----
# Wydrukuj drugi element listy.
my_list2 = [1,2,3]

print(my_list2[1])



#--- Exercise 11 -----
#Wydrukuj liczbę elementów w liście my list2.

len(my_list2)



#--- Exercise 12 -----
# Wydrukuj pierwsze 3 elementy listy my_list2

print(my_list2[0:3])


#--- Exercise 13 -----
# Dołącz do list1 liste nr 2

nowa_lista = my_list + my_list2

nowa_lista += my_list2

print(nowa_lista)


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
x = input1[:, 0]

np.sum(x.astype(int))

sum(x.astype(int))


np.sum(x)


## method 2 - basic method

suma = 0

for x in input:
    suma += x[0]
    
print(suma)

############################

import pandas as pd 
data_shops = [['Gdynia',100, 'Biedronka'], ['Gdansk',120, 'Biedronka'], ['Sopot',130, 'Lidl'], ['Gdynia',90, 'Lidl'], ['Gdansk',150, 'Kaufland'], ['Sopot', 200, 'Kaufland'], ['Gdansk', 160, 'Lidl'] ]
df_shops = pd.DataFrame(data_shops, columns=['City','Sales', 'Shops'])


#--- Exercise 16 -----
# Wybierz sklepy Lidl z ramki danych df_shops.
# Choose Lidl show from df_shops data frame.

lidl = [x for x in data_shops if x[2] == 'Lidl']
print(lidl)

df_shops[df_shops['Shops'] == 'Lidl']


#--- Exercise 17 -----
# Sprawdz gdzie sprzedaz byla wieksza niz 150 (df_shops).
# Check where sales is higher than 150 (df_shops).

sell_150 = [x for x in data_shops if x[1] > 150]

df_shops[df_shops['Sales'] > 150]


#--- Exercise 18 -----
# Sprawdz w ktorych sklepach w Gdansku i Sopocie sprzedaz przewyzszyla kwote 140. (df_shops)
# Check in what shops in Gdansk and Sopot sales is higher than 140.
 
gd_sop = [x for x in data_shops if x[0] in ['Sopot', 'Gdynia'] and x[1]>140]

df_shops[(df_shops['City'].isin(['Gdansk','Sopot'])) & (df_shops['Sales'] > 140) ]


#--- Exercise 19 -----
# Wybierz wszystkie sklepy oprocz sopockich.
# Choose all shops except Sopot.
#~~ to jest negacja 


del_sop = [x for x in data_shops if x[0] != 'Sopot']

df_shops[df_shops['City'] != 'Sopot']

df_shops[~df_shops['City'].isin(['Sopot'])]

#--- Exercise 20 -----
# Wybierz wszystkie sklepy Lidl w Gdansku i Sopocie, w ktorych sprzedaz byla wieksza niz 100 oraz mniejsza niz 210
# Choose all Lidl shops in Gdansk and Sopot where sales is higher than 100 and lower than 210.

lidl_gd_sop_100 = [x for x in data_shops if x[0] in ['Gdansk','Sopot'] and x[2] == 'Lidl' and 210 > x[1] > 100]

df_shops[(df_shops['City'].isin(['Gdansk','Sopot'])) & (df_shops['Shops'] == 'Lidl')  & ((df_shops['Sales'] > 100) & (df_shops['Sales'] < 210)) ]
