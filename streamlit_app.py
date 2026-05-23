import streamlit as st

# app.py — baris 13
st.set_page_config(
  page_title="kuliah praktisi 2305",
  layout="centered"


# Hirarki teks
st.title("📊 Dashboard")
st.header("Laporan Bulanan")
st.subheader("📈 Monthly Expenses")
st.caption("Made with ❤️ using Streamlit")
  st.write("Hello, *World!* :😎:")

if st.button("Say hello"):
    st.write("Why hello there")
else:
    st.write("Goodbye")
