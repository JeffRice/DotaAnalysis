#!/usr/bin/env python3

import requests

# matchID="5280316503"
key="KEY GOES HERE"
baseURL= "https://api.steampowered.com/IDOTA2Match_570/"

#response = requests.get(baseURL + "GetMatchHistory/V001/?key=" + key)
response = requests.get(baseURL + "GetMatchHistoryBySequenceNum/V001/?key=" + key + "&start_at_match_seq_num=4430604303")

print(response.json())

