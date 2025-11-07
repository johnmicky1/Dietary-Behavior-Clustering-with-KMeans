# 🧠 Clustering Dietary Patterns Using K-Means in Python

📂 **GitHub Repository:**  
[`git@github.com:johnmicky1/K-Means-Dietary-Pattern-Clustering.git`](git@github.com:johnmicky1/K-Means-Dietary-Pattern-Clustering.git)

---

## 📘 Overview

This Python project demonstrates how to apply **K-Means Clustering** to group individuals based on their **dietary preferences** using synthetic data.  
The dataset contains three key features representing consumption scores for different food categories:

1. **Meat_Score** – Measures the level of meat consumption *(0 = none, 10 = high)*  
2. **Dairy_Egg_Score** – Measures the consumption of dairy and egg products *(0 = none, 10 = high)*  
3. **Plant_Protein_Score** – Measures the reliance on plant-based protein sources *(0 = low, 10 = high)*  

---

### ⚙️ Workflow Summary

- **Data Preparation:**  
  Created a small illustrative dataset using **Pandas**.

- **Data Standardization:**  
  Applied **StandardScaler** from `sklearn.preprocessing` to normalize all features so that each contributes equally to the clustering process.

- **Clustering:**  
  Used the **KMeans** algorithm from `sklearn.cluster` to group the data into **three clusters**, representing distinct dietary patterns — likely **Non-Vegetarian**, **Vegetarian**, and **Vegan** categories.

- **Cluster Interpretation:**  
  Calculated and displayed the **mean feature values** for each cluster to interpret the key dietary characteristics of each group.

---

## 🧩 Purpose

This example provides a simple yet powerful demonstration of how **unsupervised learning** can be applied to uncover hidden patterns and similarities in behavioral or lifestyle data — in this case, **dietary habits**.  
It illustrates the end-to-end workflow from data preprocessing to clustering and result interpretation.

---

## 🧰 Prerequisites

Before running this script, ensure you have the following tools and libraries installed:

- 🐍 **Python 3.10+** *(latest version recommended)*  
- 🤖 **TensorFlow** *(optional for advanced extensions)*  
- 🔢 **NumPy** and **Pandas** for data handling  
- 📊 **Matplotlib** *(optional for visualizations)*  
- 💻 **Code Editor / IDE** — e.g., VS Code, PyCharm, or Jupyter Notebook  

---

### 💡 Installation Commands

Use the following commands to install the required Python packages:

```bash
pip install numpy pandas scikit-learn matplotlib tensorflow
```

---

## 📊 Results & Interpretation

After executing the script, you will see output showing **cluster centers** that summarize each group’s dietary behavior.  
These clusters typically correspond to:

| Cluster | Dietary Pattern | Characteristics |
|----------|------------------|-----------------|
| 0 | Non-Vegetarian | High Meat & Dairy, Low Plant Protein |
| 1 | Vegetarian | Moderate Dairy & Plant Protein, Low Meat |
| 2 | Vegan | High Plant Protein, Low Meat & Dairy |

---

## 🧾 License

This project is released under the **MIT License** — free to use, modify, and distribute with attribution.

---

## ✉️ Contact

**Author:** John Michael Oliba  
📧 *johnmicky1@gmail.com*  
📍 Kampala, Uganda
Copyright 2025
