import streamlit as st

st.title("kindly add city and age")
age = st.slider("Select your age:", 0, 100)

city = st.selectbox("select your city:", ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix"])

if st.button("Submit"):
    st.write("age" , age)
    st.write("city", city)