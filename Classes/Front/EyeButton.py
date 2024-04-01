"""
import pygame


class EyeButton:
    def __init__(self, x, y, width, height, open_eye_image, closed_eye_image, screen, connexion):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.open_eye_image = open_eye_image
        self.closed_eye_image = closed_eye_image
        self.screen = screen
        self.connexion = connexion
        self.show_password = False
        # Créer un attribut rect pour définir la zone du bouton
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def draw(self):
        if self.show_password:
            self.screen.blit(self.open_eye_image, (self.x, self.y))
        else:
            self.screen.blit(self.closed_eye_image, (self.x, self.y))

        # Mettre à jour la zone du bouton
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def toggle_password_visibility(self):
        self.show_password = not self.show_password
        # Appelez la méthode toggle_password_visibility de la classe Connexion
        self.connexion.toggle_password_visibility()
"""