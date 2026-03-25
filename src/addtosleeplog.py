import sqlite3
import datetime

def exists_sleep_log() -> bool:
    with sqlite3.connect("skillex.db") as connection:
        cursor = connection.cursor()
        
    
        result = cursor.execute("SELECT name FROM sqlite_master WHERE name='sleep_log'")
        if result.fetchone() is None:
            return False
        return True
    return False

def sleep_log_yesterday(user_id:int) -> bool:
    with sqlite3.connect("skillex.db") as connection:
        cursor = connection.cursor()
        
        result = cursor.execute("SELECT date FROM sleep_log WHERE user_id = ? ORDER BY date DESC", (user_id,))
        
        timestamp_date = result.fetchone()
        if timestamp_date is None:
            return False
        
        date_log = datetime.datetime.fromtimestamp(timestamp_date[0])
        
        log_yesterday = result.fetchone()
        if log_yesterday is None:
            return True
        date_log_yesterday = datetime.datetime.fromtimestamp(log_yesterday[0])
        
        yesterday = datetime.datetime.now() - datetime.timedelta(days=1)
        
        if date_log.date() == datetime.datetime.now().date() and date_log_yesterday.date() == yesterday.date():
            return True
    return False

def is_sleep_log_updated(user_id:int) -> bool:
    with sqlite3.connect("skillex.db") as connection:
        cursor = connection.cursor()
        
        result = cursor.execute("SELECT date FROM sleep_log WHERE user_id = ? ORDER BY date", (user_id,))
        
        timestamp_date = result.fetchone()
        if timestamp_date is None:
            return False
        
        date = datetime.datetime.fromtimestamp(timestamp_date[0])
        
        if date.date() == datetime.datetime.today().date():
            return True
    return False
        

def add_sleep_log_entry(sleep_hours:float, user_id:int) -> bool:
    with sqlite3.connect("skillex.db") as connection:
        cursor = connection.cursor()
        
        cursor.execute("""
                       CREATE TABLE IF NOT EXISTS sleep_log (
                           id INTEGER PRIMARY KEY ASC,
                           user_id INTEGER,
                           date FLOAT,
                           sleep_hours FLOAT,
                           FOREIGN KEY (user_id) REFERENCES users(id)
                       )
                       """)
        
        result = cursor.execute("SELECT name FROM sqlite_master WHERE name='sleep_log'")
        if result.fetchone() is None:
            raise Exception("Could not create or find table")
        
        data = (user_id, datetime.datetime.now().timestamp(), sleep_hours)
        
        cursor.execute("""
                       INSERT INTO sleep_log VALUES(NULL, ?, ?, ?)
                       """, data)
        
        connection.commit()
        
        return True
    return False
        