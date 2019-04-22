#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas
def create_dataframe():
    #name the columns
    col=['Age', 'Gender', 'Type', 'Style', 'material', 'elemnt','ArtWork']
    #create dataframe and push column names
    df=pandas.DataFrame(columns=col)
    #save the dataframe
    df.to_csv("Data.csv",index=False)
    
if __name__=="__main__": 
    create_dataframe()

