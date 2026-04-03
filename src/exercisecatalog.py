from exercise import Exercise
import sqlite3
class ExerciseCatalog:
    def __init__(self):
        self.database = "skillex.db"
        self.table = "exercises"
    
    def exists_table(self) -> bool:
        """Returns True if the related exercises table exists"""
        with sqlite3.connect("skillex.db") as connection:
            cursor = connection.cursor()
            result = cursor.execute("SELECT name FROM sqlite_master WHERE name='exercises'")
            if result.fetchone() is None:
                return False
            return True
        return False
    
    def get_exercise(self, id:str) -> Exercise:
        """Returns the exercise with the given id or None"""
        if id is None:
            return None
        with sqlite3.connect(self.database) as connection:
            cursor = connection.cursor()
            
            result = cursor.execute("SELECT id, name, body_part, target, equipment FROM exercises WHERE id = ?", (id,))
            
            if result is not None:
                exercise_tuple = result.fetchone()
                return Exercise(exercise_tuple[0], exercise_tuple[1], exercise_tuple[2], exercise_tuple[3], exercise_tuple[4])
        return None
            
    
    def search_exercise(self, query:str, partial:bool = False) -> list[Exercise]:
        """
        Returns a list of exercises
        If no search results, an empty list is returned
        """
        exercise_hits = []
        if query is None:
            return []
        with sqlite3.connect(self.database) as connection:
            cursor = connection.cursor()
            
            if not partial:
                ## Search by exact id
                result = cursor.execute("""
                            SELECT id, name, body_part, target, equipment FROM exercises WHERE id = ? 
                            """, (query,))
                row = result.fetchone()
                if row:
                    exercise_hits.append(Exercise(row[0], row[1], row[2], row[3], row[4]))
                    return exercise_hits
                
                ## Search by exact name lowered
                result = cursor.execute("""
                                    SELECT id, name, body_part, target, equipment FROM exercises WHERE lower(name) = lower(?)
                                    """, (query,))
                row = result.fetchone()
                if row:
                    exercise_hits.append(Exercise(row[0], row[1], row[2], row[3], row[4]))
                    return exercise_hits
            
            ## Search partial matching using like
            result = cursor.execute("""
                                SELECT id, name, body_part, target, equipment FROM exercises WHERE lower(name) LIKE lower(?) ORDER BY length(name)
                                """, (f"%{query.strip().lower().replace(" ", "_")}%",))
            matches = result.fetchall()
                
            if len(matches) >= 1:
                for match in matches:
                    exercise_hits.append(Exercise(match[0], match[1], match[2], match[3], match[4]))
                return exercise_hits
        
        return []
    
    def search_exercise_bodypart(self, query:str, body_part:str, partial:bool = False) -> list[Exercise]:
        """
        Returns a list of exercises
        If no search results, an empty list is returned
        """
        exercise_hits = []
        if query is None and body_part is None:
            return []
        with sqlite3.connect(self.database) as connection:
            cursor = connection.cursor()
            
            if not partial:
                ## Search by exact id
                result = cursor.execute("""
                            SELECT id, name, body_part, target, equipment FROM exercises WHERE id = ? 
                            """, (query,))
                row = result.fetchone()
                if row:
                    exercise_hits.append(Exercise(row[0], row[1], row[2], row[3], row[4]))
                    return exercise_hits
                
                ## Search by exact name lowered
                result = cursor.execute("""
                                    SELECT id, name, body_part, target, equipment FROM exercises WHERE lower(name) = lower(?) AND body_part = lower(?)
                                    """, (query, body_part))
                row = result.fetchone()
                if row:
                    exercise_hits.append(Exercise(row[0], row[1], row[2], row[3], row[4]))
                    return exercise_hits
            ## Search partial matching using like
            result = cursor.execute("""
                                SELECT id, name, body_part, target, equipment  FROM exercises WHERE lower(name) LIKE lower(?) AND body_part LIKE lower(?) ORDER BY length(name)
                                """, (f"%{query.strip().lower().replace(" ", "_")}%", body_part))
            matches = result.fetchall()
            
            
            if len(matches) >= 1:
                for match in matches:
                    exercise_hits.append(Exercise(match[0], match[1], match[2], match[3], match[4]))
                return exercise_hits
        
        return []        