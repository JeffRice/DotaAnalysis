import json
import re


dict = json.load(open("hero_id_translations.txt"))


def multiple_replace(dict, text):
  # Create a regular expression  from the dictionary keys
  # Only count exact matches, converting ids to string names
  regex = re.compile(r'\b(%s)\b' % "|".join(map(re.escape, dict.keys())))
#  regex = re.compile("\b%s\b" % "|".join(map(re.escape, dict.keys())))

  # For each match, look-up corresponding value in dictionary
  return regex.sub(lambda mo: dict[mo.string[mo.start():mo.end()]], text)


with open('testmatch2.json') as json_file:
    data = json.load(json_file)
    for p in data['result']:
        print(p)

    print('')
    print(data['result']['duration'])
    for p in data['result']['players']:
        print(p)
        current_hero = str(p['hero_id'])
        heroInt = p['hero_id']
        print(current_hero)
        mutated_hero = multiple_replace(dict, current_hero)
        p['hero_id'] = mutated_hero
        print(p['hero_id'])
        print(p)
#        s = 'Hero: ' + str(p['hero_id'])
#        print('Kills: ' + str(p['kills']))
#        print('')
    print(data['result']['radiant_win'])


