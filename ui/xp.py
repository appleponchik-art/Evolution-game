from config import settings
import pygame

class XP:
    def __init__(self):
        self.font= pygame.font.SysFont("Arial", 22)
        self.font_big = pygame.font.SysFont("Arial", 40, bold = True)

        self.evolve_message = ""
        self.evolve_message_timer = 0.0

    def show_evolve_message(self, stage_name: str):
        self.evolve_message = f"Ти тепер {stage_name}"
        self.evolve_message_timer = 2.5

    def update(self, dt: float):
        if self.evolve_message_timer >0:
            self.evolve_message_timer-= dt

    def draw(self, screen: pygame.Surface, player):
        stage_name= player.current_stage["name"]
        name_surf = self.font.render(f"Стадія зараз: {stage_name}", True, settings.COLOR_TEXT)
        screen.blit(name_surf,(20,20))

        bar_x, bar_y = 20, 50
        bar_w, bar_h = 250, 18
        pygame.draw.rect(screen, settings.COLOR_BAR_BG, (bar_x, bar_y, bar_w, bar_h))

        if not player.is_max_stage:
            progress = min(1.0, player.xp / player.xp_to_next)
        else:
            progress = 1.0
        pygame.draw.rect(screen, settings.COLOR_BAR_FILL, (bar_x, bar_y, int(bar_w * progress), bar_h))

        xp_text = ( f"{player.xp}/{player.xp_to_next}"
                    if not player.is_max_stage
                    else "MAX" )
        xp_surf = self.font.render(xp_text, True, settings.COLOR_TEXT)
        screen.blit(xp_surf, (bar_x + bar_w + 10, bar_y - 2))

        if self.evolve_message_timer > 0:
            msg_surf = self.font.render(self.evolve_message, True, (225, 30, 120))
            rect = msg_surf.get_rect(center=(settings.SCREEN_WIDTH//2, 80))
            screen.blit(msg_surf, rect)

