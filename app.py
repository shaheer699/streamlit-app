import streamlit as st
st.set_page_config(page_title="Shaheer App", page_icon="❤️", layout="centered")

st.title("Welcome Shaheer ❤️")

name = st.text_input("Enter your name")

if name:
 st.write(f"Welcome {name} ❤️")


