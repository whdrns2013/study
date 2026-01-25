
## OpenAI Whisper(위스퍼)  

![alt text](/assets/images/image.png)  
[https://github.com/openai/whisper#available-models](https://github.com/openai/whisper#available-models)  

### 개요  

- Whisper는 음성을 텍스트로 변환(STT) 하는 트랜스포머 기반 모델  
- 다국어 인식과 자동 언어 감지, 번역(음성→영어) 까지 지원  
- 실제 환경(잡음, 억양, 사투리)에 강하도록 대규모 약지도 데이터로 학습됨  

### 작동 방식  

1. 입력 음성을 Mel 스펙트로그램으로 변환  
2. Encoder–Decoder 트랜스포머가 시퀀스를 처리  
3. 텍스트 토큰을 생성하며, 필요 시 언어 감지/번역을 동시에 수행  

### 주요 특징  

- 다국어: 90개 이상 언어 인식 가능.  
- 노이즈 강인성: 회의실·야외·전화 음성에 비교적 안정적  
- 엔드투엔드: ASR + 번역을 하나의 모델로 처리한다.  
- 오픈소스: 파이썬에서 바로 사용 가능  

### 모델 크기와 선택 가이드  

| Size   | Parameters | English-only 모델 | Multilingual 모델 | Required VRAM | Relative speed |
| ------ | ---------: | --------------- | --------------- | ------------: | -------------: |
| tiny   |       39 M | tiny.en         | tiny            |         ~1 GB |           ~10× |
| base   |       74 M | base.en         | base            |         ~1 GB |            ~7× |
| small  |      244 M | small.en        | small           |         ~2 GB |            ~4× |
| medium |      769 M | medium.en       | medium          |         ~5 GB |            ~2× |
| large  |    1,550 M | N/A             | large           |        ~10 GB |             1× |
| turbo  |      809 M | N/A             | turbo           |         ~6 GB |            ~8× |


### 장점과 한계  

#### 장점  

- 설치·사용 간단, 범용성 높음.  
- 사전 튜닝 없이도 준수한 정확도.  

#### 한계  

- 초저지연 실시간 스트리밍에는 추가 최적화 필요.  
- 도메인 특화 용어(의학·법률)는 후처리/사전 보정이 유리.  

### 활용 사례  

- 회의/강의 자동 자막  
- 인터뷰·콜센터 전사  
- 팟캐스트·영상 자막 생성  
- 다국어 콘텐츠 자동 번역  


## OpenAI Whisper API  

### STT    

#### 코드  

```python
from openai import OpenAI
from configparser import ConfigParser

config = ConfigParser()
config.read("config/secret.ini")

def whisper_api(audio_file_path:str, model:str="whisper-1"):
    # API setting
    api_key = config["apikey"]["openai"]
    client = OpenAI(api_key = api_key)
    
    # audio prep
    with open(audio_file_path, "rb") as f:
        # API request
        transcription = client.audio.transcriptions.create(
            model = model,
            file = (f)
        )
        
    return transcription
```

#### 예제 파일  

https://github.com/saintdragon2/gpt_agent_2025_easyspub/blob/main/chap05/audio/lsy_audio_2023_58s.mp3  

#### 결과  

```bash
Transcription(text='안녕하세요. 이 강의는 GPT API로 챗봇 만들기라는 내용을 다루는 강의입니다. GPT API에 대해서 생소하신 분들도 있을 텐데 우리가 잘 알고 있는 채GPT, 채GPT 기능을 이용해서 우리가 원하는 프로그램을 어떻게 만드는지에 대해서 이야기할 거예요. 그래서 뭐 이런 강의들이 사실 많이 있습니다. 그래서 여러 가지들이 있는데 좀 이 강의의 특징이라고 한다면 GPT로 명확한 미션을 달성하는 챗봇 프로그램을 만드는 게 사실 쉽지는 않은데 이걸 어떻게 해서 구현을 하는지 그리고 그게 왜 필요한지에 대해서 좀 이야기를 할 거고요. 그 예제로 예제는 여러 가지가 될 수 있는데 여기서 예제로 하는 것은 음악 플레이리스트 동영상을 자동으로 대화를 통해서 생성하는 프로그램 만드는 것을 다루려고 합니다. 그래서 프로그램이 실행되는 모습을 한번 보여드릴게요. 우리가 만들 프로그램은 이런 식으로 이제 나타나게 되고', logprobs=None, usage=UsageDuration(seconds=58.0, type='duration'))
```

- 챗GPT 를 채GPT로 오인해서 아쉬움

### STT + 번역  

#### 코드  

```python
from openai import OpenAI
from configparser import ConfigParser

config = ConfigParser()
config.read("config/secret.ini")

def whisper_translation_api(audio_file_path:str, model:str="whisper-1"):
    # API setting
    api_key = config["apikey"]["openai"]
    client = OpenAI(api_key = api_key)
    
    # audio prep
    with open(audio_file_path, "rb") as f:
        # API request
        transcription = client.audio.translations.create( # transcription -> translation
            model = model,
            file = (f)
        )
        
    return transcription
```


#### 예제 파일  

https://github.com/saintdragon2/gpt_agent_2025_easyspub/blob/main/chap05/audio/lsy_audio_2023_58s.mp3  

#### 결과  

```bash
Translation(text="Hello, this is a lecture on how to make a chatbot with GPT API. Some of you may be unfamiliar with GPT API. We're going to talk about how to make the program we want using the chat GPT function that we know well. So there are a lot of lectures like this. There are a lot of things, but if I were to say the characteristics of this lecture, it's not easy to make a chatbot program that achieves a clear mission with GPT. I'm going to talk about how to implement this and why it's necessary. As an example, there can be many examples. The example here is to create a program that automatically creates a music playlist video through conversation. I'll show you how the program runs. This is how the program we're going to make appears.")
```

#### 리뷰  

- 기존 한국어에서 오인했던 채GPT 가 영문으로는 ChatGPT로 잘 옳게 번역되어있음을 볼 수 있다.  
- 이전처럼 한글 STT만 한 뒤, GPT 모델로 번역을 요청해도 되긴 하지만, 이렇게 위스퍼 API로 한 번에 (이중으로 API를 사용하지 않고) 처리하는 게 시간적, 토큰 사용량적 효율을 이룰 수 있음  


## 로컬에서 Whisper 구동  

### 필요성  

- API 로 STT를 사용할 수 없는 경우 : 대외비, 음성 파일의 길이가 길어 비용이 우려될 경우  

### huggingface  

![alt text](/assets/images/image-1.png)  

- 인공지능 모델을 개발하는 회사  
- AI 모델, 데이터셋, 문서를 올리고 공유하는 허깅페이스 플랫폼 서비스로 더욱 유명함  
- [https://huggingface.co/](https://huggingface.co/)    

### Whisper 모델 선택  

- whisper-small 모델로 선택했다.  

[https://huggingface.co/openai/whisper-small](https://huggingface.co/openai/whisper-small)  

### FFMPEG 설치  

- FFMPEG : 오디오와 비디오 파일 변환 처리 오픈소스 도구  
- 컴퓨터에서 오디오와 비디오를 처리할 때 필수적인 도구  
- [https://git.ffmpeg.org/ffmpeg.git](https://git.ffmpeg.org/ffmpeg.git)  

### 라이브러리 설치  

- whisper 모델을 local 에서 사용하기 위해서는 아래 라이브러리 설치가 필요하다  

```bash
uv add transformers accelerate librosa
```

### 코드  

- 허깅페이스 모델 설명 페이지에 있는 실습 코드를 수정해 사용  

```python
from configparser import ConfigParser
from transformers import WhisperProcessor, WhisperForConditionalGeneration
import librosa

config = ConfigParser()
config.read("config/secret.ini")

def whisper_local(audio_file_path:str,
                  model_name:str="openai/whisper-small",
                  sr:int=int(config["default"]["audio.sampling_rate"])):
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
    audio_array, sampling_rate = librosa.load(audio_file_path, sr=sr)
    input_features = processor(
        audio_array,
        sampling_rate = sr,
        return_tensors="pt"
    ).input_features
    
    # inference
    ## generate token ids
    predicted_ids = model.generate(input_features)
    ## decode token ids to text
    transcription = processor.batch_decode(predicted_ids, skip_special_tokens=False)
    
    return transcription
    
```


### 예제 파일  

https://github.com/saintdragon2/gpt_agent_2025_easyspub/blob/main/chap05/audio/lsy_audio_2023_58s.mp3  

### 결과  

```bash
[' 안녕하세요. 이 강의는 GPT API로 체법 만들기라는 내용을 다루는 강입니다. GPT API에 대해서 생소하신 분들도 있을 텐데 우리가 잘 알고 있는 채 GPT 기능을 이용해서 우리가 원하는 프로그램을 어떻게 만드는지에 대해서 이야기할 거예요. 그래서 이런 강의들이 사실 많이 있습니다. 여러 가지들이 있는데 이 강의 특징이라고 한다면 GPT로 명확한 미션을 달성하는']
```

### Trouble Shooting - 텍스트가 절반 잘린 문제  

- 기대 텍스트  

```plaintext
'안녕하세요. 이 강의는 GPT API로 챗봇 만들기라는 내용을 다루는 강의입니다. GPT API에 대해서 생소하신 분들도 있을 텐데 우리가 잘 알고 있는 채GPT, 채GPT 기능을 이용해서 우리가 원하는 프로그램을 어떻게 만드는지에 대해서 이야기할 거예요. 그래서 뭐 이런 강의들이 사실 많이 있습니다. 그래서 여러 가지들이 있는데 좀 이 강의의 특징이라고 한다면 GPT로 명확한 미션을 달성하는 챗봇 프로그램을 만드는 게 사실 쉽지는 않은데 이걸 어떻게 해서 구현을 하는지 그리고 그게 왜 필요한지에 대해서 좀 이야기를 할 거고요. 그 예제로 예제는 여러 가지가 될 수 있는데 여기서 예제로 하는 것은 음악 플레이리스트 동영상을 자동으로 대화를 통해서 생성하는 프로그램 만드는 것을 다루려고 합니다. 그래서 프로그램이 실행되는 모습을 한번 보여드릴게요. 우리가 만들 프로그램은 이런 식으로 이제 나타나게 되고'
```

- local 출력 텍스트  

```plaintext
안녕하세요. 이 강의는 GPT API로 체법 만들기라는 내용을 다루는 강입니다. GPT API에 대해서 생소하신 분들도 있을 텐데 우리가 잘 알고 있는 채 GPT 기능을 이용해서 우리가 원하는 프로그램을 어떻게 만드는지에 대해서 이야기할 거예요. 그래서 이런 강의들이 사실 많이 있습니다. 여러 가지들이 있는데 이 강의 특징이라고 한다면 GPT로 명확한 미션을 달성하는
```

- 문제 탐색 : whisper 는 30초 제한을 가지고 있으며, 경고 없이 잘린다.  
[https://openai.com/ko-KR/index/whisper/](https://openai.com/ko-KR/index/whisper/)  

![alt text](/assets/images/30s.png)  

- 코드 수정  

```python
from configparser import ConfigParser
from transformers import WhisperProcessor, WhisperForConditionalGeneration
import librosa
import time

config = ConfigParser()
config.read("config/secret.ini")

def chunk_audio(audio, # ⭐️ 오디오 30초 청킹
                sr:int=int(config["default"]["audio.sampling_rate"]),
                chunk_sec:int=30):
    chunk_size = sr * chunk_sec
    return [audio[i:i+chunk_size] for i in range(0, len(audio), chunk_size)]

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
    for audio in chunked_audios:# ⭐️ 오디오 청크마다 inference
        input_features = processor(
            audio,
            sampling_rate = sr,
            return_tensors="pt"
        ).input_features
        
        # inference
        ## generate token ids
        predicted_ids = model.generate(input_features)
        ## decode token ids to text
        transcription.append(processor.batch_decode(predicted_ids, skip_special_tokens=False))
    
    print(f"inference 소요 시간 : {time.time() - start}")
    
    return transcription
```

- 결과 : 전체 오디오를 모두 transcription 했다. 다만, 30초 오디오 사이의 발화는 누락되었다.  
- 누락된 내용 : 챗봇 

```plaintext
[
    [' 안녕하세요. 이 강의는 GPT API로 체법 만들기라는 내용을 다루는 강입니다. GPT API에 대해서 생소하신 분들도 있을 텐데 우리가 잘 알고 있는 채 GPT 기능을 이용해서 우리가 원하는 프로그램을 어떻게 만드는지에 대해서 이야기할 거예요. 그래서 이런 강의들이 사실 많이 있습니다. 여러 가지들이 있는데 이 강의 특징이라고 한다면 GPT로 명확한 미션을 달성하는'],

    [' 프로그램을 만드는 게 사실 쉽지는 않는데 이걸 어떻게 해서 구현을 하는지 그리고 왜 필요한지에 대해서 좀 이야기를 할 거고요. 그 예제로 뭐 예제는 여러 가지가 될 수 있는데 여기서 예제로 하는 것은 음악 플레이리스트 동영상을 자동으로 대화를 통해서 생성하는 프로그램을 만드는 걸 다룰 려고 합니다. 그래서 프로그램이 실행되는 모습을 한번 보여드릴게요. 우리가 만들 프로그램은 이런 식으로 이제 나타나게 되고']
]
```

- 청킹을 조금 겹치게 하면 이런 부분이 해결될 수 있다.  
- 수정 코드  

```python
from transformers import WhisperProcessor, WhisperForConditionalGeneration
import librosa
import time
from config.settings import config

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

# 오버랩 시간 내 중복 어휘 제거
def remove_overlap(prev_text: str,
                   curr_text: str,
                   min_overlap_chars: int = 10) -> str:
    max_check = min(len(prev_text), len(curr_text)) # 두 텍스트 중 짧은 길이까지만 비교
    for i in range(max_check, min_overlap_chars, -1): # 뒤에서부터 가장 긴 공통 문자열 찾기
        if prev_text[-i:] == curr_text[:i]: # 같은 문자열이 존재할 경우
            return curr_text[i:]  # 중복 제거
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
        text = processor.batch_decode(predicted_ids,skip_special_tokens=False)[0]
        
        if transcription:
            text = remove_overlap(transcription[-1], text)
        
        transcription.append(text)
    
    print(f"inference 소요 시간 : {time.time() - start}")
    
    return transcription
    
```

- 결과 : 그래도 중복 제거가 안됐다. 이유는 "여러 가지" 와 "여러가지" 가 다르기 때문    

```plaintext
[
    ' 안녕하세요. 이 강의는 GPT API로 체법 만들기라는 내용을 다루는 강입니다. GPT API에 대해서 생소하신 분들도 있을 텐데 우리가 잘 알고 있는 채 GPT 기능을 이용해서 우리가 원하는 프로그램을 어떻게 만드는지에 대해서 이야기할 거예요. 그래서 이런 강의들이 사실 많이 있습니다. 여러 가지들이 있는데 이 강의 특징이라고 한다면 GPT로 명확한 미션을 달성하는',
    ' 여러가지들이 있는데 이 강의 특징이라고 한다면 GPT로 명확한 미션을 달성하는 제법 프로그램을 만드는 게 사실 쉽지는 않은데 이걸 어떻게 해서 구현을 하는지 그리고 왜 필요한지에 대해서 이야기를 할 거고요. 예제로 여러 가지가 될 수 있는데 여기서 예제로 하는 것은 음악 플레이리스트 동영상을 자동으로 대화를 통해서 생성하는 프로그램을 만드는 것을 다룰 예정입니다.', ' 프로그램이 실행되는 모습을 한번 보여드릴게요. 우리가 만들 프로그램은 이런 식으로 이제 나타나게 되고'
]
```

- 그러면 문장부호(공백 등)을 제거한 뒤 비교하면 되겠다.  

```python
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

...
def whisper_local(audio_file_path:str,
                  model_name:str="openai/whisper-small",
                  sr:int=int(config["default"]["audio.sampling_rate"]))->list[str]:
    ...
    text = processor.batch_decode(predicted_ids,skip_special_tokens=False)[0].lstrip() # whisper 선행에 공백이 1개 있으므로 제거
```

- 결과  

```plaintext
[
    '안녕하세요. 이 강의는 GPT API로 체법 만들기라는 내용을 다루는 강입니다. GPT API에 대해서 생소하신 분들도 있을 텐데 우리가 잘 알고 있는 채 GPT 기능을 이용해서 우리가 원하는 프로그램을 어떻게 만드는지에 대해서 이야기할 거예요. 그래서 이런 강의들이 사실 많이 있습니다. 여러 가지들이 있는데 이 강의 특징이라고 한다면 GPT로 명확한 미션을 달성하는',
    ' 제법 프로그램을 만드는 게 사실 쉽지는 않은데 이걸 어떻게 해서 구현을 하는지 그리고 왜 필요한지에 대해서 이야기를 할 거고요. 예제로 여러 가지가 될 수 있는데 여기서 예제로 하는 것은 음악 플레이리스트 동영상을 자동으로 대화를 통해서 생성하는 프로그램을 만드는 것을 다룰 예정입니다.', '프로그램이 실행되는 모습을 한번 보여드릴게요. 우리가 만들 프로그램은 이런 식으로 이제 나타나게 되고'
]
```

### 리뷰  

- 소요 시간 : 모델 로딩 + STT 10.36 초 (Macbook Air M2)  
- 소요 시간 : STT 만 7초 (Macbook Air M2)  
- 58초짜리 다소 긴 오디오를 7초만에 처리했다는 것은.. 빠르다고 생각한다.  
- 텍스트 인식 품질은 API보다 안좋음  

### 그거 말고 책에서 제공한 코드 사용하기  

```python
import torch
from transformers import AutoModelForSpeechSeq2Seq, AutoProcessor, pipeline
from config.settings import config



def whisper_local_with_torch(audio_file_path:str,
                             model_name:str="openai/whisper-small",
                             sr:int=int(config["default"]["audio.sampling_rate"]),
                             chunk_sec:int=10,
                             stride_sec:int=2)->list[str]:
    
    # config
    device = "cuda:0" if torch.cuda.is_available() else "cpu"
    torch_dtype = torch.float16 if torch.cuda.is_available() else torch.float32
    model_save_dir = model_save_dir = config["path"]["dir.model.whisper"]
    
    # load model and processor
    model = AutoModelForSpeechSeq2Seq.from_pretrained(
        model_name,
        cache_dir = model_save_dir,
        torch_dtype=torch_dtype,
        low_cpu_mem_usage=True,
        use_safetensors=True
    )
    model.to(device)
    
    processor = AutoProcessor.from_pretrained(
        model_name,
        cache_dir = model_save_dir,
    )
    
    # pipeline
    pipe = pipeline(
        "automatic-speech-recognition",
        model = model,
        tokenizer = processor.tokenizer,
        feature_extractor = processor.feature_extractor,
        torch_dtype = torch_dtype,
        device = device,
        return_timestamps = True,
        chunk_length_s  = chunk_sec,
        stride_length_s = stride_sec
    )
    
    # inference
    result = pipe(audio_file_path)
    return result
```

- 결과물  

```plaintext
' 안녕하세요. 이 강의는 GPT API로 체법 만들기라는 내용을 다루는 강입니다. GPT API에 대해서 생소하신 분들도 있을텐데, 우리가 잘 알고 있는 채치 GPT, 채치 GPT를 이용해, 채치 GPT의 기능을 이용해서 우리가 원하는 프로그램을 어떻게 만드는지에 대해서 이야기할 거예요. 그래서 뭐 이런 강의들이 사실 많이 있습니다. 그래서 뭐 여러가지들이 있는데 좀 이 강의 특징이라고 한다면 GPT로 명확한 미션을 달성하는 제법 프로그램을 만드는 게 사실 쉽지는 않은는데 이걸 어떻게 해서 구현을 하는지 그리고 그게 왜 필요한지에 대해서 좀 이야기를 할 거고요. 그 예제로는 여러가지가 될 수 있는데 여기서 예제로 하는 것은 음악 플레이리스트 동영상을 자동으로 대화를 통해서 생성하는 프로그램을 만드는 것을 다루려고 합니다. 그래서 프로그램이 실행되는 모습을 한번 보여 드릴게요 우리가 만들 프로그램은 이런식으로 이제 나타나게 되고'
```

- 그런데 소요 시간이 45초인데..? 비효율적으로 보임  


## Reference  

https://github.com/openai/whisper#available-models  
doit  
