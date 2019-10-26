# -*- coding: utf-8 -*-

##########
# PART 1 #
##########

#---- hello world ----

print("Hello World!!")

#---- calculator ----

2 + 3 

2 / 3

3 * 4 

2^3

5 % 2

5 // 2

#---- math / stat functions ----

import numpy as np

np.sum([1, 2, 3])
np.mean([2, 3, 4])
np.median([2, 3, 4])

#----- variables  ----

a = 1 
b = 2
c = 3

a + b + c

np.sum([a, b, c])


#---- data types-----

## logical 

v1 = True

v2 = False

type(v1)

1 == 1



## numeric

a1 = 12345
a2 = 1.123

type(a1)



## text / string

some_text = "Hello World!"

type(some_text)

## Lists 

# define a list
myList = []

type(myList)

myList = ['a','b','c', 1, 2, 3]
myList

x = [1,2,3]

# assign from list
a,b,c = x
print(a,b,c)

# add to a list
x += x
print(x)

# check number of elements
count_elements = len(x)
print(count_elements)

# add to a list
l = []
l.append("a")
print(l) # ['a']
l.append("b")
print(l) # ['a', 'b']

# remove from list 
l = ['a', 'b', 'c','a', 'b', 'c']
print(l)

l.remove('a')
print(l)


# select element from list 
l[0]
l[1]

l[-1]
l[-2]

l[0 : 2]
l[-3 : -1]

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

print(type(poland_regions))


# add elements
poland_regions['malopolskie'] = 3372618
print(poland_regions)

# get all keys 
print(poland_regions.keys())

# get value for requested key
print(poland_regions.get("slaskie"))

# get all values

print(poland_regions.values())

# delete from dict a value with particular key
poland_regions= {
"mazowieckie": 5349114,
"slaskie": 4570849,
"wielkopolskie": 3475323
}


poland_regions['malopolskie'] = 3372618
poland_regions.pop("malopolskie")
print(poland_regions.items())


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

# logical
a=7 > 7 and 2 > -1
print(a)

a=7 > 7 or 2 > -1
print(a)


a=not(True)
print(a)

# membership 

pets=['dog','cat','fish']
'fox' in pets

'cat' in pets

'me' in 'disappointment'

## loops 

list1 = ['a','b','c']

for element in list1:
    print(element)

for el in list1:
    print(el)


## if clause 

a = 33
b = 33

if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")
else: 
    print("a is greater than b")


## functions 
    
def my_function(a, b):
    c = a + b
    return(c)

my_function(1, 3)




## - pandas, numpy: dataframe, array operations

## Numpy package
# https://docs.scipy.org/doc/numpy/user/quickstart.html
import numpy as np 

a1 = np.array([1, 2, 3])   # Create a rank 1 array
type(a1)

a1

a1.shape
print(a1[0], a1[1], a1[2])   


b1 = np.array([[1,2,3],[4,5,6]])
b1.shape

print(b1[0, 0], b1[0, 1], b1[1, 0])   

# selection 


a3 = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])
a3

b2 = a3[:2, 1:3]
b2


# calculations 

x = np.array([[1,2],[3,4]], dtype=np.float64)
y = np.array([[5,6],[7,8]], dtype=np.float64)

print(x)
print(y)

print(x + y)
print(np.add(x, y))

print(x - y)
print(np.subtract(x, y))

print(x * y)
print(np.multiply(x, y))

print(x / y)
print(np.divide(x, y))

print(np.sqrt(x))


x = np.array([[1,2],[3,4]])

print(np.sum(x))
print(np.sum(x, axis=0)) 
print(np.sum(x, axis=1)) 


## pandas package
# https://www.learndatasci.com/tutorials/python-pandas-tutorial-complete-introduction-for-beginners/
import pandas as pd

# from list
data1 = [['Alex',10],['Bob',12],['Clark',13]]
df1 = pd.DataFrame(data1, columns=['Name','Age'])

# from series 
data2 = {
    'apples': [3, 2, 0, 1], 
    'oranges': [0, 3, 7, 2]
}

df2 = pd.DataFrame(data2)

# view top rows 
df2.head()

# info about data 
df2.info()
df2.describe()


# shape / dimension
df2.shape



# select column from df
test1 = df2['apples']
test1 

type(test1)

# select columns
# .loc - locates by name
# .iloc- locates by numerical index 

# select row from df
df2.loc[0:1]
df2.iloc[0:1]


data3 = [['Gdynia',100],['Gdansk',120],['Sopot',130], ['Gdynia',90], ['Gdansk',100]]
df3 = pd.DataFrame(data3, columns=['City','Sales'])

# column filters
df3[df3['City'] == "Gdansk"]

df3[df3['Sales'] >= 100]

df3[(df3['City'] == 'Gdansk') | (df3['City'] == 'Gdynia')]

df3[df3['City'].isin(['Gdansk', 'Gdynia'])]

df3[(df3['City'] == 'Gdansk') & (df3['Sales'] >= 120)]


# multi axis selection

df3.loc[: , 'City']
df3.loc[0:1,'City']
