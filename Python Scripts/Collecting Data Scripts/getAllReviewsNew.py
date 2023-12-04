import requests
import json
import time

def make_jikan_request(anime_id, page):
    base_url = f'https://api.jikan.moe/v4/anime/{anime_id}/reviews'
    params = {'page': page, 'preliminary': 'true', 'spoiler': 'true'}
    response = requests.get(base_url, params=params)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Request failed with status code {response.status_code}")
        return None

def save_to_json(data, anime_id):
    file_name = f'anime_reviews_{anime_id}.json'
    with open(file_name, 'a', encoding='utf-8') as json_file:  # Use 'a' to append to the file
        json_file.write(json.dumps(data))
        json_file.write('\n')  # Add a newline character after each review


def fetch_reviews_for_anime(anime_id, requests_per_minute):
    page = 1
    while True:
        response = make_jikan_request(anime_id, page)

        if response:
            # Check if the response data is empty
            if not response.get('data'):
                print(f"No more reviews found for anime ID {anime_id}.")
                break

            # Append the reviews to the accumulated list
            save_to_json(response, anime_id)
            
            # Increment the page for the next request
            page += 1

            # Introduce rate limiting
            time.sleep(60 / requests_per_minute)
        else:
            # If the response is empty, stop making requests for this anime_id
            print("Empty response. Moving to the next anime ID.")
            break

def main():
    input_file = 'anime_ids_top500.txt'  # File containing anime IDs
    requests_per_minute = 60

    with open(input_file, 'r') as file:
        anime_ids = [line.strip() for line in file.readlines()]

    for anime_id in anime_ids:
        print(f"Processing anime ID: {anime_id}")
        fetch_reviews_for_anime(anime_id, requests_per_minute)

if __name__ == "__main__":
    main()
