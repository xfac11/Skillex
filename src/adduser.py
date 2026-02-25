import sqlite3
from src.user import User
def add_user(user:User) -> bool:
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
                           lower_legs INTEGER,
                           back_xp INTEGER,
                           upper_legs_xp INTEGER,
                           waist_xp INTEGER,
                           streak INTEGER,
                           sleep_streak INTEGER,
                           highest_weight INTEGER
                           )
                       """)
        
        
        