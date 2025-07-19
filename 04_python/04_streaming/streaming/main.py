from fastapi import FastAPI
from fastapi.responses import StreamingResponse
import asyncio
import os
from pathlib import Path
from PIL import Image
import io
from typing import List

app = FastAPI()

# 텍스트 스트리머
async def text_streamer(streaming_text):
    for char in streaming_text:
        yield char
        await asyncio.sleep(0.1)

# 이미지 스트리머
async def image_streamer(image_files_path:List[str]):
    for image_path in image_files_path:
            with Image.open(image_path) as img:
                buf = io.BytesIO()
                img.save(buf, format='JPEG')
                buf.seek(0)
                yield(
                    b"--frame\r\n"
                    b"Content-Type: image/jpeg\r\n\r\n" +
                    buf.read() +
                    b"\r\n"
                )
            await asyncio.sleep(0.03)

@app.get("/")
async def main(streaming_text:str):
    return StreamingResponse(text_streamer(streaming_text),
                             media_type="text/event-stream")

@app.get("/image_streaming")
async def image_streaming():
    sample_images_path = 'assets/images'
    image_path = Path(sample_images_path)
    image_files = sorted(image_path.glob('*.jpg'))
    return StreamingResponse(image_streamer(image_files),
                             media_type="multipart/x-mixed-replace; boundary=frame")

@app.get("/video_streaming")
async def video_streaming():
    sample_video_path = 'assets/rust_logo.mp4'
    def iterfile():  # (1)
        with open(sample_video_path, mode="rb") as file_like:  # (2)
            yield from file_like  # (3) 
    return StreamingResponse(iterfile(),
                             media_type="video/mp4")