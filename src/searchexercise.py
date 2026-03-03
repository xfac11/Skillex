import sqlite3



def search_exercise(query:str) -> list[tuple]:
    """
    Returns a list of exercises as a tuple with id and name -> [(exercise_id, exercise_name),...]
    If no search results, an empty list is returned
    """
    if query is None:
        return []
    with sqlite3.connect("skillex.db") as connection:
        cursor = connection.cursor()
        
        ## Search by exact id
        result = cursor.execute("""
                       SELECT id, name FROM exercises WHERE id = ? 
                       """, (query,))
        row = result.fetchone()
        if row:
            return [row]
        
        ## Search by exact name lowered
        result = cursor.execute("""
                            SELECT id, name FROM exercises WHERE lower(name) = lower(?)
                            """, (query,))
        row = result.fetchone()
        if row:
            return [row]
        
        ## Search partial matching using like
        result = cursor.execute("""
                            SELECT id, name FROM exercises WHERE lower(name) LIKE lower(?) ORDER BY length(name)
                            """, (f"%{query.strip().lower().replace(" ", "_")}%",))
        matches = result.fetchall()
            
        if len(matches) >= 1:
            return matches
    
    return []

def search_exercise_bodypart(query, body_part) -> list[tuple]:
    """
    Returns a list of exercises as a tuple with id and name -> [(exercise_id, exercise_name),...]
    If no search results, an empty list is returned
    """
    if query is None and body_part is None:
        return []
    with sqlite3.connect("skillex.db") as connection:
        cursor = connection.cursor()
        
        ## Search by exact id
        result = cursor.execute("""
                       SELECT id, name FROM exercises WHERE id = ? 
                       """, (query,))
        row = result.fetchone()
        if row:
            return [row]
        
        ## Search by exact name lowered
        result = cursor.execute("""
                            SELECT id, name FROM exercises WHERE lower(name) = lower(?) AND body_part = lower(?)
                            """, (query, body_part))
        row = result.fetchone()
        if row:
            return [row]
        
        ## Search partial matching using like
        result = cursor.execute("""
                            SELECT id, name FROM exercises WHERE lower(name) LIKE lower(?) AND body_part LIKE lower(?) ORDER BY length(name)
                            """, (f"%{query.strip().lower().replace(" ", "_")}%", body_part))
        matches = result.fetchall()
            
        if len(matches) >= 1:
            return matches
    
    return []
    
                
            
        
        
        
        
        