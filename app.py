import streamlit as st

st.set_page_config(
    page_title="Resumos Executivos - 3º Ciclo",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Lê o arquivo HTML
with open("Resumos_Executivos__offline_.html", "r", encoding="utf-8") as f:
    html_content = f.read()

# Renderiza no Streamlit
st.components.v1.html(html_content, height=1000, scrolling=True)
