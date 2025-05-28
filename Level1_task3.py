# -*- coding: utf-8 -*-
"""
Created on Mon May 26 20:57:52 2025

@author: jainp
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv("E:/intern/codveda/3) Sentiment dataset.csv")

# Set seaborn style
sns.set(style="whitegrid")

# --- 1. Bar Plot: Sentiment Distribution ---
plt.figure(figsize=(8, 5))
sns.countplot(x='Sentiment', data=df, palette='Set2')
plt.title('Distribution of Sentiment Classes')

plt.xlabel('Sentiment')
plt.ylabel('Count')
plt.tight_layout()
plt.savefig('sentiment_distribution.png')  # Export plot as image
plt.show()

# --- 2. Line Chart: Average Likes and Retweets by Hour ---
hourly_avg = df.groupby('Hour')[['Likes', 'Retweets']].mean().reset_index()

plt.figure(figsize=(10, 6))
sns.lineplot(x='Hour', y='Likes', data=hourly_avg, marker='o', label='Likes')
sns.lineplot(x='Hour', y='Retweets', data=hourly_avg, marker='o', label='Retweets')
plt.title('Average Likes and Retweets by Hour of Day')
plt.xlabel('Hour of Day')
plt.ylabel('Average Count')
plt.legend()
plt.tight_layout()
plt.savefig('engagement_by_hour.png')  # Export plot as image
plt.show()

# --- 3. Scatter Plot: Likes vs Retweets by Sentiment ---
plt.figure(figsize=(8, 6))
sns.scatterplot(x='Retweets', y='Likes', hue='Sentiment', data=df, palette='Set1')
plt.title('Likes vs Retweets by Sentiment')
plt.xlabel('Retweets')
plt.ylabel('Likes')
plt.legend(title='Sentiment')
plt.tight_layout()
plt.savefig('likes_vs_retweets.png')  # Export plot as image
plt.show()
