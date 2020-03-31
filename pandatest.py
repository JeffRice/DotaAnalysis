import pandas as panda
import json
import numpy
from pandas import json_normalize

df = panda.read_json('pandajson.json')

#df_loc = df.loc[3]

df_head = df.head(10)

print(df_head)

#print(df_loc)


df_info = df.info()

print(df_info)

#df_shape = df.shape()

#print(df_shape)



#players_data = json_normalize(data = df['players'], 
#                            meta =['account_id', 'player_slot', 'hero_id'])


#normalized_playerdata = players_data.head()

#print(normalized_playerdata)

newflat = json_normalize(df['matches'])

newflat_head = newflat.head()

type(newflat_head)

print(newflat_head)

print('test_filter')

newnew = newflat_head[newflat_head['players'] == "axe"]

print(newnew)

print('test slicing')


subset = newflat_head[['match_id', 'players']]

print('subset:')

print(subset)

#print('filter?')

#filtertest = DataFrame(subset, columns= ['players'])

#print(filtertest)


# converting to list
player_list = subset["players"].tolist()

print('players .tolist(): ')
print(player_list)

panda.set_option('display.float_format', lambda x: '%.0f' % x)

player_data = json_normalize(data=df['matches'], record_path='players', 
                            meta=['account_id', 'player_slot','hero_id'], errors='ignore', record_prefix='_')
print('player_data:')
print(player_data)

flat_player_head = player_data.head(20)

#flat_player_head = player_data.head(10)

print(flat_player_head)

print('test_filter')

newnew = player_data[player_data['_hero_id'] == "axe"]

print(newnew)


#print('test_loc')

#loc_subset = player_data.loc['axe']

#print(test_loc)

