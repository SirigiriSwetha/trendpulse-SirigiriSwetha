
import pandas as pd
import matplotlib.pyplot as plt

# 1. Setup: Load the analyzed data from Task 3
input_file = "data/trends_analysed.csv"

try:
    df = pd.read_csv(input_file)
    print("Data loaded successfully for visualization!")

    # --- Chart 1: Top 10 Stories by Score (Horizontal Bar) ---
    plt.figure(figsize=(10, 6))
    top_10 = df.nlargest(10, 'score').sort_values('score', ascending=True)
    plt.barh(top_10['title'], top_10['score'], color='skyblue')
    plt.title('Top 10 Stories by Score')
    plt.xlabel('Score')
    plt.tight_layout()
    plt.savefig('data/chart1_top_stories.png')
    plt.show()

    # --- Chart 2: Stories per Category (Bar Chart) ---
    plt.figure(figsize=(8, 6))
    cat_counts = df['category'].value_counts()
    cat_counts.plot(kind='bar', color='orange')
    plt.title('Number of Stories per Category')
    plt.ylabel('Count')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('data/chart2_categories.png')
    plt.show()

    # --- Chart 3: Score vs Comments (Scatter Plot) ---
    plt.figure(figsize=(8, 6))
    # We use 'is_popular' from Task 3 to color the dots
    colors = df['is_popular'].map({True: 'red', False: 'blue'})
    plt.scatter(df['score'], df['num_comments'], c=colors, alpha=0.5)
    plt.title('Relationship: Score vs Comments')
    plt.xlabel('Score')
    plt.ylabel('Number of Comments')
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.savefig('data/chart3_scatter.png')
    plt.show()

    # --- BONUS: Dashboard (All charts in one figure) ---
    fig, axs = plt.subplots(2, 2, figsize=(15, 10))
    fig.suptitle('TrendPulse: Data Dashboard', fontsize=20)

    # Top 10 in Dashboard
    axs[0, 0].barh(top_10['title'].str[:30], top_10['score'], color='skyblue')
    axs[0, 0].set_title('Top 10 Scores')

    # Categories in Dashboard
    cat_counts.plot(kind='bar', ax=axs[0, 1], color='orange')
    axs[0, 1].set_title('Story Counts')

    # Scatter in Dashboard
    axs[1, 0].scatter(df['score'], df['num_comments'], c=colors, alpha=0.5)
    axs[1, 0].set_title('Score vs Comments')

    # Hide the 4th empty subplot
    axs[1, 1].axis('off')

    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    plt.savefig('data/dashboard.png')
    print("Success! All charts and dashboard saved to the 'data' folder.")

except FileNotFoundError:
    print("Error: Could not find the CSV file. Did you run Task 3?")