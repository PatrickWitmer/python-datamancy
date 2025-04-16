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

# Analyze the relationship between venues and genres
# Create a cross-tabulation (contingency table)
venue_genre_cross = pd.crosstab(df["Venue"], df["Genre"])
print("\nVenue-Genre distribution:")
print(venue_genre_cross)

# Create a heatmap visualization of venues vs genres
plt.figure(figsize=(14, 10))
sns.heatmap(venue_genre_cross, cmap="Reds", annot=True, fmt="d", linewidths=0.5)
plt.title("Distribution of Genres Across Venues", fontsize=16)
plt.xlabel("Genre", fontsize=12)
plt.ylabel("Venue", fontsize=12)
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()

# Let's also look at the top genre for each venue
top_genre_by_venue = {}
for venue in df["Venue"].unique():
    venue_data = df[df["Venue"] == venue]
    top_genre = venue_data["Genre"].value_counts().idxmax()
    genre_count = venue_data["Genre"].value_counts().max()
    total_bands = len(venue_data)
    top_genre_by_venue[venue] = (top_genre, genre_count, total_bands)

print("\nDominant genre at each venue:")
for venue, (genre, count, total) in top_genre_by_venue.items():
    print(f"{venue}: {genre} ({count} out of {total} bands, {count/total*100:.1f}%)")

# Create a stacked bar chart showing genre composition at each venue
venues = df["Venue"].unique()
pivot_data = pd.crosstab(df["Venue"], df["Genre"], normalize="index")

plt.figure(figsize=(14, 8))
pivot_data.plot(kind="bar", stacked=True, colormap="Reds")
plt.title("Genre Composition by Venue", fontsize=16)
plt.xlabel("Venue", fontsize=12)
plt.ylabel("Proportion", fontsize=12)
plt.legend(title="Genre", bbox_to_anchor=(1.05, 1), loc="upper left")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
