from game_entities.food import Food
from config import settings

class Spawner:

    def __init__(self, target_count: int= settings.FOOD_COUNT):
        self.target_count = target_count

    def refill(self, food_list: list) -> None:
        while len(food_list) < self.target_count:
            food_list.append(Food.spawn_random())


