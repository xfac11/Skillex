import requests
import time
import random
import sqlite3
from enum import Enum
class ResponseCode(Enum):
    OK = 200
    FORBIDDEN  = 403
    NOT_FOUND = 404
    TOO_MANY_REQUESTS = 429

LINE_UP = '\033[1A'
LINE_CLEAR = '\x1b[2K'

HEADERS = {
        "User-Agent": "FilipFitnessApp/1.0 (personal project; contact: xfac115@gmail.com)"
    }

DB_PATH = "skillex.db"

BASE_URL = "https://raw.githubusercontent.com/yuhonas/free-exercise-db/main/dist/exercises.json"


def get_exercises_from_api(print_debug:bool = False) -> list[dict]:

    session = requests.sessions.Session()

    exercises = []
    response = session.get(BASE_URL, headers=HEADERS)        
    
    try:
        response.raise_for_status()
    except requests.HTTPError as e:
        match e.errno:
            case ResponseCode.FORBIDDEN:
                print(e)
                return []
            case ResponseCode.NOT_FOUND:
                print(e)
                return []
            case ResponseCode.TOO_MANY_REQUESTS:
                print(e)
                return []
            case _:
                print(e)
                return []
        print(e)
        return []
    data = response.json()
        
    if data is None:
        raise Exception("Couldn't retrieve data")
    exercises.extend(data)
    
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

def get_bodypart_from_muscle(primary_muscle:str, category:str) -> str:
    if category == "cardio":
        return "cardio"
    match primary_muscle:
        case "quadriceps":
            return "upper_legs"
        case "shoulders":
            return "shoulder"
        case "abdominals": 
            return "waist"
        case "chest":
            return "chest"
        case "hamstrings":
            return "upper_legs"
        case "triceps":
            return "upper_arms"
        case "biceps":
            return "upper_arms"
        case "lats":
            return "back"
        case "middle back":
            return "back"
        case "calves":
            return "lower_legs"
        case "lower back":
            return "back"
        case "forearms":
            return "lower_arms"
        case "glutes":
            return "upper_legs"
        case "traps":
            return "back"
        case "adductors":
            return "upper_legs"
        case "abductors":
            return "upper_legs"
        case "neck":
            return "neck"
        case _:
            return "cardio"

def save_exercises_to_table(connection:sqlite3.Connection, exercises):
    cursor = connection.cursor()           
              
    for exercise in exercises:
        primary_muscle = exercise["primaryMuscles"][0]
        category = exercise["category"]
        bodypart = get_bodypart_from_muscle(primary_muscle, category)
        cursor.execute("INSERT OR REPLACE INTO exercises VALUES(?, ?, ?, ?, ?, ?)",
                        (exercise["id"], exercise["name"], bodypart, primary_muscle, exercise["equipment"] or "None", str(exercise)))
    

def save_to_database(exercises):
    if exercises is None:
        raise ValueError
    with sqlite3.connect(DB_PATH) as connection:

        create_exercises_table(connection)

        save_exercises_to_table(connection, exercises)

        connection.commit()

def main():
    print("--------------------------------------")
    print(f"Downloading exercises from {BASE_URL}")

    exercises = get_exercises_from_api(True)
    if exercises is None or len(exercises) == 0:
        print("No exercises created. Aborting")
        return
    
    print(f"Saving exercises into {DB_PATH}")
    
    save_to_database(exercises)

    print("Finished!")
    print("--------------------------------------")

if __name__ == "__main__":
    main()

