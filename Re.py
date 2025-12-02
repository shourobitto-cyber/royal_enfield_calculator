# Filename: royal_enfield_calculator_pro.py
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

# Sidebar with common selling price suggestions
st.sidebar.header("Quick Suggestions")
common_sps = [371500, 417500, 432500, 437500, 447700, 483000, 508000]
selected_sps = st.sidebar.multiselect(
    "Select common Selling Prices (optional):",
    options=common_sps
)

# Main title
st.markdown("<h1 style='text-align: center; color: #D32F2F;'>Royal Enfield Price & VAT Calculator 🏍️</h1>", unsafe_allow_html=True)
st.markdown("---")

# Input section
sp_input = st.text_area(
    "Enter Selling Prices (comma separated):",
    value="",  # empty by default
    help="Type one or multiple SPs separated by commas, e.g., 371500, 417500"
)
profit_percent = st.number_input("Profit %:", value=4.5, min_value=0.0, step=0.1, help="Set your profit percentage")

# Merge sidebar selections with manual input
if selected_sps:
    sp_input = sp_input + "," + ",".join([str(x) for x in selected_sps]) if sp_input else ",".join([str(x) for x in selected_sps])

# Button to calculate
if st.button("Calculate"):
    try:
        selling_prices = [float(x.strip()) for x in sp_input.split(",") if x.strip() != ""]
        if not selling_prices:
            st.warning("Please enter at least one Selling Price.")
        else:
            profit_rate = profit_percent / 100
            data = []
            for sp in selling_prices:
                bp = sp / (1 + profit_rate)
                nsp = sp * 100 / 115
                selling_vat = nsp * 0.15
                nbp = bp * 100 / 115
                buying_vat = nbp * 0.15
                profit = sp - bp
                net_profit = nsp - nbp
                vat_diff = selling_vat - buying_vat
                data.append([sp, nsp, selling_vat, bp, nbp, buying_vat, profit, net_profit, vat_diff])

            columns = ["SP", "NSP", "Selling VAT", "BP", "NBP", "Buying VAT", "Profit", "Net Profit", "VAT Difference"]
            df = pd.DataFrame(data, columns=columns)
            df = df.round(2)

            st.success(f"Calculated results for {len(selling_prices)} SP(s)")
            st.dataframe(df, use_container_width=True)

    except Exception as e:
        st.error(f"Error: {e}")

# Footer
st.markdown("---")
st.markdown("<p style='text-align: center; color: gray;'>Royal Enfield Chuadanga | Developed by HKU</p>", unsafe_allow_html=True)