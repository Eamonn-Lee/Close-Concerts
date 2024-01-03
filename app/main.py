import json
from followedArtists import followedArtists, artistNames

with open("../config.json", "r") as config:
    config_data = json.load(config)

client_id = config_data["SPOTIFY_CLIENT_ID"]
client_secret = config_data["SPOTIFY_CLIENT_SECRET"]

user = 'streetJar'  # not actually really needed

followedArtists(client_id, client_secret, user)