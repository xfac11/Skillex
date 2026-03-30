from bodyparts import BodyParts
from calculatexperience import calculate_body_level
from calculatexperience import calculate_global_level
from enum import Enum
class SleepUpdateCode(Enum):
    SLEPT_7 = 1
    SLEPT_LESS_7 = 2
    LOGGED_YESTERDAY = 3
    FORGOT_YESTERDAY = 4
class User:
    def __init__(self, id:int, name:str, global_xp:int = 0, body_xp:BodyParts = BodyParts(), streak:int = 0, sleep_streak:int = 0):
        self.name = name
        self.id = id
        self.global_xp = global_xp
        self.body_xp = body_xp
        self.streak = streak
        self.sleep_streak = sleep_streak

    def repr():
        pass
    
    
    def increase_global_xp(self, xp:int) -> int:
        """
        returns 0 if no level was gained after increasing xp
        returns the level if a level was gained after increasing xp
        """
        level = calculate_global_level(self.global_xp)
        self.global_xp += xp
        level_after = calculate_global_level(self.global_xp)
        
        if level_after > level:
            return level_after
        return 0
        
    
    def increase_body_xp(self, bodypart:str, xp:int) -> int:
        """
        returns the level if it increased otherwise returns 0
        returns -1 if the bodypart does not exist
        """
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
    
    def reset_sleep_streak(self) -> None:
        self.sleep_streak = 1
    
    def update_highest_weight(self, weight:int):
        self.highest_weight = weight
    
    def update_sleep_streak(self, sleep_hours:float, logged_yesterday:bool) -> list[SleepUpdateCode]:
        code = list()
        if sleep_hours >= 7.0:
            code.append(SleepUpdateCode.SLEPT_7)
            if logged_yesterday:
                code.append(SleepUpdateCode.LOGGED_YESTERDAY)
                self.increase_sleep_streak()
                return code
            code.append(SleepUpdateCode.FORGOT_YESTERDAY)
            self.reset_sleep_streak()
            return code
        else:
            code.append(SleepUpdateCode.SLEPT_LESS_7)
            if logged_yesterday:
                code.append(SleepUpdateCode.LOGGED_YESTERDAY)
                self.decrease_sleep_streak()
                return code
            code.append(SleepUpdateCode.FORGOT_YESTERDAY)
            self.reset_sleep_streak()
            return code
        
