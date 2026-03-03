from calculatexperience import calculate_body_level

class BodypartList:
    def __init__(self):
        self.bodyparts = ["lower_arms", "shoulder", "cardio", "upper_arms","chest", "lower_legs", "back", "upper_legs", "waist"]

class BodyParts:
    def __init__(self, bodyparts:list[str] = BodypartList().bodyparts):
        self.__bodyparts:dict = {}
        for bodypart in bodyparts:
            self.__bodyparts[bodypart] = 0
    
    def get_bodypart_xp(self, bodypart:str) -> int:
        return self.__bodyparts.get(bodypart)
    
    def set_bodypart_xp(self, bodypart:str, experience_points:int) -> bool:
        if self.__bodyparts.get(bodypart) is not None:
            self.__bodyparts[bodypart] = experience_points
            return True
        return False
    
    def get_bodypart_level(self, bodypart:str) -> int:
        xp = self.__bodyparts.get(bodypart)
        if xp is not None:
            return calculate_body_level(xp)
        return -1
    
    def get_bodyparts(self) -> dict:
        return self.__bodyparts
    