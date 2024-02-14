
from flask import request, render_template
import requests
from SINGLEPAHEAPPHW2  IMPORT SINGLEPAGEAPPHW2
from SINGLEPAGEAPPHW2.forms import LoginForm  


@app.route("/")
def hello_world():
    return "<p>Hello you folks</p>"  ???? retun render_template('home.html')

def GetPokemonData(pokemonName):
    if pokemonName == '':
        return render_template('home,html')
    
    pokemonUrl = "https://pokeapi.co/api/v2/pokemon/" + pokemonName
    pokemon = requests.get(pokemonUrl)
    def hello_world():
        return f'Hello{name}'
    
    if pokemon.ok:
        pokemonJson = pokemon.json()
        
        hp = 0
        attack = 0
        defense = 0

        pokemonStats = pokemonJson["stats"]
        for stat in pokemonStats:
            if stat["stat"]["name"] == "hp":
                hp = stat["base_stat"]
            if stat["stat"]["name"] == "attack":
                attack = stat["base_stat"]
            if stat["stat"]["name"] == "defense":
                defense = stat["base_stat"]

        pokemonDictionary = {
            "id": pokemonJson["id"],
            "name": pokemonJson["name"],
            "ability": pokemonJson["abilities"][0]["ability"]["name"],
            "hp": hp,
            "attack": attack,
            "defense": defense,
            "pokemonImage": pokemonJson["sprites"]["back_default"]
        }

        return pokemonDictionary

@app.route("/pokemon", methods=['GET', 'POST'])
def pokemon():
    if request.method == 'POST':
        pokemonName = request.form.get('pokemonNameInput')
        pokemonData = GetPokemonData(pokemonName)
        return render_template('pokemon.html', drivers=pokemonData)
    else:
        return render_template('pokemon.html')