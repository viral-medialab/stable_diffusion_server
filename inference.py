import torch
from torch import autocast
from diffusers import StableDiffusionPipeline
assert torch.cuda.is_available()

pipe = StableDiffusionPipeline.from_pretrained(
    "CompVis/stable-diffusion-v1-4",
    use_auth_token=True
).to("cuda")
# ).to("cpu")


prompt = "a photo of an astronaut riding a horse on mars"
with autocast("cuda"):
# with autocast("cpu"):
    image = pipe(prompt)["sample"][0]  
    
image.save("astronaut_rides_horse.png")

# --precision full for running on Mac M1