
# Enhanced Image Generation Using Stable Diffusion

This project demonstrates how to enhance product or fashion images by removing their backgrounds, resizing them, and applying generative AI techniques using the Stable Diffusion model (Realistic Vision V6.0 B1 HyperVAE) to generate realistic aesthetic outputs.



## 1. Clone Stable Diffusion WebUI

```bash
git clone https://github.com/AUTOMATIC1111/stable-diffusion-webui.git
cd stable-diffusion-webui

```
## 2. Download the Model from Civitai
Model: realisticVisionV60B1_v51HyperVAE.safetensors
Download link:https://civitai.com/models/4201/realistic-vision-v60-b1?modelVersionId=245598

Move the downloaded .safetensors file into:



```bash
git clone https://github.com/AUTOMATIC1111/stable-diffusion-webui.git
cd stable-diffusion-webui

```
## 3. Install Python Dependencies(3.10)
```bash
pip install -r requirements.txt

```
## 4. Run the Stable Diffusion WebUI
```bash
.\webui-user.bat --no-half --precision full

```





    
# Processing Workflow
## Step 1: Remove Background
```bash
Bg-remover.py
```
## Step 2: Resize Image
```bash
resize.py
```
## Step 3: Enhance Image Using Stable Diffusion
Used the img2img feature in the WebUI.

Model: Realistic Vision V60B1 HyperVAE

Prompt Example: “a female model wearing the given dress, aesthetic background, ultra-realistic lighting”

## Result
 Have a look at Output folder in repository