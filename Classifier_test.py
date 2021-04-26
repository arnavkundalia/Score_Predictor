import sklearn as skl
import pandas as pd
import numpy as np
dataset=pd.read_csv('PREPROCCESED40.csv')
x=dataset.iloc[:,6:10].values
y=dataset.iloc[:,10]
from sklearn.preprocessing import LabelEncoder
labelencoder_y=LabelEncoder()
y=labelencoder_y.fit_transform(y)
from sklearn.metrics import confusion_matrix

from sklearn.model_selection import train_test_split
x_train, x_test,y_train,y_test=train_test_split(x,y,test_size=0.2)
from sklearn.neighbors import KNeighborsClassifier
classifier_knn=KNeighborsClassifier(n_neighbors=5,metric='minkowski',p=2)
classifier_knn.fit(x_train,y_train)
y_pred=classifier_knn.predict(x_test)
print(y_pred)
b=confusion_matrix(y_test,y_pred)
print(b)
def accuracy(mat):
    daigonal=np.trace(b)
    tot_arr=np.sum(b)
    acc=((daigonal/tot_arr)*100)
    return acc
print(" the accuracy of the current model is ",accuracy(b))