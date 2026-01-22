import streamlit as st  

st.title("few more features added")

name = st.text_input("Enter some text:")

if st.button("Submit"):
    st.write("hello", name)
