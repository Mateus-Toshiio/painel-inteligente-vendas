import streamlit as st
from pathlib import Path

CAMINHO_CSS = Path("styles") / "estilo.css"

def carregar_css():
    try:
        with open("styles/estilo.css", encoding="utf-8") as arquivo:
            conteudo = arquivo.read()
    except FileNotFoundError:
        st.warning("Arquivo CSS não encontrado")


    st.markdown(
        f"""
        <style>
        {conteudo}
        </style>
        """,
        unsafe_allow_html=True
    )