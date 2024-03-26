import pygame

class Button:
    def __init__(self, text, x, y, width, height, color, hover_color):
        self.text = text
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.hover_color = hover_color

    def draw(self, screen):
        # Dessiner le bouton sur l'écran
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))
        # Dessiner le texte du bouton
        font = pygame.font.Font(None, 36)
        text_surface = font.render(self.text, True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(self.x + self.width / 2, self.y + self.height / 2))
        screen.blit(text_surface, text_rect)

    def is_hover(self, pos):
        # Vérifier si la souris survole le bouton
        return self.x < pos[0] < self.x + self.width and self.y < pos[1] < self.y + self.height