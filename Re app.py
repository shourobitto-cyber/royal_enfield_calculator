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
    sp_input = st.text_area("Type prices (comma-separated):", value=st.session_state.sp_input)

with col2:
    st.subheader("Common Prices")
    common_sps = [371500, 417500, 432500, 437500, 447700, 483000, 508000]
    selected_common = st.multiselect("Select common prices to add:", options=common_sps)
    if st.button("Add to Input"):
        existing_prices = [x.strip() for x in st.session_state.sp_input.split(",") if x.strip() != ""]
        for price in selected_common:
            existing_prices.append(str(price))
        st.session_state.sp_input = ",".join(existing_prices)

# Profit %
profit_percent = st.number_input("Profit %:", value=4.5, min_value=0.0, step=0.1)

# Calculate button
if st.button("Calculate"):
    try:
        selling_prices = [float(x.strip()) for x in st.session_state.sp_input.split(",") if x.strip() != ""]
        if not selling_prices:
            st.warning("Please enter at least one Selling Price.")
        else:
            profit_rate = profit_percent / 100
            data = []
            total_vat_diff = 0
            for sp in selling_prices:
                bp = sp / (1 + profit_rate)
                nsp = sp * 100 / 115
                selling_vat = nsp * 0.15
                nbp = bp * 100 / 115
                buying