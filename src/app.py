import streamlit as st
from streamlit_option_menu import option_menu

from content.about import about_page
from content.header import header_menu
from content.main import main_page
from content.prognosis import prognosis_page
from content.help import help_page
from content.publications import publications_page

st.set_page_config(layout="wide", page_title="VALERIA", page_icon="./assets/valeria.png")

selected = header_menu()

if selected == "Início":
  main_page()
elif selected == "Ajuda":
  help_page()
elif selected == "Prognóstico":
  prognosis_page()
elif selected == "Publicações":
  publications_page()
elif selected == "Sobre":
  about_page()
  
