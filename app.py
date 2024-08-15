import streamlit as st
from PIL import Image

st.title("Focas bebés")

st.header("En este espacio voy a hablar de las focas bebés.")
st.write("Miren ahí, hay una foca bebé.")
image = Image.open('foquita.jpg')

st.write(image, caption='Una foca bebé en la naturaleza')

texto = st.text_input('Escribe algo', 'Este es mi texto')
st.write('El texto escrito es', texto)

st.subheader("Ahora usemos 2 columnas para hablar de las focas bebés")

col1, col2 = st.columns(2)

with col1:
  st.subheader("Características de las focas bebés")
  st.write("Viven en lugares super fríos y nadan muy rápido")
  resp = st.checkbox('Estoy de acuerdo')
  if resp:
    st.write('Correcto!')

with col2:
  st.subheader("Ahora hablemos de sus depredadores")
  modo = st.radio("¿Qué depredadores tienen las focas?", ('Otras focas', 'Orcas', 'Ninguno'))
  if modo == 'Otras focas':
    st.write('Algunas veces sí :(')
  if modo == 'Orcas':
    st.write('Sii, las orcas son malas ;(')
  if modo == 'Ninguno':
    st.write('Ojalá no tuvieran ninguno')
