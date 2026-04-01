
class AverageOver:
    def __init__(self, days:int, ordered_data:list[float]):
        self.days = days
        self.ordered_data = ordered_data
    
    def average(self) -> float:
        total = 0.0
        for i in range(self.days):
            total += self.ordered_data[i]
        return total / self.days