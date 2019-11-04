# -*- coding: utf-8 -*-

##########
# PART 2 #
##########
import pandas as pd
import os

# set working directory




#---- load csv ----



#---- load txt ----



#--- load xls(x) ----


#---- db connection -----
# sample tutorial: https://www.pythonsheets.com/notes/python-sqlalchemy.html

from sqlalchemy import create_engine

 
## SQLite


# STEP 1: connect to db

# STEP 2: Declare what to retrive from db. SQL query


# STEP 3a: Connect to db and retrive data (write own query)

# STEP 3b: Connect to db and retrive data (get whole table)

# Write data to DB
#new_df.to_sql('Obs', engine)




#### OTHER CONNECTIONS

engine = create_engine('postgresql://username:password@localhost:5432/mydatabase')
engine = create_engine('mysql+mysqldb://username:password@localhost/foo')
engine = create_engine('oracle://username:password@127.0.0.1:1521/sidname')
engine = create_engine('mssql+pyodbc://mydsn')
engine = create_engine('sqlite:///foo.db')
# or absolute, starting with a slash:
engine = create_engine('sqlite:////absolute/path/to/foo.db')



#---- load xml / html ----
### from link
url = 'http://www.fdic.gov/bank/individual/failed/banklist.html'
get_web_page = pd.read_html(url)
df_from_page = get_web_page[0]

### from file 

#import pandas as pd 
import xml.etree.ElementTree as et 
    
xtree = et.parse("SampleFiles//sampleXML.xml")
xroot = xtree.getroot() 

df_cols = ["TITLE", "ARTIST", "COUNTRY", "COMPANY", "PRICE", "YEAR"]
out_df = pd.DataFrame(columns = df_cols)

for node in xroot: 
    s_title = node.find("TITLE").text
    s_artist = node.find("ARTIST").text
    s_country = node.find("COUNTRY").text
    s_company = node.find("COMPANY").text
    s_price = node.find("PRICE").text
    s_year = node.find("YEAR").text
    
    out_df = out_df.append(pd.Series([s_title, s_artist, s_country,s_company, s_price, s_year], 
                                     index = df_cols), 
                           ignore_index=True)

    


	
#---- load json -----
df_json = pd.read_json("SampleFiles//sampleJSON.json")
    
#tst = df_json.loc[0, 'dogs']
#tst2 = pd.DataFrame.from_dict(tst, orient ='index').T

def my_apply(x):
    output = pd.DataFrame.from_dict(x, orient ='index').T
    return(output.iloc[0])

result = pd.DataFrame()
for column in df_json.columns:
    new_df = df_json[column].apply(my_apply)
    result = result.append(new_df)
    
result = result.reset_index()
result = result.iloc[:, 2:4]
#tst3 = df_json['dogs'].apply(my_apply)



