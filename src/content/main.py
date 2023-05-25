import streamlit as st

def main_page():
  col1, col2, col3 = st.columns(3)

  with col2:
    st.image("./assets/valeria.png")

  st.markdown("<h1 style='text-align: center; color: black;'; font-family:>Virtual Assistant for LEarning pRocesses In Arbovirus</h1>", unsafe_allow_html=True)