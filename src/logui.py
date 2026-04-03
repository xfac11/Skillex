import datetime
from exerciselogentry import ExerciseLogEntry
from exercisecatalog import ExerciseCatalog
import click
class LogUI():
    def __init__(self, entries:list[ExerciseLogEntry]):
        self.entries = entries
    
    def to_string(self) -> str:
        str = ""
        current_date = self.entries[0].date
        str += click.style(f"Date: {datetime.datetime.fromtimestamp(current_date).date()} \n", fg="blue")
        str += "--------\n"
        for entry in self.entries:
            if datetime.datetime.fromtimestamp(current_date).date() != datetime.datetime.fromtimestamp(entry.date).date():
                current_date = entry.date
                str += click.style(f"Date: {datetime.datetime.fromtimestamp(current_date).date()} \n", fg="blue")
            
            exercise = ExerciseCatalog().get_exercise(entry.exercise_id)
            
            str += click.style(exercise.name.capitalize() + "\n", fg="green")
            
            str += f"{entry.time_minutes} minutes\n{entry.xp_earned} xp\n"
            if entry.weight != 0.0:
                str += f"{entry.weight} kg\n"
            if entry.speed != 0.0:
                str += f"{entry.speed} km/h\n"
            str += "--------\n"
        return str
            