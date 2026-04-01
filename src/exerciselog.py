import sqlite3
from exercise import Exercise
from exerciselogentry import ExerciseLogEntry
import statistics
class ExerciseLog:
    def __init__(self, user_id:int):
        self.database = "skillex"
        self.user_id = user_id
    
    def add(self, exercise:Exercise, date:float, xp_earned:int, weight_volume:int, speed:float, weight:float) -> bool:
        """
        Creates a log entry in the exercise_log table. If no table exists this function also creates it. 
        """
        ### SQL handles the id creation with auto increment
        log_entry = ExerciseLogEntry(-1, date, self.user_id, exercise.id, xp_earned, weight_volume, speed, weight)

        with sqlite3.connect("skillex.db") as connection:

            cursor = connection.cursor()

            cursor.execute("""CREATE TABLE IF NOT EXISTS exercise_log (
                        id INTEGER PRIMARY KEY ASC,
                        date FLOAT,
                        user_id INT,
                        exercise_id TEXT,
                        xp_earned INT,
                        weight_volume INT,
                        speed FLOAT,
                        weight FLOAT,
                        FOREIGN KEY (user_id) REFERENCES users(id)
                        FOREIGN KEY (exercise_id) REFERENCES exercises(id)
                        )
                        """)
            
            result = cursor.execute("SELECT name FROM sqlite_master WHERE name='exercise_log'")
            if result.fetchone() is None:
                raise Exception("Could not create or find table")
            
            cursor.execute("""
                            INSERT INTO exercise_log VALUES(NULL, ?, ?, ?, ?, ?, ?, ?)
                            """, (log_entry.date, log_entry.user_id, log_entry.exercise_id, log_entry.xp_earned, log_entry.weight_volume, log_entry.speed, log_entry.weight))
            
            connection.commit()

            return True
        return False

    
    def get(self, exercise_id:str) -> list[ExerciseLogEntry]:
        pass
    
    def get_all(self) -> list[ExerciseLogEntry]:
        pass
    
    def get_average_speed(self, exercise_id:str) -> float:
        """This is the average speed calculated using the last 30 exercises of this type. """
        
        log_entries = self.get(exercise_id)
        if len(log_entries) == 0:
            return 0
        
        list_of_speeds = list(map(lambda entry : entry.speed, log_entries))
        
        average = statistics.fmean(list_of_speeds[:30])
        
        return average
    
    def get_average_weight_volume(self, exercise_id:str) -> float:
        log_entries = self.get(exercise_id)
        if len(log_entries) == 0:
            return 0
        
        list_of_volumes = list(map(lambda entry : entry.weight_volume, log_entries))
        
        average = statistics.fmean(list_of_volumes[:30])
        
        return average
    
    def get_highest_weight(self, exercise_id:str) -> float:
        log_entries = self.get(exercise_id)
        if len(log_entries) == 0:
            return 0
        
        list_of_weights = list(map(lambda entry : entry.weight, log_entries))
        
        return max(list_of_weights)