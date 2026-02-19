import sqlite3

from exercise import Exercise

def create_exercise(exercise_id:int, exercise_name:str, database:str) -> Exercise:
    connection = sqlite3.connect("exercise.db")

    cursor = connection.cursor()

    result = cursor.execute("SELECT id FROM exercises WHERE id=(?)", (exercise_id))

    exercise_api = result.fetchone()

    # id, name, bodypart, target_muscle, equipment
    new_exercise:Exercise = Exercise(exercise_api[0], exercise_api[1], exercise_api[2], exercise_api[3], exercise_api[4])

    connection.close()

    return new_exercise

def add_to_log(user_id:int, exercise:Exercise, date:int, xp_earned:int,) -> bool:
    connection = sqlite3.connect("skillex.db")

    cursor = connection.cursor()

    cursor.execute("CREATE TABLE IF ")





    

