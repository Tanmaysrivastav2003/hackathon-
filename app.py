# Install Streamlit
!pip install streamlit

# Load necessary libraries
import streamlit as st
import joblib

# Load your machine learning model
model = joblib.load('/kaggle/working/random_forest_fraud_pred.pkl')

# Create the Streamlit app
st.title('Rajasthan Hackhathon')

# Add user input components
user_input = st.text_input('Enter some text:')
prediction_button = st.button('Get Prediction')

# Make predictions
if prediction_button:
    prediction = model.predict([user_input])[0]
    st.write('Prediction:', prediction)