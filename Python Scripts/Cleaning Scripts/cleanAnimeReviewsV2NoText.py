import json
import csv

# Define the header
header = ['anime_id', 'review_id', 'date', 'score', 'tags']

# Define the name of your text file
text_file = 'anime_ids_top500.txt'

# Open the CSV file for writing
with open('animeReviewsCleanV2NoText.csv', 'w', newline='', encoding='utf-8') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(header)

    # Loop through the numbers in the text file
    with open(text_file, 'r') as file:
        for line in file:
            # Read the number from each line
            number = line.strip()

            try:
                # Open the JSON file
                with open(f'anime_reviews_{number}.json', 'r', encoding='utf-8') as json_file:
                    # Load the JSON object from the file
                    for newline in json_file:
                        json_data = json.loads(newline)

                        # Extract the 'data' objects from the JSON data (assuming 'data' is a list)
                        data_objects = json_data.get('data', [])
                        if data_objects:
                            # Iterate through each 'data' object
                            for data_obj in data_objects:
                                animeArray = [
                                    number,
                                    data_obj.get('mal_id', None),
                                    data_obj.get('date', None),
                                    data_obj.get('score', None)
                                ]

                                # Check if 'tags' is not empty before accessing its first element
                                tags = data_obj.get('tags', [])
                                if tags:
                                    animeArray.append(tags[0])
                                else:
                                    animeArray.append(None)

                                # Write the row to the CSV file
                                csv_writer.writerow(animeArray)
                                #print(f"Wrote {number} to animeReviewsCleaned.csv")
            except FileNotFoundError:
                # Handle the case where the JSON file doesn't exist
                print(f'File {number}reviews.json not found.')

print('All data has been saved to animeReviewsCleaned.csv.')
