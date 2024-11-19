import requests
import json

API_BASE = "https://rickandmortyapi.com/api"

def fetch_data(url):
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"შეცდომა URL-ზე მოთხოვნისას {url}, სტატუს კოდი: {response.status_code}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"დაკავშირების შეცდომა: {e}")
        return None

def fetch_character_episodes(characters_url):
    character_episodes = {}
    next_url = characters_url

    while next_url:
        print(f"Fetching data from: {next_url}")
        data = fetch_data(next_url)
        if not data:
            break

        for character in data['results']:
            character_name = character['name']
            episode_urls = character['episode']
            episode_names = []

            for episode_url in episode_urls:
                episode_data = fetch_data(episode_url)
                if episode_data:
                    episode_names.append(episode_data['name'])

            character_episodes[character_name] = episode_names

        next_url = data['info']['next']
    return character_episodes

api_data = fetch_data(API_BASE)
if api_data:
    characters_url = api_data.get("characters")
    locations_url = api_data.get("locations")
    episodes_url = api_data.get("episodes")

    if characters_url:
        character_episodes = fetch_character_episodes(characters_url)

        with open("character_episodes.json", "w", encoding="utf-8") as json_file:
            json.dump(character_episodes, json_file, ensure_ascii=False, indent=4)

        print("პერსონაჟების მონაცემები ჩაიწერა character_episodes.json ფაილში!")

    if locations_url:
        locations_data = fetch_data(locations_url)
        with open("locations.json", "w", encoding="utf-8") as json_file:
            json.dump(locations_data, json_file, ensure_ascii=False, indent=4)

        print("ლოკაციების მონაცემები ჩაიწერა locations.json ფაილში!")

    if episodes_url:
        episodes_data = fetch_data(episodes_url)
        with open("episodes.json", "w", encoding="utf-8") as json_file:
            json.dump(episodes_data, json_file, ensure_ascii=False, indent=4)

        print("ეპიზოდების მონაცემები ჩაიწერა episodes.json ფაილში!")