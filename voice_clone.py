from pocket_tts import TTSModel
import pyaudio

model = TTSModel.load_model()

voice_state = model.get_state_for_audio_prompt(
    "voices/dipama.wav"
)

audio = pyaudio.PyAudio()

stream = audio.open(
    format=pyaudio.paFloat32,
    channels=1,
    rate=model.sample_rate,
    output=True,
)

print("Speaking...")

text = "Good morning, everyone.\nToday, I want to talk about one of the simplest yet greatest joys in life: sleeping in on a Sunday morning.\nWe live in a fast world. All week, our alarms ring way too early. We rush to school, to work, or through our daily chores. We check our phones, reply to messages, and run from one task to another. Because of this busy routine, Sunday morning acts like a quiet pause button for our minds and bodies.\nThere is a unique magic in waking up slowly. You hear the quiet outside. You realize you do not need to rush out of bed. For me, that extra hour under the warm blanket feels like a small reward for a long week. After that rest, sipping a hot cup of tea while looking out the window feels peaceful and refreshing.\nOf course, some people say that sleeping too late wastes the day. And it is true that we should not sleep away our lives. But taking one morning to truly rest helps us recharge. It lets us catch our breath and find our balance again before a new week begins.\nTo conclude, I believe we should cherish these quiet moments of rest. They give us the energy and the calm we need to face the busy days ahead. Thank you."


for chunk in model.generate_audio_stream(
    voice_state,
    text
):
    stream.write(chunk.numpy().tobytes())

stream.stop_stream()
stream.close()
audio.terminate()

print("Finished.")