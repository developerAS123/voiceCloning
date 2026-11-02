from RealtimeTTS import TextToAudioStream, PocketTTSEngine

if __name__ == "__main__":
    engine = PocketTTSEngine()

    stream = TextToAudioStream(engine)

    stream.feed(
        "Hello! This is a real time text to speech test "
        "using PocketTTS with RealtimeTTS."
    )

    stream.play()