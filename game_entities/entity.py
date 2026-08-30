import math
import pygame

class Entity:
    def __init__(self, x:float, y:float, radius: float, color: tuple):
        self.x= x
        self.y= y
        self.radius= radius
        self.color= color

    def update(self, dt:float):
        pass

    def draw(self, screen: pygame.Surface):
        pygame.draw.circle(
            screen, self.color, (int(self.x), int(self.y)), int(self.radius)
        )

    def distance_to(self, other:'Entity') -> float:
        return math.hypot(self.x- other.x, self.y-other.y)

    def collides_with(self, other: 'Entity') ->bool:
        return self.distance_to(other) <= (self.radius + other.radius)

