import json

# Open the JSON file for reading with UTF-8 encoding
with open('anime_data.json', 'r', encoding='utf-8') as json_file:
    # Open a text file for writing
    with open('anime_ids_top500.txt', 'w') as text_file:
        # Iterate through each line in the JSON file
        for line in json_file:
            # Load the JSON object from the line
            json_data = json.loads(line)

            # Extract the 'data' objects from the JSON data (assuming 'data' is a list)
            data_objects = json_data.get('data', [])

            # Iterate through each 'data' object
            for data_obj in data_objects:
                # Extract the rank and mal_id from each 'data' object
                rank = data_obj.get('rank', None)
                animeType = data_obj.get('type',None)
                mal_id = data_obj.get('mal_id', None)

                if isinstance(rank, int) and rank < 500 and animeType == 'TV':
                    if mal_id is not None:
                        # Write the mal_id to the text file
                        text_file.write(f"{mal_id}\n")

# Print a message to confirm that the data has been written to the text file
print("mal_id values with rank less than 500 have been written to mal_ids.txt")
