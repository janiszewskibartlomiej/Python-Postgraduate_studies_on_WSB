# -*- coding: utf-8 -*-


import numpy as np 
import pandas as pd 
import patsy
import statsmodels.api as sm
from sklearn.metrics import confusion_matrix
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
#import statsmodels.formula.api as smf
#from sklearn.linear_model import LogisticRegression
#from sklearn import linear_model


#----- load data ------ 

train_df = pd.read_csv('C:/Users/U0173627/Documents/Workspace/WSB/ML_workshop/Case1/train.csv')
test_df = pd.read_csv('C:/Users/U0173627/Documents/Workspace/WSB/ML_workshop/Case1/test.csv')

train_df.head()

test_df.head()


#----- prepare data ------- 
train_df.describe(include='all')
train_df.info()

test_df.describe(include='all')
test_df.info()

#make data categorical / factor
train_df["Sex"] = train_df["Sex"].astype('category')
train_df["CarBrand"] = train_df["CarBrand"].astype('category')
train_df["CarType"] = train_df["CarType"].astype('category')
train_df["NextAccident"] = train_df["NextAccident"].astype('category')

test_df["Sex"] = test_df["Sex"].astype('category')
test_df["CarBrand"] = test_df["CarBrand"].astype('category')
test_df["CarType"] = test_df["CarType"].astype('category')
test_df["NextAccident"] = test_df["NextAccident"].astype('category')


# prepare variables
f = 'C(NextAccident) ~ BirthYear + C(Sex) + LicenseYear + C(CarBrand) + C(CarType) + CarYear + CarEngine + EngineCap + CarValue + AssistanceYears + Accidents '
y, X = patsy.dmatrices(f, train_df, return_type='dataframe')

y = y.iloc[:,0]


#----- build model(s) ------
from sklearn.feature_selection import mutual_info_classif
from sklearn.feature_selection import f_classif

# variables importance
mutual_information = mutual_info_classif(X, y)
colnames = np.asarray(list(X))


classif = f_classif(X, y)
classif1 = np.asarray(classif[1])
print(classif[1])


test1 = {
        'Vars' : colnames, 
        'mutual_info' : mutual_information,
        'F-score_pvalue': classif[1]
        }

fs = pd.DataFrame(test1)
fs = fs.round({'F-score_pvalue': 4})
fs = fs[['Vars', 'mutual_info', 'F-score_pvalue']]
print(fs)

### GLM MODEL
 


model = sm.Logit(y, X).fit()

# check model summary
print(sm.Logit(y, X).fit().summary())

accuracy_table = model.pred_table()
print(accuracy_table)
print("Accuracy:", np.diag(accuracy_table).sum()/accuracy_table.sum())



# validate with test

y_test, X_test = patsy.dmatrices(f, test_df, return_type='dataframe')
y_test = y_test.iloc[:,0]


pred_test = model.predict(X_test)

pred_test1 = np.where(pred_test < 0.5 , '0', '1')



y_test1 = np.where(y_test == 1 , '1', '0')
results = confusion_matrix(y_test1, pred_test1)


print(results)
print("Accuracy:", np.diag(results).sum()/results.sum())







### TREE MODEL


clf_gini = DecisionTreeClassifier(criterion = "gini")

model = clf_gini.fit(X, y)



# validate with test
	
Results_tree = clf_gini.predict(X_test)

accuracy_score(y_test,Results_tree)







### RANDOM FOREST

from sklearn.ensemble import RandomForestClassifier
clf=RandomForestClassifier(n_estimators=100)


clf.fit(X, y)

Results_RF =clf.predict(X_test)


accuracy_score(y_test,Results_RF)












