import streamlit as st
import speech_recognition as sr
import pyttsx3
import pywhatkit
import warnings
import random
from transformers import pipeline

# ------------------------------
# Suppress warnings
# ------------------------------
warnings.filterwarnings("ignore", category=FutureWarning)

# ------------------------------
# Streamlit Page Config & CSS
# ------------------------------
st.set_page_config(page_title="🎧 SonicMind: When BERT Learns to Listen", layout="centered")

st.markdown("""
    <style>
        .stApp {
            background-image: linear-gradient(to right top, #1a1a2e, #16213e, #0f3460, #533483, #e94560);
            background-attachment: fixed;
            color: white;
        }
        h1, h2, h3, p, .stMarkdown {
            color: #f1f1f1 !important;
        }
        .stButton button {
            background-color: #e94560;
            color: white;
            border-radius: 10px;
            border: none;
            padding: 0.6em 1.2em;
            font-size: 16px;
            font-weight: bold;
        }
        .stButton button:hover {
            background-color: #ff6b81;
            color: black;
        }
    </style>
""", unsafe_allow_html=True)

# ------------------------------
# Initialize
# ------------------------------
recognizer = sr.Recognizer()
engine = pyttsx3.init()

@st.cache_resource
def load_classifier():
    """Load smaller, faster BERT model."""
    return pipeline("zero-shot-classification", model="typeform/distilbert-base-uncased-mnli")

classifier = load_classifier()

# ------------------------------
# Helper: Speak Text
# ------------------------------
def speak(text):
    try:
        engine.say(text)
        engine.runAndWait()
    except RuntimeError:
        pass  # avoids Streamlit run loop issue

# ------------------------------
# Helper: Listen to Voice
# ------------------------------
def listen():
    with sr.Microphone() as source:
        st.info("🎙️ Listening... Speak now!")
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio)
            return text.lower()
        except sr.UnknownValueError:
            return "Sorry, I couldn't understand you."
        except sr.RequestError:
            return "Speech recognition service unavailable."

# ------------------------------
# Helper: Get Random Joke
# ------------------------------
def get_joke():
    jokes = [
        "Why don’t scientists trust atoms? Because they make up everything!",
        "Why did the computer go to therapy? It had too many bytes of emotional baggage.",
        "Why did the scarecrow win an award? Because he was outstanding in his field!",
        "I told my computer I needed a break, and now it won’t stop sending me KitKat ads.",
        "Why was the math book sad? Because it had too many problems."
    ]
    return random.choice(jokes)

# ------------------------------
# Classify Intent
# ------------------------------
def classify_intent(text):
    labels = ["play_music", "tell_joke", "search_web", "greeting", "unknown"]
    result = classifier(text, labels)
    return result["labels"][0]

# ------------------------------
# Process Command
# ------------------------------
def process_command(cmd):
    intent = classify_intent(cmd)
    st.write(f"🧠 **Detected Intent:** `{intent}`")

    if intent == "play_music" or "play" in cmd:
        song = cmd.replace("play", "").strip()
        if song:
            speak(f"Playing {song}")
            st.success(f"🎵 Playing **{song}** on YouTube...")
            pywhatkit.playonyt(song)
        else:
            st.warning("Please specify which song you want to play.")

    elif intent == "tell_joke":
        joke = get_joke()
        speak(joke)
        st.success(f"😂 {joke}")

    elif intent == "search_web" or "search" in cmd:
        query = cmd.replace("search", "").strip()
        if query:
            speak(f"Searching for {query}")
            st.info(f"🌐 Searching Google for **{query}**...")
            pywhatkit.search(query)
        else:
            st.warning("Please tell me what to search for.")

    elif intent == "greeting":
        greet = "Hello! How can I help you today?"
        speak(greet)
        st.success(greet)

    else:
        speak("Sorry, I didn’t understand the command.")
        st.warning("🤔 Could not understand your command.")

# ------------------------------
# Streamlit UI
# ------------------------------
st.title("🎧 Smart Voice Assistant (BERT + Streamlit)")
st.markdown("🎤 Try commands like:")
st.markdown("- **'Play Despacito'** 🎵")
st.markdown("- **'Tell me a joke'** 😂")
st.markdown("- **'Search Python tutorials'** 🌐")

# Text input option
user_input = st.text_input("📝 Type or say your command:")

# Button controls
col1, col2 = st.columns(2)
with col1:
    if st.button("🎙️ Speak"):
        command = listen()
        st.write(f"🗣️ You said: **{command}**")
        process_command(command)

with col2:
    if st.button("🚀 Run Command"):
        if user_input:
            st.write(f"🗣️ You typed: **{user_input}**")
            process_command(user_input)
        else:
            st.warning("Please type a command first!")
