#!/usr/local/bin/python
import json
from datetime import datetime
from dateutil.parser import *
import pytz

f = open('schedule.json', 'r')

teams = { 'GSW': 0,
	  'DEN': 0,
	  'BOS': 0,
          'MIL': 0,
          'IND': 0,
          'MEM': 0,
	  'TOR': 0, 
 	  'WAS': 0,
	  'CHI': 0,
	  'ATL': 0,
	  'CLE': 0,
	  'MIA': 0,
	  'ORL': 0,
	  'BKN': 0,
          'CHA': 0,
	  'NYK': 0,
	  'DET': 0,
	  'PHI': 0,
  	  'HOU': 0,
	  'DAL': 0,
	  'POR': 0,
	  'SAS': 0,
	  'SAC': 0,
  	  'NOP': 0,
	  'LAC': 0,
	  'PHX': 0,
	  'UTA': 0,
	  'OKC': 0,
	  'MIN': 0,
	  'LAL': 0 }


myteams = [ 'SAS', 'GSW', 'HOU', 'MIN', 'LAL', 'DEN', 'SAC', 'UTA', 'CHI', 'IND', 'BKN', 'BOS', 'DET', 'TOR', 'MIL', 'PHI' ]
johnnys = [ 'LAC', 'OKC', 'DAL', 'MEM', 'POR', 'PHX', 'NOP', 'UTA', 'CLE', 'WAS', 'MIA', 'CHA', 'ATL', 'NYK', 'ORL', 'PHI' ]

#myteams = [ 'SAS', 'GSW', 'HOU', 'MIN', 'LAL', 'DEN', 'SAC', 'UTA', 'CHI', 'IND', 'BKN', 'BOS', 'NYK', 'TOR', 'ORL', 'PHI' ]
#johnnys = [ 'LAC', 'OKC', 'DAL', 'MEM', 'POR', 'PHX', 'NOP', 'UTA', 'CLE', 'WAS', 'MIA', 'CHA', 'ATL', 'DET', 'MIL', 'PHI' ]

myhome = 0
johnnyhome = 0

buckshome = 0
pistonshome = 0
magichome = 0
knickshome = 0


myguaranteed = 0
johnnyguaranteed = 0

games = 0
x = json.load(f)
for game in x['games']:
#  if pytz.utc.localize(parse('2014-12-1')) < parse(game['scheduled']) and parse(game['scheduled']) < pytz.utc.localize(parse('2015-1-1')):
#  if pytz.utc.localize(parse('2014-10-1')) < parse(game['scheduled']) and parse(game['scheduled']) < pytz.utc.localize(parse('2014-12-1')):
  if pytz.utc.localize(parse('2014-11-26')) < parse(game['scheduled']) and parse(game['scheduled']) < pytz.utc.localize(parse('2014-12-1')):
  #if pytz.utc.localize(parse('2015-1-1')) < parse(game['scheduled']) and parse(game['scheduled']) < pytz.utc.localize(parse('2015-2-1')):
  #if pytz.utc.localize(parse('2015-2-1')) < parse(game['scheduled']) and parse(game['scheduled']) < pytz.utc.localize(parse('2015-3-1')):
  #if pytz.utc.localize(parse('2015-3-1')) < parse(game['scheduled']) and parse(game['scheduled']) < pytz.utc.localize(parse('2015-4-1')):
    games += 1
    home = game['home']['alias']
    away = game['away']['alias']
    stat = ""
    if home in myteams and away in myteams:
      stat = "+"
      myguaranteed += 1
    if home in johnnys and away in johnnys:
      stat = "-" 
      johnnyguaranteed += 1
    if stat == "":
      print game['scheduled'].split("T")[0] + " " + home + " " + away + " " + stat
    if home == 'MIL':
      buckshome += 1
#      print home + " " + away
    if home == 'DET':
      pistonshome += 1
#      print home + " " + away
    if home == 'ORL':
      magichome += 1
#      print home + " " + away
    if home == 'NYK':
      knickshome += 1
#      print home + " " + away
    if home in myteams:
      myhome += 1
    else:
      johnnyhome += 1
    if home in myteams and away in myteams or home in johnnys and away in johnnys:
      teams[home] = teams[home] + 1
      teams[away] = teams[away] + 1

total = 0
for team in myteams:
#  print team + " " + str(teams[team])
  total += teams[team]
#print total / 2
print "-------" 
total = 0
for team in johnnys:
#  print team + " " + str(teams[team])
  total += teams[team]
#print total / 2

print "net guaranteed wins: " + str(myguaranteed) + " - " + str(johnnyguaranteed) + " = " + str(myguaranteed-johnnyguaranteed)
 
#  print datetime(2014,12,1) < datetime(game['scheduled'])
#  print datetime(game['scheduled']) < datetime(2015,1,1)
#  print json.dumps(game, sort_keys=True, indent=4, separators=(',', ': '))
#print json.dumps(x, sort_keys=True, indent=4, separators=(',', ': '))
print "home games: " + str(myhome) + " + " + str(johnnyhome) + " = " + str(games)

#print "bucks home: " + str(buckshome)
#print "pistons home: " + str(pistonshome)
#print "magic home: " + str(magichome)
#print "knicks home: " + str(knickshome)

f.close()
