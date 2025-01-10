import os
import wave
import pyaudio
from datetime import datetime
from pydub import AudioSegment

def record_audio_to_mp4(output_dir, stop_event):
    current_time = datetime.now().strftime("%M-%S-%f") 
    output_mp3 = os.path.join(output_dir, f"recorded_audio_{current_time}.mp3")
    
    chunk = 1024  # Buffer size
    format = pyaudio.paInt16  # 16-bit audio
    channels = 1  # Mono audio
    rate = 44100  # Sampling rate
    temp_wav = "temp.wav"  # Temporary WAV file path

    audio = pyaudio.PyAudio()
    print("Recording started (Press 'q' to stop)...")
    stream = audio.open(format=format, channels=channels,
                        rate=rate, input=True,
                        frames_per_buffer=chunk)
    frames = []

    try:
        while not stop_event.is_set():
            data = stream.read(chunk)
            frames.append(data)
    except Exception as e:
        print(f"Error occurred during recording: {e}")
    finally:
        print("Recording stopped.")

        # Stop and release the stream and resources
        stream.stop_stream()
        stream.close()
        audio.terminate()

        # Save to WAV file
        with wave.open(temp_wav, 'wb') as wf:
            wf.setnchannels(channels)
            wf.setsampwidth(audio.get_sample_size(format))
            wf.setframerate(rate)
            wf.writeframes(b''.join(frames))

        # Convert to MP3 and save
        sound = AudioSegment.from_wav(temp_wav)
        sound.export(output_mp3, format="mp3")
        os.remove(temp_wav) 
        print(f"Recording saved as: {output_mp3}")
