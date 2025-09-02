from fastapi import FastAPI
from fastapi.responses import PlainTextResponse

app = FastAPI()

import random

ANIMALS = [
    r"""
     \   ^__^
      \  (oo)\\л_______
         (__)\\       )\/\ 
             ||----w |
             ||     ||
    """,
    r"""
      /\_/ 
     ( o.o ) 
      > ^ <  
    """,
    r"""
    〝(´ᴥ`)〞
    """,
    r"""
    ><((('>
    """,
    r"""
     (\_/)
     (o.o)
    o(\")(\") 
    """,
    r"""
    ----{,_," >
    """,
    r"""
      /\o/
    """,
    r"""
    __@/
    """,
    r"""
    _/\__/
    """,
    r"""
    Ƹ̵̡Ӝ̵̨̄Ʒ
    """,
    r"""
    @(* O *)@
    """
]

def create_speech_bubble(text: str):
    lines = text.split('\n')
    max_len = max(len(line) for line in lines)
    
    if max_len > 80:
        max_len = 80
        new_lines = []
        for line in lines:
            while len(line) > max_len:
                new_lines.append(line[:max_len])
                line = line[max_len:]
            new_lines.append(line)
        lines = new_lines
        max_len = 80

    border_top = " " + "_" * (max_len + 2)
    border_bottom = " " + "-" * (max_len + 2)

    bubbled_lines = []
    if len(lines) == 1:
        bubbled_lines.append(f"< {lines[0].ljust(max_len)} >")
    else:
        bubbled_lines.append(f"/ {lines[0].ljust(max_len)} /")
        for i in range(1, len(lines) - 1):
            bubbled_lines.append(f"| {lines[i].ljust(max_len)} |")
        bubbled_lines.append(f"\ {lines[-1].ljust(max_len)} /")

    return "\n".join([border_top] + bubbled_lines + [border_bottom])

@app.get("/", response_class=PlainTextResponse)
async def root(message: str = "What does the animal say?"):
    return await animalsay(message)

@app.get("/animalsay", response_class=PlainTextResponse)
async def animalsay(message: str = "What does the animal say?"):
    """
    Generates an animal saying the given message.
    """
    animal = random.choice(ANIMALS)
    bubble = create_speech_bubble(message)
    return f"{bubble}{animal}"

# For backward compatibility
@app.get("/cowsay", response_class=PlainTextResponse)
def cowsay_redirect(message: str = "Moo?"):
    return animalsay(message)


def create_speech_bubble(text: str):
    lines = text.split('\n')
    max_len = max(len(line) for line in lines)
    
    if max_len > 80:
        max_len = 80
        new_lines = []
        for line in lines:
            while len(line) > max_len:
                new_lines.append(line[:max_len])
                line = line[max_len:]
            new_lines.append(line)
        lines = new_lines
        max_len = 80

    border_top = " " + "_" * (max_len + 2)
    border_bottom = " " + "-" * (max_len + 2)

    bubbled_lines = []
    if len(lines) == 1:
        bubbled_lines.append(f"< {lines[0].ljust(max_len)} >")
    else:
        bubbled_lines.append(f"/ {lines[0].ljust(max_len)} /")
        for i in range(1, len(lines) - 1):
            bubbled_lines.append(f"| {lines[i].ljust(max_len)} |")
        bubbled_lines.append(f"/ {lines[-1].ljust(max_len)} /")

    return "\n".join([border_top] + bubbled_lines + [border_bottom])

@app.get("/", response_class=PlainTextResponse)
async def root(message: str = "Moo?"):
    return await cowsay(message)

@app.get("/cowsay", response_class=PlainTextResponse)
async def cowsay(message: str = "Moo?"):
    """
    Generates a cowsay image with the given message.
    """
    bubble = create_speech_bubble(message)
    return f"{bubble}"