import pygame

class InputField:
    def __init__(self, label, x, y, width, height):
        self.label = label
        self.rect = pygame.Rect(x, y, width, height)
        self.text = ""
        self.font = pygame.font.Font(None, 32)
        self.active = False

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = not self.active
            else:
                self.active = False
        elif event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode

    def draw(self, screen):
        color = pygame.Color('lightskyblue3') if self.active else pygame.Color('gray15')
        pygame.draw.rect(screen, color, self.rect, 2)
        text_surface = self.font.render(self.text, True, pygame.Color('black'))
        screen.blit(text_surface, (self.rect.x + 5, self.rect.y + 5))
        pygame.draw.rect(screen, pygame.Color('gray15'), self.rect, 2)
