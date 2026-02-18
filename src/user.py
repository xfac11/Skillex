class User:
    def __init__(self, id:int, name:str, global_xp:int, body_xp:dict, streak:int, sleep_streak:int, history:list, highest_weight):
        self.name = name
        self.id = id
        self.global_xp = global_xp
        self.body_xp = body_xp
        self.streak = streak
        self.sleep_streak = sleep_streak
        self.history = history
        self.highest_weight = highest_weight

    def repr():
        pass

    def increase_xp(xp) -> bool:
        pass
