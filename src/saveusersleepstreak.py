import sqlite3
from user import User
def save_user_sleep_streak(user:User, sleep_streak:int) -> bool:
    if user is None:
        return False
    with sqlite3.connect("skillex.db") as connection:
        cursor = connection.cursor()
            
        cursor.execute("""
                    UPDATE users SET sleep_streak = ? WHERE id = ?
                    """, (sleep_streak, user.id))
        
        connection.commit()
        
        return True
    return False