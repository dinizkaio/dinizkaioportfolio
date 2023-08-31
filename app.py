import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


st.markdown(
           """
 # AnÃ¡lise de performance de Estudantes
"""             
            )

def mostra_linhas(df):
    qtd = st.sidebar.slider("Selecione quantas linhas vocÃª quer", min_value=1, max_value=len(df),step=1)
    st.write(df.head(qtd).style.format(subset=['math score'], formatter='{:.2f}'))

df = pd.read_csv('StudentsPerformance.csv', sep=';')

checkbox = st.sidebar.checkbox("Show table")

if checkbox:

    st.sidebar.markdown('## Filtro de dados')

    gen = list(df['gender'].unique())
    gen.append("All")

    genders = st.sidebar.selectbox("Selecione o gÃªnero", options=gen)

    if genders != "All":

        df_gen = df.query('gender == @genders')
        mostra_linhas(df_gen)
    else:
        mostra_linhas(df)


    
# st.dataframe(df)
# plt.title('Pairplot')
# st.pyplot(sns.pairplot(df))

