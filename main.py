from fighter import Fighter
import threading, requests
from random import sample, choice

with open('dictionary.csv', 'r', encoding='utf8') as file:
    dictionary = {}
    for line in file:
        line = line.strip().split(';')
        if line[0] == 'english':
            continue
        dictionary.update({line[0]: line[1]})


with open('winner.txt', 'r', encoding='utf8') as file:
    winner = file.read()


keys_list = list(dictionary.keys())
items = sample(keys_list, 2)

if len(winner):
    items = []
    items.append(winner)

    while len(items) < 2:
        x = choice(keys_list)
        if x not in items: items.append(x)


api_url = 'https://api.calorieninjas.com/v1/nutrition?query='
query = ' and '.join(items)
response = requests.get(api_url + query, headers={'X-Api-Key': '12RYtNfNTPMo11yTGxd07w==D4zYdmIX69rtsiug'})

if response.status_code == requests.codes.ok:
    fighters = response.json()['items']
else:
    print("Error:", response.status_code, response.text)

fighter1 = Fighter(fighters[0]['name'], dictionary[fighters[0]['name']],  fighters[0]['calories'], fighters[0]['carbohydrates_total_g'], fighters[0]['protein_g'], round((fighters[0]["carbohydrates_total_g"] + fighters[0]["protein_g"] + fighters[0]["fat_total_g"]), 2))

fighter2 = Fighter(fighters[1]['name'], dictionary[fighters[1]['name']], fighters[1]['calories'], fighters[1]['carbohydrates_total_g'], fighters[1]['protein_g'], round((fighters[1]["carbohydrates_total_g"] + fighters[1]["protein_g"] + fighters[1]["fat_total_g"]), 2))


fighter1.set_rival(fighter2)
fighter2.set_rival(fighter1)


def attack(fighter: object, time: float) -> None:
    t1 = threading.Timer(time, fighter.strike).start()
    t2 = threading.Timer(time + 0.01, fighter.is_winner).start()
    

fighter1.print_info()
print('  VS ')
fighter2.print_info()
print('0 s\t\ttaistelu alkaa\n')


time1 = fighter1.delay
time2 = fighter2.delay

for _ in range(100):

    attack(fighter1, time1)
    time1 += fighter1.delay

    attack(fighter2, time2)
    time2 += fighter2.delay
