import sqlite3
from user import User
def save_user(user:User, bodypart_id:str) -> bool:
    with sqlite3.connect("skillex.db") as connection:
        cursor = connection.cursor()
            
        cursor.execute("""
                    UPDATE users SET global_xp = ?, {} = ? WHERE id = ?
                    """.format(bodypart_id + "_xp"), (user.global_xp, user.body_xp.get_bodypart_xp(bodypart_id), user.id))
        
        connection.commit()
        
        return True
    return False