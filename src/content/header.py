from streamlit_option_menu import option_menu

def header_menu():
  return option_menu(None, ["Início", "Prognóstico",  "Ajuda", 'Sobre', "Publicações"], 
      icons=['house', 'file-medical', "question-circle", 'info-circle', 'info-circle'], 
      menu_icon="cast", default_index=0, orientation="horizontal",
      styles={
        "nav-link-selected": {"background-color": "#3DB7A0"},
      }
    )