#!/usr/bin/env python
# coding: utf-8

# In[1]:


import geopandas as gpd
import matplotlib.pyplot as plt
import  numpy as np


# In[2]:


shapefile_path = "C:\data\ParcelsWithZoning\ParcelsWithZoning.shp"


# In[3]:


gdf = gpd.read_file(shapefile_path)


# In[4]:


fig,ax = plt.subplots(figsize=(10,10))
gdf.plot(ax=ax, column = "Zoning")


# In[ ]:




