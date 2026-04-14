import pandas as pd
import numpy as np

# 1. Load and Explore
# We use the CLEANED data from Task 2
csv_filename = "data/trends_clean.csv"

try:
    df = pd.read_csv(csv_filename)
    print(f"Loaded data: {df.shape}")
    print("\nFirst 5 rows:")
    print(df.head())

    # 2. Basic Analysis with NumPy
    # We use NumPy to calculate statistics on the 'score' column
    scores = df['score'].values 
    
    avg_score = np.mean(scores)
    median_score = np.median(scores) 
    max_score = np.max(scores)
    min_score = np.min(scores)
    std_dev = np.std(scores)

    print("\n--- NumPy Stats ---")
    print(f"Mean Score: {avg_score:.2f}")
    print(f"Median Score: {median_score}") 
    print(f"Max Score: {max_score}")
    print(f"Min Score: {min_score}")
    print(f"Std Deviation: {std_dev:.2f}")

    # 3. Add New Columns
    # Column A: Engagement (Comments / Score)
    # We add 1 to the denominator to avoid 'division by zero' errors
    df['engagement'] = df['num_comments'] / (df['score'] + 1)

    # Column B: Is Popular (True if score is above average)
    df['is_popular'] = df['score'] > avg_score

    # 4. Save the Result
    output_file = "data/trends_analysed.csv"
    df.to_csv(output_file, index=False)

    # Find the story with the most comments (as shown in Expected Output)
    most_comments = df.loc[df['num_comments'].idxmax()]
    
    print("\n--- Final Analysis ---")
    print(f"Most comments story: '{most_comments['title']}' with {most_comments['num_comments']} comments.")
    print(f"Saved to: {output_file}")

except FileNotFoundError:
    print("Error: Cleaned CSV not found. Please run Task 2 first.")