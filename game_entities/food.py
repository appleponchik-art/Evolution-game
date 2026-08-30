import random
from game_entities.entity import Entity
from config import settings

class Food(Entity):
    def __init__(self, x: float =None, y: float = None):
        x = x if x is not None else random.randint(
            settings.FOOD_RADIUS, settings.WORLD_WIDTH - settings.FOOD_RADIUS
        )
        y = y if y is not None else random.randint(
            settings.FOOD_RADIUS, settings.WORLD_HEIGHT - settings.FOOD_RADIUS
        )
        super().__init__(x,y, settings.FOOD_RADIUS, settings.FOOD_COLOR)
        self.value = settings.FOOD_VALUE

    @staticmethod
    def spawn_random() -> "Food":
        return Food()