import json
import csv

# This script is to extract the necessary information from the json files
# Open the JSON file for reading with UTF-8 encoding

animeArray = []
header = ['anime_id','members']

with open('anime_data.json', 'r', encoding='utf-8') as json_file:
    # Open a text file for writing
    with open('anime_members.csv', 'w', newline = '', encoding='utf-8') as csv_file:
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
                # Check the type, only want 'TV'
                animeType = data_obj.get('type', None)
                animeStatus = data_obj.get('status', None)
                if animeType == 'TV' and animeStatus != 'Not yet aired':
                    animeArray.append(data_obj.get('mal_id', None))
                    animeArray.append(data_obj.get('members',None))

                    # write to the csv file
                    if animeArray[0] is not None:
                        # Write the mal_id to the text file
                        csv_writer.writerow(animeArray)
                    animeArray.clear()

# Print a message to confirm that the data has been written to the text file
print("Data values have been written to anime_members.csv")
