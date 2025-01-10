import speech_recognition as sr
import os

def voice_to_text(output_dir, shared_text, stop_event, user_input):
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    print("Starting speech recognition...")
    try:
        with microphone as source:
            recognizer.adjust_for_ambient_noise(source)
            while not stop_event.is_set():
                print("Listening...")
                audio = recognizer.listen(source)
                
                try:
                    text = recognizer.recognize_google(audio, language=user_input) # ko-KR, zh-TW .....
                    print(f"Recognized text: {text}")
                    shared_text.append(text)
                except sr.UnknownValueError:
                    print("Unable to recognize speech.")
                except sr.RequestError as e:
                    print(f"API request error: {e}")
    except KeyboardInterrupt:
        print("\nUser interrupted")
    finally:
        print("Speech recognition terminated.")

