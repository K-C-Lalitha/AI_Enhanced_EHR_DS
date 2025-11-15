# 🧩 Module 1 — Data Collection and Preprocessing  
**Project:** AI-Powered Enhanced EHR Imaging & Documentation System  

---

## 📘 Overview
This module prepares **medical imaging data (MRI scans)** and related metadata for AI-based analysis and documentation.  
The goal is to **collect**, **preprocess**, and **extract statistical and texture features** from medical images to build a structured dataset for later modules.

---

## 🎯 Objectives
- Collect and organize medical imaging datasets (e.g., MRI brain scans).  
- Preprocess images for consistency and model compatibility.  
- Extract key numerical and texture features.  
- Generate a clean CSV file linking image features with clinical labels.

---
## 🧠 Key Functionalities

### 1️⃣ Image Loading & Preprocessing
- Converts MRI scans to grayscale.  
- Normalizes pixel intensities to [0, 1].  
- Resizes all images to a standard resolution (128×128 or 256×256).  

### 2️⃣ Statistical Feature Extraction
- Mean Intensity  
- Standard Deviation  
- Variance  
- Skewness  
- Kurtosis  

### 3️⃣ Texture Feature Extraction (GLCM)
- Contrast  
- Correlation  
- Energy  
- Homogeneity  

### 4️⃣ Edge and Entropy Analysis
- **Edge Density:** Percentage of edge pixels detected.  
- **Entropy:** Randomness or complexity of image texture.  

---

## 🧮 Output Features

| Feature | Description |
|----------|-------------|
| `mean_intensity` | Average pixel brightness |
| `std_intensity` | Variation in pixel intensity |
| `variance` | Spread of intensity values |
| `skewness` | Asymmetry in intensity distribution |
| `kurtosis` | Sharpness of distribution |
| `contrast` | Local intensity variation |
| `correlation` | Linear relation between pixels |
| `energy` | Uniformity of texture |
| `homogeneity` | Smoothness of pixel distribution |
| `edge_density` | Fraction of edge pixels |
| `entropy` | Information richness of the image |

---

## 💾 Output Files

| File | Description |
|------|-------------|
| `brain_tumor_features_with_clinical_data.csv` | Features plus clinical labels |
| `brain_tumor_features_balanced_400.csv` | Balanced dataset across tumor classes |
| `brain_tumor_info.csv` | Final preprocessed dataset with unique IDs |

---

## 📊 Visual Outputs
Generated plots for feature comparison:  
- `contrast_distribution.png`  
- `entropy_distribution.png`  

These visualize how contrast and entropy differ among tumor categories (glioma, meningioma, pituitary, no tumor).

---

## 🧠 Technologies Used

| Category | Libraries |
|-----------|------------|
| Image Processing | OpenCV, Scikit-Image |
| Statistics & Analysis | NumPy, Pandas, SciPy |
| Visualization | Matplotlib, Seaborn |
| Data Handling | OS, CSV, Google Drive Integration |

---

## 🧩 Module Outcome
- MRI data preprocessed and standardized.  
- Structured CSV dataset generated with clinical labels.  
- Statistical and visual insights obtained for model readiness.  

This dataset serves as input for **Module 2 – AI-Driven Analysis & Clinical Note Generation**.

---
## 📚 References
- [Scikit-Image Documentation](https://scikit-image.org/docs/stable/)  
- [Scikit-Learn Documentation](https://scikit-learn.org/stable/)  
- [ICD-10 Codes Reference](https://icd10data.com/)