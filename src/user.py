from bodyparts import BodyParts
from calculatexperience import calculate_body_level
from calculatexperience import calculate_global_level
class User:
    def __init__(self, id:int, name:str, global_xp:int, body_xp:BodyParts, streak:int, sleep_streak:int, highest_weight:int):
        self.name = name
        self.id = id
        self.global_xp = global_xp
        self.body_xp = body_xp
        self.streak = streak
        self.sleep_streak = sleep_streak
        self.highest_weight = highest_weight

    def repr():
        pass
    
    """
    returns 0 if no level was gained after increasing xp
    returns the level if a level was gained after increasing xp
    """
    def increase_global_xp(self, xp:int) -> int:
        level = calculate_global_level(self.global_xp)
        self.global_xp += xp
        level_after = calculate_global_level(self.global_xp)
        
        if level_after > level:
            return level_after
        return 0
        
    """
    returns the level if it increased otherwise returns 0
    returns -1 if the bodypart does not exist
    """
    def increase_body_xp(self, bodypart:str, xp:int) -> int:
        xp_before = self.body_xp.get_bodypart_xp(bodypart)
        if xp_before is None:
            return -1 
        level = self.body_xp.get_bodypart_level(bodypart)
        self.body_xp.set_bodypart_xp(bodypart, xp_before + xp)
        level_after = self.body_xp.get_bodypart_level(bodypart)
        
        if level_after > level:
            return level_after
        return 0
        
    def decrease_sleep_streak(self) -> None:
        self.sleep_streak = max(self.sleep_streak - 1, 0)
    
    def increase_sleep_streak(self) -> None:
        self.sleep_streak += 1
    
    def update_highest_weight(self, weight:int):
        self.highest_weight = weight
    
    
        
