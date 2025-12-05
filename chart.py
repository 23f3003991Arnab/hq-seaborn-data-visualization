import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Set professional styling
sns.set_style("whitegrid")
sns.set_context("notebook", font_scale=1.1)

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

# Create figure with exact size for 512x512 output (IMPORTANT: Remove bbox_inches='tight')
fig, ax = plt.subplots(figsize=(512/64, 512/64), dpi=64)

# Create barplot with professional color palette
sns.barplot(
    data=df,
    x='Average Satisfaction',
    y='Product Category',
    palette='Blues_d',
    edgecolor='black',
    linewidth=1.2,
    ax=ax
)

# Add professional titles and labels
ax.set_title('Customer Satisfaction by Product Category\nAverage Rating Score (1-5 Scale)',
             fontsize=14, fontweight='bold', pad=15)
ax.set_xlabel('Average Satisfaction Score', fontsize=11, fontweight='bold')
ax.set_ylabel('Product Category', fontsize=11, fontweight='bold')

# Add value labels on bars
for i, v in enumerate(df['Average Satisfaction']):
    ax.text(v + 0.05, i, f'{v:.1f}', 
            va='center', fontsize=10, fontweight='bold')

# Set x-axis limits for better presentation
ax.set_xlim(0, 5)

# Adjust layout to fit within exact dimensions
plt.subplots_adjust(left=0.25, right=0.95, top=0.92, bottom=0.08)

# Save chart with exact specifications (NO bbox_inches='tight')
plt.savefig('chart.png', dpi=64)
print("Chart saved successfully as chart.png (512x512 pixels)")

# Display the chart
plt.show()
