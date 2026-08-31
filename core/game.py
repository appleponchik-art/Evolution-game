import pygame
from config import settings
from game_entities.player import Player
from world.spawner import Spawner
from ui.xp import XP


class Game:
    """Керує ігровим циклом: input -> update -> render."""

    def __init__(self, screen: pygame.Surface):
        self.screen = screen

        self.player = Player(settings.WORLD_WIDTH // 2, settings.WORLD_HEIGHT // 2)
        self.food_list = []
        self.spawner = Spawner()
        self.xp = XP()

        self.player.on_evolve = self.xp.show_evolve_message

        self.spawner.refill(self.food_list)

    def handle_input(self):
        pass

    def update(self, dt: float):
        self.player.update(dt)
        self.xp.update(dt)

        eaten = [f for f in self.food_list if self.player.collides_with(f)]
        for food in eaten:
            self.player.eat(food)
            self.food_list.remove(food)

        self.spawner.refill(self.food_list)

    def render(self):
        self.screen.fill(settings.BG_COLOR)

        for food in self.food_list:
            food.draw(self.screen)

        self.player.draw(self.screen)
        self.xp.draw(self.screen, self.player)