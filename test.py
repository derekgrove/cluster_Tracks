import pandas as pd
import numpy as np

# Read the entire file
with open('cluster_data.txt', 'r') as f:
    content = f.read()

# Split the content by line breaks
data_sets = content.split('\n')

# Print the number of data sets
#print(f"Number of data sets: {len(data_sets)}")


dfs = []

for data_set in data_sets:
    # Skip if line is empty
    if data_set.strip() == '':
        continue

    # Convert string to list of floats
    data = list(map(float, data_set.split()))

    # Reshape the data and create DataFrame
    data = np.array(data).reshape(-1, 3)
    df = pd.DataFrame(data, columns=['x', 'y', 'charge'])

    # Sort and reset index
    df = df.sort_values(by=['x', 'y']).reset_index(drop=True)
    
    # Add DataFrame to the list
    dfs.append(df)

# Print dataframes
for i, df in enumerate(dfs):
    print(f"Data set {i+1}:")
    print(df)
    print()
