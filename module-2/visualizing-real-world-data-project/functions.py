
# coding: utf-8

# In[1]:


from folium import plugins
import pymongo
import pandas as pd
import numpy as np
from pandas.io.json import json_normalize
from pymongo import MongoClient


# In[2]:


client=MongoClient()
db=client.companies


# In[ ]:


coordenadas=[]
for i in range(len(data_cat1.offices)):
    coordenadas.append((data_cat1.offices[i][0]['latitude'],data_cat1.offices[i][0]['longitude']))

coordenadas_t=[]
for i in range(len(data_cat2.offices)):
    coordenadas_t.append((data_cat2.offices[i][0]['latitude'],data_cat2.offices[i][0]['longitude']))
    
coordenadas_t_t=[]
for i in range(len(data_cat3.offices)):
    coordenadas_t_t.append((data_cat3.offices[i][0]['latitude'],data_cat3.offices[i][0]['longitude']))

coordenadastt=[]
for i in range(len(data_cat4.offices)):
    coordenadastt.append((data_cat4.offices[i][0]['latitude'],data_cat4.offices[i][0]['longitude']))
    
coordenadasttt=[]
for i in range(len(data_cat5.offices)):
    coordenadastt.append((data_cat5.offices[i][0]['latitude'],data_cat5.offices[i][0]['longitude']))         


# In[ ]:


for e in coordenadas:
    folium.CircleMarker([e[0], e[1]], radius=2, icon=folium.Icon(),color = 'green').add_to(mapa)
    
for e in coordenadas_t:
    folium.CircleMarker([e[0], e[1]], radius=2, icon=folium.Icon(),color = 'red').add_to(mapa)
    
for e in coordenadas_t_t:
    folium.CircleMarker([e[0], e[1]], radius=2, icon=folium.Icon(),color = 'orange').add_to(mapa)

for e in coordenadastt:
    folium.CircleMarker([e[0], e[1]], radius=2, icon=folium.Icon(),color = 'blue').add_to(mapa)
    
for e in coordenadasttt:
    folium.CircleMarker([e[0], e[1]], radius=2, icon=folium.Icon(),color = 'yellow').add_to(mapa)            


# In[3]:


def get_first(data):
    res=[]
    ofi=[]
    
    data=data['offices']
    for e in data:
        principal=None   
        if e[0]['latitude'] and e[0]['longitude']:
            principal={'type':'Point',
                       'coordinates':[
                           e[0]['longitude'],
                           e[0]['latitude']
                       ]}
            
        ofi.append(principal)
        
        res.append({
            'total_offices':len(e),
            'lat':e[0]['latitude'],
            'lng':e[0]['longitude'],
            'oficina_principal':principal
        })
    
    return res, ofi


# In[4]:


def find_near(geopoint, radio=1000):
    return db.first_office.find({
        'oficina_principal':{'$near':{'$geometry':geopoint,
                                     '$maxDistance':radio}
            
        }
    }
    )


# In[ ]:


for i in range(len(lat_clt)):
    folium.CircleMarker(
        location=[float(lat_clt[i]), float(lon_clt[i])],
        radius = 2,
        color = '#3186cc',
        fill=True,
        fill_color= '#3186cc'
    ).add_to(map2)

