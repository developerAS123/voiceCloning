from pocket_tts import TTSModel
import pyaudio


TEXT = "Hello! This is real time text to speech running locally on my computer."


model = TTSModel.load_model()

voice_state = model.get_state_for_audio_prompt("alba")


audio = pyaudio.PyAudio()

stream = audio.open(
    format=pyaudio.paFloat32,
    channels=1,
    rate=24000,
    output=True,
)


print("Speaking...")

for chunk in model.generate_audio_stream(
    voice_state,
    TEXT,
):
    stream.write(chunk.numpy().tobytes())


stream.stop_stream()
stream.close()
audio.terminate()

print("Finished.")