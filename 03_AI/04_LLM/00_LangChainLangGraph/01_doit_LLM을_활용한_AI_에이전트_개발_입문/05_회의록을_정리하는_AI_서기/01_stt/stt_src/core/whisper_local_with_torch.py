import torch
from transformers import AutoModelForSpeechSeq2Seq, AutoProcessor, pipeline
from config.settings import config
import time


def whisper_local_with_torch(audio_file_path:str,
                             model_name:str="openai/whisper-small",
                             sr:int=int(config["default"]["audio.sampling_rate"]),
                             chunk_sec:int=10,
                             stride_sec:int=2)->list[str]:
    
    # config
    if torch.cuda.is_available():
        device = torch.device("cuda:0")
        torch_dtype = torch.float16
        print("using cuda:0")
    elif torch.backends.mps.is_available():
        device = torch.device("mps")
        torch_dtype = torch.float32
        print("using mps")
    else:
        device = torch.device("cpu")
        torch_dtype = torch.float32
        print("using cpu")
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
    start = time.time()
    result = pipe(audio_file_path)
    print(f"inference time : {time.time() - start}")
    return result