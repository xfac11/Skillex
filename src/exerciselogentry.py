class ExerciseLogEntry:
    def __init__(self, id:int, date:int, user_id:int, exercise_id:str, xp_earned:int, weight_volume:int):
        self.id = id
        self.user_id = user_id
        self.date = date
        self.exercise_id = exercise_id
        self.xp_earned = xp_earned
        self.weight_volume = weight_volume