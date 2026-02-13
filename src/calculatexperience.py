import math
CONSTANT = 0.11
SLEEP_CONSTANT = 100
def calculate_exercise_experience(repeats:int=0, weight:float = 1, distance:float=0, time_minutes:float=0) -> int:
    if distance == 0:
        otherXP = (repeats * 5 * weight)
        return int(otherXP)
    avg_speed_kmh = distance / (time_minutes / 60)
    cardioXP = max((distance * (time_minutes/60) * avg_speed_kmh), avg_speed_kmh*10)
    return cardioXP
    

def calculate_sleep_experience(sleep_streak:int) -> int:
    return sleep_streak*SLEEP_CONSTANT

def calculate_level(current_xp:int) -> int:
    return CONSTANT * math.sqrt(current_xp)

def calculate_experience(current_level:int) -> int:
    return (current_level / CONSTANT)**2