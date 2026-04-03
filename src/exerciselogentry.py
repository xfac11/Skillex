class ExerciseLogEntry:
    def __init__(self, id:int, date:float, user_id:int, exercise_id:str, xp_earned:int, weight_volume:int, speed:float, weight:float, time_minutes:int):
        self.id = id
        self.user_id = user_id
        self.date = date
        self.exercise_id = exercise_id
        self.xp_earned = xp_earned
        self.weight_volume = weight_volume
        self.weight = weight
        self.speed = speed
        self.time_minutes = time_minutes
    
    def __repr__(self):
        return f"{self.date} , {self.user_id}"
