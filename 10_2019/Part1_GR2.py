# -*- coding: utf-8 -*-

##########
# PART 1 #
##########

#---- hello world ----
#pierwsza linia kodu
print("Hello WSB :)")

#---- calculator ----

1 + 1
2 * 10
5 / 2

5 % 2   #reszta z dzielenia

#---- math / stat functions ----

import numpy as np

np.sum([1, 2, 3])
np.mean([1,2,3])  #srednia
np.median([1,2,3])   

#----- variables  ----

a = 1410

abc_Test = "test"


#---- data types-----

## logical 

c =True
d = False

1 == 1

type(c)

## numeric

a = 123

type(a)

b = 1.25

type(b)


## text / string

myText = "Python is awesome"
type(myText)

## Lists 


myList = []

myList = [1,2,3, "bla", "bla"]


# define a list



# assign from list
myList1 = [1,2,3]

a, b, c, = myList1

# add to a list

x = [1,2,3]
y = [3,4,5]

x += y

# check number of elements

len(x)

# add to a list
l = []

l.append([3,4,5])

# remove from list 
l = ['a', 'b', 'c','a', 'b', 'c']
print(l)

l.remove('a')

print(l)

# select element from list 
l = ['a', 'b', 'c','a', 'b', 'c']
l[0]
l[-1]

## Tuples
myTuple = ()
type(myTuple)

myTuple = ('a', 'b')
myTuple[0] = 'z'

myTuple1 = ('a', 'b','a', 'b')
print(myTuple1)

myTuple2 = ('a', 'b', 'c')
print(myTuple2.index('b'))

# nested

myTuple1 = ('a', 'b', 'c')
myTuple2 = ('d', 'e', 'f')
sampleTuple = myTuple1, myTuple2

print(sampleTuple)
sampleTuple
sampleTuple[1]
sampleTuple[1][0]


## Sets 
mySet = {'a'}
print(type(mySet))

print(mySet)

# add new element
mySet = {'a'}
mySet.add('a')
print(mySet)

# check diff

mySet1 = {"a", "b", "c"}
mySet2 = {"b","c", "d"}
print(mySet1.difference(mySet2))

# check what is the same 

mySet1 = {"a", "b", "c"}
mySet2 = {"b","c", "d"}
print(mySet1.intersection(mySet2))

# check if the whole set is inside another
mySet1 = {"a", "b", "c"}
mySet2 = {"a", "b", "c", "d"}
print(mySet1.issubset(mySet2))




## Dicts

poland_regions = {
"mazowieckie": 5349114,
"slaskie": 4570849,
"wielkopolskie": 3475323
}



# add elements

poland_regions['malopolskie'] = 337268

# get all keys 

poland_regions.keys()

tst1 = poland_regions.keys()
type(tst1)

# get value for requested key

poland_regions.get("slaskie")

# get all values

poland_regions.values()

# delete from dict a value with particular key
poland_regions= {
"mazowieckie": 5349114,
"slaskie": 4570849,
"wielkopolskie": 3475323
}



poland_regions['malopolskie'] = 3372618

poland_regions.pop("malopolskie")


## operators 

# relation 
3 < 4
3 > 4
7 <= 7
0 >= 0

3 == 3.0
1 == True
7 == True
0 == False
0.5 == True
1 != -1.0
0.1 == False

# logical

a = 3 < 4
b = 3 > 4

a
b

a&b   #and
a|b   #lub OR





# membership 

pets=['dog','cat','fish']

'fox' in pets

'dog' in pets


## loops 

list1 = ['a','b','c']


for element in list1:
    print(element)

for l in list1:
    print(l)


## if clause 

a = 33
b = 33

if a > b:
    print("ohh no")
elif a <=b:
    print("let it be")
else:
    print("Year")

## functions 
    

def mySum(a,b):
    result = a + b
    
    return(result)

mySum(5, b = 6)


## - pandas, numpy: dataframe, array operations

## Numpy package
# https://docs.scipy.org/doc/numpy/user/quickstart.html
import numpy as np 

a1 = np.array([1,2,3])
a2 = np.array([[1,2,3],
              [4,5,6]])




#to jest tabelaryczne przedstawienie gdzie podajemy wiersz i kolune  czyli a2[wiersz,kolumna]

# selection 

a1[0]
a1[1]
a1[2]


a2[0,1]

test = a2[0:2, 0:1]

# calculations 

x = np.array([[1,2],[3,4]], dtype=np.float64)
y = np.array([[5,6],[7,8]], dtype=np.float64)

x + y

np.add(x, y)

x - y

np.subtract(x,y)

x / y

np.divide(x,y)


x = np.array([[1,2],[3,4]])

np.sqrt(x)

x.shape # ile wierszy i kolumn


## pandas package
# https://www.learndatasci.com/tutorials/python-pandas-tutorial-complete-introduction-for-beginners/
import pandas as pd

# from list

data1 = [['Alex',10],
         ['Bob',12],
         ['Clark',13]]

df1 = pd.DataFrame(data1, columns=['Name','Age'])

data2 = [['Kasia', 10],
         ['Krzys', 12],
         ['Ala', 12]]

df2 = pd.DataFrame(data1,
                   columns = ['Name', 'Age'])

# from dict

data3 = {'apples':[3,10,15,8],
         'oranges':[1,2,3,4],
         'mango': [1,10,20,14]} 

df3 = pd.DataFrame(data2)

# view top rows 


df3.head(2)

# info about data 

df3.info()
df3.describe()



# shape / dimension

df3.shape


# select column from df

df3[['oranges', 'apples']]

# select columns
# .loc - locates by name   name location
# .iloc- locates by numerical index index location

df3.loc[:, ['oranges', 'apples']]

df3.iloc[:, 0:2]

# select row from df


df3.loc[0:1, ['oranges', 'apples']]


data4 = [['Gdynia',100],['Gdansk',120],['Sopot',130], ['Gdynia',90], ['Gdansk',100]]
df4 = pd.DataFrame(data4, columns=['City','Sales'])

# column filters

df4.loc[:,['City']]

# multi axis selection

df4[df4['City']=='Sopot']

df4[(df4['City']=='Sopot') | (df4['City'] == 'Gdansk')]

df4[df4['City'].isin(['Sopot', 'Gdansk'])]
