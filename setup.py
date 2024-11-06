# setup.py
from setuptools import setup, find_packages

setup(
    name="safetensors_image_generator",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "torch",
        "transformers",
        "diffusers",
        "safetensors",
        "Pillow"
    ],
    entry_points={
        "console_scripts": [
            "safetensors_image_generator=main:ImageGeneratorApp"
        ]
    },
    author="Your Name",
    description="A GUI app for generating images from safetensors models.",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)
