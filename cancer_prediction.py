import numpy as np
import joblib
import streamlit as st

# Load the trained model
model = joblib.load("cancer_model_revised.pkl")

# Prediction function
def prediction(ucell_size, ucell_shape, bnuclei):
    y = model.predict(np.array([[ucell_size, ucell_shape, bnuclei]]))
    return y

# Main Streamlit app
def main():
    st.title('🧬 Cancer Classification Model by Telvin')
    st.markdown("This app predicts whether a cancer case is **Benign (Non-cancerous)** or **Malignant (Cancerous)**.")

    # Input fields
    ucell_size = st.text_input('Uniform Cell Size:')
    ucell_shape = st.text_input('Uniform Cell Shape:')
    bnuclei = st.text_input('Bare Nuclei:')

    # Prediction button
    if st.button('Predict'):
        try:
            # Convert inputs to integers
            result = prediction(int(ucell_size), int(ucell_shape), int(bnuclei))

            if result[0] == 1:
                st.success('🔴 The cancer case is **Malignant**.')
            else:
                st.success('🟢 The cancer case is **Benign**.')
        except ValueError:
            st.error("⚠️ Please enter valid numeric values.")

# Entry point
if __name__ == '__main__':
    main()

