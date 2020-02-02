# -*- coding: utf-8 -*-



import numpy as np 
import pandas as pd 
import patsy
from sklearn.model_selection import train_test_split
import statsmodels.api as sm
from sklearn.metrics import confusion_matrix
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier


#----- load data ------ 

clients_df = pd.read_csv('C:/Users/U0173627/Documents/Workspace/WSB/ML_workshop/Case2/clients.txt', 
                           sep = ',',
                           encoding = 'iso8859_13')

clients_df.head()
list(clients_df)

#----- prepare data ------- 
clients_df.describe(include='all')
clients_df.info()

clients_df["wyksztalcenie"] = clients_df["wyksztalcenie"].astype('category')
clients_df["miejsce"] = clients_df["miejsce"].astype('category')
clients_df["wojewodztwo"] = clients_df["wojewodztwo"].astype('category')


# choose variables 
f2 = 'C(zakup) ~ wiek + C(plec) + C(wyksztalcenie) + C(miejsce) + kwota + C(wojewodztwo) + C(wysylka_oferty)'
y2, X2 = patsy.dmatrices(f2, clients_df, return_type='dataframe')

y2 = y2.iloc[:,1]


X_train2, X_test2, y_train2, y_test2 = train_test_split(X2, y2, test_size=0.3) # 70% training and 30% test




#----- build model(s) ------
from sklearn.feature_selection import mutual_info_classif
from sklearn.feature_selection import f_classif

# variables importance
mutual_information2 = mutual_info_classif(X_train2, y_train2)
colnames2 = np.asarray(list(X_train2))





classif2 = f_classif(X_train2, y_train2)
classif12 = np.asarray(classif2[1])
print(classif2[1])



test2 = {
        'Vars' : colnames2, 
        'mutual_info' : mutual_information2,
        'F-score_pvalue': classif2[1]
        }

fs2 = pd.DataFrame(test2)
fs2 = fs2.round({'F-score_pvalue': 4})
fs2 = fs2[['Vars', 'mutual_info', 'F-score_pvalue']]
print(fs2)



### GLM MODEL

# check model summary




model = sm.Logit(y2, X2).fit()

# check model summary
print(sm.Logit(y2, X2).fit().summary())

# predict
accuracy_table = model.pred_table()

print(accuracy_table)
print("Accuracy:", np.diag(accuracy_table).sum()/accuracy_table.sum())





# predict test data
pred_test2 = model.predict(X_test2)

pred_test22 = np.where(pred_test2 < 0.6 , '0', '1')


y_test22 = np.where(y_test2 == 1 , '1', '0')


# validate with test
results = confusion_matrix(y_test22, pred_test22)


print(results)
print("Accuracy:", np.diag(results).sum()/results.sum())











### TREE MODEL


clf_gini = DecisionTreeClassifier(criterion = "gini")

model = clf_gini.fit(X2, y2)




Results_tree2 = clf_gini.predict(X_test2)

# validate with test
accuracy_score(y_test2, Results_tree2)







### RANDOM FOREST



clf=RandomForestClassifier(n_estimators=100)


	
clf.fit(X_train2, y_train2)


# predict test
Results_RF2 =clf.predict(X_test2)

# validate with test
accuracy_score(y_test2,Results_RF2)









