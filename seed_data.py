import requests
from random import choice, randint, uniform
from datetime import date

BASE_URL = "http://127.0.0.1:8000"

# Creators
creators_data = [
    {"country": "Italy", "full_name": "Leonardo da Vinci", "years_of_life": "1452-1519", "main_direction": "Renaissance"},
    {"country": "Netherlands", "full_name": "Vincent van Gogh", "years_of_life": "1853-1890", "main_direction": "Post-Impressionism"},
    {"country": "Spain", "full_name": "Pablo Picasso", "years_of_life": "1881-1973", "main_direction": "Cubism"},
    {"country": "Norway", "full_name": "Edvard Munch", "years_of_life": "1863-1944", "main_direction": "Expressionism"},
    {"country": "France", "full_name": "Claude Monet", "years_of_life": "1840-1926", "main_direction": "Impressionism"},
    {"country": "USA", "full_name": "Andy Warhol", "years_of_life": "1928-1987", "main_direction": "Pop Art"},
]

creator_ids = []
for creator in creators_data:
    r = requests.post(f"{BASE_URL}/creators/", json=creator)
    resp = r.json()
    creator_ids.append(resp["id"])
    print(f"Created creator: {resp['full_name']} (id={resp['id']})")

# Storage Places
storage_places_data = [
    {"name": "Louvre", "type": "Museum", "country": "France", "opening_date": "1793-08-10"},
    {"name": "Van Gogh Museum", "type": "Museum", "country": "Netherlands", "opening_date": "1973-06-02"},
    {"name": "Prado Museum", "type": "Museum", "country": "Spain", "opening_date": "1819-11-19"},
    {"name": "MoMA", "type": "Museum", "country": "USA", "opening_date": "1929-11-07"},
]

storage_ids = []
for storage in storage_places_data:
    r = requests.post(f"{BASE_URL}/storage_places/", json=storage)
    resp = r.json()
    storage_ids.append(resp["id"])
    print(f"Created storage place: {resp['name']} (id={resp['id']})")

# Artworks
artworks_data = []

base_names = [
    "Mona Lisa",
    "Starry Night",
    "Guernica",
    "The Scream",
    "Water Lilies",
    "Campbell's Soup Cans",
    "Girl with a Pearl Earring",
    "The Persistence of Memory",
    "American Gothic",
    "The Night Watch"
]

for i in range(1, 101):
    artwork = {
        "price": round(uniform(100000, 2000000), 2),
        "type": choice(["Painting", "Sculpture", "Drawing"]),
        "name": f"{choice(base_names)} #{i}",
        "material": choice([
            "Oil on canvas",
            "Oil on poplar",
            "Tempera on panel",
            "Marble"
        ]),
        "dimensions": f"{randint(50, 300)}x{randint(50, 300)} cm",
        "created_year": randint(1450, 2000),
        "creator_id": choice(creator_ids),
        "storage_place_id": choice(storage_ids)
    }
    artworks_data.append(artwork)

for artwork in artworks_data:
    r = requests.post(f"{BASE_URL}/artworks/", json=artwork)
    resp = r.json()
    print(f"Created artwork: {resp['name']} (id={resp['id']})")

print("Seed data loaded successfully!")

