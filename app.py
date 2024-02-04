import streamlit as st
import scipy.stats
import time

st.header('Lanzar una moneda')

chart = st.line_chart([0.5])

def toss_coin(n): #funcion que hace el lanzamiento de una moneda
  trial_outcomes = scyipy.stats.bernoulli.rvs(p=0.5, size=n)

  mean = None
  outcome_no = 0
  outcome_1_count = 0

  for r in trial_outcomes:
    outcome_no += 1
    if r == 1:
      outcome_1_count += 1
    mean = outcome_1_count/outcome_no
    chart.add_rows([mean])
    time.sleep(0.05)
return mean

number_of_trials = st.slider ('¿Cuántos intentos quieres?' , 1, 1000, 10)
start_button = st.button( 'Empezar')

if start_button:
  st.write(f'Experimento con {number_of_trials} intentos en curso.')
  mean = toss_coin(number_of_trials)

st.write ('App creada por eli jiji')
