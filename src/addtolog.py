import sqlite3

from src.exercise import Exercise

def create_exercise(exercise_id:str) -> Exercise:
    with sqlite3.connect("exercises.db") as connection:

        cursor = connection.cursor()

        result = cursor.execute("SELECT * FROM exercises WHERE id=(?)", (exercise_id,))

        exercise_api = result.fetchone()

        if exercise_api is None:
            return None

        # id, name, bodypart, target_muscle, equipment
        new_exercise:Exercise = Exercise(exercise_api[0], exercise_api[1], exercise_api[2], exercise_api[3], exercise_api[4])

        return new_exercise
    return None

def add_to_log(user_id:int, exercise:Exercise, date:int, xp_earned:int,) -> bool:
    connection = sqlite3.connect("skillex.db")

    cursor = connection.cursor()

    cursor.execute("CREATE TABLE IF ")





    

