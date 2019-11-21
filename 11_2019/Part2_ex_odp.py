# -*- coding: utf-8 -*-

#######################
# exercises 2 answers #
#######################
import os 

os.chdir('D:\\Python_learning\\Python_WSB')

#---- ex 1 -------
# load file Sample1.txt to data frame
# Zaladuj plik Sample1.txt do ramki danych

import pandas as pd

sampleDF = pd.read_csv("SampleFiles\\Sample2.txt", sep = "|", header=None)

#---- ex 2 -------
# name columns in data frame loaded in ex 1
# nadaj nazwy kolumn ramce danych zaladowanej z zadania nr 1

sampleDF.columns = ['ID', 'ObsDate', 'Value', 'RelDate']

#----- ex 3 ------
# load file Obs2.xlsx to data frame
# zaladuj plik Obs2.xlsx do ramki danych 


sampleDF2 = pd.read_excel("SampleFiles\\Obs2.xlsx", sheet_name = "Observations2", header = None )


#---- ex 4 --------------------------
# name columns in data frame loaded in ex 3
# nadaj nazwy kolumn ramce danych zaladowanej z zadania nr 3

sampleDF2.columns = ['ID', 'ObsDate', 'Value']

#----- ex 5 ------
# connect to SampleDb2.db and list all available tables in the database
# podlacz sie do bazy SampleDb2.db oraz wylistuj wszystkie dostepne tablice w bazie

from sqlalchemy import create_engine


engine = create_engine('sqlite:///SampleFiles//SampleDB2.db')


print (engine.table_names())

