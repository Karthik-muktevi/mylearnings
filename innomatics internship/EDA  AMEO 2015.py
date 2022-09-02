#!/usr/bin/env python
# coding: utf-8

# Data Info:The dataset was released by Aspiring Minds from the Aspiring Mind Employment Outcome 2015 (AMEO). The study is primarily limited  only to students with engineering disciplines. The dataset contains the employment outcomes of engineering graduates as dependent variables (Salary, Job Titles, and Job Locations) along with the standardized scores from three different areas – cognitive skills, technical skills and personality skills. The dataset also contains demographic features. The dataset  contains  around  40 independent variables and 4000 data points. The independent variables are both continuous and categorical in nature. The dataset contains a unique identifier for each candidate.
# 
# Objective:Times of India article dated Jan 18, 2019 states that “After doing your Computer Science
# Engineering if you take up jobs as a Programming Analyst, Software Engineer,
# Hardware Engineer and Associate Engineer you can earn up to 2.5-3 lakhs as a fresh
# graduate.” 
# - Is there a relationship between gender and specialisation? (i.e. Does the preference of
# Specialisation depend on the Gender?)

# In[342]:


#importing libraries


# In[343]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[344]:


#loading the dataset


# In[345]:


df = pd.read_excel(r"D:\aspiring_minds_employability_outcomes_2015.xlsx")


# In[346]:


df_o =df.copy()


# In[347]:


#checking the first five rows of the dataset


# In[348]:


df.head()


# In[349]:


df.shape


# In[350]:


##The dataset contains 3998 rows and 39 columns


# In[351]:


df.columns


# In[352]:


df.drop(['Unnamed: 0'],axis=1,inplace=True)


# In[353]:


df.head(2)


# In[354]:


df.set_index(['ID']).head(2)


# In[355]:


#checking the datatypes of the columns


# In[356]:


df.dtypes


# In[357]:


#getting the mean,standard deviation,minimum,maximum values and the quartiles info


# In[358]:


round(df.describe()).T


# In[359]:


df.info()


# In[360]:


import datetime as dt


# In[361]:


df['DOL'].replace('present',dt.datetime.today(),inplace=True)


# In[362]:


#the datatype of DOL column is object.
#Changing the datatype to datetime format


# In[363]:


df['DOL'] = pd.to_datetime(df['DOL'])


# In[364]:


df['10board'].value_counts().head(40)


# In[365]:


df['10board'].unique()


# In[366]:


#from the above we can observe that there are some duplications regarding board,i.e cbse, central board of secondary education,cbse[gulf zone] etc come under cbse.So we combine all of them to cbse


# In[367]:


#From the valuecounts of 10th board we can observe that there exists 0 which means the board is unknown and some are of count 1
#So we replace the 0 and other boards whose value counts are very less.


# In[368]:


df['10board'].replace([ 'cbse', 'cbse[gulf zone]','new delhi', 'cbse board','central board of secondary education'], 'cbse',inplace=True)


# In[369]:


df['10board'].replace("cicse","icse",inplace=True)


# In[370]:


#replacing all the state boards to one category -state board


# In[371]:


board_10 = df['10board'].unique()
board_10_other = []
for i in board_10:
    if i == 'cbse' or i == 'icse' or i=='state board':
        continue
    else:
        board_10_other.append(i)


# In[372]:


for i in board_10_other:
    df['10board'].replace(i, 'state board',inplace=True)


# In[373]:


df['10board'].value_counts()


# In[374]:


df['12board'].value_counts().head(40)


# In[375]:


df['12board'].unique()


# In[376]:


df['12board'].replace(['all india board','central board of secondary education, new delhi', 'cbese'], 'cbse',inplace=True)


# In[377]:


df['12board'].replace(['isc', 'isc board', 'isce', 'cicse','isc board , new delhi'], 'icse',inplace=True)


# In[378]:


board_12 = df['12board'].unique()
board_12_other = []
for i in board_12:
    if i == 'cbse' or i == 'icse':
        continue
    else:
        board_12_other.append(i)

for j in board_12_other:
    df['12board'].replace(j,'state board',inplace=True)


df['12board'].unique()


# In[379]:


#As we can see many -1 and 0 values in the dataset we replace them with NAN


# In[380]:



df.replace([-1,'n/a',0],np.NaN,inplace=True)


# In[381]:


df.isnull().sum()


# In[382]:


df['JobCity'].fillna(df['JobCity'].mode()[0], inplace=True)


# In[383]:


df['Domain'].fillna(df['Domain'].mode()[0], inplace=True)


# In[384]:


df['10board'].fillna(df['10board'].mode()[0], inplace=True)


# In[385]:


df['12board'].fillna(df['12board'].mode()[0], inplace=True)


# In[386]:


df.drop(columns=['ElectronicsAndSemicon'],axis=1,inplace=True)
df.drop(columns=['MechanicalEngg'],axis=1,inplace=True)
df.drop(columns=['ElectricalEngg'],axis=1,inplace=True)
df.drop(columns=['CivilEngg'],axis=1,inplace=True)
df.drop(columns=['ComputerScience'],axis=1,inplace=True)
df.drop(columns=['CollegeCityTier'],axis=1,inplace=True)
df.drop(columns=['TelecomEngg'],axis=1,inplace=True)


# UNIVARIATE AND BIVARIATE ANALYSIS
# 

# In[387]:


(df['DOJ'].dt.year).value_counts().plot(kind='bar')


# In[388]:


#The year 2014 has greater number of joinings


# In[389]:


count = df.groupby('10board').size()
count.plot.bar()


# In[390]:


#More students belong to state board


# In[391]:


count_12 = df.groupby(by='12board').size()
count_12.plot.bar()


# In[392]:


#More students belong to state board


# In[393]:


plt.figsize=(8,8)
sns.kdeplot(df['Salary'])
plt.axvline(df['Salary'].mean())


# In[394]:


#From above plot, we see the distribution is right skewed and has Log Normal Distribution


# In[395]:


sns.displot(df['10percentage'])


# In[490]:


sns.kdeplot(df['10percentage'])


# In[396]:


df['10percentage'].skew()


# In[397]:


#The data is negatively skewed


# In[491]:


sns.distplot(df['12percentage'])


# In[398]:


sns.kdeplot(df['12percentage'])


# In[399]:


round(df['12percentage'].skew(),2)


# In[400]:


#data distribution has a minimal skewness.Nearly normal


# In[494]:


sns.displot(df['collegeGPA'])


# In[401]:


df['Gender'].value_counts().plot(kind='bar')


# In[402]:


# m~male;f~female
#The count of male is greater than female


# In[403]:


df['Specialization'].value_counts()


# In[404]:


df['Specialization'].value_counts().plot(kind='bar',figsize=(15,10))


# In[405]:


# As there are siimlar fields given under different categories we try to group them together by mapping similar entities.


# In[406]:


map_specialization = {'electronics and communication engineering' : 'EC',
 'computer science & engineering' : 'CS',
 'information technology' : 'CS' ,
 'computer engineering' : 'CS',
 'computer application' : 'CS',
 'mechanical engineering' : 'ME',
 'electronics and electrical engineering' : 'EC',
 'electronics & telecommunications' : 'EC',
 'electrical engineering' : 'EL',
 'electronics & instrumentation eng' : 'EC',
 'civil engineering' : 'CE',
 'electronics and instrumentation engineering' : 'EC',
 'information science engineering' : 'CS',
 'instrumentation and control engineering' : 'EC',
 'electronics engineering' : 'EC',
 'biotechnology' : 'other',
 'other' : 'other',
 'industrial & production engineering' : 'other',
 'chemical engineering' : 'other',
 'applied electronics and instrumentation' : 'EC',
 'computer science and technology' : 'CS',
 'telecommunication engineering' : 'EC',
 'mechanical and automation' : 'ME',
 'automobile/automotive engineering' : 'ME',
 'instrumentation engineering' : 'EC',
 'mechatronics' : 'ME',
 'electronics and computer engineering' : 'CS',
 'aeronautical engineering' : 'ME',
 'computer science' : 'CS',
 'metallurgical engineering' : 'other',
 'biomedical engineering' : 'other',
 'industrial engineering' : 'other',
 'information & communication technology' : 'EC',
 'electrical and power engineering' : 'EL',
 'industrial & management engineering' : 'other',
 'computer networking' : 'CS',
 'embedded systems technology' : 'EC',
 'power systems and automation' : 'EL',
 'computer and communication engineering' : 'CS',
 'information science' : 'CS',
 'internal combustion engine' : 'ME',
 'ceramic engineering' : 'other',
 'mechanical & production engineering' : 'ME',
 'control and instrumentation engineering' : 'EC',
 'polymer technology' : 'other',
 'electronics' : 'EC'}


# In[407]:


df['Specialization'] = df['Specialization'].map(map_specialization)


# In[408]:


df['Specialization'].value_counts().plot(kind='bar',figsize=(15,8))


# In[409]:


#computer science engineering specialization is the majority followed by electronics engineering.


# CHECKING FOR OUTLIERS

# In[410]:


def outliers(df,col):
    q1 = df[col].quantile(0.25)
    q3 = df[col].quantile(0.75)
    iqr = q3-q1
    lb = q1-(1.5*iqr)
    ub = q3+(1.5*iqr)
    outlier = []
    for i in df[col]:
        if i<lb or i>ub:
            outlier.append(i)
    return len(outlier),outlier


# In[411]:


outliers(df,'Salary')


# In[412]:


outliers(df,'10percentage')


# In[413]:


outliers(df,'12percentage')


# In[414]:


outliers(df,'ComputerProgramming')


# In[415]:


imp_val=df['ComputerProgramming'].median()

df['ComputerProgramming'].fillna(value=imp_val, inplace=True)


# In[420]:


sns.boxplot(x='Salary',data=df)


# In[421]:


sns.boxplot(x='Gender',y='Salary',data=df)


# In[422]:


#more number of outliers are observed in male category


# Research Questions
# - Times of India article dated Jan 18, 2019 states that “After doing your Computer Science
# Engineering if you take up jobs as a Programming Analyst, Software Engineer,
# Hardware Engineer and Associate Engineer you can earn up to 2.5-3 lakhs as a fresh
# graduate.” Test this claim with the data given to you.
# - Is there a relationship between gender and specialisation? (i.e. Does the preference of
# Specialisation depend on the Gender?)

# In[423]:


sns.countplot(x='Specialization',hue='Gender',data=df)


# In[424]:


#computer science students are more in number and dominant with regards to gender too
# Females have less preference for CE department,ME department and departments other than CS & EC.
#CE department is less preferred by males too.


# In[511]:


sns.boxplot(x='Specialization',y='Salary',data=df)


# In[ ]:


#CE department students are getting higher Salary when compared to others.
#There are considerable number of outliers in the data(specialization vs salary) which is clearly visible from boxplot


# In[525]:



sns.barplot(x='Salary',y='Specialization',data=df)


# #The belief that computer science specialization is the highest paying field is partially true as it remained to be the highest paying field but other specializations are also earning equally good showing no much difference betwwen the salary vs specialization which implies ''hardwork is the key to success''

# In[446]:


sns.histplot(x='Gender',y='Specialization',data=df)


# In[451]:


sns.distplot(df['Salary'],kde=True,bins=20)


# In[468]:


sns.factorplot(x='Gender',y='Salary',data=df)


# In[469]:


#Salary of male aspirants is more than female


# In[470]:


sns.jointplot(x='Salary',y='12board',data=df)


# In[471]:


sns.jointplot(x='Salary',y='10board',data=df)


# In[472]:


#Salary is more  for the aspirants coming from state board when compared to others


# In[474]:


sns.lineplot(x='Specialization',y='Salary',data=df)


# In[483]:





# In[498]:


sns.pairplot(df)


# In[501]:


corr = df.corr()
plt.figure(figsize=(10,8))
sns.heatmap(corr)


# In[503]:


df[['Salary','10percentage', '12percentage', 'collegeGPA']].corr()


# In[504]:


#Students having higher percentage of marks in 10th Class performed similarly in 12th Class(Correlation Coefficient ~0.64) .

#However correlation between marks scored and the starting salary is quite low (around 0.17) for 10th and 12th Class percentage scores and even lesser (~0.13) for College CGPA and goes against the widely accepted notation that higher grades result in higher salary.


# FEATURE ENCODING

# In[527]:


from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()


# In[529]:


num_col  = pd.DataFrame()
num_col = df[['Salary','10percentage','12percentage']]


# In[530]:


num_col


# In[532]:


scaler.fit_transform(num_col)


# In[544]:


cat_col = df[['Gender','Designation','JobCity','Specialization','10board','12board','Degree']]


# In[545]:


pd.get_dummies(cat_col,drop_first=True)


# In[ ]:




