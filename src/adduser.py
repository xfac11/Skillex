import sqlite3
from user import User
def add_user(user:User) -> bool:
    if user is None:
        return False
    with sqlite3.connect("skillex.db") as connection:
        cursor = connection.cursor()
        cursor.execute("""
                       CREATE TABLE IF NOT EXISTS users(
                           id INTEGER PRIMARY KEY ASC,
                           name TEXT,
                           global_xp INTEGER,
                           lower_arms_xp INTEGER,
                           shoulder_xp INTEGER,
                           cardio_xp INTEGER,
                           upper_arms_xp INTEGER,
                           chest_xp INTEGER,
                           lower_legs_xp INTEGER,
                           back_xp INTEGER,
                           upper_legs_xp INTEGER,
                           waist_xp INTEGER,
                           streak INTEGER,
                           sleep_streak INTEGER,
                           highest_weight INTEGER
                           )
                       """)
        params = (user.name,)
        result = cursor.execute("""
                       SELECT * FROM users where name = ?
                       """, params)
        if len(result.fetchall()) != 0:
            return False
        params = (user.name,
                  user.global_xp,
                  user.body_xp.get_bodypart_xp("lower_arms"),
                  user.body_xp.get_bodypart_xp("shoulder"), 
                  user.body_xp.get_bodypart_xp("cardio"),
                  user.body_xp.get_bodypart_xp("upper_arms"),
                  user.body_xp.get_bodypart_xp("chest"),
                  user.body_xp.get_bodypart_xp("lower_legs"),
                  user.body_xp.get_bodypart_xp("back"),
                  user.body_xp.get_bodypart_xp("upper_legs"),
                  user.body_xp.get_bodypart_xp("waist"),
                  user.streak,
                  user.sleep_streak,
                  user.highest_weight)
        cursor.execute("""
                       INSERT INTO users VALUES(NULL, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                       """, params
                       
        )
        
        connection.commit()
        
    return True
        
            
    
        
        