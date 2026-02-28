from src.user import User
from src.bodyparts import BodyParts
import sqlite3
def get_user(name:str) -> User:
    with sqlite3.connect("skillex.db") as connection:
    
        cursor = connection.cursor()

        params = (name,)
        result = cursor.execute("SELECT * FROM users WHERE name = ?", params)

        user_db = result.fetchone()
        if user_db == None:
            return None
        body_parts = BodyParts()
        user = User(user_db[0], user_db[1], user_db[2], body_parts, user_db[12], user_db[13], user_db[14])
        user.body_xp.set_bodypart_xp("lower_arms", user_db[3])
        user.body_xp.set_bodypart_xp("shoulder", user_db[4])
        user.body_xp.set_bodypart_xp("cardio", user_db[5])
        user.body_xp.set_bodypart_xp("upper_arms", user_db[6])
        user.body_xp.set_bodypart_xp("chest", user_db[7])
        user.body_xp.set_bodypart_xp("lower_legs", user_db[8])
        user.body_xp.set_bodypart_xp("back", user_db[9])
        user.body_xp.set_bodypart_xp("upper_legs", user_db[10])
        user.body_xp.set_bodypart_xp("waist", user_db[11])

        return user
    return None





