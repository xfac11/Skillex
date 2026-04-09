from exercise import Exercise
from exercisecatalog import ExerciseCatalog
import click
import ast
class ExerciseUI:
    def __init__(self, exercise:Exercise):
        self.exercise = exercise
        
    def to_string(self) -> str:
        base_url = "https://raw.githubusercontent.com/yuhonas/free-exercise-db/main/exercises/"
        dict_str = ExerciseCatalog().get_exercise_raw_json(self.exercise.id)
        data = ast.literal_eval(dict_str)
        string = ""
        string += click.style(f"{self.exercise.name.capitalize()}\n", fg="green")
        string += f"Body part: {self.exercise.bodypart.capitalize()}\n"
        string += f"Target muscle: {self.exercise.target_muscle.capitalize()}\n"
        string += f"Equipment: {self.exercise.equipment.capitalize()}\n"
        string += f"Instructions:\n"
        step_index = 1
        for step in data["instructions"]:
            string += f"    Step {str(step_index)}: "
            step_index += 1
            string += f"{step}\n\n"
        return string