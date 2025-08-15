import google.generativeai as genai
import speech_recognition as sr
import pyttsx3
import webbrowser

# ===== CONFIGURE GEMINI =====
API_KEY = "AIzaSyD4-HSn6FvX5V94N8yoHvlhKBqvqd-6ICw" # Replace with your Gemini API key
genai.configure(api_key=API_KEY)

# Use Gemini 1.5 Flash (free-tier friendly)
model = genai.GenerativeModel("gemini-1.5-flash")

# ===== SPEECH TO TEXT =====
def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Neo is listening...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    try:
        text = r.recognize_google(audio)
        print(f"🗣 You: {text}")
        return text
    except sr.UnknownValueError:
        print("❌ Neo: I couldn't catch that, please repeat.")
        return ""
    except sr.RequestError:
        print("⚠ Neo: Speech service is down.")
        return ""

# ===== TEXT TO SPEECH =====
def speak(text):
    engine = pyttsx3.init()
    engine.setProperty("rate", 170)
    engine.setProperty("volume", 1)
    voices = engine.getProperty("voices")
    engine.setProperty("voice", voices[1].id)  # female voice
    engine.say(text)
    engine.runAndWait()


def main():
    speak("Hello, I am Neo. How can I help you today?")
    print("🤖 Neo is ready! Say 'exit' to quit.")

    while True:
        query = listen()
        query.lower()

        if query.strip() == "":
            continue

        if query.lower() in ["exit", "quit", "stop"]:
            speak("Goodbye, have a great day!")
            break


        if query.lower() in [f"open youtube"]:
            webbrowser.open("https://www.youtube.com")
            speak("Opening YouTube for you.")
            speak("What would you like to search for on YouTube?")
            newquery = listen()
            print(newquery)  
            webbrowser.open(f"https://www.youtube.com/results?search_query={newquery}")
            
            
       

        # Personality prompt with "Answer in short"
        personality_prompt = """
        You are Neo, my personal voice assistant.
        You should:
        - Be concise and clear.
        - Sound friendly and conversational.
        - Avoid overly technical explanations unless requested.
        - Use simple everyday language.
        - Give small and precise answers.
        - Answer in short.
        """

        # Send to Gemini API
        full_prompt = f"{personality_prompt}\nUser: {query}\nNeo:"
        response = model.generate_content(full_prompt)
        reply = response.text
        print(f"🤖 Neo: {reply}")
        speak(reply)

if __name__ == "__main__":
    main()
