import pickle
import streamlit as st
import pandas as pd
import numpy as np
import joblib
from sklearn.preprocessing import StandardScaler
from prueba1 import Algeria_app
from data_afric import Animal_app
import streamlit as st
#from streamlit_option_menu import option_menu

st.set_page_config(
    page_title='Home',
    page_icon='house'
)
st.image('logo3.jpeg')
texto = ('ForestGuard es una herramienta esencial para quienes desean proteger y preservar los bosques y la vida silvestre de Argelia. Únete a nosotros en la lucha contra los incendios forestales y en la promoción de la coexistencia armoniosa con la fauna salvaje en nuestro hermoso país.') 
st.markdown(f'<p style="text-align: justify;">{texto}</p>', unsafe_allow_html=True)
st.markdown('---')
with st.sidebar:
    st.image('logo_ie.png')
    st.write('Student: Evelyn Venegas')
    modelo = st.selectbox('Select model',('Home','Algeria Forest Fires','Animal Wildlife'))

# Mostrar una vista diferente para cada modelo seleccionado
if modelo == 'Algeria Forest Fires':
    Algeria_app()

elif modelo == 'Animal Wildlife':
    Animal_app()