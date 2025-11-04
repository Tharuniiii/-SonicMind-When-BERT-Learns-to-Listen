# -SonicMind-When-BERT-Learns-to-Listen
SonicMind is an AI-powered voice assistant that can understand natural language commands, play music, tell jokes, and even search the web — all through voice or text. Built using Streamlit, BERT (via Hugging Face Transformers), and Speech Recognition, it bridges the gap between human speech and intelligent machine understanding.


# 🚀 Features

✅ Voice Recognition – Speak naturally, and SonicMind will understand you using Google Speech Recognition.
✅ Intent Detection with BERT – Uses zero-shot classification via DistilBERT to identify what you mean.
✅ Play Songs on YouTube – Just say “Play song name” and it automatically opens YouTube and plays it.
✅ Tell Jokes – Need a laugh? Ask “Tell me a joke” and SonicMind delivers one.
✅ Search Online – Say “Search for topic” to get quick results through Google.
✅ Text or Voice Input – Use your microphone or type your command manually.
✅ Stylish Streamlit UI – A custom CSS gradient interface for a vibrant and modern look.

# 🧠 Tech Stack
```
| Component                       | Technology Used                      |
| ------------------------------- | ------------------------------------ |
| **Frontend**                    | Streamlit (Python)                   |
| **Speech Recognition**          | `speech_recognition`                 |
| **Text-to-Speech (TTS)**        | `pyttsx3`                            |
| **Intent Classification (NLP)** | BERT via Hugging Face `transformers` |
| **Automation**                  | `pywhatkit` (for YouTube and Google) |
| **Core Language**               | Python 3.9+                          |
```

# 📂 Project Structure
```
SonicMind/
│
├── app.py                     # Main Streamlit app file
├── requirements.txt            # Python dependencies
├── README.md                   # Documentation file
└── assets/                     # Optional: for icons or background media

```
# 🗣️ Example Commands

🎵 “Play Shape of You” → Plays the song on YouTube.
😂 “Tell me a joke” → Returns a random tech-related joke.
🌐 “Search for AI tutorials” → Opens a Google search for that topic.
👋 “Hello” → Greets you back warmly.

# 🖌️ UI Preview

🎨 Gradient background + interactive buttons

Left button → Speak your command

Right button → Run typed command

You can easily customize the theme by modifying the CSS in the st.markdown() section inside app.py.

# 💡 Future Enhancements

🔹 Add chat-based conversation memory using a lightweight LLM or BERT QA model.
🔹 Integrate Spotify API for authenticated music playback.
🔹 Add weather, news, and reminders modules.
🔹 Add voice wake word (“Hey SonicMind”) to activate the mic automatically.

# 🧩 Dependencies
```
streamlit
speechrecognition
pyttsx3
pywhatkit
transformers
torch
(Optional: add pyaudio for microphone input)
```

# Sample output
<img width="1126" height="820" alt="image" src="https://github.com/user-attachments/assets/c9a07c97-2321-433e-99ae-dedd9c51b2a9" />

⭐ Acknowledgments

Hugging Face Transformers
 for BERT models

Streamlit
 for the awesome UI framework

PyWhatKit
 for music automation

SpeechRecognition
 for voice input

 ---
 “SonicMind isn’t just listening — it’s understanding you.” 🎙️
