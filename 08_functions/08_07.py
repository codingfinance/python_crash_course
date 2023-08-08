# Album
from typing import Dict


def make_album(artist_name: str, album_title: str) -> Dict:
    album = {artist_name:album_title}
    return album

print(make_album("Jlo", "Bronx"))