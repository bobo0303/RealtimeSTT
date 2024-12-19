from RealtimeSTT import AudioToTextRecorder

if __name__ == '__main__':
    with AudioToTextRecorder(use_microphone=False) as recorder:
        with open("audio/hey_check_14.pcm", "rb") as f:
            audio_chunk = f.read()
        recorder.feed_audio(audio_chunk)
        print("Transcription: ", recorder.text())