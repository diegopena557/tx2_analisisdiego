import streamlit as st
from textblob import TextBlob
from googletrans import Translator

# --- Configuración inicial ---
st.set_page_config(page_title="Análisis de Sentimientos", page_icon="💬", layout="centered")

translator = Translator()
st.title('💡 Analizador de Sentimientos con TextBlob')

# --- Selector de tono visual ---
st.sidebar.title("🎨 Personaliza la interfaz")
tone = st.sidebar.selectbox("Selecciona el tono visual:", ["Optimista 🌞", "Serio 🌙", "Creativo 🌈"])

# --- Configuración de estilos según tono ---
if "Optimista" in tone:
    st.markdown("""
        <style>
            .stApp { background-color: #FFF8E1; color: #4E342E; }
            h1, h2, h3 { color: #F9A825; }
            .stButton>button { background-color: #FBC02D; color: white; border-radius: 10px; }
        </style>
    """, unsafe_allow_html=True)
    emoji_positive = "😄"
    emoji_neutral = "😐"
    emoji_negative = "😞"

elif "Serio" in tone:
    st.markdown("""
        <style>
            .stApp { background-color: #ECEFF1; color: #263238; }
            h1, h2, h3 { color: #37474F; }
            .stButton>button { background-color: #455A64; color: white; border-radius: 10px; }
        </style>
    """, unsafe_allow_html=True)
    emoji_positive = "🙂"
    emoji_neutral = "😐"
    emoji_negative = "🙁"

elif "Creativo" in tone:
    st.markdown("""
        <style>
            .stApp { background: linear-gradient(120deg, #FF9A9E 0%, #FAD0C4 100%); color: #4A148C; }
            h1, h2, h3 { color: #6A1B9A; }
            .stButton>button { background-color: #8E24AA; color: white; border-radius: 10px; }
        </style>
    """, unsafe_allow_html=True)
    emoji_positive = "🤩"
    emoji_neutral = "😶"
    emoji_negative = "😢"

# --- Panel lateral explicativo ---
with st.sidebar:
    st.subheader("📊 Polaridad y Subjetividad")
    st.markdown("""
        **Polaridad:**  
        Mide si el sentimiento expresado es positivo, negativo o neutral.  
        Valores entre -1 (muy negativo) y 1 (muy positivo).

        **Subjetividad:**  
        Indica cuánto del texto es una opinión o emoción (1) frente a hechos (0).
    """)

# --- Análisis de texto ---
with st.expander('🔍 Analizar Polaridad y Subjetividad'):
    text1 = st.text_area('Escribe un texto para analizar:')
    if text1:
        translation = translator.translate(text1, src="es", dest="en")
        trans_text = translation.text
        blob = TextBlob(trans_text)
        
        polarity = round(blob.sentiment.polarity, 2)
        subjectivity = round(blob.sentiment.subjectivity, 2)
        
        st.write(f'**Polaridad:** {polarity}')
        st.write(f'**Subjetividad:** {subjectivity}')
        
        if polarity >= 0.5:
            st.success(f"Sentimiento Positivo {emoji_positive}")
        elif polarity <= -0.5:
            st.error(f"Sentimiento Negativo {emoji_negative}")
        else:
            st.info(f"Sentimiento Neutral {emoji_neutral}")

# --- Corrección en inglés ---
with st.expander('📝 Corrección en inglés'):
    text2 = st.text_area('Escribe un texto en inglés:', key='4')
    if text2:
        blob2 = TextBlob(text2)
        st.write("✅ Versión corregida:")
        st.write(blob2.correct())

