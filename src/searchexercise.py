import sqlite3


## Returns an exercise as a tuple with id and name -> (id, name)
def search_exercise(query:str) -> list:
    if query is None:
        return None
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
                            """, (f"%{query}%",))
        matches = result.fetchall()
            
        if len(matches) >= 1:
            return matches
    
    return None
    
                
            
        
        
        
        
        