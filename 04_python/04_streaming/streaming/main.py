from fastapi import FastAPI
from fastapi.responses import StreamingResponse
import asyncio

app = FastAPI()

async def text_streamer(streaming_text):
    for char in streaming_text:
        yield char
        await asyncio.sleep(0.1)

@app.get("/")
async def main(streaming_text:str):
    return StreamingResponse(text_streamer(streaming_text),
                             media_type="text/event-stream")