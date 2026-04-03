import sqlite3
from exercise import Exercise
from exerciselogentry import ExerciseLogEntry
import statistics
import datetime
class ExerciseLog:
    def __init__(self, user_id:int):
        self.database = "skillex"
        self.user_id = user_id
        
    def exists(self) -> bool:
        with sqlite3.connect("skillex.db") as connection:

            cursor = connection.cursor()
            
            result = cursor.execute("SELECT name FROM sqlite_master WHERE name='exercise_log'")
            if result.fetchone() is None:
                return False

            return True
        return False
    
    def add(self, exercise:Exercise, date:float, xp_earned:int, weight_volume:int, speed:float, weight:float, time_minutes:int) -> bool:
        """
        Creates a log entry in the exercise_log table. If no table exists this function also creates it. 
        """
        ### SQL handles the id creation with auto increment
        log_entry = ExerciseLogEntry(-1, date, self.user_id, exercise.id, xp_earned, weight_volume, speed, weight, time_minutes)

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
                        time_minutes INT,
                        FOREIGN KEY (user_id) REFERENCES users(id)
                        FOREIGN KEY (exercise_id) REFERENCES exercises(id)
                        )
                        """)
            
            result = cursor.execute("SELECT name FROM sqlite_master WHERE name='exercise_log'")
            if result.fetchone() is None:
                raise Exception("Could not create or find table")
            
            cursor.execute("""
                            INSERT INTO exercise_log VALUES(NULL, ?, ?, ?, ?, ?, ?, ?, ?)
                            """, (log_entry.date, log_entry.user_id, log_entry.exercise_id, log_entry.xp_earned, log_entry.weight_volume, log_entry.speed, log_entry.weight, log_entry.time_minutes))
            
            connection.commit()

            return True
        return False

    
    def get(self, exercise_id:str) -> list[ExerciseLogEntry]:
        if not self.exists():
            return []
        with sqlite3.connect("skillex.db") as connection:
            cursor = connection.cursor()
            
            result = cursor.execute("SELECT * FROM exercise_log WHERE exercise_id = ? AND user_id = ? ORDER BY date DESC", (exercise_id, self.user_id))
            
            if result is None:
                return []
            
            logs = []
            entries = result.fetchall()
            for entry in entries:
                logs.append(self.create_log_entry_from_tuple(entry))
            
            return logs
        return []
            
    
    def get_all(self) -> list[ExerciseLogEntry]:
        """Returns all entries in the log that belongs to the user ordered by date DESC"""
        with sqlite3.connect("skillex.db") as connection:
            cursor = connection.cursor()
            
            result = cursor.execute("SELECT * FROM exercise_log WHERE user_id = ? ORDER BY date DESC", (self.user_id,))
            
            if result is None:
                return []
            
            logs = []
            entries = result.fetchall()
            for entry in entries:
                logs.append(self.create_log_entry_from_tuple(entry))
            
            return logs
        return []
    
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
    
    def create_log_entry_from_tuple(self, tuple) -> ExerciseLogEntry:
        return ExerciseLogEntry(tuple[0], tuple[1], tuple[2], tuple[3], tuple[4], tuple[5], tuple[6], tuple[7], tuple[8])
    
    def get_days(self, past_days:int = 0, exercise_id:str = None) -> list[ExerciseLogEntry]:
        all_entries = None
        if exercise_id is None:
            all_entries = self.get_all()
        else:
            all_entries = self.get(exercise_id)
        entries = []
        if past_days == 0:
            return all_entries
        
        limit = datetime.datetime.now() - datetime.timedelta(days=past_days)
        for entry in all_entries:
            date = datetime.datetime.fromtimestamp(entry.date)
            if date.date() == limit.date():
                return entries
            entries.append(entry)
        return entries
    