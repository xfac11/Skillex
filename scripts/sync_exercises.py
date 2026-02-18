import requests
import time
import random
import sqlite3

LINE_UP = '\033[1A'
LINE_CLEAR = '\x1b[2K'

HEADERS = {
        "User-Agent": "FilipFitnessApp/1.0 (personal project; contact: xfac115@gmail.com)"
    }

DB_PATH = "exercises.db"

BASEURL = "https://exercisedb.dev/api/v1/exercises"


def get_exercises_from_api():

    session = requests.sessions.Session()

    current_page = BASEURL
    exercises = []
    progress = 1/150
    while current_page != None:
        response = session.get(current_page, headers=HEADERS)
        if response.status_code == 429:
            wait = 20
            print(f"{int(progress*100)}%")
            time.sleep(wait)
            print(LINE_UP, end=LINE_CLEAR)
            continue

        response.raise_for_status()

        data = response.json()
        
        if data["success"] != True:
            raise Exception("Couln't retrieve data")
        exercises.extend(data["data"])
        
        progress = data["metadata"]["currentPage"] / 150
        print(f"{int(progress*100)}%")

        current_page = data["metadata"]["nextPage"]
        time.sleep(random.uniform(1.0, 3.0))

        print(LINE_UP, end=LINE_CLEAR)
    
    return exercises

def create_table(connection):
    cursor = connection.cursor()

    cursor.execute("""
                   CREATE TABLE IF NOT EXISTS exercises (
                        id TEXT PRIMARY KEY,
                        name TEXT,
                        body_part TEXT,
                        target TEXT,
                        equipment TEXT,
                        raw_json TEXT
                    )
                   """)
    
    result = cursor.execute("SELECT name FROM sqlite_master WHERE name='exercises'")
    if result.fetchone() is None:
        raise Exception("Could not create or find table")
        

