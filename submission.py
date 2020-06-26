#Data  preprocessing

#importing libraries 
#location,pension feature engineering
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')


#Importing The dataset_train

dataset_train=pd.read_csv('train.csv')


print(dataset_train.head)
dataset_train.shape
dataset_train.info()
dataset_train.count(axis=0, level=None, numeric_only=False)
print(dataset_train['employer'].value_counts())

# handling Null Values
#------------------------------------------------------------------------------
print(dataset_train.isnull().sum())
#filling Lump_sum_pay by 0
dataset_train['lump_sum_pay']=dataset_train['lump_sum_pay'].fillna(0)
#Analysing and filling null value of retirement_cost_covered by 0
print(dataset_train.retirement_cost_covered.describe())
dataset_train['retirement_cost_covered']=dataset_train['retirement_cost_covered'].fillna(0)


dataset_train=dataset_train.drop(['pension', 'location'], axis=1)
print(dataset_train.isnull().sum())
#------------------------------------------------------------------------------
#Label encoding on employer
dataset_train.info()
print(dataset_train['employer'].value_counts())
from sklearn.preprocessing import LabelEncoder
labelencoder=LabelEncoder();
dataset_train['employer']=labelencoder.fit_transform(dataset_train['employer'])



#dropping Employee URL
dataset_train=dataset_train.drop(['employer_url'], axis=1)
#DOB extracting years
dataset_train.info()
from datetime import datetime
dataset_train['DOB'] = pd.to_datetime(dataset_train['DOB'])
dataset_train['Month'] = dataset_train['DOB'].dt.month
dataset_train['year']=dataset_train['DOB'].dt.year
dataset_train=dataset_train.drop(['DOB'], axis=1)
dataset_train.info()
print(dataset_train)
#drop id
dataset_train=dataset_train.drop(['Id'], axis=1)
print(dataset_train.head())
Y = dataset_train["total_wages"]
X = dataset_train.drop(["total_wages"],axis=1)

from sklearn.ensemble import RandomForestRegressor
lr = RandomForestRegressor()
lr.fit(X,Y)

#------------------------------test-------------------------------------------------------
dataset_test=pd.read_csv('test.csv')


print(dataset_test.head)
dataset_test.shape
dataset_test.info()
dataset_test.count(axis=0, level=None, numeric_only=False)
print(dataset_test['employer'].value_counts())

# handling Null Values
#------------------------------------------------------------------------------
print(dataset_test.isnull().sum())
#filling Lump_sum_pay by 0
dataset_test['lump_sum_pay']=dataset_test['lump_sum_pay'].fillna(0)
#Analysing and filling null value of retirement_cost_covered by 0
print(dataset_test.retirement_cost_covered.describe())
dataset_test['retirement_cost_covered']=dataset_test['retirement_cost_covered'].fillna(0)


dataset_test=dataset_test.drop(['pension', 'location'], axis=1)
print(dataset_test.isnull().sum())
#------------------------------------------------------------------------------
#Label encoding on employer
dataset_test.info()
print(dataset_test['employer'].value_counts())
from sklearn.preprocessing import LabelEncoder
labelencoder=LabelEncoder();
dataset_test['employer']=labelencoder.fit_transform(dataset_test['employer'])

#dropping Employee URL
dataset_test=dataset_test.drop(['employer_url'], axis=1)
#DOB extracting years
dataset_test.info()
dataset_test['DOB'] = pd.to_datetime(dataset_test['DOB'])
dataset_test['Month'] = dataset_test['DOB'].dt.month
dataset_test['year']=dataset_test['DOB'].dt.year
dataset_test=dataset_test.drop(['DOB'], axis=1)
dataset_test.info()
print(dataset_test)
#drop id
Id = dataset_test['Id']
dataset_test=dataset_test.drop(['Id'], axis=1)
print("---------------------------Final test dataset---------------------------------------------")
print(dataset_test)
dataset_test.to_csv("prepros.csv")
print("------------------------------------------------------------------------")

prediction_test=lr.predict(dataset_test)
my_solution=pd.DataFrame(prediction_test,Id,columns=["total_wages"])
print(my_solution.shape)
my_solution.to_csv("tanishq.csv",index_label=["Id"])


#---------------------------------------------------------------------------
import pickle

# Saving model to disk
pickle.dump(lr, open('model.pkl','wb'))

# Loading model to compare the results
model = pickle.load(open('model.pkl','rb'))
print(model.predict([[15,49512,66192,0,0,2576.11,0,0,4,1963]]))

