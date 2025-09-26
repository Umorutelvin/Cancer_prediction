import numpy as np 
import pandas as pd
import joblib 
import streamlit as st 

model = joblib.load('cancer_model.joblib')

def prediction(ucell_size, ucell_shape,bnuclei):
    y = model.predict(np.array([ucell_size, ucell_shape, bnuclei]))
    return y 

def main():
    st.title('cancel classification model')
    
    ucell_size = st.text_input('u cell size: ')
    ucellshape = st.text_input('u cell shape: ')
    bnuclei = st.text_import('b nuclei: ')
    
if _name_=='_main_':
    main()
    
