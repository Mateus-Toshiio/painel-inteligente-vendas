import streamlit as st

def carregar_css():
    with open("styles/estilo.css", encoding="utf-8") as arquivo:
        conteudo = arquivo.read()


    st.markdown(
        f"""
        <style>
        {conteudo}
        </style>
        """,
        unsafe_allow_html=True
    )