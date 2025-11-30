import os
import requests

# Base URL for football-data.co.uk
BASE_URL = "https://www.football-data.co.uk/mmz4281/{season}/E0.csv"

# Seasons to download
SEASONS = ["2223", '2324', '2425', '2526']

RAW_DATA_PATH = os.path.join("data", "raw")
print(f"Raw data string: {RAW_DATA_PATH}")

def download_season(season_code):
    url = BASE_URL.format(season=season_code)
    save_path = os.path.join(RAW_DATA_PATH, f"{season_code}.csv")

    print(f"Downloading season {season_code}...")

    response = requests.get(url)

    if response.status_code == 200:
        with open(save_path, 'wb') as f:
            f.write(response.content)
        print(f"Saved: {save_path}")
    else:
        print(f"Failed to download {season_code}: HTTP {response.status_code}")

def refresh_data():
    #Downloads all seasons to data/raw"
    if not os.path.exists(RAW_DATA_PATH):
        os.makedirs(RAW_DATA_PATH)

    for season in SEASONS:
        download_season(season)

if __name__ == '__main__':
    refresh_data()