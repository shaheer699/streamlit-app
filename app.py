import streamlit as st

st.title("Welcome Shaheer 👋")

name = st.text_input("Enter your name")

if name:
  i' st.write(f"Welcome {name} ❤️")

st.set_page_config(page_title="Shaheer App", page_icon="🔥", layout="centered")