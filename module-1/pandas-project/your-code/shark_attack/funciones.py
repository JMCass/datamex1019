import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
import re
import seaborn as sns
sns.set(style="whitegrid")
sns.set_color_codes("pastel")
from collections import Counter
from gensim import corpora, models
import pylab as plt


data = pd.read_csv('./attacks.csv')

data_country = data["Country"].value_counts()

data_area = data["Area"].value_counts()

data_location = data["Location"].value_counts()

data_name = data["Name"].value_counts()

data_age = data["Age"].value_counts()

data_injury = data["Injury"].value_counts()

data_species = data["Species "].value_counts()


data[['href']] = data[['href']].fillna('href formula')
data["href"].value_counts()

data[['href formula']] = data[['href formula']].fillna('http://sharkattackfile.net/spreadsheets/pdf_directory/1975.01.19-Barrowman.pdf')


data[['Country', 'Area', 'Location']]= data[['Country', 'Area', 'Location']].fillna('UNKNOWN')

#Limpiando los valores de Country
data['Country'] = data['Country'].astype('str')
data["Country"] = data["Country"].str.rstrip()
data["Country"] = data["Country"].str.lstrip()

#Limpiando los valores de Country
data['Country'] = data['Country'].str.replace('Fiji','FIJI')
data['Country'] = data['Country'].str.replace('St Helena','ST HELENA')
data['Country'] = data['Country'].str.replace('Sierra Leone','SIERRA LEONE')
data['Country'] = data['Country'].str.replace('Seychelles','SEYCHELLES')
data['Country'] = data['Country'].str.replace('?', '')
data['Country'] = data['Country'].str.replace('-', '')
data['Country'] = data['Country'].str.replace('Coast of AFRICA','COAST OF AFRICA')
data['Country'] = data['Country'].str.replace('EGYPT / ISRAEL','EGYPT')
data['Country'] = data['Country'].str.replace('RED SEA / INDIAN OCEAN','YEMEN')
data['Country'] = data['Country'].str.replace('ANDAMAN / NICOBAR ISLANDAS','INDIA')
data['Country'] = data['Country'].str.replace('EQUATORIAL GUINEA / CAMEROON','EQUATORIAL GUINEA')
data['Country'] = data['Country'].str.replace('IRAN / IRAQ','IRAN')
data['Country'] = data['Country'].str.replace('ITALY / CROATIA','CROATIA')
data['Country'] = data['Country'].str.replace('SOLOMON ISLANDS / VANUATU','SOLOMON ISLANDS')
data['Country'] = data['Country'].str.replace('UNITED ARAB EMIRATES (UAE)','UNITED ARAB EMIRATES')
data['Country'] = data['Country'].str.replace(' (UAE)','')
data['Country'] = data['Country'].str.replace(' (SRI LANKA)','')
data['Country'] = data['Country'].str.replace('CEYLON \(SRI LANKA\)','SRI LANKA')
data['Country'] = data['Country'].str.replace('Between PORTUGAL & INDIA','PORTUGAL')
data["Country"] = data["Country"].str.replace("ST. MAARTIN","SAINT MARTIN")
data["Country"] = data["Country"].str.replace("ST. MARTIN","SAINT MARTIN")
data["Country"] = data["Country"].str.replace("COLUMBIA","COLOMBIA")
data["Country"] = data["Country"].str.replace("UNITED ARAB EMIRATES \(UAE\)","UNITED ARAB EMIRATES")
data["Country"] = data["Country"].str.replace("ENGLAND","UNITED KINGDOM")
data["Country"] = data["Country"].str.replace("SCOTLAND","UNITED KINGDOM")
data["Country"] = data["Country"].str.replace("(.*)\?","UNKNOWN")
data["Country"] = data["Country"].str.replace("Trinidad & Tobago","TRINIDAD AND TOBAGO")
data["Country"] = data["Country"].str.replace("^(New Guinea)","PAPUA NEW GUINEA")
data["Country"] = data["Country"].str.replace("New Britain","APUA NEW GUINEA")

#Limpiando la columna de la edad
data['Age']= data['Age'].str.replace('N/A', 'UNKNOWN')
data['Age']= data['Age'].str.replace('X', 'UNKNOWN')
data['Age']= data['Age'].str.replace('†', 'UNKNOWN')
data['Age']= data['Age'].str.replace('† ', 'UNKNOWN')
data['Age']= data['Age'].str.replace('MAKE LINE GREEN', 'UNKNOWN')
data['Age']= data['Age'].str.replace('A.M.', 'UNKNOWN')
data['Age']= data['Age'].str.replace('--', 'UNKNOWN')
data.loc[data.Age=='60s', 'Age'] = '60'
data.loc[data.Age=="60's", 'Age'] = '60'
data.loc[data.Age=='50s', 'Age'] = '50' 
data.loc[data.Age=='40s', 'Age'] = '40'
data.loc[data.Age=='30s', 'Age'] = '30' 
data.loc[data.Age=='20s', 'Age'] = '20' 
data.loc[data.Age=='Teen', 'Age'] = '15'
data.loc[data.Age== 'teen', 'Age'] = '15'
data.loc[data.Age=='Teens', 'Age'] = '15'
data.loc[data.Age=='18 months', 'Age'] = '1'
data.loc[data.Age=='M', 'Age'] = 'UNKNOWN'
data.loc[data.Age=='F', 'Age'] = 'UNKNOWN'
data.loc[data.Age== 'mid-30s', 'Age'] = '35'
data.loc[data.Age=='28 & 26', 'Age'] = '27'
data.loc[data.Age=='18 or 20', 'Age'] = '19'
data.loc[data.Age=='12 or 13', 'Age'] = '13'
data.loc[data.Age=='46 & 34', 'Age'] = '40'
data.loc[data.Age=='28, 23 & 30', 'Age'] = '27'
data.loc[data.Age=='30 or 36', 'Age'] = '33'
data.loc[data.Age=='6½', 'Age'] = '6'
data.loc[data.Age=='23 & 20', 'Age'] = '21'
data.loc[data.Age=='8 or 10', 'Age'] = '9'
data.loc[data.Age=='7      &    31', 'Age'] = '31'
data.loc[data.Age=='20?', 'Age'] = '20'
data.loc[data.Age=='21 & ?', 'Age'] = '21'
data.loc[data.Age=='36 & 26', 'Age'] = '31'
data.loc[data.Age=='32 & 30', 'Age'] = '31'
data.loc[data.Age=='33 or 37', 'Age'] = '35'
data.loc[data.Age=='16 to 18', 'Age'] = '17'
data.loc[data.Age=='13 or 18', 'Age'] = '15'
data.loc[data.Age==' ', 'Age'] = 'UNKNOWN'
data.loc[data.Age==' 30', 'Age'] = '30'
data.loc[data.Age=='mid-20s', 'Age'] = '25'
data.loc[data.Age=='18 to 22', 'Age'] = '20'
data.loc[data.Age=='Ca. 33', 'Age'] = '33'
data.loc[data.Age=='74 ', 'Age'] = '74'
data.loc[data.Age=='45 ', 'Age'] = '45'
data.loc[data.Age=='21 or 26', 'Age'] = '24'
data.loc[data.Age=='20 ', 'Age'] = '20'
data.loc[data.Age=='>50', 'Age'] = '51'
data.loc[data.Age=='>50', 'Age'] = '51'
data.loc[data.Age=='9 & 12', 'Age'] = '11'
data.loc[data.Age=='? & 19', 'Age'] = '19'
data.loc[data.Age=='9 months', 'Age'] = '1'
data.loc[data.Age=='25 to 35', 'Age'] = '30'
data.loc[data.Age=='23 & 26', 'Age'] = '24'
data.loc[data.Age=='33 & 37', 'Age'] = '35'
data.loc[data.Age=='25 or 28', 'Age'] = '27'
data.loc[data.Age=='37, 67, 35, 27,  ? & 27', 'Age'] = '39'
data.loc[data.Age=='21, 34,24 & 35', 'Age'] = '30'
data.loc[data.Age=='30 & 32', 'Age'] = '31'
data.loc[data.Age=='50 & 30', 'Age'] = '40'
data.loc[data.Age=='17 & 35', 'Age'] = '26'
data.loc[data.Age=='34 & 19', 'Age'] = '26'
data.loc[data.Age=='2 to 3 months', 'Age'] = '0'
data.loc[data.Age=='7 or 8', 'Age'] = '7'
data.loc[data.Age=='17 & 16', 'Age'] = '16'
data.loc[data.Age=='Both 11', 'Age'] = '11'
data.loc[data.Age=='13 or 14', 'Age'] = '13'
data.loc[data.Age=='2½', 'Age'] = '2'
data.loc[data.Age==' 43', 'Age'] = '43'
data.loc[data.Age=='9 or 10', 'Age'] = '10'
data.loc[data.Age=='36 & 23', 'Age'] = '30'
data.loc[data.Age=='  ', 'Age'] = 'UNKNOWN'
data.loc[data.Age=='10 or 12', 'Age'] = '10'
data.loc[data.Age=='?    &   14', 'Age'] = '14'
data.loc[data.Age=='31 or 33', 'Age'] = '32'
data.loc[data.Age=='Elderly', 'Age'] = '70'
data.loc[data.Age=='(adult)', 'Age'] = '40'
data.loc[data.Age=='adult', 'Age'] = '40'
data.loc[data.Age=='"middle-age"', 'Age'] = '50'
data.loc[data.Age=='"young"', 'Age'] = '20'
data.loc[data.Age=='young', 'Age'] = '20'
data['Age'].fillna(0, inplace=True)