import streamlit as st
import pandas as pd
import random
import time

st.set_page_config(page_title="Monitoramento Ambiental", layout="centered")

st.title("📊 Monitoramento de Umidade - Escola Vivendo e Aprendendo")
st.markdown("Local: 604 Norte, Brasília - DF")
st.markdown("Coordenadas: **Latitude: -15.7833, Longitude: -47.9167**")

# Simula leituras de umidade
def gerar_umidade():
    return round(random.uniform(20, 60), 2)

# Dados simulados
if 'umidades' not in st.session_state:
    st.session_state.umidades = []

umidade_atual = gerar_umidade()
st.session_state.umidades.append(umidade_atual)

# Mostrar a leitura atual
st.metric("Umidade Atual", f"{umidade_atual}%")

# Verificação de risco
if umidade_atual < 30:
    st.error("⚠️ Atenção: Nível de umidade muito baixo! Risco à saúde!")

# Mostrar gráfico
st.line_chart(st.session_state.umidades)

st.caption("Atualize a página para nova leitura")
