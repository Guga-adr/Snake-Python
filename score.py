import pygame


class Score:
    def __init__(self):
        self.current_score = 0
        self.font = pygame.font.Font(None, 36)

    def increment_score(self):
        self.current_score += 1

    def display_score(self, screen, color, position):
        score_text = self.font.render(f"Score: {self.current_score}", True, color)
        screen.blit(score_text, position)
