import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Set professional styling
sns.set_style("whitegrid")
sns.set_context("notebook", font_scale=1.2)

# Generate realistic synthetic data for customer satisfaction by product category
data = {
    'Product Category': [
        'Electronics',
        'Clothing',
        'Home & Garden',
        'Sports & Outdoors',
        'Books & Media',
        'Beauty & Health',
        'Toys & Games',
        'Food & Beverages'
    ],
    'Average Satisfaction': [
        4.2,
        4.5,
        4.1,
        4.3,
        4.6,
        4.4,
        4.0,
        4.7
    ]
}

# Create DataFrame
df = pd.DataFrame(data)

# Sort by satisfaction score for better visualization
df = df.sort_values('Average Satisfaction', ascending=False)

# Create figure with specified size for 512x512 output
plt.figure(figsize=(8, 8))

# Create barplot with professional color palette
sns.barplot(
    data=df,
    x='Average Satisfaction',
    y='Product Category',
    palette='Blues_d',
    edgecolor='black',
    linewidth=1.2
)

# Add professional titles and labels
plt.title('Customer Satisfaction by Product Category\nAverage Rating Score (1-5 Scale)',
          fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Average Satisfaction Score', fontsize=13, fontweight='bold')
plt.ylabel('Product Category', fontsize=13, fontweight='bold')

# Add value labels on bars
for i, v in enumerate(df['Average Satisfaction']):
    plt.text(v + 0.05, i, f'{v:.1f}', 
             va='center', fontsize=11, fontweight='bold')

# Set x-axis limits for better presentation
plt.xlim(0, 5)

# Adjust layout for clean appearance
plt.tight_layout()

# Save chart with exact specifications
plt.savefig('chart.png', dpi=64, bbox_inches='tight')
print("Chart saved successfully as chart.png (512x512 pixels)")

# Display the chart
plt.show()
