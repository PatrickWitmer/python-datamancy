# Import the necessary libraries
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# Set the Style of our plots
plt.style.use("dark_background")  # Seems appropriate for metal
sns.set(style="darkgrid")

# Load the CSV File
df = pd.read_csv("maryland-deathfest-2025.csv")

# Let's see what the data looks like
print("First 5 rows of the dataset:")
print(df.head())

# Get basic information about the dataset
print("\nDataset information:")
print(df.info())

# Summary of statistics
print("\nSummary statistics:")
print(df.describe())
