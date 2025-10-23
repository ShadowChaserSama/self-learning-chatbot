import json
from difflib import SequenceMatcher
import pyttsx3


def speak(text):
    try:
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()
        engine.stop()
    except Exception as e:
        print(f"🔇 Voice error: {e}")


try:
    with open('text.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
except FileNotFoundError:
    data = {}

def save():
    with open('text.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

# === Oxşarlıq funksiyaları ===
def similarity(a, b):
    return SequenceMatcher(None, a, b).ratio()

def find_similar(question):
    if len(question) < 4:
        return None

    best_match = None
    best_score = 0.0

    for saved in data.keys():
        score = similarity(question, saved)
        if score > best_score:
            best_match = saved
            best_score = score

    if best_score >= 0.8:
        return best_match
    return None


def analyze(text, voice_mode):
    text = text.strip().lower()
    if not text:
        print("⚠️ You entered an empty question.")
        if voice_mode:
            speak("You entered an empty question.")
        return

    if text in data:
        print(f"💬 {data[text]}")
        if voice_mode:
            speak(data[text])
    else:
        similar = find_similar(text)
        if similar:
            print(f"🤔 Did you mean: '{similar}'?")
            print(f"💬 {data[similar]}")
            if voice_mode:
                speak(f"Did you mean {similar}?")
                speak(data[similar])
        else:
            print("❓ I don't know the answer to this question. Please teach me.")
            if voice_mode:
                speak("I don't know the answer to this question. Please teach me.")
            answer = input("Enter the answer: ").strip()
            if answer:
                data[text] = answer
                save()
                print("✅ Learned successfully. Thank you!")
                if voice_mode:
                    speak("Learned successfully. Thank you!")
            else:
                print("⚠️ Empty answer ignored.")
                if voice_mode:
                    speak("Empty answer ignored.")


print("🧠 Simple Self-Learning Chatbot\n")

mode = input("🔈 Do you want to activate voice mode? (yes/no): ").strip().lower()
voice_mode = mode in ["yes", "y", "1"]

if voice_mode:
    print("🎤 Voice mode activated! Speak through text input.")
    speak("Voice mode activated. Hello, how can I help you?")
else:
    print("💬 Text mode activated!")

print("Type 'exit' or 'quit' to stop.\n")

while True:
    question = input("🗨️ Question: ").strip()
    if question.lower() in ['exit', 'quit']:
        print("👋 Goodbye!")
        if voice_mode:
            speak("Goodbye!")
        break
    analyze(question, voice_mode)
