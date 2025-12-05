import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Set styling for professional appearance
sns.set_style("whitegrid")
sns.set_context("talk")

# Generate realistic synthetic data for customer satisfaction by product category
np.random.seed(42)
categories = [
    "Electronics", "Home & Kitchen", "Apparel", "Beauty & Personal Care",
    "Books", "Toys & Games", "Sports & Outdoors", "Grocery"
]
satisfaction_scores = np.random.normal(loc=4.0, scale=0.5, size=len(categories))
satisfaction_scores = np.clip(satisfaction_scores, 1.0, 5.0)  # Ensure scores between 1-5

data = pd.DataFrame({
    "Product Category": categories,
    "Avg Customer Satisfaction": satisfaction_scores
})

# Sort by satisfaction score for better visual interpretation
data = data.sort_values("Avg Customer Satisfaction", ascending=False)

# Create the figure
plt.figure(figsize=(8, 8))

# Create barplot
barplot = sns.barplot(
    data=data,
    x="Avg Customer Satisfaction",
    y="Product Category",
    palette="viridis"
)

# Customize labels and title
plt.title("Average Customer Satisfaction by Product Category\n(Retail Client Analysis)", fontsize=16, pad=20)
plt.xlabel("Average Satisfaction Score (1–5 Scale)", fontsize=12)
plt.ylabel("Product Category", fontsize=12)

# Adjust layout and save
plt.tight_layout()
plt.savefig('chart.png', dpi=64, bbox_inches='tight')  # 8*64 = 512 pixels
