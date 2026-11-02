from pocket_tts import TTSModel
import pyaudio


model = TTSModel.load_model()

voice_state = model.get_state_for_audio_prompt("alba")

audio = pyaudio.PyAudio()

stream = audio.open(
    format=pyaudio.paFloat32,
    channels=1,
    rate=24000,
    output=True,
)

print("Local PocketTTS")
print("Type 'exit' to quit.\n")

try:
    while True:
        text = input("Enter text: ")

        if text.lower() == "exit":
            break

        if not text.strip():
            continue

        print("Speaking...")

        for chunk in model.generate_audio_stream(
            voice_state,
            text,
        ):
            stream.write(chunk.numpy().tobytes())

        print("Done.\n")

finally:
    stream.stop_stream()
    stream.close()
    audio.terminate()