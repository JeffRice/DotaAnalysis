#!/usr/bin/env python3

import requests

matchID="5280316503"
key="KEY GOES HERE"
baseURL= "http://api.steampowered.com/IEconDOTA2_570/GetHeroes/v1/"

response = requests.get(baseURL + "?key=" + key)

print(response.status_code)

print(response.json())
