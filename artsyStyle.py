import os
import time
import random
import sys

from picamera2 import Picamera2
import torch
import onnxruntime as ort
import numpy as np
from PIL import Image
import torchvision.transforms as transforms

# Set a random seed for style selection (ensures randomness in each execution)
random.seed(random.randrange(sys.maxsize))

# List of available ONNX style models
styles = [
    "candy.onnx",
    "futurism.onnx",
    "pop_art.onnx",
    "starry_night.onnx",
    "cubism.onnx",
    "mosaic.onnx",
    "rain_princess.onnx"
]

# Directory where ONNX models are stored
onnx_models_dir = "models_onnx"


def capture_image():
    """
    Captures an image using the Raspberry Pi Camera module and saves it to the `images/` directory.
    """
    picam2 = Picamera2()
    filename = f"images/captured_{int(time.time())}.jpg"

    # Capture image without showing a preview
    picam2.start_and_capture_file(filename, show_preview=False)

    # Stop camera preview and close the camera
    picam2.stop_preview()
    picam2.close()
    
    return filename


def process_image(image_path, style_model):
    """
    Applies a selected artistic style to the captured image.

    Args:
        image_path (str): Path to the captured image.
        style_model (str): The ONNX model filename for the selected artistic style.

    Returns:
        str: Path to the stylized output image.
    """
    print(f"Model chosen: {style_model}")
    output_path = image_path.replace("captured", "styled")
    print(f"Output path: {output_path}")
    
    apply_style(image_path, output_path, style_model)

    print(f"Styled image saved as: {output_path}")
    return output_path


def apply_style(input_image_path, output_image_path, style_model):
    """
    Loads an ONNX model and applies neural style transfer to an image.

    Args:
        input_image_path (str): Path to the input image.
        output_image_path (str): Path to save the stylized image.
        style_model (str): The ONNX model filename for the selected artistic style.
    """
    # Load the ONNX model
    ort_session = ort.InferenceSession(os.path.join(onnx_models_dir, style_model))

    # Load and store original image size
    image = Image.open(input_image_path).convert("RGB")
    original_size = image.size

    # Convert image to tensor format for ONNX model
    transform = transforms.Compose([
        transforms.ToTensor(),
        transforms.Lambda(lambda x: x.mul(255))  # Scale values to match model expectations
    ])
    input_tensor = transform(image).unsqueeze(0).numpy()

    # Run inference on the ONNX model
    ort_inputs = {"input_image": input_tensor}
    ort_output = ort_session.run(["output_image"], ort_inputs)[0]

    # Convert output tensor back to an image and restore original size
    output_image = transforms.ToPILImage()(torch.tensor(ort_output).squeeze(0).div(255).clamp(0, 1))
    output_image = output_image.resize(original_size, Image.LANCZOS)
    output_image.save(output_image_path)

    print(f"Styled image saved as: {output_image_path}")


if __name__ == "__main__":
    """
    Main execution flow:
    1. Capture an image from the camera.
    2. Select a random artistic style from the available ONNX models.
    3. Apply the selected style to the image.
    4. Close any previous `feh` instance before displaying the new styled image.
    5. Display the new image in full-screen mode using `feh`.
    - The DISPLAY=:0.0 is necessary so feh knows where to show the image.
    - Because he's being invoked from cron
    """

    # Capture image
    img_path = capture_image()

    # Process image with a randomly chosen style
    styled_path = process_image(img_path, random.choice(styles))

    # Close any previously running `feh` instance to allow new image display
    os.system("pkill -f feh")

    # Display the stylized image in full-screen mode
    os.system(f"DISPLAY=:0.0 feh --fullscreen {styled_path}")
