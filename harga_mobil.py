import streamlit as st

from pyngrok import ngrok
from joblib import load

trained_model = load("Model_toyota.pkl")

form = st.form(key='my-form')

models = st.sidebar.selectbox("Masukkan model: ", ('GT86', 'Corolla', 'RAV4', 'Yaris', 'Auris', 'Aygo', 'C-HR',
       'Prius', 'Avensis', 'Verso', 'Hilux', 'PROACE VERSO', 'Land Cruiser', 'Supra', 'Camry', 'Verso-S', 'IQ',
       'Urban Cruiser'))
Model = {'GT86': 6, 'Corolla': 5, 'RAV4': 12, 'Yaris': 17, 'Auris': 0, 'Aygo': 2, 'C-HR': 3,
       'Prius': 10, 'Avensis': 1, 'Verso': 15, 'Hilux': 7, 'PROACE VERSO': 11,
       'Land Cruiser': 9, 'Supra': 13, 'Camry': 4, 'Verso-S': 16, 'IQ': 8, 'Urban Cruiser': 14}
if models:
  model = Model[models]

years = st.slider("Masukkan tahun: ", 1998, 2020)
Year = {'1998': 0, '1999': 1, '2000': 2, '2001': 3, '2002': 4, '2003': 5, '2004': 6, '2005': 7, '2006': 8, '2007': 9, 
        '2008': 10, '2009': 11, '2010': 12, '2011': 13, '2012': 14, '2013': 15, '2014': 16, '2015': 17, '2016': 18, '2017': 19,
        '2018': 20, '2019': 21, '2020': 22}
if years:
  year = Year[str(years)]

Trans = st.sidebar.selectbox("Masukkan transmission: ", ('manual', 'automatic', 'semi-auto', 'other'))
transmission = {'manual': 1, 'automatic': 0, 'semi-auto': 3, 'other': 2}
if Trans:
  trans = transmission[Trans]

Fuel = st.sidebar.selectbox("Masukkan fuelType: ", ('Petrol', 'Other', 'Hybrid', 'Diesel'))
fuelType = {'Petrol': 3, 'Other': 2, 'Hybrid': 1, 'Diesel': 0}
if Fuel:
  fuel = fuelType[Fuel]

mile = form.text_input("Masukkan mileage (Km): ")
tax = form.text_input("Masukkan tax: ")
mpg = st.slider("Masukkan mpg (litres): ", 2.8, 235.0)
engSize = st.slider("Masukkan engineSize (litre): ", 0.0, 4.5)

submit = form.form_submit_button("Cek Harga")

if submit:
  hasil_akhir = trained_model.predict([[
    int(model),
    int(year),
    int(trans),
    int(mile),
    int(fuel),
    int(tax),
    float(mpg), 
    float(engSize)]])
  st.write("Kategori Harga:")
  st.write(hasil_akhir[0])

# ngrok_tunnel = ngrok.connect(8501)
# print('Public URL:', ngrok_tunnel.public_url)