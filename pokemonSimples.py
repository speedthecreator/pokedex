import requests
def buscarPokemon():
    pokemon = input(
        'Digite o número ou nome do Pokémon que deseja pesquisar: ')

    if pokemon.isdigit():
        response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{pokemon}')
    else:
        response = requests.get(
            f'https://pokeapi.co/api/v2/pokemon/{pokemon.lower().strip()}')

    if response.status_code == 200:
        pokemon_data = response.json()

        print(f"Name: {pokemon_data['name']}")
        print(
            f"Type(s): {[type_data['type']['name'] for type_data in pokemon_data['types']]}")
        print(
            f"Abilities: {[ability_data['ability']['name'] for ability_data in pokemon_data['abilities']]}")
        print(
            f"Stats: {[stat_data['base_stat'] for stat_data in pokemon_data['stats']]}")

        evolution_chain_url = pokemon_data['species']['url']
        response = requests.get(evolution_chain_url)
        species_data = response.json()
        evolution_chain = species_data['evolution_chain']['url']
        response = requests.get(evolution_chain)
        evolution_data = response.json()

        for chain in evolution_data['chain']['evolves_to']:
            print(
                f"Evolution(s): {[evolution_data['species']['name'] for evolution_data in chain['evolves_to']]}")
    else:
        print('Pokémon não encontrado.')
buscarPokemon()
