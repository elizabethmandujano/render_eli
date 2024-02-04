import streamlit as st

st.header('Lanzar una moneda')

number_of_trials = st.slider ('¿Cuántos intentos quieres?' , 1, 1000, 10)
start_button = st.button( 'Empezar')

if start_button:
  st.write(f'Experimento con {number_of_trials} intentos en curso.')

st.write ('Esta aplicación aún no es funcional. Sigue en contrucción... disculpe la demora jiji')
