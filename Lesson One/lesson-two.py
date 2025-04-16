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

# Detailed analysis
print("Column names in the dataset:", df.columns.tolist())

# Count how many bands playing each day
day_counts = df["Day"].value_counts().sort_index()
print("\nNumber of bands playing each day:")
print(day_counts)

# My test count and list all metal genres
genre_counts = df["Genre"].value_counts().sort_index()
print("\nNumber of genres:")
print(genre_counts)

# Check which venues are being used
venue_counts = df["Venue"].value_counts()
print("\nFestival venues and how many bands are playing at each:")
print(venue_counts)

# Let's create some visualizations

# 1. Bands per day visualization
plt.figure(figsize=(10, 6))
day_counts.plot(kind="bar", color="crimson")
plt.title("Number of Bands Playing Each Day", fontsize=16)
plt.xlabel("Day", fontsize=12)
plt.ylabel("Number of Bands", fontsize=12)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 2. Genre distribution (top 10)
plt.figure(figsize=(12, 7))
top_genres = genre_counts.head(10)
top_genres.plot(kind="barh", color="darkred")
plt.title("Top 10 Genres at the Festival", fontsize=16)
plt.xlabel("Number of Bands", fontsize=12)
plt.ylabel("Genre", fontsize=12)
plt.tight_layout()
plt.show()

# 3. Venue distribution
plt.figure(figsize=(12, 7))
venue_counts.plot(
    kind="pie",
    autopct="%1.1f%%",
    shadow=True,
    colors=plt.cm.Reds(np.linspace(0.5, 0.8, len(venue_counts))),
)
plt.title("Band Distribution by Venue", fontsize=16)
plt.ylabel("")  # Hide the ylabel
plt.tight_layout()
plt.show()
