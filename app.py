import streamlit as st
from PIL import Image

st.title("Focas bebés")

st.header("En este espacio voy a hablar de las focas bebés")
st.write("Miren ahí hay una foca bebé")
image = Image.open('foquitas.jpg')

st.write(image, caption='Una foca bebé en la naturaleza')

texto = st.text_input('Escribe algo', 'Este es mi texto')
st.write('El texto escrito es', texto)
