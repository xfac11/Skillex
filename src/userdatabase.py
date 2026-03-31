from user import User
import sqlite3
class UserDatabase:
    def __init__(self, database_path:str = "skillex.db"):
        self.database_path = database_path
        self.table = "users"
    
    def add_user(self, user:User) -> bool:
        """Adds the user to the database table. 
        Returns False if user is none or has the same name as some other user. 
        Otherwise returns True"""
        if user is None:
            return False
        with sqlite3.connect(self.database_path) as connection:
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
    
    def remove_user(self, name:str) -> bool:
        raise NotImplementedError
    
    def get_user(self, name:str) -> User:
        """Returns the user with this name or None if no was found"""
        with sqlite3.connect(self.database_path) as connection:
    
            cursor = connection.cursor()

            params = (name,)
            result = cursor.execute("SELECT * FROM users WHERE name = ?", params)

            user_db = result.fetchone()
            if user_db == None:
                return None
            user = User(id=user_db[0], name=user_db[1], global_xp=user_db[2], streak=user_db[12], sleep_streak=user_db[13])
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
    
    def save_user(self, user:User) -> bool:
        """Saves all the variables of a user to the database"""
        with sqlite3.connection(self.database_path) as connection:
            cursor = connection.cursor()
            
            cursor.execute("""
                    UPDATE users 
                    SET name = ?,
                    global_xp = ?,
                    lower_arms_xp = ?,
                    shoulder_xp = ?,
                    cardio_xp = ?,
                    upper_arms_xp = ?,
                    chest_xp = ?,
                    lower_legs_xp = ?,
                    back_xp = ?,
                    upper_legs_xp = ?,
                    waist_xp = ?,
                    streak = ?,
                    sleep_streak = ?
                    WHERE id = ?
                    """, (user.name,
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
                          user.sleep_streak)
            )
        
            connection.commit()
            
            return True
        return False