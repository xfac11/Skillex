import sqlite3
def exists_exercise_table() -> bool:
    with sqlite3.connect("skillex.db") as connection:
        cursor = connection.cursor()
        result = cursor.execute("SELECT name FROM sqlite_master WHERE name='exercises'")
        if result.fetchone() is None:
            return False
        return True