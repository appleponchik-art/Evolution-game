import pygame
import math
from game_entities.entity import Entity
from game_evolution.evolution_stages import STAGES
from config import settings

class Player(Entity):
    def __init__(self, x: float, y: float):
        stage= STAGES[0]
        super().__init__(x,y, stage['radius'], stage['color'])

        self.stage_index=  0
        self.xp= 0
        self.speed= stage["speed"]

        self.on_evolve = None

    @property
    def current_stage(self) -> dict:
        return STAGES[self.stage_index]

    @property
    def xp_to_next(self) -> float:
        return self.current_stage["xp_to_next"]

    @property
    def is_max_stage(self) -> bool:
        return self.stage_index>= len(STAGES) - 1

    def handle_input(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        dx, dy = mouse_x - self.x, mouse_y - self.y
        distance = math.hypot(dx, dy)

        if distance > 2:
            dx, dy = dx/ distance, dy/ distance
            self.x += dx * self.speed
            self.y += dy * self.speed

        self.x = max(self.radius, min(settings.WORLD_WIDTH - self.radius, self.x))
        self.y = max(self.radius, min(settings.WORLD_HEIGHT - self.radius, self.y))

    def eat(self,food) -> None:
        self.xp+= food.value
        self._check_revolution()

    def _check_revolution(self) -> None:
        if self.is_max_stage:
            return
        if self.xp>= self.xp_to_next:
            self.xp-= self.xp_to_next
            self.stage_index += 1

            new_stage = self.current_stage
            self.radius= new_stage["radius"]
            self.color= new_stage["color"]
            self.speed= new_stage["speed"]

            if self.on_evolve:
                self.on_evolve(new_stage["name"])

            self._check_revolution()

    def update(self, dt:float):
        self.handle_input()
