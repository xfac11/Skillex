import sqlite3
from exercise import Exercise
from exerciselogentry import ExerciseLogEntry
class ExerciseLog:
    def __init__(self, user_id:int):
        self.database = "skillex"
        self.user_id = user_id
    
    def add(self, exercise:Exercise, date:float, xp_earned:int, weight_volume:int) -> bool:
        """
        Creates a log entry in the exercise_log table. If no table exists this function also creates it. 
        """
        ### SQL handles the id creation with auto increment
        log_entry = ExerciseLogEntry(-1, date, self.user_id, exercise.id, xp_earned, weight_volume)

        with sqlite3.connect("skillex.db") as connection:

            cursor = connection.cursor()

            cursor.execute("""CREATE TABLE IF NOT EXISTS exercise_log (
                        id INTEGER PRIMARY KEY ASC,
                        date FLOAT,
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

    
    def get(self, exercise_id:str) -> list[ExerciseLogEntry]:
        pass
    
    def get_all(self) -> list[ExerciseLogEntry]:
        pass