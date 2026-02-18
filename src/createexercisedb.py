import requests
import time
import random
def get_exercises_from_api():

    HEADERS = {
        "User-Agent": "FilipFitnessApp/1.0 (personal project; contact: xfac115@gmail.com)"
    }

    session = requests.sessions.Session()

    baseurl = "https://exercisedb.dev/api/v1/"

    endpoint = "exercises"

    current_page = baseurl + endpoint
    exercises = {}
    index = 0
    progress = 1/150
    while current_page != None:
        for _ in range(5):
            r = session.get(current_page, headers=HEADERS)
            if r.status_code == 429:
                wait = 15
                print(f"Rate limited. Waiting {wait}s...")
                time.sleep(wait)
                continue
            break

        
        data = r.json()
        
        if data["success"] != True:
            raise Exception("Couln't retrieve data")
        progress = data["metadata"]["currentPage"] / 150
        print(f"{int(progress*100)}%")
        exercises_in_api = data["data"]
        for exercise in exercises_in_api:
            exercises[index] = exercise
            index += 1
        
        if data["metadata"]["nextPage"] == None:
            break
        current_page = data["metadata"]["nextPage"]
        time.sleep(random.uniform(1.0, 3.0))
    
    return exercises


        

