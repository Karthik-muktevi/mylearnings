import streamlit as st
import pandas as pd
import numpy as np
df = pd.read_csv('Open_Pubs.csv')
x = df[['latitude','longitude']]

st.title('Find the location of 5 nearest pubs')


lat = st.number_input('Enter latitude')
long = st.number_input('Enter longitude')
submit = st.button(label='submit')
x1 = np.array([lat,long])

dist = np.sqrt(np.sum((x1 - x)**2,axis=1))


k=5
sort = np.argsort(distances)[:k]
if submit:
    st.map(df.iloc[sort])
