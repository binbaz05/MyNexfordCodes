# Import needed python libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import zipfile
import os

# initialize file paths or directory

file_path = 'netflix_data.csv'
zipfile_path = 'netflix_data.zip'
extdir_path = '.'

# Check if the file is a zip file 

if zipfile.is_zipfile(zipfile_path):
    with zipfile.ZipFile(zipfile_path, 'r') as zip_fs:
        zip_fs.extractall(extdir_path)

    # find and renambe the extracted file to 'Netflix_shows_movies.csv'

    current_file_name = 'netflix_data.csv'
    new_file_name = 'Netflix_shows_movies.csv'

    if os.path.exists(current_file_name):
        os.rename(current_file_name, new_file_name)
        file_path = new_file_name
        print(f"File extracted and renamed to {new_file_name}")
    else:
        print(f"FIle provided is not a ZIP file, attempting to read it directly.")

# Load data set from the file

try:
    df = pd.read_csv(file_path)
    print(f"File Loaded successfully.")
except FileNotFoundError:
    print(f"Error: The file '{file_path} was not found.")
    exit()

# Check for missing values

print("Missing Values Before Cleaning:\n", df.isnull().sum())

# Handling Missing values

df['director'] = df['director'].fillna('Unknown')
df['cast'] = df['cast'].fillna('Unknown')
df.dropna(subset=['country','date_added'])

print("Missing Values after cleaning: \n", df.isnull().sum())

# This section explores the data for analysis

print("\nData Description:\n", df.describe(include='all'))

# Count of Unique movie types

movie_counts = df['type'].value_counts()
print("\nMovie Counts:\n", movie_counts)

# Analysis by Release Years

release_year_count = df['release_year'].value_counts().sort_index()
print("\n Release Year Distribution:\n", release_year_count)

# Generate Data Visualization

genres = df['listed_in'].str.get_dummies(sep=',').sum().sort_values(ascending=False)
plt.figure(figsize=(10, 6))
sns.barplot(x=genres.values, y=genres.index, hue=genres.index, dodge=False, palette="viridis")
plt.title('Most Watched Genres')
plt.xlabel('Count')
plt.ylabel('Genre')
plt.legend([], [], frameon=False)
plt.show()

# Display Move Rating Distributions

plt.figure(figsize=(10,6))
sns.countplot(y='rating', data=df, order=df['rating'].value_counts().index, hue=df['rating'], dodge=False, palette="coolwarm")
plt.title('Distribution of Ratings')
plt.xlabel('Count')
plt.ylabel('Rating')
plt.legend([], [], frameon=False)
plt.show()

# Save the 'Most Watched Genres' plot as PNG file to integrate with R

plt.figure(figsize=(10, 6))
sns.barplot(x=genres.values, y=genres.index, hue=genres.index, dodge=False, palette="viridis")
plt.title('Most Watched Genres')
plt.xlabel('Count')
plt.ylabel('Genre')
plt.legend([], [], frameon=False)
plt.savefig('most_watched_genres.png')

print("\nVisualizations completed and one saved for R integration.")
