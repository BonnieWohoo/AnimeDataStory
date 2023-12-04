import csv

# Replace 'your_input.csv' with the path to your CSV file
csv_file_path = 'anime_clean.csv'
mal_id_column_name = 'anime_id'  # The column name containing 'mal_id'

# List to store 'mal_id' values
mal_ids = []

# Read the CSV file and extract 'mal_id' values
with open(csv_file_path, mode='r', newline='', encoding='ISO-8859-1') as csv_file:
    reader = csv.DictReader(csv_file)
    
    for row in reader:
        mal_id = row.get(mal_id_column_name)
        if mal_id:
            mal_ids.append(mal_id)

# Write the 'mal_id' values to a .txt file with one value per line
with open('malidsclean2.txt', 'w', encoding='utf-8') as file:
    for mal_id in mal_ids:
        file.write(str(mal_id) + '\n')
