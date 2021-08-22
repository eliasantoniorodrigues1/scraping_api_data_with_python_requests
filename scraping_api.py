import requests
import json

url = "https://api.afl.com.au/cfs/afl/wagering?application=Web"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:75.0) Gecko/20100101 Firefox/75.0',
    'Accept': '*/*',
    'Accept-Language': 'pt-BR,pt;q=0.8,en-US;q=0.5,en;q=0.3',
    'Referer': 'https://www.afl.com.au/stats/team-rankings?CompSeason=20&GameWeeks=-1',
    'x-media-mis-token': 'a9e97c8dda00e798f202cbbf172f1b2f',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Origin': 'https://www.afl.com.au',
    'Connection': 'keep-alive'
}

r = requests.get(url, headers=headers)
playdata = r.json()

with open('afl_data.json', 'w') as file:
  file.write(json.dumps(playdata, indent=4))


