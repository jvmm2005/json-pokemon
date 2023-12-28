import requests
import json
import pandas as pd

# Load Pokémon data from the JSON file into a pandas DataFrame
url = 'https://raw.githubusercontent.com/fanzeyi/pokemon.json/master/pokedex.json'
response = requests.get(url)
data = response.json()
pokemon_data = pd.DataFrame(data["pokemon"])

# Display the first 10 rows of the DataFrame
print("First 10 rows of the DataFrame:")
print(pokemon_data.head(10))

# Display the first 10 rows of the DataFrame
print("First 10 rows of the DataFrame:")
print(pokemon_data.head(10))

# a. Total number of Pokémon
total_pokemon = len(pokemon_data)

# b. Highest base HP among all Pokémon
highest_base_hp = pokemon_data['base']['HP'].max()

# c. Pokémon with the highest base Attack
highest_base_attack_pokemon = pokemon_data.loc[pokemon_data['base']['Attack'].idxmax()]['name']['english']

# d. Pokémon with the highest base Defense
highest_base_defense_pokemon = pokemon_data.loc[pokemon_data['base']['Defense'].idxmax()]['name']['english']

# e. Average base Speed of all Pokémon
average_base_speed = pokemon_data['base']['Speed'].mean()

# Displaying the answers
print("\nNumber of Pokémon in total:", total_pokemon)
print("Highest base HP among all Pokémon:", highest_base_hp)
print("Pokémon with the highest base Attack:", highest_base_attack_pokemon)
print("Pokémon with the highest base Defense:", highest_base_defense_pokemon)
print("Average base Speed of all Pokémon:", average_base_speed)