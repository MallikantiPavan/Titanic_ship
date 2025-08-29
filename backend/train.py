import numpy as np
import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
import joblib

train=pd.read_csv(r'C:\Users\pavan\Downloads\Titanic-Dataset (2).csv')
#test=pd.read_csv('/kaggle/input/titanic/test.csv')

train['Age']=train['Age'].fillna(train['Age'].median())
train['Embarked']=train['Embarked'].fillna(train['Embarked'].mode()[0])

# test['Age']=test['Age'].fillna(test['Age'].median())
# test['Fare']=test['Fare'].fillna(test['Fare'].median())

train=train.drop(['Cabin'],axis=1)
# test=test.drop(['Cabin'],axis=1)

drop_cols=['Name','Ticket','PassengerId']

train=train.drop(columns=drop_cols)
# test_df=test.drop(columns=drop_cols)

train=pd.get_dummies(train,columns=['Sex','Embarked'],drop_first=True) #get_dummies create new columns for categorical data
# test_cat=pd.get_dummies(test,columns=['Sex','Embarked'],drop_first=True)

# test_cat = test_cat.reindex(columns=train.drop("Survived", axis=1).columns, fill_value=0)

x=train.drop(['Survived'],axis=1)
y=train['Survived']

x_train,x_test,y_train,y_test=train_test_split(x,y,random_state=42)

# model=RandomForestClassifier(n_estimators=1000,random_state=0)
model=LogisticRegression(class_weight='balanced',max_iter=500)
model.fit(x_train,y_train)

joblib.dump(model,'titanic_model.pkl')
print("model_saved")
