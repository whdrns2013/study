from core.whisper_api import whisper_api
from core.whisper_translation_api import whisper_translation_api
from core.whisper_local import whisper_local
from core.whisper_local_with_torch import whisper_local_with_torch
# from core.speaker_diarization import speaker_diarization
import time

def whisper_api_test():
    audio_file_path = "data/mp3/audio.mp3"
    transcription = whisper_api(audio_file_path)
    print(transcription)

def whisper_translation_api_test():
    audio_file_path = "data/mp3/audio.mp3"
    translation = whisper_translation_api(audio_file_path)
    print(translation)

def whisper_local_test():
    audio_file_path = "data/mp3/audio.mp3"
    translation = whisper_local(audio_file_path)
    print(translation)    

def whisper_local_with_torch_test():
    audio_file_path = "data/mp3/audio.mp3"
    transcription = whisper_local_with_torch(audio_file_path)
    print(transcription)

# def speaker_diarization_test():
#     audio_file_path = "data/mp3/guitar.mp3"
#     diarization_result = speaker_diarization(audio_file_path)
#     print(diarization_result)

def main():
    start = time.time()
    whisper_local_with_torch_test()
    print(f"소요 시간 : {time.time() - start}")


if __name__ == "__main__":
    main()
