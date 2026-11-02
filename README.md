# Voice Cloning with RealtimeTTS

This project demonstrates low-latency text-to-speech with voice cloning using [RealtimeTTS](https://github.com/KoljaB/RealtimeTTS) and the local [PocketTTS](https://pypi.org/project/pocket-tts/) model.

The example in [`voice_clone.py`](voice_clone.py) loads a short reference recording, uses it as a voice prompt, synthesizes text, and plays the generated audio as a stream through the computer's default audio device.

> Use voice cloning only with the speaker's permission. Do not impersonate people, mislead listeners, or upload private voice recordings and credentials to a public repository.

## Features

- Local voice cloning from a WAV reference clip
- Streaming audio playback while text is synthesized
- Simple Python entry point that is easy to customize
- RealtimeTTS support for additional TTS engines and integrations

## Requirements

- Python 3.10–3.14
- A working audio output device
- A short, clear reference recording in WAV format
- PortAudio/PyAudio support for playback
- Enough CPU/GPU memory for the PocketTTS model

## Installation

Create and activate a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate       # Linux/macOS
# .venv\Scripts\activate      # Windows PowerShell
python -m pip install --upgrade pip
```

Install the dependencies used by the voice-cloning example:

```bash
pip install pocket-tts pyaudio
```

To install the complete RealtimeTTS project and its optional engine dependencies instead:

```bash
pip install -e ".[all]"
```

On Debian/Ubuntu, PyAudio may require PortAudio development packages first:

```bash
sudo apt update
sudo apt install portaudio19-dev python3-dev
```

## Prepare a reference voice

Place a consented voice sample at `voices/my_voice.wav`, or update the path in `voice_clone.py`.

For best results, use a clean recording with:

- one speaker
- little or no background noise or music
- no overlapping speech
- a natural speaking style
- roughly 10–30 seconds of speech
- a mono WAV file, preferably 16-bit PCM

The `voices/` directory is ignored by Git so personal recordings are not accidentally published.

## Run the example

```bash
python voice_clone.py
```

Before running, edit these values in `voice_clone.py` if needed:

```python
voice_state = model.get_state_for_audio_prompt("voices/my_voice.wav")
text = "Text to synthesize goes here."
```

The script loads the model, creates a voice state from the reference audio, generates audio chunks, and sends them to PyAudio for immediate playback.

## Project layout

```text
.
├── voice_clone.py       # Voice-cloning example
├── RealtimeTTS/         # RealtimeTTS library source
├── voices/              # Local reference recordings (ignored by Git)
├── tests/               # Automated tests
├── requirements.txt     # Broad project dependencies
└── setup.py             # Package metadata and optional extras
```

## Troubleshooting

### `ModuleNotFoundError: pocket_tts`

Activate the virtual environment and install the example dependencies again:

```bash
python -m pip install pocket-tts pyaudio
```

### PyAudio fails to install

Install PortAudio using your operating system's package manager, then retry the pip command. On Windows, install a compatible PyAudio wheel or use the project's supported Python environment.

### Playback is silent or uses the wrong device

Check the operating system's default output device. For advanced routing, adapt the `audio.open(...)` call in `voice_clone.py` and provide the appropriate PyAudio device settings.

### Generation is slow

The first run may download model files. CPU performance, available memory, and the length of the input text all affect latency. Keep reference audio and synthesis text reasonably short while testing.

## Testing

Run the test suite from the repository root:

```bash
python -m pytest
```

Some tests and optional engines require additional dependencies or external credentials.

## GitHub: first push

Create an empty repository on GitHub, then run the following from this project directory. Replace the URL with your own repository URL:

```bash
git init
git branch -M main
git add README.md .gitignore LICENSE LICENSING_ADDENDUM.md CHANGELOG.md MANIFEST.in pyproject.toml setup.py requirements.txt RealtimeTTS voice_clone.py tests
git status
git commit -m "Document voice cloning project"
git remote add origin https://github.com/<your-username>/<your-repository>.git
git push -u origin main
```

If GitHub created a README or license for the repository, clone that repository first or resolve the resulting history conflict before pushing. Never commit API keys, `.venv/`, model caches, private voice recordings, or generated audio files.

For later updates:

```bash
git add .
git commit -m "Describe the change"
git push
```

## License

This project is distributed under the MIT License. See [`LICENSE`](LICENSE) and [`LICENSING_ADDENDUM.md`](LICENSING_ADDENDUM.md). Check the licenses and usage terms of PocketTTS, model files, and any other optional backend before redistribution.
