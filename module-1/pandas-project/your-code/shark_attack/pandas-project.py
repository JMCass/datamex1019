from funciones import *

import pandas as pd
import numpy as np
###################################################################
print(data.head())

data = data.drop('Unnamed: 22', axis=1)

data = data.drop('Unnamed: 23', axis=1)

data = data.rename(columns={'Fatal (Y/N)': 'Fatal'})

data = data.rename(columns={'Sex ': 'Sex'})

data = data.rename(columns={'Species ': 'Species'})

data = data.rename(columns={'original order': 'Order'})

data = data.rename(columns={'Investigator or Source': 'Investigator'})

print(data.Country.unique())
print(data['Country'].value_counts())

print(data['Fatal'].value_counts())
#####################################################################
#Limpiando la columna de los ataques
data['Fatal']= data['Fatal'].fillna('UNKNOWN')
data.loc[data["Fatal"] == " N", "Fatal"] = "N"
data.loc[data["Fatal"] == "N ", "Fatal"] = "N"
data.loc[data["Fatal"] == "n", "Fatal"] = "N"
data.loc[data["Fatal"] == "F", "Fatal"] = "Y"
data.loc[data["Fatal"] == "#VALUE!", "Fatal"] = "UNKNOWN"
data.loc[data["Fatal"] == "--M524--M3133Y", "Fatal"] = "UNKNOWN"

def clean_fatal(fatal):
    if fatal == 'N' or fatal == 'Y':
        return fatal
    else:
        return 'UNKNOWN'

data['Fatal'] = data['Fatal'].apply(clean_fatal)

fatal_vals = data['Fatal'].value_counts().tolist()
######################################################################
f, ax = plt.subplots(figsize=(5, 5))

labels = ['N', 'Y', 'U']
colors = ['#E7E7E7', '#B4E1F6', '#EBF4F7']

plt.pie(fatal_vals, labels=labels, colors=colors,
        autopct='%1.1f%%', startangle=90)
 
axis = plt.axis('equal')
#####################################################################
#Limpiando la columna del sexo
data[['Sex']]= data[['Sex']].fillna('UNKNOWN')
data['Sex']= data['Sex'].str.replace('lli', 'UNKNOWN')
data['Sex']= data['Sex'].str.replace('.', 'UNKNOWN')
data['Sex']= data['Sex'].str.replace('M ', 'M')

def clean_sex(sex):
    if sex == 'M' or sex == 'F':
        return sex
    else:
        return 'UNKNOWN'
#####################################################################
data['Sex'] = data['Sex'].apply(clean_sex)

print(data['Sex'].value_counts())

sex_vals = data['Sex'].value_counts().tolist()
##########################################################################
f, ax = plt.subplots(figsize=(5, 5))

labels = ['M', 'F', 'U']
colors = ['#E7E7E7', '#B4E1F6', '#EBF4F7']

plt.pie(sex_vals, labels=labels, colors=colors,
        autopct='%1.1f%%', startangle=90)

axis = plt.axis('equal')
#####################################################################
def clean_age(age):
    try:
        age = int(age)
    except ValueError:
        age = 0
    if (age > 0 and age <= 100):
        return age
    else:
        return np.nan

data['Age'] = data['Age'].apply(clean_age)

print(data.Age.unique())

print(data['Age'].value_counts())
#################################################################
fig, ax = plt.subplots(figsize=(8, 6))

sns.distplot(data['Age'].dropna(), hist_kws={"alpha": 1, "color": "#295A83"}, kde=False, bins=15)

ax = ax.set(ylabel="Count", xlabel="Age")

data['Age'].fillna('UNKNOWN', inplace=True)
########################################################################
#Limpiando la columna de las actividades
data[['Activity']]= data[['Activity']].fillna('UNKNOWN')
data['Activity']= data['Activity'].str.replace('.', 'UNKNOWN')

def clean_act(x):
    if isinstance(x, str):
        x = x.lower()
        if 'surfing' in x:
            return "Surfing"
        elif 'swimming' in x:
            return "Swimming"
        elif 'fishing' in x:
            return "Fishing"
        elif 'bathing' in x:
            return "Bathing"
        elif 'wading' in x:
            return "Wading"
        elif 'diving'or 'free' in x:
            return "Diving"
        elif 'yacht' in x:
            return "Yacht"
        else:
            return "UNKNOWN"
    else:
        return "UNKNOWN"
#########    ################################################  
data["Activity"] = data["Activity"].apply(lambda x: clean_act(x))

print(data['Activity'].value_counts())

popular_activities = Counter(data['Activity'].tolist()).most_common(20)
activities = [actv_list[0] for actv_list in popular_activities]
counts = [actv_list[1] for actv_list in popular_activities]
###########################################################################
fig, ax = plt.subplots(figsize=(12, 5))

sns.barplot(x=activities, y=counts, color='#295A83', ax=ax)
ax.set(ylabel="Attacks Count", xlabel="Activities")

ticks = plt.setp(ax.get_xticklabels(), rotation=60, fontsize=9)
########################################################################
#Corrigiendo errores de la columna date   
def clean_date(date):
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    num_months = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
    
    date = str(date)
    if (len(date) == 11 and date[2] == '-'):
        for i in range(len(months)):
            date = date.replace(months[i], num_months[i])
        return date
    else:
        return np.nan
###########################################################
data['Date'] = data['Date'].apply(clean_date)

dates = pd.to_datetime(data['Date'], dayfirst=True, errors='coerce')

days = dates.map(lambda x: x.day)
days_counter = Counter(days)
days_keys = list(days_counter.keys())
days_values = list(days_counter.values())

############################################################
months = dates.map(lambda x: x.month)

def season(month):
    if month >= 3 and month <= 5:
        return 'primavera'
    elif month >= 6 and month <= 8:
        return 'verano'
    elif month >= 9 and month <= 11:
        return 'otoño'
    else:
        return 'invierno'
##################################################
months_labels = months.apply(season)

months_counter = Counter(months_labels)
months_keys = list(months_counter.keys())
months_values = list(months_counter.values())

fig, ax = plt.subplots(figsize=(10, 2))
sns.barplot(x=days_keys, y=days_values, color='#B4E1F6', ax=ax)
ax = ax.set(ylabel="Attacks Count", xlabel="Day")

fig, ax = plt.subplots(figsize=(6, 3))
sns.barplot(x=months_keys, y=months_values, color='#B4E1F6', ax=ax)
ax = ax.set(ylabel="Attacks Count", xlabel="Month")

print(data['Date'].value_counts())

print(data['Date'].unique())
#######################################################
data['Year']= data['Year'].fillna('UNKNOWN')

def clean_year(year):
    if year > int(1000): 
        return year
    else:
        return 'UNKNOWN'

data['Year'] = data['Year'].apply(clean_year)

print(data['Year'].value_counts())

##########################################################

data[['Injury']]= data[['Injury']].fillna('UNKNOWN')

activity_injury = data['Injury'].tolist()

print(activity_injury[:10])

print(data['Injury'].value_counts())
##############################################################
data[['Investigator']]= data[['Investigator']].fillna('UNKNOWN')

data['Investigator'].value_counts()

def clean_invest(x):
    if isinstance(x, str):
        x = x.lower()
        if 'moore' in x:
            return "C. Moore"
        elif 'sohn' in x:
            return "S. Petersohn"
        elif 'well' in x:
            return "C. Creswell"
        elif 'collier' in x:
            return "R. Collier"
        elif 'peak' in x:
            return "T. Peake"
        elif 'leaklye' in x:
            return "A. Bleaklye"
        elif 'renneka' in x:
            return "A. Brenneka"
        elif 'ddalena' in x:
            return "A. de Maddalena"
        elif 'apson' in x:
            return "A. M. Rapson"
        elif 'isbane' in x:
            return "Brisbane Courier"
        elif 'arpe' in x:
            return "A. Sharpe"
        elif 'lack' in x:
            return "C. Black"
        elif 'oday' in x:
            return "Florida Today"
        elif 'arter' in x:
            return "G. Carter"
        elif 'ouvelles' in x:
            return "Les Nouvelles Caledoniennes"
        else:
            return "UNKNOWN"
    else:
        return "UNKNOWN"
       
data["Investigator"] = data["Investigator"].apply(lambda x: clean_invest(x))

print(data.Investigator.unique())

print(data['Investigator'].value_counts())

Investigators = [1,2,3,4,5]
Mentions = [247, 178, 167, 152, 97]

LABELS = ["Collier", "Petersohn", "Creswell", "Moore", "Sharpe",]

plt.bar(Investigators, Mentions, align='center')
plt.xticks(Investigators, LABELS)
plt.show()

################################################################
data['Time']= data['Time'].fillna('UNKNOWN')
data['Time']= data['Time'].str.replace('X', 'UNKNOWN')
data['Time']= data['Time'].str.replace('†', 'UNKNOWN')
data['Time']= data['Time'].str.replace('† ', 'UNKNOWN')

print(data['Time'].value_counts())

################################################################
data[['Name']]= data[['Name']].fillna('UNKNOWN')

print(data['Name'].value_counts())

#################################################################

#limpiando la columna de especies
def clean_species(x):
    if isinstance(x, str):
        x = x.lower()
        if 'white' in x:
            return "White Shark"
        elif 'tiger' in x:
            return "Tiger Shark"
        elif 'lemon' in x:
            return "Lemon Shark"
        elif 'mako' in x:
            return "Mako Shark"
        elif 'nurse' in x:
            return "Nurse Shark"
        elif 'grey' in x:
            return "Grey Reef Shark"
        elif 'copper' in x:
            return "Copper Shark"
        elif 'hammerhead' in x:
            return "Hammerhead Shark"
        elif 'wobbegong' in x:
            return "Wobbegong Shark"
        elif 'blacktip' in x:
            return "Blacktip Shark"
        elif 'caribbean' in x:
            return "Caribbean Reef Shark"
        elif 'blue'or 'porbeagle' in x:
            return "Blue Shark"
        elif 'dusky' in x:
            return "Dusky Shark"
        elif 'bull' in x:
            return "Bull Shark"
        elif 'zambesi' in x:
            return "Zambesi Shark"
        elif 'cocktail' in x:
            return "Cocktail Shark"
        elif 'vertiser' in x:
            return "The Advertiser"
        else:
            return "UNKNOWN"
    else:
        return "UNKNOWN"
       
data["Species"] = data["Species"].apply(lambda x: clean_species(x))

print(data['Species'].value_counts())

print(data.Species.unique())

Sharks = [1,2,3,4,5]
Attacks = [1704, 646, 282, 102, 93]

LABELS = ["Blue", "White", "Tiger", "Blacktip", "Nurse",]

plt.bar(Sharks, Attacks, align='center')
plt.xticks(Sharks, LABELS)
plt.show()

#################################################################
print(data['Area'].value_counts())

Area = [1,2,3,4,5]
Attacks = [990, 468, 402, 300, 282]

LABELS = ["Florida", "New South Wales", "UNKNOWN", "Queensland", "Hawaii",]

plt.bar(Sharks, Attacks, align='center')
plt.xticks(Sharks, LABELS)
plt.show()

data['Area'] = data['Area'].str.replace('?', '')
data['Area'] = data['Area'].str.replace('-', '')
data["Area"] = data["Area"].str.replace("(.*)\?"," ")
data["Area"] = data["Area"].str.replace("\d\d"," ")
data["Area"] = data["Area"].str.replace("\d"," ")

print(data.Area.unique())

null_cols = data.isnull().sum()
print(null_cols[null_cols > 0])

print(data.dtypes)

data.to_csv('data_attack_cleaned.csv', index=False)

