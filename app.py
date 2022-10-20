from flask import Flask, request, send_file, jsonify, render_template, send_from_directory
from flask_cors import CORS
import io
import torch
from torch import autocast
from diffusers import StableDiffusionPipeline

app = Flask(__name__, static_url_path='', static_folder='frontend/build')
app.debug=True

CORS(app)

assert torch.cuda.is_available()

pipe = StableDiffusionPipeline.from_pretrained(
        "CompVis/stable-diffusion-v1-4", 
        use_auth_token=True
).to("cuda")


def run_inference(prompt):
    with autocast("cuda"):
        image = pipe(prompt)["sample"][0]  
    img_data = io.BytesIO()
    image.save(img_data, "PNG")
    img_data.seek(0)
    return img_data

@app.route('/')
def myapp():
    if "prompt" not in request.args:
        return "Please specify a prompt parameter", 400
    prompt = request.args["prompt"]
    img_data = run_inference(prompt)
    return send_file(img_data, mimetype='image/png')

@app.route('/app', defaults={'path':''})
def serve(path):
    return send_from_directory(app.static_folder,'index.html')

@app.route('/app/inference', methods=['POST'])
def handleAppInference():
    data = request.get_json()
    prompt = data["prompt"]
    img_data = run_inference(prompt)
    return img_data
    
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=3000)