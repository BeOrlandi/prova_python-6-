import pandas as pd
import openpyxl
import streamlit as st
df = pd.read_excel("pib.xlsx")
df["ano"] = df["Data"].astype(str).str[:4]
media = df.groupby("ano")["PIB real"].mean().reset_index()

st.title("PIB real do Brasil")


st.sidebar.header("Análise do PIb do Brasil de acordo com http://www.ipeadata.gov.br/")

arquivo = st.sidebar.file_uploader(
    "Envie a planilha do PIB",
    type=["xlsx", "xls", "csv"]
)

df_pib.xlsx = pib.xlsx[pib.xlsx["NOMEUP"] == "Taquaril"]
fig_linha_taquaril = px.line(

df_pib.xlsx,
x="DATA",
y="PIB REAL",
markers=True,
template="plotly_dark"
)
