from fighter import Fighter
import threading, requests
from random import sample


with open('dictionary.csv', 'r', encoding='utf8') as file:
    dictionary = {}
    for line in file:
        line = line.strip().split(';')
        if line[0] == 'english':
            continue
        dictionary.update({line[0]: line[1]})
        
keys_list = list(dictionary.keys())
items = sample(keys_list, 2)

api_url = 'https://api.calorieninjas.com/v1/nutrition?query='
query = ' and '.join(items)
response = requests.get(api_url + query, headers={'X-Api-Key': '12RYtNfNTPMo11yTGxd07w==D4zYdmIX69rtsiug'})

if response.status_code == requests.codes.ok:
    fighters = response.json()['items']
else:
    print("Error:", response.status_code, response.text)


fighter1 = Fighter(dictionary[fighters[0]['name']], fighters[0]['calories'], fighters[0]['carbohydrates_total_g'], fighters[0]['protein_g'], round((fighters[0]["carbohydrates_total_g"] + fighters[0]["protein_g"] + fighters[0]["fat_total_g"]), 2))

fighter2 = Fighter(dictionary[fighters[1]['name']], fighters[1]['calories'], fighters[1]['carbohydrates_total_g'], fighters[1]['protein_g'], round((fighters[1]["carbohydrates_total_g"] + fighters[1]["protein_g"] + fighters[1]["fat_total_g"]), 2))

fighter1.set_rival(fighter2)
fighter2.set_rival(fighter1)

fighter1.print_info()
print('VS')
fighter2.print_info()

time1 = fighter1.delay
time2 = fighter2.delay

print('0 s\t\ttaistelu alkaa')

for _ in range(100):

    t1 = threading.Timer(time1, fighter1.strike).start()
    t2 = threading.Timer(time1 + 0.01, fighter1.is_winner).start()    
    time1 += fighter1.delay

    t3 = threading.Timer(time2, fighter2.strike).start()
    t4 = threading.Timer(time2 + 0.01, fighter2.is_winner).start()    
    time2 += fighter2.delay
