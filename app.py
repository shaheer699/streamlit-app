import streamlit as st

st.title("Welcome Shaheer 👋")

name = st.text_input("Enter your name")

if name:
    st.write(f"Welcome {name} ❤️")
