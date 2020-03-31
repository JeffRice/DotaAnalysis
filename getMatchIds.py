import time
import json
import requests
import pymongo
import re

#external dict file for translations
dict = json.load(open("hero_id_translations.txt"))


## converting hero ids to string names
def multiple_replace(dict, text):
  # Create a regular expression  from the dictionary keys
  # Only count exact matches, use external dict to convert
  regex = re.compile(r'\b(%s)\b' % "|".join(map(re.escape, dict.keys())))

  # For each match, look-up corresponding value in dictionary
  return regex.sub(lambda mo: dict[mo.string[mo.start():mo.end()]], text)



#url and key for dota2 api
key="KEY GOES HERE"
baseURL= "https://api.steampowered.com/IDOTA2Match_570/"

#store and count match ids
new_matches = []
matchesCount = 0


with open('latest100matches.json') as json_file:
    data = json.load(json_file)
#    for p in data['result']:
 #       print(p)

    for p in data['result']['matches']:
        print(str(matchesCount) + " match id:" + str(p['match_id']))
        new_matches.append(p['match_id'])
        matchesCount+=1

print(new_matches)
#        s = 'Hero: ' + str(p['hero_id'])
#        print('Kills: ' + str(p['kills']))
#        print('')



## db connection
from pymongo import MongoClient
client = MongoClient('mongodb://localhost:27017')

db = client.dotamatches

matches = db.matches725b



for i in new_matches:
    time.sleep(3)
    print(i)
    matchID=str(i)
    response = requests.get(baseURL + "GetMatchDetails/V001/?key=" + key + "&match_id=" + matchID)
#   call the dota2 api with the current match_id
    print(response.status_code)
    print(response.json())
    print(response.json()['result']['human_players'])
    if response.json()['result']['human_players'] < 10:
        #could update this var, it includes matchleavers, and 10 human players conditions
        continue
#    print(response.json()['result']['game_mode'])


    matchLeavers = "no"
    players = response.json()['result']['players']
    players_array = []
    dire_players = []
    radiant_players = []
    for x in players:
        current_hero = str(x['hero_id'])
#        print(current_hero)
        ## call function to convert hero ids
        mutated_hero = multiple_replace(dict, current_hero)
        x['hero_id'] = mutated_hero
        players_array.append(mutated_hero)
        print(x['leaver_status'])
        if x['leaver_status'] > 0:
            matchLeavers = "yes"
        if x['player_slot'] < 5:
            radiant_players.append(mutated_hero)
        if x['player_slot'] > 5:
            dire_players.append(mutated_hero)
    match_duration = response.json()['result']['duration']
    if match_duration < 2700:
        print('Match less than 45 mins')
    print(match_duration)
    print(matchLeavers)
    print(response.json()['result']['game_mode'])
    if matchLeavers == "no":
        match_data = response.json()['result']
#this is a match we want, store just the data we want in filtered_match_data
        filtered_match_data = {"match_id": match_data['match_id'], "players": players_array, "duration": match_data['duration'], 
        "start_time" : match_data["start_time"], "radiant_win" : match_data["radiant_win"], "game_mode": match_data['game_mode'],
        "radiant_players" : radiant_players, "dire_players" : dire_players }
#        "radiant_players" : radiant_players, "dire_players" : dire_players, "all_player_data": match_data['players'] }
        print("filtered match data: ")
        print(filtered_match_data)
        result = matches.insert_one(filtered_match_data)
        print('One match: {0}'.format(result.inserted_id))

#   check the details to see if you want to store the game
#done
#   if yes, add the match details to an object, WAIT 3 SECONDS!!!
#eh, why not just insert the current match, DONE
#   after finishing loop, bulk insert the match details into mongodb
#done
print('jobs dun')
