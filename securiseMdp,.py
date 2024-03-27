import pygame
import re

class SecuriseMdp:
    def __init__(self):
        self.screen = pygame.display.get_surface()
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 32)

        self.password = ""

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    self.password = self.password[:-1]
                elif event.key == pygame.K_RETURN:
                    # Valider le mot de passe lorsqu'appuyé sur Entrée
                    if self.validate_password():
                        print("Mot de passe valide")
                    else:
                        print("Mot de passe non valide")
                else:
                    self.password += event.unicode

    def validate_password(password):
        # Vérifie si le mot de passe contient au moins une majuscule
        if not re.search(r'[A-Z]', password):
            return False

        # Vérifie si le mot de passe contient au moins une minuscule
        if not re.search(r'[a-z]', password):
            return False

        # Vérifie si le mot de passe contient au moins un caractère spécial
        if not re.search(r'[^A-Za-z0-9]', password):
            return False

        # Vérifie si le mot de passe contient au moins un chiffre
        if not re.search(r'[0-9]', password):
            return False

        # Vérifie si le mot de passe a une longueur minimale de 10 caractères
        if len(password) < 10:
            return False

        return True
    
    
    # Exemple d'utilisation
    password = "MotDePasse123!"
    if validate_password(password):
        print("Le mot de passe est sécurisé.")
    else:
        print("Le mot de passe ne répond pas aux critères de sécurité requis.")

    def run(self):
        running = True
        while running:
            self.handle_events()

            # Dessiner l'interface utilisateur
            self.screen.fill((255, 255, 255))
            pygame.draw.rect(self.screen, (0, 0, 0), (100, 100, 400, 50))
            text_surface = self.font.render(self.password, True, (255, 255, 255))
            self.screen.blit(text_surface, (110, 110))
            pygame.display.flip()

            self.clock.tick(60)


# Exemple d'utilisation
if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((600, 400))
    pygame.display.set_caption("Mot de passe")
    password_page = SecuriseMdp()
    password_page.run()
