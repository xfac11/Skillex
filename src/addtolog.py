import sqlite3

from src.exercise import Exercise
from src.exerciselogentry import ExerciseLogEntry

def create_exercise(exercise_id:str) -> Exercise:
    with sqlite3.connect("skillex.db") as connection:

        cursor = connection.cursor()

        result = cursor.execute("SELECT * FROM exercises WHERE id=(?)", (exercise_id,))

        exercise_api = result.fetchone()

        if exercise_api is None:
            return None

        # id, name, bodypart, target_muscle, equipment
        new_exercise:Exercise = Exercise(exercise_api[0], exercise_api[1], exercise_api[2], exercise_api[3], exercise_api[4])

        return new_exercise
    return None

def add_to_log(user_id:int, exercise:Exercise, date:int, xp_earned:int, weight_volume:int) -> bool:

    ### SQL handles the id creation with auto increment
    log_entry = ExerciseLogEntry(-1, date, user_id, exercise.id, xp_earned, weight_volume)

    with sqlite3.connect("skillex.db") as connection:

        cursor = connection.cursor()

        cursor.execute("""CREATE TABLE IF NOT EXISTS exercise_log (
                       id INTEGER PRIMARY KEY ASC,
                       date INT,
                       user_id INT,
                       exercise_id TEXT,
                       xp_earned INT,
                       weight_volume INT,
                       FOREIGN KEY (user_id) REFERENCES users(id)
                       FOREIGN KEY (exercise_id) REFERENCES exercises(id)
                       )
                       """)
        
        result = cursor.execute("SELECT name FROM sqlite_master WHERE name='exercise_log'")
        if result.fetchone() is None:
            raise Exception("Could not create or find table")
        
        cursor.execute("""
                        INSERT INTO exercise_log VALUES(NULL, ?, ?, ?, ?, ?)
                        """, (log_entry.date, log_entry.user_id, log_entry.exercise_id, log_entry.xp_earned, log_entry.weight_volume))
        
        connection.commit()

        return True
    return False









    

