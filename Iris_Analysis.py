# ✅ Task 1: Load and Explore the Dataset
# Dataset: Iris dataset loaded using sklearn.datasets.load_iris().

# Exploration:

# Displayed the first few rows with .head().

# Used .info() and .isnull() to confirm no missing values.

# Cleaning: No missing values detected; dataset is clean.

# ✅ Task 2: Basic Data Analysis
# Used .describe() to get statistics like mean, median, and standard deviation.

# Grouped by species and calculated the mean for numerical columns.

# Findings:

# Setosa has the smallest petal size.

# Virginica shows the largest sepal and petal dimensions.

# ✅ Task 3: Data Visualization
# Line Chart: Sepal length vs. Petal length (first 30 entries).

# Bar Chart: Average petal length per species.

# Histogram: Distribution of sepal length.

# Scatter Plot: Sepal length vs. Petal length by species.

# Iris Dataset Analysis Script

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

# Set plotting style
sns.set(style="whitegrid")

# Load the dataset
try:
    iris = load_iris(as_frame=True)
    df = iris.frame
    df['species'] = df['target'].apply(lambda x: iris.target_names[x])
except Exception as e:
    print("Error loading dataset:", e)

# Display first few rows
print(df.head())

# Explore dataset structure
print(df.info())
print("Missing values:\n", df.isnull().sum())

# Clean data
df_cleaned = df.dropna()

# Basic statistics
print("\nDescriptive Statistics:")
print(df_cleaned.describe())

# Group by species and compute means
grouped_means = df_cleaned.groupby('species').mean(numeric_only=True)
print("\nGrouped Means by Species:")
print(grouped_means)

# Visualizations

# Line Chart
df_cleaned.iloc[:30].plot(x='sepal length (cm)', y='petal length (cm)', kind='line', title='Line Chart: Sepal vs Petal Length (first 30 records)')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Petal Length (cm)')
plt.grid(True)
plt.tight_layout()
plt.show()

# Bar Chart
sns.barplot(data=grouped_means.reset_index(), x='species', y='petal length (cm)')
plt.title('Average Petal Length per Species')
plt.xlabel('Species')
plt.ylabel('Average Petal Length (cm)')
plt.tight_layout()
plt.show()

# Histogram
sns.histplot(df_cleaned['sepal length (cm)'], bins=15, kde=True)
plt.title('Distribution of Sepal Length')
plt.xlabel('Sepal Length (cm)')
plt.tight_layout()
plt.show()

# Scatter Plot
sns.scatterplot(data=df_cleaned, x='sepal length (cm)', y='petal length (cm)', hue='species')
plt.title('Sepal Length vs Petal Length by Species')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Petal Length (cm)')
plt.legend(title='Species')
plt.tight_layout()
plt.show()
