import pandas as pd
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import Response
import io
import numpy as np
from PIL import Image

from liminal.model.registry import load_model

app = FastAPI()
app.state.model_white = load_model(biome='white', resolution=256)
app.state.model_yellow = load_model(biome='yellow', resolution=256)
app.state.model_green = load_model(biome='green', resolution=256)
app.state.model_mix = load_model(biome='mix', resolution=256)
app.state.model_512 = load_model(biome='mix', resolution=512)


# Optional, good practice for dev purposes. Allow all middlewares
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

# http://localhost:8000/generate?diffusion_steps=10&resolution=256&biome=white
# https://api-second-version-hoqbdqxmgq-ew.a.run.app/generate?diffusion_steps=10&resolution=256&biome=green
@app.get("/generate")
def generate(diffusion_steps=30,
             biome='white',
             resolution=256,
             response_class=Response):
    """
    Generate images
    """
    model_white = app.state.model_white
    model_yellow = app.state.model_yellow
    model_green = app.state.model_green
    model_mix = app.state.model_mix
    model_512 = app.state.model_512

    # Generate images depending on chosen parameters
    if int(resolution) == 256:
        if biome == 'white':
            imgs_gen = model_white.generate(1, int(diffusion_steps), image_size=int(resolution))
        elif biome == 'yellow':
            imgs_gen = model_yellow.generate(1, int(diffusion_steps), image_size=int(resolution))
        elif biome == 'green':
            imgs_gen = model_green.generate(1, int(diffusion_steps), image_size=int(resolution))
        elif biome == 'mix':
            imgs_gen = model_mix.generate(1, int(diffusion_steps), image_size=int(resolution))
    elif int(resolution) == 512:
        imgs_gen = model_512.generate(1, int(diffusion_steps), image_size=int(resolution))

    print(f'Params:\n {diffusion_steps} diffusion steps, {biome} biome, {resolution}x{resolution} resolution')
    print(f'✅ Image from {biome} biome, resolution {resolution} generated')

    # Convert tensor to np.array and then PIL.Image
    imgs_gen = imgs_gen*255
    img_np = np.array(imgs_gen[0,:,:,:], dtype=np.uint8)

    im = Image.fromarray(img_np)

    # save image to an in-memory bytes buffer
    with io.BytesIO() as buf:
        im.save(buf, format='PNG')
        im_bytes = buf.getvalue()

    headers = {'Content-Disposition': 'inline; filename="test.png"'}
    return Response(im_bytes, headers=headers, media_type='image/png')


@app.get("/")
def root():
    return {
    'endpoint': '/generate'
    }
