import pyttsx3

def speak(text: str):
    engine = pyttsx3.init()  # ✅ Move init inside the function
    engine.setProperty('rate', 150)
    engine.setProperty('volume', 1.0)
    engine.say(text)
    engine.runAndWait()
    engine.stop()  # ✅ Cleanly stop after each use

# --- Run it ---
def run():
    while True:  # ✅ Use a loop instead of recursion
        text = input("Enter text to speak: ")
        if text.lower() == "b":
            print("Exiting...")
            break
        else:
            speak(text)

run()
