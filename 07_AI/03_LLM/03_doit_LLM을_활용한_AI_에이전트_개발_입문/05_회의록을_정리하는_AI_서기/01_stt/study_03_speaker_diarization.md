

## 화자 분리  

### 준비  

- pyannote.audio speaker-diarization-3.1 모델  
- [https://huggingface.co/pyannote/speaker-diarization-3.1](https://huggingface.co/pyannote/speaker-diarization-3.1)  
- 사용을 위해 허깅페이스 토큰을 발급받아야 하고, pynnote 에 소속 기관과 웹사이트 정보를 입력해줘야 한다.  
(책 참고)  
- [https://huggingface.co/pyannote/segmentation-3.0](https://huggingface.co/pyannote/segmentation-3.0)  
- 위 세그멘테이션에도 정보 입력  
- [https://huggingface.co/pyannote/speaker-diarization-community-1](https://huggingface.co/pyannote/speaker-diarization-community-1)  
- 이것도 입력  

### 예시 오디오 파일  

https://github.com/saintdragon2/gpt_agent_2025_easyspub/blob/main/chap05/audio/%EC%8B%BC%EA%B8%B0%ED%83%80_%EB%B9%84%EC%8B%BC%EA%B8%B0%ED%83%80.mp3  

### 라이브러리 설치  

- numpy, pynnote, soundfile 설치 필요  

```bash
uv add torch torchaudio pyannote.audio numpy 
```

### 코드  

```python
# instantiate the pipeline
from pyannote.audio import Pipeline
from config.settings import config
import torch

def speaker_diarization(audio_file_path:str,
                        model_name:str="pyannote/speaker-diarization-3.1"):
    
    # api key setting
    api_key = config["apikey"]["huggingface"]
    
    # pipeline
    pipeline = Pipeline.from_pretrained(model_name, token=api_key)

    # CUDA 사용 여부
    if torch.cuda.is_available():
        pipeline.to(torch.device("cuda"))
    else:
        pass
    
    # run the pipeline on an audio file
    diarization = pipeline(audio_file_path)

    # dump the diarization output to disk using RTTM format
    file_name = audio_file_path.split("/")[-1].split(".")[-1]
    with open(config["path"]["dir.artifact.rttm"] + file_name + "rttm", "w") as rttm:
        diarization.write_rttm(rttm)

```

- 결과물  

