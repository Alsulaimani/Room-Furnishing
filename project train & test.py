#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
import numpy
import pandas
import seaborn as sns


# In[2]:


#load the data
df=pandas.read_csv('Data.csv')

#split the lables from the features
lable=df[['Image1','Image2']]
features=df.drop(['Image1','Image2'], axis=1, inplace=True)
#convert features to matrix
features= df.as_matrix()


# In[3]:


#conver lables to matrix
lable=lable.as_matrix()


# In[4]:


#checking the shape of the features
features.shape


# In[5]:


#checking the shape of the lables
lable.shape


# In[6]:


#split the data to train and test
from sklearn.model_selection import train_test_split
xtrain,xtest,ytrain,ytest=train_test_split(features,lable,test_size=0.2)


# In[7]:


#train the model with decision tree
from sklearn.tree import DecisionTreeClassifier
model=DecisionTreeClassifier(criterion='gini', max_depth=5, 
                              min_samples_leaf=3, min_samples_split=7, max_leaf_nodes=10)
model.fit(xtrain,ytrain)


# In[8]:


#visulaize the tree tree
import graphviz 
from sklearn import tree
fnames=['Age', 'Gender', 'Type', 'Style', 'Material', 'Elemnt','ArtWork']
cnames=['Image1','Image2']
dot_data= tree.export_graphviz(model,out_file=None, feature_names=fnames, class_names=cnames,
                              rounded=True, filled=True)
graph=graphviz.Source(dot_data)
graph


# In[9]:


#preformance analysis of Machine Learning model 
ypred=model.predict(xtest) #feeding xtest to model and getting the corresponding prediction
from sklearn.metrics import accuracy_score
accuracy_score(ytest,ypred)


# In[10]:


#save the model
from sklearn.externals import joblib
joblib.dump(model, 'model.pkl')


# In[ ]:




