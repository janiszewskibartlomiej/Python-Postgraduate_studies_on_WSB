# -*- coding: utf-8 -*-

#######################
# exercises 2 answers #
#######################
import os 

os.chdir('D:\GITHUB\Python-Postgraduate_studies_on_WSB')

#---- ex 1 -------
# load file Sample1.txt to data frame
# Zaladuj plik Sample1.txt do ramki danych

import pandas as pd

metadata = pd.read_csv("D:\\GITHUB\\Python-Postgraduate_studies_on_WSB\\11_2019\\SampleFiles\\Sample2.txt",
                       sep="|",
                       header = None)

#---- ex 2 -------
# name columns in data frame loaded in ex 1
# nadaj nazwy kolumn ramce danych zaladowanej z zadania nr 1

metadata.columns = ['ID', 'ObsDate', 'Value', 'RelDate']


#----- ex 3 ------
# load file Obs2.xlsx to data frame
# zaladuj plik Obs2.xlsx do ramki danych 


metadata2 = pd.read_excel("D:\\GITHUB\\Python-Postgraduate_studies_on_WSB\\11_2019\\SampleFiles\\Obs2.xlsx")

#---- ex 4 --------------------------
# name columns in data frame loaded in ex 3
# nadaj nazwy kolumn ramce danych zaladowanej z zadania nr 3

metadata2.columns = [ 'Dane', 'Data', 'Value' ]

#----- ex 5 ------
# connect to SampleDb2.db and list all available tables in the database
# podlacz sie do bazy SampleDb2.db oraz wylistuj wszystkie dostepne tablice w bazie

from sqlalchemy import create_engine
from sqlalchemy import inspect

db_uri = 'sqlite:///11_2019//SampleFiles//sampleDB2.db'
engine = create_engine(db_uri)

inspector = inspect(engine)

# Get table information
table_info = inspector.get_table_names()
print(table_info)

# Get column information
column_info = inspector.get_columns('Obs')
column_info2 = inspector.get_columns('Metadane')
print(column_info, "\n", column_info2)

data_column1 = pd.DataFrame(column_info)
