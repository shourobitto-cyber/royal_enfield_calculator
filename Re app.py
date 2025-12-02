import streamlit as st
import pandas as pd

# App config
st.set_page_config(page_title="Royal Enfield Calculator", page_icon="🏍️", layout="wide")

# Style
st.markdown("""
<style>
h1 { color: #D32F2F; }
.highlight { background-color: #FFF3E0; padding: 15px; border-radius: 10px; font-size: 22px; font-weight: bold; text-align: center; color: #D32F2F;}
</style>
""", unsafe_allow_html=True)

st.markdown("<h1 style='text-align:center;'>Royal Enfield Price & VAT Calculator 🏍️</h1>", unsafe_allow_html=True)
st.markdown("<hr>")

# Initialize session state
if "sp_input" not in st.session_state:
    st.session_state.sp_input = ""

# Columns
col1, col2 = st.columns([3,1])

with col1:
    st.subheader("Enter Selling Prices")
    sp_input = st.text_area("Type prices (comma-separated):", value=st.session_state.sp_input, height=150)

with col2:
    st.subheader("Common Prices")
    common