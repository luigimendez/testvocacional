import streamlit as st

# Preguntas y respuestas
preguntas = [
    ("¿Qué actividad disfrutas más?", ["Leer artículos científicos", "Pintar o dibujar", "Reparar cosas", "Ayudar a personas"]),
    ("¿Qué asignatura prefieres?", ["Matemáticas", "Arte", "Tecnología", "Psicología"]),
    ("¿Cómo te gusta trabajar?", ["Analizando datos", "Creando cosas nuevas", "Con herramientas", "En equipo con personas"]),
    ("¿Qué hobby te interesa más?", ["Resolver acertijos", "Tocar un instrumento", "Armar circuitos", "Voluntariado"]),
    ("¿Qué valoras más en un trabajo?", ["Descubrimiento", "Expresión", "Precisión", "Impacto social"]),
    ("¿Con qué palabra te identificas más?", ["Lógico", "Creativo", "Práctico", "Empático"])
]

# Mapa de respuestas a perfiles
perfil_map = {
    "Leer artículos científicos": "científico",
    "Matemáticas": "científico",
    "Analizando datos": "científico",
    "Resolver acertijos": "científico",
    "Descubrimiento": "científico",
    "Lógico": "científico",
    "Pintar o dibujar": "artístico",
    "Arte": "artístico",
    "Creando cosas nuevas": "artístico",
    "Tocar un instrumento": "artístico",
    "Expresión": "artístico",
    "Creativo": "artístico",
    "Reparar cosas": "técnico",
    "Tecnología": "técnico",
    "Con herramientas": "técnico",
    "Armar circuitos": "técnico",
    "Precisión": "técnico",
    "Práctico": "técnico",
    "Ayudar a personas": "social",
    "Psicología": "social",
    "En equipo con personas": "social",
    "Voluntariado": "social",
    "Impacto social": "social",
    "Empático": "social"
}

# Recomendaciones por perfil
recomendaciones = {
    "científico": "🔬 Perfil Científico: Podrías destacar en áreas como Física, Matemáticas, Biología, Ingeniería o Investigación.",
    "artístico": "🎨 Perfil Artístico: Podrías sobresalir en Diseño, Música, Artes Visuales, Publicidad o Cine.",
    "técnico": "🔧 Perfil Técnico: Carreras como Mecatrónica, Robótica, Sistemas o Mantenimiento son una excelente opción.",
    "social": "👥 Perfil Social: Psicología, Educación, Trabajo Social o Comunicación podrían ser tu vocación."
}

# Inicializar sesión de usuario
if "indice" not in st.session_state:
    st.session_state.indice = 0
    st.session_state.respuestas = []
    st.session_state.conteo = {"científico": 0, "artístico": 0, "técnico": 0, "social": 0}

# Mostrar progreso
st.progress(st.session_state.indice / len(preguntas))

# Mostrar pregunta actual
if st.session_state.indice < len(preguntas):
    pregunta, opciones = preguntas[st.session_state.indice]
    st.write(f"**{pregunta}**")
    seleccion = st.radio("Selecciona una opción:", opciones, key=f"preg_{st.session_state.indice}")

    if st.button("Siguiente"):
        st.session_state.respuestas.append(seleccion)
        perfil = perfil_map.get(seleccion)
        if perfil:
            st.session_state.conteo[perfil] += 1
        st.session_state.indice += 1
        st.experimental_rerun()

# Mostrar resultado final
else:
    st.success("✅ Test completado.")
    perfil_final = max(st.session_state.conteo, key=st.session_state.conteo.get)
    st.markdown(f"### 🔎 Tu perfil vocacional dominante es: **{perfil_final.upper()}**")
    st.write(recomendaciones[perfil_final])
    
    st.subheader("📋 Respuestas seleccionadas:")
    for i, r in enumerate(st.session_state.respuestas):
        st.write(f"{i+1}. {preguntas[i][0]} → {r}")

    if st.button("🔄 Reiniciar"):
        st.session_state.indice = 0
        st.session_state.respuestas = []
        st.session_state.conteo = {"científico": 0, "artístico": 0, "técnico": 0, "social": 0}
        st.experimental_rerun()
