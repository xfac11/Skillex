from exercise import Exercise
from exercisecatalog import ExerciseCatalog
import click
import ast
class ExerciseUI:
    def __init__(self, exercise:Exercise):
        self.exercise = exercise
        
    def to_string(self) -> str:
        dict_str = ExerciseCatalog().get_exercise_raw_json(self.exercise.id)
        data = ast.literal_eval(dict_str)
        string = ""
        string += click.style(f"{self.exercise.name.capitalize()}\n", fg="green")
        string += f"Body part: {self.exercise.bodypart.capitalize()}\n"
        string += f"Target muscle: {self.exercise.target_muscle.capitalize()}\n"
        string += f"Equipment: {self.exercise.equipment.capitalize()}\n"
        string += f"Link to gif: {data["gifUrl"]}\n"
        string += f"Instructions:\n"
        for step in data["instructions"]:
            string += f"    {step}\n"
        return string