import streamlit as st
from streamlit_option_menu import option_menu

from models.patient import Patient

st.set_page_config(layout="wide", page_title="VALERIA", page_icon="./assets/valeria.png")

selected = option_menu(None, ["Início", "Prognóstico",  "Dúvidas", 'Sobre'], 
    icons=['house', 'file-medical', "question-circle", 'info-circle'], 
    menu_icon="cast", default_index=0, orientation="horizontal",
    styles={
      "nav-link-selected": {"background-color": "#3DB7A0"},
    }
)

if selected == "Início":
  col1, col2, col3 = st.columns(3)

  with col2:
    st.image("./assets/valeria.png")

  st.markdown("<h1 style='text-align: center; color: black;'; font-family:>Virtual Assistant for LEarning pRocesses In Arbovirus</h1>", unsafe_allow_html=True)
elif selected == "Prognóstico":
  st.title("Prognóstico")
  # st.write("### Preencha os campos com as informações do paciente para obter o resultado:")
  
  patient = Patient()
  temp = True
  
  with st.expander("Preencha os campos com as informações do paciente para obter o resultado", expanded=temp):
    with st.form("diagnostico_form", clear_on_submit=True):
      patient.setDays(st.number_input("Quantos dias o paciente está sentindo os sintomas?", min_value=0, format="%d"))
    
      st.write("Informe os sintomas do paciente:")

      col_symptoms_1, col_symptoms_2, col_symptoms_3 = st.columns(3)

      patient.setFever(col_symptoms_1.checkbox("Febre"))

      patient.setMyalgia(col_symptoms_1.checkbox("Mialgia", help="Dor muscular"))

      patient.setHeadache(col_symptoms_1.checkbox("Cefaleia", help="Dor de cabeça"))

      patient.setRash(col_symptoms_1.checkbox("Exantema", help="Manchas vermelhas em um região"))

      patient.setNausea(col_symptoms_2.checkbox("Náusea"))

      patient.setBackPain(col_symptoms_2.checkbox("Dor nas costas"))

      patient.setConjunctivitis(col_symptoms_2.checkbox("Conjuntivite"))

      patient.setArthritis(col_symptoms_2.checkbox("Artrite", help="Inflamação das articulações"))

      patient.setArthralgia(col_symptoms_3.checkbox("Artralgia", help="Dor nas articulações"))

      patient.setPetechia(col_symptoms_3.checkbox("Petéquias", help="Pequenas manchas vermelhas ou marrom que surgem geralmente aglomeradas, mais frequentemente nos braços, pernas ou barriga"))

      patient.setEyePain(col_symptoms_3.checkbox("Dor Retroorbital", help="Dor ao redor dos olhos"))

      st.write("Informe as condições prévias do paciente:")

      col_comorbidities_1, col_comorbidities_2, col_comorbidities_3 = st.columns(3)

      patient.setDiabetes(col_comorbidities_1.checkbox("Diabetes", help=""))

      patient.setHypertension(col_comorbidities_2.checkbox("Hipertensão", help=""))
      
      st.markdown("----")
      
      if (st.form_submit_button("Resultado")):
        temp = False
        # with st.spinner("Processando..."):
        #   result, probability_df = patient.diagnosis()
        #   exp_pos, exp_neg = patient.explainer()
  
  if temp == False:
    st.title("Resultado")
    st.title(temp)
  
elif selected == "Sobre":
    st.title("Sobre")

    st.write("A VALERIA foi desenvolvida pelos alunos do Programa de Pós Graduação em Engenharia da Computação (PPGEC) da Universidade de Pernambuco (UPE) que fazem parte do grupo de pesquisa dotLAB Brazil, sob a orientação da Profa. Dra. Patricia Takako Endo, também do grupo de pesquisa e do PPGEC. Além disso, o projeto é desenvolvido em parceria com o Prof. Dr. Vanderson de Souza Sampaio, da Fundação de Medicina Tropical Doutor Heitor Vieira Dourado (FMT).")

    st.write("## Equipe")
    st.write("- [Me. Thomás Tabosa de Oliveira](http://lattes.cnpq.br/0487004776163889) - Pesquisador dotLAB Brazil")
    st.write("- [Me. Sebastião Rogério da Silva Neto](http://lattes.cnpq.br/5589837708731892) - Aluno de Doutorado do PPGEC")
    st.write("- [Me. Igor Vitor Teixera](http://lattes.cnpq.br/7616014062895959) - Pesquisador dotLAB Brazil")
    st.write("- [Dra. Patricia Takako Endo](http://lattes.cnpq.br/5055727404635243) - Professora do PPGEC")
    st.write("- [Dr. Vanderson de Souza Sampaio](http://lattes.cnpq.br/0039836167659650) - Professor da FMT")
    
    st.write("## Recursos")

    st.write("Este projeto possui recursos advindo dos seguintes editais:")
    st.write("- Edital CNPq/AWS 032/2019 - Acesso às Plataformas de Computação em Nuvem da AWS (Cloud Credits for Research), no valor de  USD \$ 11.226 (em créditos em serviço de computação em nuvem da AWS);")
    st.write("- Edital 006/2019 referente ao Programa de Apoio à Pesquisa - Universal Amazonas da FAPEAM, no valor de R\$ 62.212,00;")
    st.write("- Edital de Apoio a Pós-Graduação Stricto Sensu da UPE 2020 - Modalidade Auxílio para Projetos de Pesquisa (APQ), no valor de R\$ 5.000,00;")
    st.write("- Edital 20/2019 referente à Concessão de Bolsas de Pós-Graduação Stricto Sensu da FACEPE - Bolsa de Mestrado e de Doutorado.")

    st.write("## Parceiros")

    st.image("./assets/sobre.png")
  
