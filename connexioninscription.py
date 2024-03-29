import pygame
from pygame.locals import *
# Initialiser Pygame
pygame.init()

# Définir les dimensions de la fenêtre
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Couleurs
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Définir la police par défaut
DEFAULT_FONT = pygame.font.Font(None, 36)

# Classe pour créer des boutons
class Button:
    def __init__(self, screen, x, y, width, height, color, hover_color, text_color, text, action=None, params=None):
        self.screen = screen
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.hover_color = hover_color
        self.text_color = text_color
        self.text = text
        self.action = action
        self.params = params
        self.hovered = False

    def draw(self):
        if self.hovered:
            pygame.draw.rect(self.screen, self.hover_color, self.rect)
        else:
            pygame.draw.rect(self.screen, self.color, self.rect)
        self.render_text()

    def render_text(self):
        font_size = min(self.rect.width // len(self.text), self.rect.height // 2)
        font = pygame.font.Font(None, font_size)
        font_surface = font.render(self.text, True, self.text_color)
        text_rect = font_surface.get_rect(center=self.rect.center)
        self.screen.blit(font_surface, text_rect)

    def update(self, event):
        if event.type == pygame.MOUSEMOTION:
            self.hovered = self.rect.collidepoint(event.pos)
        elif event.type == pygame.MOUSEBUTTONDOWN and self.hovered:
            if self.action:
                if self.params:
                    self.action(*self.params)
                else:
                    self.action()

# Classe pour la saisie de texte
class TextInputBox:
    def __init__(self, screen, x, y, width, height, font, color=(255, 255, 255), cursor_color=(0, 0, 0)):
        self.screen = screen
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.cursor_color = cursor_color
        self.text = ''
        self.font = font
        self.active = False
        self.cursor_visible = True
        self.cursor_timer = 0

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Si le clic de souris est dans le rectangle du TextInputBox, activez le focus
            self.active = self.rect.collidepoint(event.pos)
        elif event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    # Lorsque la touche Entrée est enfoncée, désactivez le focus
                    self.active = False
                elif event.key == pygame.K_BACKSPACE:
                    # Supprimer le dernier caractère
                    self.text = self.text[:-1]
                else:
                    # Ajouter le caractère à la fin du texte
                    self.text += event.unicode

    def update(self):
        # Mettre à jour le curseur
        self.cursor_timer += 1
        if self.cursor_timer >= 30:
            self.cursor_visible = not self.cursor_visible
            self.cursor_timer = 0

    def draw(self):
        # Dessiner le rectangle de saisie de texte
        pygame.draw.rect(self.screen, self.color, self.rect, 2)

        # Dessiner le texte
        text_surface = self.font.render(self.text, True, self.color)
        self.screen.blit(text_surface, (self.rect.x + 5, self.rect.y + 5))

        # Dessiner le curseur
        if self.active and self.cursor_visible:
            cursor_x = self.rect.x + 5 + text_surface.get_width()
            pygame.draw.line(self.screen, self.cursor_color, (cursor_x, self.rect.y + 5), (cursor_x, self.rect.y + self.rect.height - 5), 2)

def handle_register():
    print("S'inscrire")

def handle_login():
    print("Se connecter")

def handle_password_reset(screen):
    # Créer une interface graphique pour la saisie du mot de passe oublié
    screen.fill(WHITE)
    draw_text(screen, "Mot de passe oublié", BLACK, SCREEN_WIDTH // 2, 50, 48)
    text_input_box_first_name = TextInputBox(screen, 300, 200, 200, 50, DEFAULT_FONT)
    text_input_box_last_name = TextInputBox(screen, 300, 300, 200, 50, DEFAULT_FONT)
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                return
            text_input_box_first_name.handle_event(event)
            text_input_box_last_name.handle_event(event)
            if event.type == KEYDOWN and event.key == K_RETURN:
                print("Prénom:", text_input_box_first_name.text)
                print("Nom:", text_input_box_last_name.text)
                pygame.quit()
                return

        screen.fill(WHITE)
        draw_text(screen, "Mot de passe oublié", BLACK, SCREEN_WIDTH // 2, 50, 48)
        draw_text(screen, "Prénom:", BLACK, 200, 210, 24)
        draw_text(screen, "Nom:", BLACK, 220, 310, 24)
        text_input_box_first_name.draw()
        text_input_box_last_name.draw()

        pygame.display.flip()

def draw_text(screen, text, color, x, y, size):
    font = pygame.font.Font(None, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=(x, y))
    screen.blit(text_surface, text_rect)

def main():
    # Initialiser la fenêtre
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Bienvenue sur Buget Buddy")

    running = True

    # Charger l'image de fond
    background_image = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
    background_image.fill(GRAY)

    # Création des boutons
    buttons = [
        Button(screen, 300, 200, 200, 50, GREEN, (0, 200, 0), BLACK, "S'inscrire", handle_register),
        Button(screen, 300, 275, 200, 50, GREEN, (0, 200, 0), BLACK, "Se connecter", handle_login),
        Button(screen, 300, 350, 200, 50, GREEN, (0, 200, 0), BLACK, "Mot de passe oublié", handle_password_reset, [screen]),
    ]

    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False

        # Afficher l'animation de fond
        screen.blit(background_image, (0, 0))

        # Gérer les événements pour les boutons
        for button in buttons:
            button.update(event)
            button.draw()

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()

