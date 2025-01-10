import threading
import keyboard
import os

from voice_to_text import voice_to_text
from record_audio_to_mp4 import record_audio_to_mp4
from summarize_text import sanitize_filename, summarize_text

# Use a threading.Event to handle the stop flag
stop_event = threading.Event()

def listen_for_exit():
    """Monitor for 'q' key press to stop the program."""
    while not stop_event.is_set():
        if keyboard.is_pressed("q"):
            print("'q' key detected. Terminating the program.")
            stop_event.set()

user_input = input("Select the language (en-US, ko-KR, zh-TW): ")
print(f"User selected language: {user_input}")

output_dir = "output_files"
shared_text = []  # Shared list to store recognized text

# Create threads
record_thread = threading.Thread(target=record_audio_to_mp4, args=(output_dir, stop_event))
voice_thread = threading.Thread(target=voice_to_text, args=(output_dir, shared_text, stop_event, user_input))
exit_thread = threading.Thread(target=listen_for_exit)

# Start threads
record_thread.start()
voice_thread.start()
exit_thread.start()

# Wait for threads to finish
record_thread.join()
voice_thread.join()
exit_thread.join()

# Summarize and save the text
all_text = " ".join(shared_text)
summary = summarize_text(all_text)

# Sanitize and save the summary
sanitized_summary = sanitize_filename(summary)
output_file = os.path.join(output_dir, f"{sanitized_summary[:50]}.txt")

with open(output_file, "w", encoding="utf-8") as file:
    file.write(all_text)

print(f"Text summarization completed and saved: {output_file}")
