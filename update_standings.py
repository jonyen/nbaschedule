#!/usr/bin/python
import urllib2
import json
import datetime

import gdata.spreadsheet.service
import gdata.service
import gdata.spreadsheet

#response = urllib2.urlopen("https://api.sportsdatallc.org/nba-t3/schema/nba/standings-v2.0.xsd?api_key=ngcqnwsexw78njrzuxak5kcj")
response = urllib2.urlopen("https://api.sportsdatallc.org/nba-t3/seasontd/2014/reg/standings.json?api_key=ngcqnwsexw78njrzuxak5kcj")
r = response
standings = json.load(r)
#print standings.keys()

client = gdata.spreadsheet.service.SpreadsheetsService()
client.ClientLogin('jonyen@gmail.com', 'mllrojbpmkugsaoe')

doc_key = '1tC2LR7slerVyxVLAmHYxYhvto3yLjim6xWTL2vLlTX8'

mine_west = ['Spurs', 'Warriors', 'Rockets', 'Timberwolves', 'Lakers', 'Nuggets', 'Kings', 'Jazz']
mine_east = ['Bulls', 'Pacers', 'Nets', 'Celtics', 'Pistons', 'Raptors', 'Bucks', '76ers']
johnny_west = ['Clippers', 'Thunder', 'Mavericks', 'Grizzlies', 'Trail Blazers', 'Suns', 'Pelicans', 'Jazz']
johnny_east = ['Cavaliers', 'Wizards', 'Heat', 'Hornets', 'Hawks', 'Knicks', 'Magic', '76ers']

for conference in standings['conferences']:
  for division in conference['divisions']:
    for team in division['teams']:
      print team['name'] + " " + str(team['wins'])
      if team['name'] in mine_west:
        client.UpdateCell(4 + mine_west.index(team['name']), 5, str(team['wins']), doc_key, 5)
      if team['name'] in mine_east:
        client.UpdateCell(13 + mine_east.index(team['name']), 5, str(team['wins']), doc_key, 5)
      if team['name'] in johnny_west:
        client.UpdateCell(4 + johnny_west.index(team['name']), 3, str(team['wins']), doc_key, 5)
      if team['name'] in johnny_east:
        client.UpdateCell(13 + johnny_east.index(team['name']), 3, str(team['wins']), doc_key, 5)

client.UpdateCell(3, 7, datetime.datetime.now().strftime("Last updated: %c"), doc_key, 5)

#print client.GetCellsFeed(doc_key, 5, "R1C1")
