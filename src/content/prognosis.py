import streamlit as st

from models.patient import Patient

def prognosis_page():
  st.write("# Preencha os campos com as informações do paciente para obter o resultado:")
  
  patient = Patient()
  
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
    
    if (st.form_submit_button("Resultado", use_container_width=True)):
      with st.spinner("Processando..."):
        result, probability_df = patient.diagnosis()
        exp_pos, exp_neg, fig = patient.explainer()
        
      st.write(f"## O resultado mais provável é **{result}**")

      st.write("### Resultado detalhado")

      st.write(f"Abaixo é possível observar o resultado detalhado. Caso haja alguma dúvida sobre como esses valores foram gerados, você pode consultar a tela de Ajuda no canto esquerdo.")

      st.write("#### Probabilidade de cada doença")
      st.dataframe(probability_df.sort_values(by=["Porcentagem"], ascending=False))

      st.write(f"Atributos que contribuíram para o resultado {result}")
      # st.dataframe(exp_pos)
      st.plotly_chart(fig)

      st.write("---")
      st.warning("**AVISO IMPORTANTE: este resultado é proveniente de um modelo de _machine learning_, não é definitivo. Analise também a situação epidemiológica da sua região.**")