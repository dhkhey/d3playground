import numpy as np
import pandas as pd

# Number of rows and columns
n = 200

# Generate a random matrix
matrix = np.random.rand(n, n)

# Convert the matrix to a dataframe for easier csv export
df = pd.DataFrame(matrix)

# Assuming you want headers like 'item1', 'item2'... for both rows and columns
headers = ['item'+str(i+1) for i in range(n)]
df.columns = headers
df.index = headers

# Save the dataframe to a csv file
df.to_csv('similarity_matrix.csv')

print("CSV file generated!")