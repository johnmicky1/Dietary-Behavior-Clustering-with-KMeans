import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import numpy as np

# Illustrative Dataset (Synthetic Data)
# Features:
# 1. Meat_Score (0=None, 10=High)
# 2. Dairy_Egg_Score (0=None, 10=High)
# 3. Plant_Protein_Score (0=Low, 10=High)

data = {
    'Meat_Score': [8, 9, 7, 0, 0, 0, 0, 0, 0, 5, 4, 6],
    'Dairy_Egg_Score': [7, 6, 8, 9, 8, 7, 0, 1, 0, 5, 6, 4],
    'Plant_Protein_Score': [4, 3, 5, 7, 8, 6, 9, 8, 7, 5, 6, 4]
}
df = pd.DataFrame(data)

#  Prepare Data for Clustering
# Scaling is crucial for K-Means to prevent features with larger values from dominating.
scaler = StandardScaler()
df_scaled = scaler.fit_transform(df)

# 🛠️ Execute K-Means
# We set n_clusters=3 to match your 3 target groups (Vegetarian, Non-Vegetarian, Vegan)
kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
df['Cluster'] = kmeans.fit_predict(df_scaled)

#  Interpret Cluster Centers
# Check the mean of the original (unscaled) features for each cluster
cluster_centers = df.groupby('Cluster').mean().sort_values(by='Meat_Score', ascending=False)

print("--- Cluster Centers (Mean Feature Values) ---")
print(cluster_centers)

print("\n--- Final Assignments ---")
print(df)