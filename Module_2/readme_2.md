# 🧩 Module 2 — Medical Imaging Enhancement  
**Project:** AI-Powered Enhanced EHR Imaging & Documentation System  

---

## 📘 Overview
This module enhances the **quality and clarity of medical images (MRI scans)** using **Generative AI (GenAI)**.  
The primary goal is to **denoise**, **reconstruct**, and **improve visualization** for clinical diagnosis by applying deep learning–based enhancement models such as **U-Net**.

---

## 🎯 Objectives
- Apply **GenAI** to denoise and reconstruct medical images.  
- Enhance image **resolution**, **contrast**, and **clarity** for improved interpretation.  
- Compute **quantitative quality metrics (PSNR, SSIM)** to evaluate enhancement performance.  
- Save enhanced images and update patient metadata in the dataset CSV.

---

## ⚙️ Workflow Overview

---

## 🧩 Code Components

| File | Description |
|------|-------------|
| `train_enhancer.py` | Trains the U-Net model using self-reconstruction loss (MSE). |
| `enhance_images.py` | Applies the trained model to enhance MRI images and computes PSNR & SSIM metrics. |
| `visualize_results.py` | Displays original vs enhanced MRI images with performance metrics. |

---

## 🧠 Key Functionalities

### 1️⃣ Model Architecture (U-Net)
- Encoder–decoder structure for image-to-image translation.  
- Skip connections preserve spatial details during reconstruction.  
- Activation: **ReLU**  
- Output activation: **Sigmoid** (for normalized grayscale images).  

### 2️⃣ Training
- **Loss Function:** Mean Squared Error (MSE)  
- **Optimizer:** Adam (learning rate = 1e-4)  
- **Epochs:** 10 (configurable)  
- Input = Output (self-reconstruction objective for denoising).  

### 3️⃣ Evaluation Metrics
- **PSNR (Peak Signal-to-Noise Ratio):** Measures enhancement quality.  
- **SSIM (Structural Similarity Index):** Measures structural preservation and realism.  

### 4️⃣ Visualization
- Displays **before vs after** images for visual comparison.  
- Annotates PSNR and SSIM values on enhanced images.

---

## 🧮 Output Columns in CSV

| Column | Description |
|--------|--------------|
| `image_path` | Path to original MRI image |
| `enhanced_image_path` | Path to saved enhanced image |
| `PSNR` | Peak Signal-to-Noise Ratio value |
| `SSIM` | Structural Similarity Index value |
| `patient_id` | Associated patient ID from previous module |

---

## 💾 Output Files

| File | Description |
|------|-------------|
| `enhanced_images/` | Directory containing enhanced MRI images |
| `brain_tumor_info_metrics.csv` | Updated dataset with PSNR, SSIM, and enhanced image paths |

---

## 📊 Visual Outputs
The script randomly selects three patients and shows their **original vs enhanced** MRI scans side-by-side.  
Each pair is labeled with PSNR and SSIM values for easy performance interpretation.

---

## 🧠 Technologies Used

| Category | Libraries |
|-----------|------------|
| Deep Learning | PyTorch |
| Image Processing | OpenCV, PIL |
| Quality Metrics | scikit-image |
| Data Handling | Pandas, NumPy |
| Visualization | Matplotlib |
| Utilities | tqdm, torchvision |

---

## 🧩 Module Outcome
- Enhanced MRI scans with improved clarity and structure.  
- Quantitative metrics (PSNR, SSIM) integrated into patient data.  
- Clean, standardized enhanced dataset prepared for **Module 3: Clinical Note Generation**.  

---

## 📚 References
- [PyTorch Documentation](https://pytorch.org/docs/stable/)  
- [scikit-image Metrics](https://scikit-image.org/docs/stable/api/skimage.metrics.html)  
- [UNet Architecture Paper](https://arxiv.org/abs/1505.04597)
