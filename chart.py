
---

### `chart.py` contents:
```python
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Set professional styling
sns.set_style("whitegrid")
sns.set_context("talk")  # Larger text for presentations

# Generate realistic synthetic data for retail product categories
np.random.seed(42)  # For reproducibility
categories = ['Electronics', 'Clothing & Apparel', 'Home & Kitchen', 
              'Beauty & Personal Care', 'Sports & Outdoors', 'Books & Media']

# Create realistic satisfaction scores (scale 1-10)
data = []
for category in categories:
    # Different base scores per category with realistic variations
    if category == 'Electronics':
        base_score = 8.7
        variation = 0.8
    elif category == 'Clothing & Apparel':
        base_score = 7.9
        variation = 1.2
    elif category == 'Home & Kitchen':
        base_score = 8.2
        variation = 0.7
    elif category == 'Beauty & Personal Care':
        base_score = 8.9
        variation = 0.6
    elif category == 'Sports & Outdoors':
        base_score = 8.5
        variation = 1.0
    else:  # Books & Media
        base_score = 8.4
        variation = 0.9
    
    # Generate 100 samples per category
    scores = np.random.normal(base_score, variation, 100)
    scores = np.clip(scores, 1, 10)  # Ensure within 1-10 scale
    
    for score in scores:
        data.append({'Product Category': category, 'Satisfaction Score': score})

df = pd.DataFrame(data)

# Create the visualization
plt.figure(figsize=(8, 8))

# Create barplot with professional color palette
barplot = sns.barplot(
    data=df,
    x='Product Category',
    y='Satisfaction Score',
    palette='Blues_d',
    errorbar='ci',  # Confidence intervals
    capsize=0.1,
    width=0.7
)

# Customize appearance
plt.title('Customer Satisfaction by Product Category\nDouglas Buckridge Retail Analysis', 
          fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Product Category', fontsize=14, fontweight='semibold')
plt.ylabel('Average Satisfaction Score (1-10)', fontsize=14, fontweight='semibold')

# Rotate x-axis labels for better readability
plt.xticks(rotation=15, ha='right')

# Add value labels on top of bars
for i, bar in enumerate(barplot.patches):
    barplot.text(
        bar.get_x() + bar.get_width() / 2,
        bar.get_height() + 0.05,
        f'{bar.get_height():.1f}',
        ha='center',
        va='bottom',
        fontsize=11,
        fontweight='bold'
    )

# Set y-axis limits for better visual appeal
plt.ylim(6, 10)

# Adjust layout and save
plt.tight_layout()
plt.savefig('chart.png', dpi=64, bbox_inches='tight')  # 8*64 = 512 pixels
plt.show()

print("Chart saved as 'chart.png' (512×512 pixels)")
