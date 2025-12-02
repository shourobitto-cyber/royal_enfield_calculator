# Filename: royal_enfield_calculator_final.py
import streamlit as st
import pandas as pd

# -------------------
# App configuration
# -------------------
st.set_page_config(
    page_title="Royal Enfield Price & VAT Calculator",
    page_icon="🏍️",
    layout="wide"
)

# Title
st.markdown("<h1 style='text-align: center; color: #D32F2F;'>Royal Enfield Price & VAT Calculator 🏍️</h1>", unsafe_allow_html=True)
st.markdown("---")

# Pre-filled Selling Prices
common_sps = [371500, 417500, 432500, 437500, 447700, 483000, 508000]
st.subheader("Select Selling Prices")
selected_sps = st.multiselect(
    "Choose one or multiple Selling Prices:",
    options=common_sps,
    default=[],
    help="You can select multiple prices"
)

# Profit %
profit_percent = st.number_input("Profit %:", value=4.5, min_value=0.0, step=0.1, help="Set your profit percentage")

# Calculate button
if st.button("Calculate"):
    if not selected_sps:
        st.warning("Please select at least one Selling Price.")
    else:
        profit_rate = profit_percent / 100
        data = []
        total_vat_diff = 0
        for sp in selected_sps:
            bp = sp / (1 + profit_rate)
            nsp = sp * 100 / 115
            selling_vat = nsp * 0.15
            nbp = bp * 100 / 115
            buying_vat = nbp * 0.15
            profit = sp - bp
            net_profit = nsp - nbp
            vat_diff = selling_vat - buying_vat
            total_vat_diff += vat_diff
            data.append([sp, nsp, selling_vat, bp, nbp, buying_vat, profit, net_profit, vat_diff])

        columns = ["SP", "NSP", "Selling VAT", "BP", "NBP", "Buying VAT", "Profit", "Net Profit", "VAT Difference"]
        df = pd.DataFrame(data, columns=columns)
        df = df.round(2)

        st.success(f"Calculated results for {len(selected_sps)} SP(s)")
        st.dataframe(df, use_container_width=True)

        # Highlight total VAT difference
        st.markdown(f"<h3 style='color: #D32F2F;'>Total VAT Difference: {total_vat_diff:,.2f} BDT</h3>", unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("<p style='text-align: center; color: gray;'>Royal Enfield Chuadanga | Developed by HKU</p>", unsafe_allow_html=True)