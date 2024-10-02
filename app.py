from flask import Flask, render_template, request, jsonify
from diffusers import StableDiffusionPipeline
import torch

app = Flask(__name__)

# Load the pre-trained model (optimized for CPU)
model_id = "CompVis/stable-diffusion-v1-4"
pipe = StableDiffusionPipeline.from_pretrained(model_id)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate_image():
    data = request.get_json()
    text_prompt = data.get('prompt', '')

    if text_prompt:
        # Generate an image from the text prompt
        image = pipe(text_prompt).images[0]
        # Save the image locally (to be optimized for UI display later)
        image_path = "static/generated_image.png"
        image.save(image_path)

        return jsonify({"image_path": image_path})
    else:
        return jsonify({"error": "No prompt provided!"})

if __name__ == '__main__':
    app.run(debug=True)

