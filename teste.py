import streamlit as st

st.title("Meu programa")

st.write("Gerador de nome completo")

nome = st.text_input("Digite o seu primeiro nome:")
if nome:
  st.write(nome.upper())
sobrenome = st.text_input("Digite o seu sobrenome:")
if sobrenome:
  st.write(nome.upper())

if st.button("Mostrar nome completo"):
    st.success(f"O seu nome completo é {nome} {sobrenome}")
