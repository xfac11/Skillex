class Exercise:
    def __init__(self, id:str, name, bodypart, target_muscle, equipment, exercise_multiplier = 1.0):
        self.id = id
        self.name = name
        self.bodypart = bodypart
        self.target_muscle = target_muscle
        self.equipment = equipment
        self.exercise_multiplier = exercise_multiplier
