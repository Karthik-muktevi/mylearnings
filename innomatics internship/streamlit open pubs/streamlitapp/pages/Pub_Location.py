import pandas as pd
import streamlit as st
import pandas as pd

df = pd.read_csv('Open_pubs.csv')

st.title('Location of pubs based on local authority or postal code')
select = st.selectbox('Select either local authority or postal code',['local_authority','postalcode'])

if True:
    if select =='local_authority':
        form = st.form(key='my_form')
        input = form.text_input('Enter local_authority/postalcode')
        submit = form.form_submit_button(label='submit')
        lat = df.loc[df['local_authority']==input,'latitude']
        long = df.loc[df['local_authority']==input,'longitude']
        rdf = pd.DataFrame((lat,long)).T
        st.map(rdf)
    elif select=='postalcode':
        form = st.form(key='my_form')
        input = form.text_input('Enter local_authority/postalcode')
        submit = form.form_submit_button(label='submit')
        lat = df.loc[df['postcode'] == input, 'latitude']
        long = df.loc[df['postcode'] == input, 'longitude']
        rdf = pd.DataFrame((lat, long)).T
        st.map(rdf)