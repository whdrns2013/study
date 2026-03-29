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
