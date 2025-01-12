# HDAPM-NCP

This repository provides the data and codes for model HDAPM-NCP, which can be used to predict herb-disease associations. Several herb and disease properties are employed to construct multiple herb and disease kernels. Above kernels are fused into one herb kernel and one disease kernel. Network consistency projection is applied to the herb and disease kernels as well as the association adjacency matrix to generate the recommendation matrix. 

![Figure 1](https://github.com/1006447230/HDAPM-NCP/blob/main/HDAPM-NCP/img/Figure%201.jpg)

# Datasets

The 'datasets' folder includes the data of HDAPM-NCP. Below is a brief description of each file  in this folder:

1. **disease_herb** folder:

   + **disease_herb01.txt**: Association matrix between 400 diseases and 25 herbs
   + **disease_herb_kernel.txt**:Disease kernel calculated using associations between 400 diseases and 25 herbs
   + **herb_disease_kernel.txt**:Herb kernel calculated using associations between 25 herbs and 400 diseases 

2. **disease_kernel** folder:
   + **disease_id.csv**: IDs of 400 diseases  
   + **disease_ingredients.txt**: Disease kernel calculated using associations between 400 diseases and 349 ingredients (reference mining)  
   + **disease_ingredients_ref.txt**: Disease kernel calculated using associations between 400 diseases and 4607 ingredients (statistical inference)  
   + **disease_similarty_kernel.txt**: Disease kernel obtained by Wang et al.’s method 
   + **disease_target.txt**: Disease kernel calculated using associations between 400 diseases and 10364 targets

3. **herb_kernel** folder:
   + **herb_id.csv**: IDs of 25 herbs  
   + **herb_Gene_Targets.txt**:Herb kernel calculated using associations between 25 herbs and 1227 targets (statistical inference)  
   + **herb_go_enrichment.txt**: Herb kernel calculated using associations between 25 herbs and 2980 GO terms
   + **herb_ingredient.txt**: Herb kernel calculated using associations between 25 herbs and 2059 ingredients 
   + **herb_KEGG_enrichment.txt**: Herb kernel calculated using associations between 25 herbs and 149 KEGG pathways
   + **herb_target.txt**: Herb kernel calculated using associations between 25 herbs and 32 targets (reference mining) 

# Five-fold cross-validation data

The five-fold cross-validation data is stored in the **data_cross_verification** folder.

**data_cross_verification**  folder:

​	cross_verification\*(where * represents the numbers 1, 2, 3, 4, 5) folder:

   + guass_dis-\*(where * represents the numbers 1, 2, 3, 4, 5).txt：Disease kernel calculated using the training set data of associations between 400 diseases and 25 herbs
   + guass_herb-\*(where * represents the numbers 1, 2, 3, 4, 5).txt：Herb kernel calculated using the training set data of associations between 25 herbs and 400 diseases 

# Code

1.The **data_processing** folder contains the code for data processing.

2.The **disease_similarity** folder contains the code for calculating the similarity among 400 diseases.

3.The main program is stored in the **main_test** folder, where the **main.py** file contains the source code of the model. This folder also includes the ROC and PR curve images under five-fold cross-validation.

# Supplementary code content

### **1. Folder for Dividing 400 Diseases into 5 Groups**

#### Includes:

- `Five-fold-cross-validation-grouping/`
  - Folder for splitting data for five-fold cross-validation.
- `Split-data.py`
  - Script: Divides 400 diseases into 5 groups.
- `Main.py`
  - Main program entry file.
- `Forecast-result/`
  - Folder for storing forecast results.

------

### **2. Folder for Averaging Five Kernel Matrices**

#### Includes:

- `Calculate the average of the five matrices.py`
  - Script: Calculates the average of five matrices.
- `Main.py`
  - Main program entry file.
- `corr/`
  - Includes:
    - Calculated **`corr`** matrix.
    - Calculation script **`corr.py`**.
- `MI/`
  - Includes:
    - Calculated **`MI`** matrix.
    - Calculation script **`MI.py`**.
- `cos/`
  - Includes:
    - Calculated **`cos`** matrix.
    - Calculation script **`cos.py`**.
- `jacc/`
  - Includes:
    - Calculated **`jacc`** matrix.
    - Calculation script **`jacc.py`**.

------

### **3. Folder for Cross-Validation of 25 Herbs Divided into 5 Groups**

#### Includes:

- `Five-fold-cross-validation-grouping/`
  - Folder for splitting data for five-fold cross-validation.
- `Split-data.py`
  - Script: Divides 25 herbs into 5 groups.
- `Main.py`
  - Main program entry file.

------
### **4. Other Validation Strategies: External Validation Dataset**

#### Includes:

- `Five-fold-cross-validation-grouping/`
  - A folder used for splitting data for five-fold cross-validation.
- `Split-data.py`
  - Code: Used to split the data, dividing 400 diseases into two groups: D1 and D2. D1 accounts for 80% of the total number of diseases, while D2 accounts for 20%. Similarly, 25 herbs are divided into two groups: H1 and H2, with H1 accounting for 80% and H2 for 20%.
- `Main-A.py`
  - Main program entry file (using A as the external validation dataset).
- `Main-B.py`
  - Main program entry file (using B as the external validation dataset).
- `Main-C.py`
  - Main program entry file (using C as the external validation dataset).
- `Forecast-result/`
  - Folder for storing prediction results.

The meanings of A, B, and C are as follows:

- **A** = {(d, h) ∣ d ∈ D2, h ∈ H2}
- **B** = {(d, h) ∣ d ∈ D2, h ∈ H1}
- **C** = {(d, h) ∣ d ∈ D1, h ∈ H2}
  

------

# Requirements

+ python==3.7
+ scikit-learn==1.3.2
+ numpy==1.23.5
+ pandas==1.2.4
+ matplotlib==3.4.0

# Quick start

Run code/main.py to Run HDAPM-NCP













