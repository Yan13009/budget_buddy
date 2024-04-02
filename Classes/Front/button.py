import pygame
N = (0, 0, 0)
L = (97, 84, 105)

class Button:
    def __init__(self, x, y, width, height, color, text, font):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.text = text
        self.font = font
        self.action = None

    def draw_button(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)
        text_surface = self.font.render(self.text, True, L)
        text_rect = text_surface.get_rect(center=self.rect.center)
        surface.blit(text_surface, text_rect)

    def is_clicked(self, mouse_pos):
        return self.rect.collidepoint(mouse_pos)
    
    def set_action(self, action):
        self.action = action  # Méthode pour définir l'action à exécuter lors du clic

    def handle_click(self):
        if self.action:
            self.action()  # Appeler l'action si elle est définie lors du clic sur le bouton
    



        

