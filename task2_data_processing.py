import pandas as pd
import json
import os

# 1. Load the JSON File
# Make sure the filename matches what you saved in Task 1
json_filename = "data/trends_20260414.json"

try:
    with open(json_filename, 'r') as f:
        data = json.load(f)
    
    # Convert the list of dictionaries into a DataFrame (a table)
    df = pd.DataFrame(data)
    print(f"Loaded {len(df)} stories from {json_filename}")

    # 2. Clean the Data
    # Step A: Remove duplicates (based on the post_id)
    df = df.drop_duplicates(subset=['post_id'])
    print(f"After removing duplicates: {len(df)}")

    # Step B: Handle missing values
    # Drop rows where 'title' or 'category' is missing
    df = df.dropna(subset=['title', 'category'])
    print(f"After removing empty rows: {len(df)}")

    # Step C: Basic filtering (Example: keep only stories with a score > 0)
    df = df[df['score'] >= 0]
    print(f"Final clean count: {len(df)}")

    # 3. Save as CSV and Print Summary
    csv_filename = "data/trends_clean.csv"
    df.to_csv(csv_filename, index=False)
    
    print(f"\nSuccess! Saved to {csv_filename}")
    print("\n--- Summary by Category ---")
    # This matches the 'Expected Output' in your image
    print(df['category'].value_counts())

except FileNotFoundError:
    print(f"Error: Could not find {json_filename}. Did you run Task 1 first?")
except Exception as e:
    print(f"An error occurred: {e}")