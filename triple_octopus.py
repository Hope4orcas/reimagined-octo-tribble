import streamlit as st

texto=":violet[hellouda]"
st.markdown(texto)

asignaturas= ("Lengua","Inglés","Matemáticas","E.F","Física y Química")
resultado=st.radio("¿Cual es tu asignatura favorita", asignaturas)

st.write(resultado)
if resultado==asignaturas[0]:
  st.warning("No")
if resultado==asignaturas[1]:
  st.baloons()
if resutado==asignaturas[2]:
  st.success("Buena elección")
if resultado==asignaturas[3]:
  st.error("incorrecto")
if resultado==asignaturas[4]:
  st.success("Biennnnn")
