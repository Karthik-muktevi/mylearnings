import streamlit as st
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsRegressor
from sklearn.ensemble import RandomForestRegressor,GradientBoostingRegressor
from sklearn.linear_model import LinearRegression
from sklearn import metrics

st.title('Welcome to Diamond Price Prediction App using Streamlit')
df = pd.read_csv('diamonds.csv')
scaler = StandardScaler()
df['carat'] = scaler.fit_transform(df[['carat']])
clarity_encoder = {'I1':1, 'SI2':2, 'SI1':3, 'VS2':4, 'VS1':5, 'VVS2':6, 'VVS1':7, 'IF':8}
df['clarity'] = df['clarity'].apply(lambda x: clarity_encoder[x])
cut_encoder = {'Fair' : 1, 'Good' : 2, 'Very Good' : 3, 'Ideal' : 4, 'Premium' : 5}
df['cut'] = df['cut'].apply(lambda x: cut_encoder[x])
color_encoder = {'J':1, 'I':2, 'H':3, 'G':4, 'F':5, 'E':6, 'D':7}
df['color'] = df['color'].apply(lambda x: color_encoder[x])
X = df[['carat','cut','color','clarity']]
y = df['price']
dataset = st.selectbox('Select Dataset',['diamonds.csv'])
carat = st.number_input(label='carat',min_value=0.2,max_value=5.01)
cut = st.selectbox('cut',('Fair', 'Good', 'Very' 'Good', 'Premium', 'Ideal'))
color = st.selectbox('color',('D','E','F','G','H','I','J'))
clarity = st.selectbox('clarity',('I1', 'SI2', 'SI1', 'VS2', 'VS1', 'VVS2', 'VVS1', 'IF'))
r = pd.DataFrame()

regressor = st.sidebar.selectbox('Select Algorithm',('LinearRegression','KNeighborsRegressor','RandomForestRegressor','GradientBoostingRegressor'))

def hyperparam(reg_name):
    hp=dict()
    if reg_name =='KNeighborsRegressor':
        K = st.sidebar.slider('K',3,40)
        hp['K'] = K
    elif reg_name =='RandomForestRegressor':
        max_depth = st.sidebar.slider('max_depth',2,15)
        n_estimators = st.sidebar.slider('n_estimators',1,100)
        hp['max_depth'] = max_depth
        hp['n_estimators'] = n_estimators
    elif reg_name =='GradientBoostingRegressor':
        max_depth_g = st.sidebar.slider('max_depth',1,9)
        n_estimators_g = st.sidebar.slider('n_estimators',5,500)
        hp['max_depth_g'] = max_depth_g
        hp['n_estimators_g'] = n_estimators_g
    return hp

hp = hyperparam(regressor)

def regressorr(reg_name,hp):
    if reg_name =='KNeighborsRegressor':
        reg = KNeighborsRegressor(n_neighbors=hp['K'])
    elif reg_name == 'LinearRegression':
        reg = LinearRegression()
    elif reg_name == 'RandomForestRegressor':
        reg = RandomForestRegressor(n_estimators=hp['n_estimators'],max_depth=hp['max_depth'])
    elif reg_name == 'GradientBoostingRegressor':
        reg = GradientBoostingRegressor(n_estimators=hp['n_estimators_g'],max_depth=hp['max_depth_g'])
    return reg
reg = regressorr(regressor,hp)
reg.fit(X,y)

test_dict = {'carat':carat,'cut':cut,'color':color,'clarity':clarity}
test = pd.DataFrame(test_dict,index=[0])
test['carat'] = scaler.transform(test[['carat']])
test['cut'] = test['cut'].apply(lambda x:cut_encoder[x])
test['color'] = test['color'].apply(lambda x:color_encoder[x])
test['clarity'] = test['clarity'].apply(lambda x:clarity_encoder[x])
y_test = [2616]

y_pred = reg.predict(test)

mae = metrics.mean_absolute_error(y_test,y_pred)
mse = metrics.mean_squared_error(y_test,y_pred)
submit = st.button('Predict')
if submit:
    st.write(f'The predicted price is =${y_pred}')
    st.write(f'The Mean Absolute error for prediction is = {mae}')
    st.write(f'The Mean square error for prediction is = {mse}')

actual =st.checkbox(f'Check the actual value',)
if actual:
    st.write(f'The actual price is =$2616')



