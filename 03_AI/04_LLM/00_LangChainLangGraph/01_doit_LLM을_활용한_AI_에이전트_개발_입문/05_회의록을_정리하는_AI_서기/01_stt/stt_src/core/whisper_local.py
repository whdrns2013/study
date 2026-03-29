from transformers import WhisperProcessor, WhisperForConditionalGeneration
import librosa
import time
from config.settings import config
import re

# 오디오 30초 청킹
def chunk_audio(audio,
                sr:int=int(config["default"]["audio.sampling_rate"]),
                chunk_sec:int=30,
                overlap_sec:int=5): # 청크 오버랩
    chunk_size = sr * chunk_sec
    overlap_size = sr * overlap_sec
    hop_size = chunk_size - overlap_size
    
    chunks = []
    for start in range(0, len(audio), hop_size): # audio 전체를 hop_size 만큼 반복
        end = start + chunk_size # end 에 hop_size 가 아닌 chunk_size 를 더하므로, overlap_sec 만큼 겹침
        chunk = audio[start:end]
        if len(chunk) < sr:
            break
        chunks.append(chunk)
    return chunks

# 문장 정규화
def normalize(text: str) -> str:
    text = text.strip()
    text = re.sub(r"\s+", "", text)   # 공백 제거
    return text

# 오버랩 시간 내 중복 어휘 제거
def remove_overlap(prev_text: str,
                   curr_text: str,
                   min_overlap_chars: int = 1) -> str:
    prev_norm = normalize(prev_text)
    curr_norm = normalize(curr_text)
    max_check = min(len(prev_norm), len(curr_norm)) # 두 텍스트 중 짧은 길이까지만 비교
    for k in range(max_check, min_overlap_chars, -1): # 문장 전체 비교 -> 한 글자씩 줄여나감
        if prev_norm[-k:] == curr_norm[:k]: # 앞문장의 뒤에서부터 k자, 뒷문장의 앞에서부터 k자를 비교
            cut = next(j for j in range(len(curr_text)+1) if normalize(curr_text[:j]) == curr_norm[:k])
            return curr_text[cut:]
    return curr_text # 중복이 없으면 현재 텍스트 그대로 반환

def whisper_local(audio_file_path:str,
                  model_name:str="openai/whisper-small",
                  sr:int=int(config["default"]["audio.sampling_rate"]))->list[str]:
    # config
    model_save_dir = config["path"]["dir.model.whisper"]
    
    # load model and processor
    processor = WhisperProcessor.from_pretrained(
        model_name,
        cache_dir = model_save_dir
    )
    model = WhisperForConditionalGeneration.from_pretrained(
        model_name,
        cache_dir = model_save_dir
    )
    model.config.forced_decoder_ids = None
    
    # load audio data
    start = time.time()
    audio_array, sampling_rate = librosa.load(audio_file_path, sr=sr)
    chunked_audios = chunk_audio(audio_array)
    transcription = []
    for audio in chunked_audios:
        input_features = processor(
            audio,
            sampling_rate = sr,
            return_tensors="pt"
        ).input_features
        
        # inference
        ## generate token ids
        predicted_ids = model.generate(input_features)
        ## decode token ids to text
        text = processor.batch_decode(predicted_ids,skip_special_tokens=False)[0].lstrip() # whisper 선행에 공백이 1개 있으므로 제거
        
        if transcription:
            text = remove_overlap(transcription[-1], text)
        
        transcription.append(text)
    
    print(f"inference 소요 시간 : {time.time() - start}")
    
    return transcription
    
    
