# stream_iris.py

import streamlit as st
import numpy as np
import pickle

# Load trained pipeline
with open("iris.pkl", "rb") as f:
    pipeline = pickle.load(f)

# Iris class names
class_names = ['Setosa', 'Versicolor', 'Virginica']

# App title
st.title("🌸 Iris Flower Classifier")

# Input fields
sl = st.number_input("Sepal Length (cm)", min_value=0.0, max_value=10.0, value=5.1)
sw = st.number_input("Sepal Width (cm)", min_value=0.0, max_value=10.0, value=3.5)
pl = st.number_input("Petal Length (cm)", min_value=0.0, max_value=10.0, value=1.4)
pw = st.number_input("Petal Width (cm)", min_value=0.0, max_value=10.0, value=0.2)

# Predict button
if st.button("Predict"):
    user_input = np.array([[sl, sw, pl, pw]], dtype=float)
    prediction = pipeline.predict(user_input)[0]
    st.success(f"The predicted class is: {class_names[int(prediction)]}")