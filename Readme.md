# **AI Art Frame - Transforming Reality into Masterpieces**

## **Overview**
The AI Art Frame is a Raspberry Pi-powered project that continuously captures images and applies deep learning-based **neural style transfer**, transforming them into famous painting styles. Whether it's a **Van Gogh swirl, a pop-art splash, or a cubist abstraction**, this project turns everyday moments into unique works of art, displayed dynamically on a 24-inch monitor.

## **The Story Behind the Project**
This project was born from a love for **art, AI, and automation**. Inspired by how deep learning can mimic human creativity, the idea was to create a digital art frame that constantly evolves—never displaying the same image twice. With a **Raspberry Pi, neural networks, and a rotating selection of artistic models**, the AI Art Frame became a real-time, ever-changing **interactive digital artwork**.

---
## **Installation Guide**
### **1. Install Raspbian OS (64-bit Desktop Version)**
Ensure you're using the **64-bit desktop version** of Raspberry Pi OS for full compatibility with ONNX and PyTorch.
- Download the latest **Raspberry Pi OS (64-bit Desktop)** from the [official site](https://www.raspberrypi.com/software/).
- Flash it onto an **SD card** using [Raspberry Pi Imager](https://www.raspberrypi.com/software/).
- Boot your Raspberry Pi and connect it to the internet.

### **2. Install Required Dependencies**
First, update the system and install necessary packages:
```bash
sudo apt update && sudo apt upgrade -y
sudo apt install python3-pip python3-picamera2 feh
```
### **3. Clone the Repository & Set Up**
```bash
git clone https://github.com/yourgithubusername/ai-art-frame.git
```
### **4. Create and activate virtual environment**
```bash
python -m venv ai-art-frame
source ai-art-frame/bin/activate
cd ai-art-frame
```

### **5. Install Python Dependencies**
Install the required Python packages:
```bash
pip install torch torchvision onnxruntime==1.20 pillow numpy
```
**Note:** Avoid ONNX Runtime 1.21 on Raspberry Pi due to compatibility issues.

[The issue for version 1.21 has been reported and it has been solved](https://github.com/microsoft/onnxruntime/issues/23957#event-16782011854).

Try it and if it does not work, use version 1.20

## **Running the AI Art Frame**

### **Manual Execution**
To **capture an image, apply style transfer, and display it**, run:
```bash
python3 artsyStyle.py
```
This will:
1. Capture an image using the Raspberry Pi Camera.
2. Randomly select a style transfer model.
3. Apply the style and save the new artwork.
4. Display the styled image on the monitor using `feh`.

### **Automate with Crontab**
To schedule the script to run every **2 hours**, edit the crontab:
```bash
crontab -e
```
Add the following line:
```bash
0 */2 * * * cd /home/pi/artsyStyle && /home/pi/artsyStyle/bin/python artsyStyle.py
```
This ensures the script **runs in the background every 2 hours**, creating a continuous art display.

---
## **Project Roadmap & Future Improvements**
✅ **New Artistic Styles** - Add more ONNX models for diverse artistic effects.  
✅ **Raspberry Pi AI HAT+** - Add support for the Raspberry PI AI HAT+.  
✅ **Performance Optimization** - Improve speed using AI accelerators like Coral TPU or NVIDIA Jetson.  

---
## **Contributing**
Feel free to **fork, modify, and contribute** to this project! Pull requests are welcome.

---
## **License**
This project is open-source and licensed under the **MIT License**.

---
## **Credits**
Inspired by PyTorch’s Fast Neural Style Transfer. Special thanks to the **open-source AI community** for making these advancements possible!

