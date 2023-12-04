import pandas as pd

# Load the CSV Data and select only the 'anime_id' and 'studios' columns
studioCols = ['anime_id', 'studios']
producerCols = ['anime_id', 'producers']
genreCols = ['anime_id','genres']
themeCols = ['anime_id', 'themes']
demoCols = ['anime_id', 'demographics']

df = pd.read_csv("anime_clean_3.csv", usecols=selected_columns)

# Split the 'studios' Column
df['studios'] = df['studios'].str.split(',')

# Explode the Data
df = df.explode('studios')

# Clean and Further Process the Data (optional)
df['studios'] = df['studios'].str.strip()

# Save the Cleaned Data
df.to_csv("animeStudioRelation.csv", index=False)



