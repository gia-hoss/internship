#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import seaborn as sns
import numpy as np


# In[2]:


# Import daily_requests.csv file from database
df = pd.read_csv('/Users/zack/Documents/GIA HOANG/HOSS/daily_requests.csv')
df


# In[3]:


# Filter necessary columns
df1= df[['account_id', 'account_name','date','requests']]
df1


# In[4]:


# Replace NA values in "account_name" with its "account_id"
df1._update_inplace= df1['account_name'].fillna(df1['account_id'], inplace= True)
df1


# In[5]:


# Pivot the df1 dataframe to get a desired format
daily_request= df1.pivot_table(index=['account_id','account_name'], columns=['date'], values=['requests'])
daily_request


# In[6]:


# Sort the table by descending requests 
daily_request['total_request']= daily_request.sum(axis= 1)
daily_request_sorted= daily_request.sort_values(by= ['total_request'], ascending= False)
daily_request_sorted


# In[7]:


# Hightlight the result with color palette
cm = sns.light_palette('green', as_cmap=True)
table = daily_request_sorted.style.background_gradient(cmap=cm).highlight_null(null_color='white').format('{0:,.0f}',na_rep= '').set_caption('No. of daily request by Account').set_table_styles([{
    'selector': 'caption',
    'props': [('color', 'black'), ('font-size', '18px')]}])\
.set_properties(**{'border-color': 'black','text-align': 'center','border-width':'thin','border-style':'dotted'})
table


# In[ ]:




