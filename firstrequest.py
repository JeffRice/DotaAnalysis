#!/usr/bin/env python3

import requests

matchID="5280317169"
key="KEY GOES HERE"
baseURL= "https://api.steampowered.com/IDOTA2Match_570/"

response = requests.get(baseURL + "GetMatchDetails/V001/?key=" + key + "&match_id=" + matchID)

print(response.status_code)

print(response.json())
