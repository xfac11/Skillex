import sqlite3
import datetime
class SleepLogEntry:
    def __init__(self, id:int, user_id:int, date:float, sleep_hours:float):
        self.id = id
        self.user_id = user_id
        self.date = date
        self.sleep_hours = sleep_hours

class SleepLog:
    def __init__(self, user_id):
        self.user_id = user_id
    
    def add_sleep_log_entry(self, sleep_hours:float, date:float = None) -> bool:
        """Adds a sleep log entry with the amount of sleep_hours and the date. If date is None, today is used"""
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
            
            data = (self.user_id, date or datetime.datetime.now().timestamp(), sleep_hours)
            
            cursor.execute("""
                        INSERT INTO sleep_log VALUES(NULL, ?, ?, ?)
                        """, data)
            
            connection.commit()
            
            return True
        return False
    
    def get_all(self) -> list[SleepLogEntry]:
        """Returns all sleep log entries belonging to the user_id"""
        entries = []
        with sqlite3.connect("skillex.db") as connection:
            cursor = connection.cursor()
            
            result = cursor.execute("SELECT * FROM sleep_log WHERE user_id = ? ORDER BY date DESC", (self.user_id))
            
            log = result.fetchall()
            for entry in log:
                entries.append(SleepLogEntry(entry[0], entry[1], entry[2], entry[3]))
        
        return entries
    
    def is_sleep_logged(self) -> bool:
        """Returns True if the user has logged sleep for today. Otherwise False"""
        with sqlite3.connect("skillex.db") as connection:
            cursor = connection.cursor()
            
            result = cursor.execute("SELECT date FROM sleep_log WHERE user_id = ? ORDER BY date DESC", (self.user_id,))
            
            timestamp_date = result.fetchone()
            if timestamp_date is None:
                return False
            
            date = datetime.datetime.fromtimestamp(timestamp_date[0])
            
            if date.date() == datetime.datetime.today().date():
                return True
        return False
    
    def has_logged_yesterday(self) -> bool:
        """Returns True if there is a logged sleep yesterday"""
        with sqlite3.connect("skillex.db") as connection:
            cursor = connection.cursor()
            
            result = cursor.execute("SELECT date FROM sleep_log WHERE user_id = ? ORDER BY date DESC", (self.user_id,))
            
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
    
    def exists(self) -> bool:
        """Returns True if the sleep log table exists in the database"""
        with sqlite3.connect("skillex.db") as connection:
            cursor = connection.cursor()
        
    
            result = cursor.execute("SELECT name FROM sqlite_master WHERE name='sleep_log'")
            if result.fetchone() is None:
                return False
            return True
        return False
        