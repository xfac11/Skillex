import math
GLOBAL_CONSTANT = 0.35
BODY_CONSTANT = 0.25
SCALING_INTENSITY = 0.03
BASE_RATE = 10 ## xp per minute
SLEEP_STREAK_CAP = 0.1
SLEEP_STREAK_RATE = 0.01
def clamp(number, smallest, largest): 
    return max(smallest, min(number, largest))

class ExerciseExperience:
    def __init__(self, time_minutes, base_rate = BASE_RATE):
        self.__exercise_xp = time_minutes * base_rate
        self.__intensity_multiplier = 1.0
        self.__sleep_multiplier = 1.0
        self.__strength_multiplier = 1.0
        self.__strength_record_multiplier = 1.0
        self.__effort_multiplier = 1.0
        self.__exercise_multiplier = 1.0
        self.__multiplier = 1.0
    
    ##Gives a multipler from 1.0 (means 0% bonus) to 2.0 means 100% bonus
    def apply_intensity_multiplier(self, user_speed, exercise_avg_speed, scaling_intensity = SCALING_INTENSITY):
        relative_intensity = (user_speed - exercise_avg_speed) / exercise_avg_speed
        relative_intensity = clamp(relative_intensity, 0.0, 1.0) 
        
        intensity_m = 1 + relative_intensity * scaling_intensity
        
        self.__multiplier *= intensity_m
        self.__intensity_multiplier = intensity_m
        self.__exercise_xp *= intensity_m

        return self
    
    ## Gives a multiplier from 1.0 to sleep_streak_cap. Each streak day inreaces the multiplier by sleep_streak_rate
    def apply_sleep_multiplier(self, sleep_streak:int, sleep_streak_rate = SLEEP_STREAK_RATE, sleep_streak_cap = SLEEP_STREAK_CAP):
        sleep_m = 1 + min(sleep_streak * sleep_streak_rate, sleep_streak_cap)

        self.__multiplier *= sleep_m
        self.__sleep_multiplier = sleep_m
        self.__exercise_xp *= sleep_m

        return self
    
    def apply_strength_multiplier(self, weight, reps, sets, average_volume):
        volume = weight * reps * sets
        relative_volume =  volume / average_volume

        improvement = max(relative_volume - 1.02, 0)

        strength_bonus = min(improvement * 0.25, 0.05)

        strength_m = 1 + strength_bonus
        
        self.__multiplier *= strength_m
        self.__strength_multiplier = strength_m
        self.__exercise_xp *= strength_m

        return self
    
    def apply_strength_record_multiplier(self, weight, highest_weight):
        if weight > highest_weight:
            self.__strength_record_multiplier = 1.05
            self.__exercise_xp *= 1.05
    
    def apply_exercise_multiplier(self, exercise_multiplier = 1.0):
        self.__exercise_multiplier = exercise_multiplier
        self.__multiplier *= exercise_multiplier
        self.__exercise_xp *= exercise_multiplier

        return self
    
    def apply_effort_multiplier(self, effort_multiplier = 1.0):
        self.__effort_multiplier = effort_multiplier
        self.__multiplier *= effort_multiplier
        self.__exercise_xp *= effort_multiplier

        return self
    
    def get_experience_points(self):
        return self.__exercise_xp
    
    def get_multiplier(self):
        return self.__multiplier
    
    def get_effort_multiplier(self):
        return self.__effort_multiplier
    
    def get_exercise_multiplier(self):
        return self.__exercise_multiplier
    
    def get_sleep_multiplier(self):
        return self.__sleep_multiplier
    
    def get_strength_multiplier(self):
        return self.__strength_multiplier
    
    def get_intensity_multiplier(self):
        return self.__intensity_multiplier
    
    def get_strength_record_multiplier(self):
        return self.__strength_record_multiplier

def create_exercise_experience(sleep_streak = 1,
                                  repeats:int=0,
                                  sets=0,
                                  weight:float = 1,
                                  average_volume = 60,
                                  highest_weight = 100,
                                  distance:float=0,
                                  time_minutes:float=0,
                                  effort_multiplier = 1.0,
                                  exercise_factor = 1.0,
                                  exercise_avg_speed_kmh = 20) -> ExerciseExperience:
    
    user_speed = distance / (time_minutes / 60)

    exercise_exp = ExerciseExperience(time_minutes, BASE_RATE)

    exercise_exp.apply_effort_multiplier(effort_multiplier)
    exercise_exp.apply_exercise_multiplier(exercise_factor)
    exercise_exp.apply_intensity_multiplier(user_speed, exercise_avg_speed_kmh, SCALING_INTENSITY)
    exercise_exp.apply_sleep_multiplier(sleep_streak, SLEEP_STREAK_RATE, SLEEP_STREAK_CAP)
    exercise_exp.apply_strength_multiplier(weight, repeats, sets, average_volume, highest_weight)

    return exercise_exp
    

def calculate_global_level(current_xp:int):
    return math.floor(GLOBAL_CONSTANT * math.sqrt(current_xp))

def calculate_body_level(current_xp:int):
    return math.floor(BODY_CONSTANT * math.sqrt(current_xp))

def calculate_body_experience(current_level:int): ##Never use for storing or for displaying current xp
    return (current_level / BODY_CONSTANT)**2

def calculate_global_experience(current_level:int): ##Never use for storing or for displaying current xp
    return (current_level / GLOBAL_CONSTANT)**2

def calculate_body_progress_to_next(xp):
    level = calculate_body_level(xp)
    current_level_xp = calculate_body_experience(level)
    next_level_xp = calculate_body_experience(level + 1)
    return (xp -  current_level_xp) / (next_level_xp - current_level_xp)

def calculate_global_progress_to_next(xp):
    level = calculate_global_level(xp)
    current_level_xp = calculate_global_experience(level)
    next_level_xp = calculate_global_experience(level + 1)
    return (xp -  current_level_xp) / (next_level_xp - current_level_xp)