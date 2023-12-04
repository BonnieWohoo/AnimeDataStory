import json
import csv

# This script is to extract the necessary information from the json files
# Open the JSON file for reading with UTF-8 encoding

animeArray = []
header = ['mal_id','title','title_english','rank']

with open('anime_data.json', 'r', encoding='utf-8') as json_file:
    # Open a text file for writing
    with open('top_anime_clean.csv', 'w', newline = '', encoding='utf-8') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(header)
        # Iterate through each line in the JSON file
        for line in json_file:
            # Load the JSON object from the line
            json_data = json.loads(line)

            # Extract the 'data' objects from the JSON data (assuming 'data' is a list)
            data_objects = json_data.get('data', [])

            # Iterate through each 'data' object
            for data_obj in data_objects:
                animeType = data_obj.get('type', None)
                # Only want TV anime
                if animeType == 'TV':
                    animeArray.append(data_obj.get('mal_id', None))
                    animeArray.append(data_obj.get('title', None))
                    animeArray.append(data_obj.get('rank', None))

                    if animeArray[0] is not None:
                        # Write the mal_id to the text file
                        csv_writer.writerow(animeArray)
                    animeArray.clear()

# Print a message to confirm that the data has been written to the text file
print("Data values have been written to top_anime_clean.csv")
