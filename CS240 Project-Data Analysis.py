#!/usr/bin/env python
# coding: utf-8

# In[4]:


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


# In[5]:


rawData = pd.read_csv('google_video.csv')


# In[139]:


print(rawData)
print("(rows,columns):",rawData.shape)


# In[140]:


X = rawData.iloc[:,:86].values
Y = rawData.iloc[:,86].values.reshape((1716,1))
print(X)
print('---------------------------------------------')
print(Y)


# In[41]:


# Category and Application protocol
X_category_AppProtocol = X[:,84:86]
X_category = X_category_AppProtocol[:,0]
X_category = X_category.reshape(X_category.shape[0],1)

X_appProtocol = X_category_AppProtocol[:,1]
X_appProtocol = X_appProtocol.reshape(X_appProtocol.shape[0],1)

print(X_category_AppProtocol)


# In[37]:


# plot category
plt.style.use('seaborn')
x_category_labels = np.unique(X_category)
fig, ax = plt.subplots(figsize=(15,5))

ax.hist(X_category,rwidth=0.5,bins=np.arange(-0.5,len(x_category_labels)),edgecolor='black')

plt.show()


# In[133]:


# plot what app protocols the network traffic use
x_network_appProtocol = X_category_AppProtocol[np.where(X_category_AppProtocol[:,0] == 'Network')]
x_network_appProtocol = x_network_appProtocol[:,1]
x_network_appProtocol = x_network_appProtocol.reshape(x_network_appProtocol.shape[0],1)
x_network_app_labels = np.unique(x_network_appProtocol)



fig, ax = plt.subplots(figsize=(15,5))

ax.hist(x_network_appProtocol,rwidth=0.05,bins=np.arange(-0.5,len(x_network_app_labels)),edgecolor='black')
ax.set_title("Network Traffic",fontsize=15)
plt.show()


# In[137]:


# plot what app protocols the web traffic use
x_network_appProtocol = X_category_AppProtocol[np.where(X_category_AppProtocol[:,0] == 'Web')]
x_network_appProtocol = x_network_appProtocol[:,1]
x_network_appProtocol = x_network_appProtocol.reshape(x_network_appProtocol.shape[0],1)
x_network_app_labels = np.unique(x_network_appProtocol)


fig, ax = plt.subplots(figsize=(15,5))

ax.hist(x_network_appProtocol,rwidth=0.3,bins=np.arange(-0.5,len(x_network_app_labels)),edgecolor='black')
ax.set_title("Web Traffic",fontsize=15)
plt.show()


# In[ ]:




