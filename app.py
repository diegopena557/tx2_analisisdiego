import streamlit as st
from textblob import TextBlob
from googletrans import Translator
import matplotlib.pyplot as plt

# Configuración inicial
translator = Translator()
st.set_page_config(page_title="EmoText Analyzer 💬", layout="centered")

st.title("💬 EmoText Analyzer — Analiza emociones y mejora tu tono")
st.write("""
Esta aplicación analiza el **sentimiento y la subjetividad** de un texto y te sugiere cómo **mejorar el tono emocional o la claridad**.  
Escribe una frase en **español o inglés** para comenzar.
""")

# 📘 Sidebar con información
with st.sidebar:
    st.header("📊 Conceptos")
    st.markdown("""
    **Polaridad:**  
    Valor entre -1 (muy negativo) y 1 (muy positivo).  
    **Subjetividad:**  
    Valor entre 0 (objetivo) y 1 (subjetivo).
    
    **Nuevo:**  
    También se analiza el tipo de **emoción** predominante y se ofrecen sugerencias de mejora del tono.
    """)

# 🧩 Expander: Análisis de sentimiento
with st.expander("🧠 Analizar Polaridad, Subjetividad y Emoción"):
    text1 = st.text_area("Escribe una frase:", placeholder="Por ejemplo: Hoy fue un día increíble, lleno de energía 🌞")

    if text1:
        # Detectar idioma y traducir si es necesario
        try:
            translation = translator.translate(text1, src="auto", dest="en")
            trans_text = translation.text
        except Exception:
            trans_text = text1  # En caso de error, usar texto original
        
        blob = TextBlob(trans_text)

        polarity = round(blob.sentiment.polarity, 2)
        subjectivity = round(blob.sentiment.subjectivity, 2)

        # Mostrar resultados
        st.write(f"**Polarity:** {polarity}")
        st.write(f"**Subjectivity:** {subjectivity}")

        # Determinar emoción aproximada
        if polarity >= 0.6:
            emotion = "Alegría 😄"
            suggestion = "¡Sigue transmitiendo energía positiva! Podrías agregar un toque de gratitud o humor."
        elif polarity >= 0.2:
            emotion = "Tranquilidad 🙂"
            suggestion = "Podrías hacerlo más entusiasta agregando adjetivos positivos."
        elif polarity <= -0.6:
            emotion = "Tristeza 😢"
            suggestion = "Tal vez quieras reformularlo con esperanza o resiliencia."
        elif polarity <= -0.2:
            emotion = "Enojo 😠"
            suggestion = "Intenta suavizar el tono usando expresiones más neutras o constructivas."
        else:
            emotion = "Neutral 😐"
            suggestion = "Puedes hacerlo más expresivo si agregas emociones o detalles."

        # Mostrar emoción
        st.subheader(f"💡 Emoción detectada: {emotion}")
        st.info(suggestion)

        # Visualización gráfica
        fig, ax = plt.subplots(figsize=(5, 0.4))
        ax.barh(["Sentimiento"], [polarity], color="skyblue")
        ax.set_xlim(-1, 1)
        ax.axvline(0, color="black", linewidth=0.8)
        ax.set_title("📈 Termómetro emocional")
        st.pyplot(fig)

# 📝 Expander: Corrección gramatical
with st.expander("✍️ Corrección en inglés"):
    text2 = st.text_area("Escribe una frase en inglés:", key="correction", placeholder="I is happy to learn NLP")
    if text2:
        blob2 = TextBlob(text2)
        corrected = blob2.correct()
        st.write("✅ **Versión corregida:**")
        st.success(corrected)

# 🌈 Expander: Reformulación de tono
with st.expander("🎨 Reformula tu texto con otro tono"):
    text3 = st.text_area("Introduce tu frase:", key="rewrite", placeholder="I am very tired of studying all day.")
    tone = st.selectbox
