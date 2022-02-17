from abc import ABC,abstractmethod
class Transportation(ABC):

    def __init__(self, start_place, end_place, distance):
        self.start = start_place
        self.end = end_place
        self.distance = distance
        
    @abstractmethod
    def find_cost(self):
        pass

class Walk(Transportation):

    def __init__(self, start_place, end_place, distance):
        super().__init__(start_place, end_place, distance)

    def find_cost(self):
        cost = 0
        return cost

class Taxi(Transportation):

    def __init__(self, start_place, end_place, distance):
        super().__init__(start_place, end_place, distance)

    def find_cost(self):
        price = 40
        cost = self.distance * price
        return cost

class Train(Transportation):

    def __init__(self,start_place, end_place, distance, station):
        super().__init__(start_place, end_place, distance)
        self.station = station

    def find_cost(self):
        price = 5
        cost = self.station * price
        return cost

w = Walk("KMITL", "KMITL SCB Bank", 0.6)
print(w.find_cost())

ta1 = Taxi("KMITL SCB Bank", "Ladkrabang Station", 5)
print(ta1.find_cost())

tr = Train("Ladkrabang Station", "Payathai Station", 40, 6)
print(tr.find_cost())

ta2 = Taxi("Payathai Station", "The British Council", 3)
print(ta2.find_cost())
