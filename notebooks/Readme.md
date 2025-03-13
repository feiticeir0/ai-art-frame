# **AI Art Frame - Jupyter Notebooks**

This directory contains **Jupyter notebooks** for training, converting, and exporting neural style transfer models. These notebooks allow you to create custom artistic styles and deploy them for real-time use on a Raspberry Pi.

## **Notebooks Overview**

### **1. train_new_style.ipynb** - Train a New Style Model
This notebook trains a **new neural style transfer model** using a dataset of content images and a single reference style image. It leverages a **VGG-based feature extractor** to learn how to apply the style while preserving the structure of input images.

**Steps covered in this notebook:**
- Clone the **PyTorch examples repository** to access `fast_neural_style`:
  ```bash
  git clone https://github.com/pytorch/examples.git
  cd examples/fast_neural_style
  ```
- Load content and style images
- Extract features using a pre-trained VGG network
- Optimize the style transfer loss function
- Save the trained model in PyTorch's `.pth` format

### **2. convert_pth_to_model.ipynb** - Convert `.pth` to a Fixed Model
This notebook converts a **trained PyTorch model (.pth)** into a standardized format that ensures compatibility with future conversions.

**Why this is needed:**
- Removes unnecessary metadata from the `.pth` file
- Ensures correct layer structures for ONNX export
- Prepares the model for deployment on resource-constrained devices (e.g., Raspberry Pi)

### **3. convert_to_onnx.ipynb** - Convert Model to ONNX
This notebook exports a trained model to **ONNX format**, making it **optimized for fast inference** on the Raspberry Pi using **ONNX Runtime**.

**Steps covered:**
- Load the fixed PyTorch model
- Define input/output tensor shapes
- Export the model to `.onnx`
- Test the ONNX model for correctness

## **How to Use These Notebooks**

### **Prerequisites**
Before running these notebooks, install the required dependencies:
```bash
pip install torch torchvision onnx onnxruntime notebook
```

### **Running the Notebooks**
1. Start Jupyter Notebook:
   ```bash
   jupyter notebook
   ```
2. Open the notebook you want to run (e.g., `train_new_style.ipynb`).
3. Follow the instructions inside each notebook to train, convert, and export models.

## **Next Steps**
After converting the model to ONNX, move it to the **models_onnx/** directory in the main repository and use it in `artsyStyle.py` for real-time image transformation.

---
By following these steps, you can **train custom style transfer models** and deploy them for AI-powered artistic transformations! 🚀🎨


