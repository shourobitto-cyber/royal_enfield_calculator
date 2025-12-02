# Filename: royal_enfield_calculator.py
import streamlit as st
import pandas as pd

st.title("Royal Enfield Price & VAT Calculator")

# Input SP(s)
sp_input = st.text_area("Enter Selling Prices (comma separated)", "371500, 417500, 432500, 437500, 447700, 483000, 508000")
profit_percent = st.number_input("Profit %", value=4.5)

if st.button("Calculate"):
    try:
        selling_prices = [float(x.strip()) for x in sp_input.split(",")]
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
        st.dataframe(df)

    except Exception as e:
        st.error(f"Error: {e}")