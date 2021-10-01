# using streamlit we don't have to write html,css and js 
import streamlit as st
import numpy as np
import pandas as pd
import pickle

model = pickle.load(open('LinearRegressionModel.pkl','rb'))


df = pd.read_csv('cleaned_car.csv')

company_name = sorted(df['company'].unique())


brand_name = []

for i in df['name']:
    s = " ".join(i.split()[:])
    brand_name.append(s)

brand_name = sorted(brand_name)


st.title('Welcome to Car Price Predictor')


company_name.insert(0,'Select a Company')
company = st.selectbox('Company',company_name)


brand_name.insert(0,'Select a brand')
name = st.selectbox('Brand',brand_name)

year = st.number_input('Year of Pourchase')


fuel_type = st.selectbox('Fuel Type',('Petrol','Diesel','LPG'))

kms_driven = st.number_input('KMs Driven')

if st.button('Predict Price'):
    prediction=model.predict(pd.DataFrame(columns=['name', 'company', 'year', 'kms_driven', 'fuel_type'],data=np.array([name,company,year,kms_driven,fuel_type]).reshape(1, 5)))
    st.title('Prediction: ₹'+str(np.round(prediction[0])))


