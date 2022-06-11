# Add imports here
from tinydb import TinyDB, Query
import airtable
import json
import csv
import requests as r
from random import randint, choice
from menus import main_menu
from player import create_character, load_character
from locations import add_location, get_location
from d20 import roll
from rich import print
from rich.table import Table
import os
from replit import db

# init config
tdb = TinyDB('./db.json')

print("Starting game...\n")
#player = main_menu()
#print(f"{player.name} had been loaded")

at_key = os.environ['AT_KEY']

t_station = airtable.Airtable(base_id='apphBqi4nVudO75tM', api_key=at_key)

j1 = t_station.iterate(table_name="Jobs",batch_size=5)
loc = t_station.iterate(table_name="Locations",batch_size=5)


