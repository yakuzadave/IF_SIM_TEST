# Add imports
from tinydb import TinyDB, Query
import json
import csv
import requests as r
from random import randint, choice



# init DB
tdb = TinyDB('./player_db.json')


# Create a character with defaults and add to TinyDB
def create_character(name):
	obj = {}
	obj['name'] = name
	obj['hp'] = 8
	obj['ac'] = 10
	obj['str'] = 8
	obj['dex'] = 8
	obj['con'] = 8
	obj['int'] = 8
	obj['wis'] = 8
	obj['cha'] = 8
	obj['inv'] = []
	obj['skills'] = []
	obj['conditions'] = []
	obj['lvl'] = 1


	tdb.insert(obj)

	return obj


def load_character(name):
	q = Query()
	players = tdb.search(q.name == name)
	if len(players) > 0:
		player = players[0]
		return player

if __name__ == '__main__':
	load_character('dorne')