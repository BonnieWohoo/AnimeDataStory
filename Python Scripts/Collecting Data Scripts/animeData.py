import requests
import json
import time

base_url = 'https://api.jikan.moe/v4/anime/'

page = 1
has_more_data = True
requests_per_minute = 45
seconds_per_minute = 60
from datetime import datetime

# Get the current date and time
current_time = datetime.now().isoformat()

# Open a file for writing
with open('anime_data.json', 'w', encoding='utf-8') as output_file:

    # Add the initial timestamp to the JSON file
    initial_data = {"timestamp": current_time}
    json.dump(initial_data, output_file, ensure_ascii=False)
    output_file.write('\n')  # Add a newline to separate entries
    
    while has_more_data:
        # Calculate the time to wait between requests to achieve the rate limit
        time_to_wait = seconds_per_minute / requests_per_minute
        
        # Make a GET request to the current page
        url = f'{base_url}?page={page}'
        response = requests.get(url)
        
        if response.status_code == 200:
            data = response.json()
            
            # Write the data to the output file
            json.dump(data, output_file, ensure_ascii=False)
            output_file.write('\n')  # Add a newline to separate entries

            try:
                has_next_page = data["pagination"]["has_next_page"]
                #print(True)
            except KeyError:
                has_next_page = False

            if has_next_page == False:
                break;
            
            # Increment the page number
            page += 1
            
            # Sleep to respect the rate limit
            time.sleep(time_to_wait)
        else:
            print(f'Failed to retrieve data from page {page}.')

# File will be automatically closed when the "with" block is exited
print("done")
