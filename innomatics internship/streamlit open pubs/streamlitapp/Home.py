import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import io





st.title('Welcome to Open Pubs')
st.write('Overview of the Open Pubs dataset')
df=pd.read_csv('Open_Pubs.csv')
df.drop(['Unnamed: 0'],axis=1,inplace=True)
df1= st.dataframe(df)
st.write('The columns of the dataset are :')
st.write(df.columns)

st.write('The shape of the dataset is : {} '.format(df.shape))
st.text('')

st.write('The decription of the dataset is :')
st.dataframe(df.describe())

buffer = io.StringIO()
df.info(buf=buffer)
s = buffer.getvalue()
st.write('The info of the dataset is :')
st.text(s)
st.text('')
st.write('The bar plot of first twenty value counts of the pubs based on local authority : ')

st.bar_chart(df['local_authority'].value_counts().head(20))

