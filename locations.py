# Add imports
from tinydb import TinyDB, Query
import json
import csv
import requests as r
from random import randint, choice

# init DB
tdb = TinyDB('./location_db.json')


def add_location(location):
    tdb.insert(location)
    print(f"{location['name']} has been successfully added to the DB.")


def get_location(query):
    if 'name' in query:
        q = Query()
        res = tdb.search(q.name == query['name'])
        return res
