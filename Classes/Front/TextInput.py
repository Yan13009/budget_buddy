import pygame


class TextInput:
    def __init__(self, x, y, width, height, font, text_color, bg_color, active_color, max_length=None):
        self.rect = pygame.Rect(x, y, width, height)
        self.font = font
        self.text_color = text_color
        self.bg_color = bg_color
        self.active_color = active_color
        self.text = ''
        self.active = False
        self.max_length = max_length

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Si le clic de souris est à l'intérieur de la zone de texte
            self.active = self.rect.collidepoint(event.pos)
        elif event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                elif self.max_length is None or len(self.text) < self.max_length:
                    self.text += event.unicode    


    def draw(self, screen):
        color = self.active_color if self.active else self.bg_color
        pygame.draw.rect(screen, color, self.rect)
        text_surface = self.font.render(self.text, True, self.text_color)
        screen.blit(text_surface, (self.rect.x + 5, self.rect.y + 5))

    def get_text(self):
        return self.text