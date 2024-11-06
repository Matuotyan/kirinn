# generate_image.py
from diffusers import StableDiffusionPipeline
import torch
from safetensors.torch import load_file

class ImageGenerator:
    def __init__(self, model_path):
        # safetensorsモデルを読み込み
        self.pipe = StableDiffusionPipeline.from_single_file(model_path)
        self.pipe = self.pipe.to("cuda" if torch.cuda.is_available() else "cpu")

    def generate_image(self, prompt, output_path="generated_image.png"):
        # プロンプトに基づき画像を生成
        image = self.pipe(prompt).images[0]
        image.save(output_path)
        return output_path
