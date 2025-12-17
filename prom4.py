
import requests

params = {"limit": 10}
url = "https://pokeapi.co/api/v2/pokemon"

response = requests.get(url, params=params)

if response.status_code == 200:
    lista_pokemon = response.json().get("results", [])
    print("Primeros 10 Pokémon:")
    for pokemon in lista_pokemon:
        print(f"- {pokemon['name'].capitalize()}")
else:
    print("No se pudo conectar con PokéAPI")