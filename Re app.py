# Filename: royal_enfield_calculator_side.py
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

# -------------------
# Light theme styling
# -------------------
st.markdown("""
<style>
.main {
    background-color: #FFFFFF;
    color: #1A1A1A;
}
h1 {
    color: #D32F2F;
}
h3 {
    color: #1976D2;
}
.highlight {
    background-color: #FFF3E0;
    padding: 15px;
    border-radius: 10px;
    font-size: 22px;
    font-weight: bold;
    text-align: center;
    color: #D32F2F;
}
</style>
""", unsafe_allow_html=True)

# -------------------
# Title
# -------------------
st.markdown("<h1 style='text-align: center;'>Royal Enfield Price & VAT Calculator 🏍️</h1>", unsafe_allow_html=True)
st.markdown("<hr>")

# -------------------
# Columns: input box (left) and common prices (right)
# -------------------
col1, col2 = st.columns([3, 1])

with col1:
    st.subheader("Enter Selling Prices")
    # Initialize session state for dynamic updates
    if "sp_input" not in st.session_state:
        st.session_state.sp_input = ""
    sp_input = st.text_area(
        "Type prices (comma-separated):",
        value=st.session_state.sp_input,
        help="You can type any prices, e.g., 371500, 417500, 450000"
    )

with col2:
    st.subheader("Common Prices")
    common_sps = [371500, 417500, 432500, 437500, 447700, 483000, 508000]
    selected_common = st.multiselect(
        "Choose common prices to add:",
        options=common_sps,
        default=[]
    )
    
    # Append selected common prices to input box dynamically
    if selected_common:
        existing_prices = [x.strip() for x in st.session_state.sp_input.split(",") if x.strip() != ""]
        for price in selected_common:
            existing_prices.append(str(price))
        st.session_state.sp_input = ",".join(existing_prices)
        # Clear the multiselect to allow multiple selections again
        st.experimental_rerun()

# -------------------
# Profit %
# -------------------
profit_percent = st.number_input(
    "Profit %:", value=4.5, min_value=0.0, step=0.1, help="Set your profit percentage"
)

# -------------------
# Calculate button
# -------------------
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
                buying_vat = nbp * 0.15
                profit = sp - bp
                net_profit = nsp - nbp
                vat_diff = selling_vat - buying_vat
                total_vat_diff += vat_diff
                data.append([sp, nsp, selling_vat, bp, nbp, buying_vat, profit, net_profit, vat_diff])

            columns = ["SP", "NSP", "Selling VAT", "BP", "NBP", "Buying VAT", "Profit", "Net Profit", "VAT Difference"]
            df = pd.DataFrame(data, columns=columns)
            df = df.round(2)

            st.success(f"Calculated results for {len(selling_prices)} SP(s)")
            st.dataframe(df.style.set_properties(**{'background-color': '#F9F9F9', 'color': '#000000', 'border-color': '#D32F2F'}), use_container_width=True)

            # Highlight total VAT difference
            st.markdown(f"<div class='highlight'>Total VAT Difference: {total_vat_diff:,.2f} BDT</div>", unsafe_allow_html=True)
    except Exception as e:
        st.error(f"Error: {e}")

# -------------------
# Footer
# -------------------
st.markdown("<hr>")
st.markdown("<p style='text-align: center; color: gray;'>Royal Enfield Chuadanga | Developed by HKU</p>", unsafe_allow_html=True)