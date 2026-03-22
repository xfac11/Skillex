from enum import Enum
class EffortLevel(Enum):
    EASY = 1
    NORMAL = 2
    HARD = 3
class Effort:
    def __init__(self, effort_level:EffortLevel):
        self.value = 0
        match effort_level:
            case EffortLevel.EASY:
                self.value = 0.9
            case EffortLevel.NORMAL:
                self.value = 1.1
            case EffortLevel.HARD:
                self.value = 1.3