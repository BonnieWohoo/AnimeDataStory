import json
import csv

# This script is to extract the necessary information from the json files
# Open the JSON file for reading with UTF-8 encoding

animeArray = []
header = ['anime_id','url', 'title','title_english','source','episodes','status','aired start','aired finish','duration(minutes per episode)','rating','score','scored by (#users)','rank','popularity(rank)','season','year','broadcast day','broadcast time', 'broadcast timezone','producer', 'studios','genres','themes','demographics']

with open('anime_data.json', 'r', encoding='utf-8') as json_file:
    # Open a text file for writing
    with open('anime_clean.csv', 'w', newline = '', encoding='utf-8') as csv_file:
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
                    animeArray.append(data_obj.get('url', None))
                    animeArray.append(data_obj.get('title', None))
                    animeArray.append(data_obj.get('title_english', None))
                    animeArray.append(data_obj.get('source', None))
                    animeArray.append(data_obj.get('episodes', None))
                    animeArray.append(animeStatus)
                    animeArray.append(data_obj.get('aired', None).get('from', None))
                    animeArray.append(data_obj.get('aired', None).get('to', None))

                    # duration is either 'Unknown' or 'X min per ep', extract only digit or 'Unknown'
                    durationString = data_obj.get('duration', None)
                    if durationString == 'Unknown':
                        animeArray.append(durationString)
                    else:
                        durationInteger = [int(word) for word in durationString.split() if word.isdigit()]
                        animeArray.append(durationInteger[0])
                    
                    animeArray.append(data_obj.get('rating', None))
                    animeArray.append(data_obj.get('score', None))
                    animeArray.append(data_obj.get('scored_by', None))
                    animeArray.append(data_obj.get('rank', None))
                    animeArray.append(data_obj.get('popularity', None))
                    animeArray.append(data_obj.get('season', None))
                    animeArray.append(data_obj.get('year', None))
                    
                    # get broadcast information separated
                    broadcast = data_obj.get('broadcast', None)
                    if broadcast.get('day', None) == None:
                        animeArray.append('Unknown')
                        animeArray.append('Unknown')
                        animeArray.append('Unknown')
                    else:
                        animeArray.append(broadcast.get('day', None))
                        animeArray.append(broadcast.get('time', None))
                        animeArray.append(broadcast.get('timezone', None))

                    # get the producers as a list of just the names
                    producerNames = []
                    producers = data_obj.get('producers', None)
                    for producer in producers:
                        producerName = producer.get('name', None)
                        producerNames.append(producerName)
                    if len(producerNames) == 0:
                        animeArray.append('Unknown')
                    else:
                        animeArray.append(producerNames)

                    # get the studios as a list of just the names
                    studioNames = []
                    studios = data_obj.get('studios', None)
                    for studio in studios:
                        studioName = studio.get('name', None)
                        studioNames.append(studioName)
                    if len(studioNames) == 0:
                        animeArray.append('Unknown')
                    else:
                        animeArray.append(studioNames)

                    # get the genres as a list of just the names
                    genreNames = []
                    genres = data_obj.get('genres', None)
                    for genre in genres:
                        genreName = genre.get('name', None)
                        genreNames.append(genreName)
                    if len(genreNames) == 0:
                        animeArray.append('NA')
                    else:
                        animeArray.append(genreNames)
                    
                    # get the themes as a list of just the theme names
                    themeNames = []
                    themes = data_obj.get('themes', None)
                    for theme in themes:
                        themeName = theme.get('name', None)
                        themeNames.append(themeName)
                    if len(themeNames) == 0:
                        animeArray.append('NA')
                    else:
                        animeArray.append(themeNames)

                    # get the demographics as a list of just demographic names
                    demographicNames = []
                    demographics = data_obj.get('demographics', None)
                    for demo in demographics:
                        demoName = demo.get('name', None)
                        demographicNames.append(demoName)
                    if len(demographicNames) == 0:
                        animeArray.append('NA')
                    else:
                        animeArray.append(demographicNames)

                    # write to the csv file
                    if animeArray[0] is not None:
                        # Write the mal_id to the text file
                        csv_writer.writerow(animeArray)
                    animeArray.clear()

# Print a message to confirm that the data has been written to the text file
print("Data values have been written to anime_clean.csv")
