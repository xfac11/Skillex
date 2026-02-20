import requests
import time
import random
import sqlite3

LINE_UP = '\033[1A'
LINE_CLEAR = '\x1b[2K'

HEADERS = {
        "User-Agent": "FilipFitnessApp/1.0 (personal project; contact: xfac115@gmail.com)"
    }

DB_PATH = "skillex.db"

BASE_URL = "https://exercisedb.dev/api/v1/exercises"


def get_exercises_from_api(print_debug:bool = False) -> list[dict]:

    session = requests.sessions.Session()

    current_page = BASE_URL
    exercises = []
    progress = 1/150
    while current_page != None:
        response = session.get(current_page, headers=HEADERS)
        if response.status_code == 429:
            wait = 20
            if print_debug : print(f"{int(progress*100)}%")
            time.sleep(wait)
            if print_debug : print(LINE_UP, end=LINE_CLEAR)
            continue

        response.raise_for_status()

        data = response.json()
        
        if data["success"] != True:
            raise Exception("Couln't retrieve data")
        exercises.extend(data["data"])
        
        progress = data["metadata"]["currentPage"] / 150
        if print_debug : print(f"{int(progress*100)}%")

        current_page = data["metadata"]["nextPage"]
        time.sleep(random.uniform(1.0, 3.0))

        if print_debug: print(LINE_UP, end=LINE_CLEAR)
    
    return exercises

def create_exercises_table(connection):
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
    
def save_exercises_to_table(connection:sqlite3.Connection, exercises):
    cursor = connection.cursor()

    for exercise in exercises:
        cursor.execute("INSERT OR REPLACE INTO exercises VALUES(?, ?, ?, ?, ?, ?)",
                        (exercise["exerciseId"], exercise["name"], exercise["bodyParts"][0], exercise["targetMuscles"][0], exercise["equipments"][0], str(exercise)))
    

def save_to_database(exercises):
    with sqlite3.connect(DB_PATH) as connection:

        create_exercises_table(connection)

        save_exercises_to_table(connection, exercises)

        connection.commit()

def main():
    print("--------------------------------------")
    print(f"Downloading exercises from {BASE_URL}")

    exercises = get_exercises_from_api(True)

    print(f"Saving exercises into {DB_PATH}")
    save_to_database(exercises)

    print("Finished!")
    print("--------------------------------------")

if __name__ == "__main__":
    main()

