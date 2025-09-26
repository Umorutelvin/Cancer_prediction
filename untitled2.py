import numpy as np 
import pandas as pd
import joblib 
import streamlit as st 

model = joblib.load("cancer_model_revised.joblib")

def prediction(ucell_size, ucell_shape, bnuclei):
    y = model.predict(np.array([[ucell_size, ucell_shape, bnuclei]]))
    return y

def main():
    st.title('cancel classification model')
    
    ucell_size = st.text_input('u cell size: ')
    ucell_shape = st.text_input('u cell shape: ')
    bnuclei = st.text_input('b nuclei: ')
    
# prediction 
if st.button('predict'):
    result = prediction(int(ucell_size), int(ucell_shape), int(bnuclei))
    if result[0]==1:
        st.success('The cancer case is malignant')
    else:
        st.success('The cancer case is benign')
    
if  __name__ == '_main_': 
    main()
    
