import pandas as pd

# Load the CSV Data
df = pd.read_csv("anime_clean_3.csv")

# Define the columns to be split and processed
columns_to_process = [
    ('studios', 'animeStudioRelation.csv'),
    ('producers', 'animeProducerRelation.csv'),
    ('genres', 'animeGenreRelation.csv'),
    ('theme', 'animeThemeRelation.csv'),
    ('demographic', 'animeDemographicRelation.csv')
]

# Loop through the columns and process them
for column, output_file in columns_to_process:
    df_copy = df.copy()
    # Split the specified column
    df_copy[column] = df_copy[column].str.split(',')
    
    # Explode the Data
    df_copy = df_copy.explode(column)
    
    # Clean and Further Process the Data (optional)
    df_copy[column] = df_copy[column].str.strip()
    df_copy = df_copy.copy()[['anime_id',column]]

    # Save the Cleaned Data
    df_copy.to_csv(output_file, index=False)
