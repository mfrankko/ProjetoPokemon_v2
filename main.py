import requests
from bs4 import BeautifulSoup

def get_pokemon_data(pokemon_name):
    try:
        pokemon_name = pokemon_name.lower()
        pokemon_url = f'https://www.pikalytics.com/pokedex/gen9vgc2023series1/{pokemon_name}'
        res = requests.get(pokemon_url)
        res.raise_for_status()
        soup = BeautifulSoup(res.text, 'html.parser')
        move1 = soup.select_one('#moves_wrapper > div > div:nth-child(1) > div:nth-child(1)').text.strip()
        move2 = soup.select_one('#moves_wrapper > div > div:nth-child(2) > div:nth-child(1)').text.strip()
        move3 = soup.select_one('#moves_wrapper > div > div:nth-child(3) > div:nth-child(1)').text.strip()
        move4 = soup.select_one('#moves_wrapper > div > div:nth-child(4) > div:nth-child(1)').text.strip()
        item = soup.select_one('#items_wrapper > div > div:nth-child(1) > div:nth-child(2)').text.strip()
        ability = soup.select_one('#abilities_wrapper > div > div:nth-child(1) > div:nth-child(1)').text.strip()
        nature = soup.select_one('#dex_spreads_wrapper > div > div:nth-child(1) > div:nth-child(1)').text.strip()
        ev_hp = soup.select_one('#dex_spreads_wrapper > div > div:nth-child(1) > div:nth-child(2)').text.strip()
        ev_atk = soup.select_one('#dex_spreads_wrapper > div > div:nth-child(1) > div:nth-child(3)').text.strip()
        ev_def = soup.select_one('#dex_spreads_wrapper > div > div:nth-child(1) > div:nth-child(4)').text.strip()
        ev_spa = soup.select_one('#dex_spreads_wrapper > div > div:nth-child(1) > div:nth-child(5)').text.strip()
        ev_spd = soup.select_one('#dex_spreads_wrapper > div > div:nth-child(1) > div:nth-child(6)').text.strip()
        ev_spe = soup.select_one('#dex_spreads_wrapper > div > div:nth-child(1) > div:nth-child(7)').text.strip()
        return {
            "move1": move1,
            "move2": move2,
            "move3": move3,
            "move4": move4,
            "item": item,
            "ability": ability,
            "nature": nature,
            "ev_hp": ev_hp,
            "ev_atk": ev_atk,
            "ev_def": ev_def,
            "ev_spa": ev_spa,
            "ev_spd": ev_spd,
            "ev_spe": ev_spe
        }
    except requests.exceptions.HTTPError as e:
        print(f'Error: {e}')
    except Exception as e:
        print(f'Error: Pokemon not found')

pokemon = input('Enter the name of the Pokemon: ')
data = get_pokemon_data(pokemon)
print(pokemon + ' @' + data.get('item'))
print(data.get('ability') + ' | ' + data.get('nature'))
print(data.get('move1') + '|' + data.get('move2') + '|' + data.get('move3') + '|' + data.get('move4') + '|')
print(data.get('ev_hp') + data.get('ev_atk') + data.get('ev_def') + data.get('ev_spa') + data.get('ev_spd') + data.get('ev_spe'))
