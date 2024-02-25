# -*- coding: utf-8 -*-
"""
Created on Sun Feb 12 20:31:52 2023

@author: insshubh
"""

"""import pandas as pd
data=pd.read_csv('fab_dataset.csv')
data.describe()
data.info()
pci_mean=data["income"].mean()
data["income"].fillna(pci_mean,inplace=True)
age_max=data["age"].max()
data["age"].fillna(age_max,inplace=True)
ds_min=data["service"].min()
data["service"].fillna(ds_min,inplace=True)

#manual encoding

import pandas as pd
data=pd.read_csv('fab_dataset.csv')
data.info()
data["type"].describe()
data["type"].unique()
data.loc[data["type"]=='permanent',"type"]=0
data.loc[data["type"]=='contractual',"type"]=1

#label encoding

import pandas as pd
data=pd.read_csv('fab_dataset.csv')
data["location"].describe()
data["location"].unique()
# data.loc[data["location"]==' Rural ',"location"]='0'
# data.loc[data["location"]==' Urban',"location"]='1'
from sklearn.preprocessing import LabelEncoder
le=LabelEncoder()
data["location"]=le.fit_transform(data["location"])

###one hot encoding

import pandas as pd
data=pd.read_csv('fab_dataset.csv')
data["track"].describe()
data["track"].unique()
from sklearn.preprocessing import OneHotEncoder
oe=OneHotEncoder()
#df=pd.DataFrame([1,2,3])
 
df=pd.DataFrame(oe.fit_transform(data[["track"]]).toarray())
df.columns=['j0','j1']
data=data.join(df)
data.drop("track",axis=1,inplace=True)


#standard scalar

import pandas as pd
data=pd.read_csv('fab_dataset.csv')
ncols=['age','income','service','deasis4']
nudata=data[['age','income']]
from sklearn.preprocessing import StandardScaler
ss=StandardScaler()
ss.fit(nudata)
scaled=ss.transform(nudata)
df1=pd.DataFrame(scaled)
data.drop(['age','income'],axis=1,inplace=True)
df1.columns=['age','income']
data=data.join(df1)



#min-max scalar-normalization


import pandas as pd
data=pd.read_csv('fab_dataset.csv')
nudata2=data[['service','deasis4']]
from sklearn.preprocessing import MinMaxScaler
norm=MinMaxScaler()
norm.fit(nudata2)
scaled2=norm.transform(nudata2)
df2=pd.DataFrame(scaled2)
data.drop(['service','deasis4'],axis=1,inplace=True)
df2.columns=['service','deasis4']
data=data.join(df2)"""




import pandas as pd
data=pd.read_csv('dataset3.csv')
data.describe()
data.info()
data["Model"].describe()
data["Model"].unique()
from sklearn.preprocessing import LabelEncoder
le=LabelEncoder()
data["Model"]=le.fit_transform(data["Model"])

from sklearn.preprocessing import LabelEncoder
le=LabelEncoder()
data["Price"]=le.fit_transform(data["Price"])
data["Status"].describe()
data["Status"].unique()
from sklearn.preprocessing import LabelEncoder
le=LabelEncoder()
data["Status"]=le.fit_transform(data["Status"])

data["Mileage"].describe()
data["Mileage"].unique()
from sklearn.preprocessing import LabelEncoder
le=LabelEncoder()
data["Mileage"]=le.fit_transform(data["Mileage"])

data["MSRP"].describe()
data["MSRP"].unique()
from sklearn.preprocessing import LabelEncoder
le=LabelEncoder()
data["MSRP"]=le.fit_transform(data["MSRP"])

ncols=['Model','Status','Mileage','MSRP']
nudata=data[['Model','Status','Mileage','MSRP']]
from sklearn.preprocessing import StandardScaler
ss=StandardScaler()
ss.fit(nudata)
scaled=ss.transform(nudata)
df1=pd.DataFrame(scaled)
data.drop(['Model','Status','Mileage','MSRP'],axis=1,inplace=True)
df1.columns=['Model','Status','Mileage','MSRP']
data=data.join(df1)

data.drop(['Model'],axis=1,inplace=True)
y=data[["MSRP"]]
x=data.drop(["MSRP"],axis=1)
from sklearn import svm
from sklearn.model_selection import train_test_split
from sklearn import metrics

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)
svm=svm.SVC()
svm.fit(x_train,y_train)
prediction=svm.presict(x_test)
metrics.accuracy_score(y_test,prediction)
metrics.confusion_matrix(y_test,prediction)






















import pandas as pd
data=pd.read_csv('dataset2.csv')
data.describe()
data.info()

data["Profession"].fillna('Engineer',inplace=True)

data.describe()
data.info()


ncols=['CustomerID','Age','Annual Income ($)','Spending Score (1-100)','Work Experience','Family Size']
nudata=data[['CustomerID','Age','Annual Income ($)','Spending Score (1-100)','Work Experience','Family Size']]
from sklearn.preprocessing import StandardScaler
ss=StandardScaler()
ss.fit(nudata)
scaled=ss.transform(nudata)
df1=pd.DataFrame(scaled)
data.drop(['CustomerID','Age','Annual Income ($)','Spending Score (1-100)','Work Experience','Family Size'],axis=1,inplace=True)
df1.columns=['CustomerID','Age','Annual Income ($)','Spending Score (1-100)','Work Experience','Family Size']
data=data.join(df1)

from sklearn.preprocessing import LabelEncoder
le=LabelEncoder()
data["Profession"]=le.fit_transform(data["Profession"])

y=data["Gender"] 
x=data.drop(["Gender"],axis=1)
from sklearn import svm
from sklearn.model_selection import train_test_split
from sklearn import metrics
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=(42))
svm=svm.SVC()
svm.fit(x_train,y_train)
prediction=svm.predict(x_test)
metrics.accuracy_score(y_test,prediction)
metrics.confusion_matrix(y_test,prediction)

import matplotlib.pyplot as plt 
fig,ax =plt.subplots(figsize=(7,5))

ax.set_title("Model")
ax.set_xlabel("X")
ax.set_ylabel("Y")

#values=['CustomerID','Gender','Age','Annual Income ($)','Spending Score (1-100)','Profession',' Work Experience','Family Size']
#names=['Gender']
ax.scatter(y,prediction)

plt.show()
