import pygame
N = (0, 0, 0)
L = (97, 84, 105)

class Button:
    def __init__(self, x, y, width, height, color, text, font):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.text = text
        self.font = font

    def draw_button(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)
        text_surface = self.font.render(self.text, True, L)
        text_rect = text_surface.get_rect(center=self.rect.center)
        surface.blit(text_surface, text_rect)

    def is_clicked(self, mouse_pos):
        return self.rect.collidepoint(mouse_pos)
    
class EyeButton:
    def __init__(self, x, y, width, height, open_eye_image, closed_eye_image, screen):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.open_eye_image = open_eye_image
        self.closed_eye_image = closed_eye_image
        self.screen = screen
        self.show_password = False

    def draw(self):
        if self.show_password:
            self.screen.blit(self.open_eye_image, (self.x, self.y))
        else:
            self.screen.blit(self.closed_eye_image, (self.x, self.y))

    def toggle_password_visibility(self):
        self.show_password = not self.show_password

