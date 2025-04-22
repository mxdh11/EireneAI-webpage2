import streamlit as st
from transformers import pipeline
import requests

# Load emotion detection model
emotion_classifier = pipeline("text-classification", model="bhadresh-savani/distilbert-base-uncased-emotion")

# LibreTranslate API function
def translate_text(text, target_lang="ar"):
    url = "https://libretranslate.com/translate"
    payload = {
        "q": text,
        "source": "en",
        "target": target_lang,
        "format": "text"
    }
    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }
    response = requests.post(url, data=payload, headers=headers)
    return response.json().get("translatedText", "Translation error")

# Empathy Story Generator (simulated)
def generate_empathy_story():
    return (
        "Once, a child from Syria met a boy from Ukraine in a refugee shelter. They didn't speak the same language, "
        "but they played together every day. Through shared games, food, and smiles, they formed a bond stronger than words."
    )

# Emergency Help Instructions
def emergency_help():
    return (
        "It seems you're in distress. Please try to move to a safe location. Contact local authorities if you're in danger. "
        "Stay calm and try to reach someone you trust. Type 'emergency numbers' if you need more help."
    )

# Streamlit Mobile-Friendly UI
st.set_page_config(page_title="EireneAI", layout="centered")
st.markdown("""
    <style>
        .main {
            padding: 1rem;
            font-family: 'Arial';
        }
        .block-container {
            padding-top: 2rem;
        }
    </style>
""", unsafe_allow_html=True)

st.image("https://i.imgur.com/wBxrAlM.png", width=100)  # Logo placeholder
st.title("📱 EireneAI Mobile Preview")
st.markdown("A peace & empathy companion — for emotions, support, and culture 🌍")

# User Interaction
user_input = st.text_input("💬 How are you feeling today?")

if user_input:
    emotion_result = emotion_classifier(user_input)[0]
    label = emotion_result['label']
    score = emotion_result['score']

    st.markdown(f"### 🧠 Emotion Detected: **{label}** ({round(score * 100, 2)}%)")

    if label in ["anger", "fear", "sadness"]:
        st.markdown("### 🚨 Emergency Help")
        st.warning(emergency_help())
    else:
        st.markdown("### 🤝 You're doing okay!")
        st.success("Would you like a heartwarming story or cultural fact?")

    # Buttons for further help
    col1, col2 = st.columns(2)
    with col1:
        if st.button("📖 Empathy Story"):
            st.info(generate_empathy_story())
    with col2:
        if st.button("🌍 Translate Response"):
            translation = translate_text("I'm here to support you.", target_lang="ar")
            st.markdown(f"**Arabic Translation:** {translation}")

# Footer
st.markdown("""
---
**Team EireneAI**  
Janhavi Shajin • Maanasika Shankar • Mahdiya Fatima  
Pace International School | April 2025
""")