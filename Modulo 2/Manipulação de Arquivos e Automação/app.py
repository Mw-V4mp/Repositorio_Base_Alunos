import streamlit as st
from datetime import datetime

st.sidebar.title("Locadora de Automoveis")
st.sidebar.image("logo.png")
carro = st.sidebar.selectbox("Selecione o carro que deseja alugar: ", ["Uno","Fastback","Mustang GT","Civic Type R","BMW X7"])
st.image(f"{carro}.png", width=1000000)
valores_diarias = {"Uno":150, "Fastback":283, "Mustang GT":865, "Civic Type R":740, "BMW X7":518}
st.subheader(f"Valor da diária: R$ {valores_diarias[carro]}")
data_retirada = st.date_input("Selecione a data de retirada: ", datetime.now())
data_devolucao = st.date_input("Selecione a data de devolução", data_retirada)

if st.button("Alugar"):
    dias = (data_devolucao - data_retirada).days
    total = dias * valores_diarias[carro]
    st.success(f"Alugando o carro por {dias} dias o custo total é: R$ {total}")