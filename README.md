🧩 Module 1 — Data Collection and Preprocessing

Project: AI-Powered Enhanced EHR Imaging & Documentation System

📘 Overview

This module prepares medical imaging data (MRI scans) and related metadata for AI-based analysis and documentation.
The goal is to collect, preprocess, and extract statistical and texture features from medical images to build a structured dataset for later modules.

🎯 Objectives

Collect and organize medical imaging datasets (e.g., MRI brain scans).

Preprocess images for consistency and model compatibility.

Extract key numerical and texture features.

Generate a clean CSV file linking image features with clinical labels.

🧠 Key Functionalities
1️⃣ Image Loading & Preprocessing

Converts MRI scans to grayscale.

Normalizes pixel intensities to [0, 1].

Resizes all images to a standard resolution (128×128 or 256×256).

2️⃣ Statistical Feature Extraction

Mean Intensity

Standard Deviation

Variance

Skewness

Kurtosis

3️⃣ Texture Feature Extraction (GLCM)

Contrast

Correlation

Energy

Homogeneity

4️⃣ Edge and Entropy Analysis

Edge Density: Percentage of edge pixels detected.

Entropy: Randomness or complexity of image texture.

🧮 Output Features
Feature	Description
mean_intensity	Average pixel brightness
std_intensity	Variation in pixel intensity
variance	Spread of intensity values
skewness	Asymmetry in intensity distribution
kurtosis	Sharpness of distribution
contrast	Local intensity variation
correlation	Linear relation between pixels
energy	Uniformity of texture
homogeneity	Smoothness of pixel distribution
edge_density	Fraction of edge pixels
entropy	Information richness of the image
💾 Output Files
File	Description
brain_tumor_features_with_clinical_data.csv	Features plus clinical labels
brain_tumor_features_balanced_400.csv	Balanced dataset across tumor classes
brain_tumor_info.csv	Final preprocessed dataset with unique IDs
📊 Visual Outputs

Generated plots for feature comparison:

contrast_distribution.png

entropy_distribution.png

These visualize how contrast and entropy differ among tumor categories (glioma, meningioma, pituitary, no tumor).

🧠 Technologies Used
Category	Libraries
Image Processing	OpenCV, Scikit-Image
Statistics & Analysis	NumPy, Pandas, SciPy
Visualization	Matplotlib, Seaborn
Data Handling	OS, CSV, Google Drive Integration
🧩 Module Outcome

MRI data preprocessed and standardized.

Structured CSV dataset generated with clinical labels.

Statistical and visual insights obtained for model readiness.

This dataset serves as input for Module 2 – AI-Driven Analysis & Clinical Note Generation.

📚 References

Scikit-Image Documentation

Scikit-Learn Documentation

ICD-10 Codes Reference

🧩 Module 2 — Medical Imaging Enhancement

Project: AI-Powered Enhanced EHR Imaging & Documentation System**

📘 Overview
This module enhances the quality and clarity of medical images (MRI scans) using Generative AI (GenAI).
The primary goal is to denoise, reconstruct, and improve visualization for clinical diagnosis by applying deep learning–based enhancement models such as U-Net.

🎯 Objectives

Apply GenAI to denoise and reconstruct medical images.

Enhance image resolution, contrast, and clarity for improved interpretation.

Compute quantitative quality metrics (PSNR, SSIM) to evaluate enhancement performance.

Save enhanced images and update patient metadata in the dataset CSV.

⚙️ Workflow Overview

🧩 Code Components

File	Description
train_enhancer.py	Trains the U-Net model using self-reconstruction loss (MSE).
enhance_images.py	Applies the trained model to enhance MRI images and computes PSNR & SSIM metrics.
visualize_results.py	Displays original vs enhanced MRI images with performance metrics.

🧠 Key Functionalities

1️⃣ Model Architecture (U-Net)

Encoder–decoder structure

Skip connections for spatial detail preservation

Activation: ReLU

Output: Sigmoid

2️⃣ Training

Loss: MSE

Optimizer: Adam (LR = 1e-4)

Epochs: 10

Input = Output (self-reconstruction denoising)

3️⃣ Evaluation Metrics

PSNR: Measures image restoration quality

SSIM: Measures structural similarity

4️⃣ Visualization

Side-by-side comparison

Metric annotation

🧮 Output Columns in CSV

Column	Description
image_path	Original MRI path
enhanced_image_path	Enhanced image saved path
PSNR	Peak Signal-to-Noise Ratio
SSIM	Structural Similarity Index
patient_id	Unique identifier

💾 Output Files

enhanced_images/

brain_tumor_info_metrics.csv

📊 Visual Outputs
Displays original vs enhanced image pairs with PSNR & SSIM metrics.

🧠 Technologies Used
PyTorch, PIL, OpenCV, scikit-image, tqdm, torchvision, Pandas, NumPy, Matplotlib

🧩 Module Outcome
Enhanced MRI scans with improved clarity and structure.
Quantitative metrics (PSNR, SSIM) integrated into the dataset.
Ready for Module 3: Clinical Note Generation.

📚 References

PyTorch Documentation

scikit-image Metrics

UNet Architecture Paper

🧩 Module 3 — Clinical Note Generation & ICD-10 Coding Automation

Project: AI-Powered Enhanced EHR Imaging & Documentation System**

📘 Overview
This module leverages Google Gemini (GenAI) to automatically generate structured clinical notes and validate ICD-10 codes for each patient record.
It enhances the electronic health record (EHR) workflow by converting raw tumor metrics into professional, standardized documentation suitable for medical review.

🎯 Objectives

Use Generative AI to produce structured clinical summaries.

Validate and cross-check ICD-10 codes based on tumor details.

Automate manual EHR data entry tasks for faster and more consistent documentation.

⚙️ Prerequisites
🧩 Install Required Libraries:

pip install --upgrade google-generativeai pandas

🧩 Module 4 — Frontend UI & Image Processing Integration

Project: AI-Powered Enhanced EHR Imaging & Documentation System**

📘 Overview

Module 4 provides an interactive, user-friendly web interface using Flask + HTML + CSS + JavaScript.
It integrates all previous modules and allows medical users to:

Upload MRI images

View original + enhanced images

Automatically generate clinical notes

Navigate easily with a polished UI

🎯 Objectives

Provide a seamless UI for MRI image enhancement and note generation

Build a multi-page interface (Home → Processing Page)

Improve user experience with back/refresh navigation

Remove unnecessary features (PDF download)

Display AI-generated outputs cleanly

🧠 Key Functionalities
1️⃣ Home Page

Displays system title and description

Contains an Enter button to navigate to the processing module

2️⃣ Image Processing Page

Upload MRI/CT images

View Original and Enhanced images

Automatically generate structured clinical notes

Refresh button resets the session

Back button returns to home page

3️⃣ Image Enhancement

Uses Pillow for:

Contrast improvement

Sharpness enhancement

4️⃣ Clinical Note Rendering

Markdown-based formatting

Bold text, bullet points, line breaks

Structured SOAP note generation

📁 File Structure (Module 4)
Module_4/
│── app.py
│── templates/
│     ├── home.html
│     └── predict.html
│── static/
      ├── style.css
      ├── script.js
      ├── uploads/
      └── enhanced/

🧰 Technologies Used
Layer	Tools
Backend	Flask
Frontend	HTML, CSS, JavaScript
Image Processing	PIL (Pillow)
Integration	Fetch API (JavaScript)
