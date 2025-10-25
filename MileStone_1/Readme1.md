# Heart MRI Patient Clustering and Disease Labeling

## Project Overview
This project aims to analyze heart MRI images combined with structured patient metadata to group patients into disease-like categories. We used an **unsupervised approach** based on **ResNet feature extraction** and **KMeans clustering** to generate preliminary disease labels.

---

## Dataset
- **MRI Images:** Slices of heart MRIs stored in patient-specific folders.  
- **Structured Metadata:** A cleaned CSV file containing patient information such as:
  - `patient_id`
  - `age`
  - `gender`
  - `modality`
  - `num_slices`
  - `folder_path` (path to MRI slices)
- All patient folders were preprocessed to ensure consistent naming and formatting.

---

## Approach

### 1. Feature Extraction using ResNet
- A pretrained **ResNet18** model (from ImageNet) was used as a **feature extractor**.  
- The final classification layer was removed to obtain **512-dimensional feature vectors**.  
- Each MRI slice was resized to `224x224` and normalized before feature extraction.  
- For each patient, the **average feature vector across all slices** was calculated.

### 2. Integrating Metadata
- Additional features from the structured EHR were included:
  - **Age** (numeric)
  - **Gender** (encoded as `1` for Male, `0` for Female)  
- This enriched the patient representation with both **image** and **clinical** data.

### 3. Clustering Patients
- Features were standardized using `StandardScaler`.
- **KMeans clustering** was applied to group patients into **4 clusters**, representing potential disease groups.
- Cluster assignments were then manually mapped to disease names:
  - `0 → Cardiomyopathy`
  - `1 → Myocardial_Infarction`
  - `2 → Heart_Failure`
  - `3 → Normal`

### 4. Generating the Labeled Dataset
- The final dataset includes:
  - Patient metadata
  - Assigned disease labels (`Disease`)
  - Optional: clusters removed for clarity
- Saved as `final_labeled_patients_with_icd_10.csv`.


## Next Steps
1. **Assign ICD-10 Codes:** Map disease labels to ICD-10 codes for medical record integration.
2. **Validation:** Compare clusters with actual diagnoses (if available) to assess accuracy.
3. **Advanced Modeling:** Consider supervised models or multimodal models like **CLIP** for more accurate disease prediction.

---

## Dependencies
- Python >= 3.8  
- `pandas`, `numpy`, `torch`, `torchvision`, `scikit-learn`, `PIL`, `tqdm`  
- ResNet18 from `torchvision.models`

---
