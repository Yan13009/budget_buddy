import pygame
from button import Button



class InterfaceGrafique:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Gestion financière")
        self.clock = pygame.time.Clock()

        # Initialisation des boutons
        self.connexion_button = Button("Connexion", 300, 200, 200, 50, (0, 0, 255), (0, 0, 200))
        self.inscription_button = Button("Inscription", 300, 300, 200, 50, (0, 0, 255), (0, 0, 200))

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.connexion_button.is_hover(pygame.mouse.get_pos()):
                        # Action à effectuer lors du clic sur le bouton de connexion
                        print("Bouton de connexion cliqué")
                    elif self.inscription_button.is_hover(pygame.mouse.get_pos()):
                        # Action à effectuer lors du clic sur le bouton d'inscription
                        print("Bouton d'inscription cliqué")

            self.screen.fill((255, 255, 255))  # Remplir l'écran avec une couleur de fond
            # Dessiner les boutons
            self.connexion_button.draw(self.screen)
            self.inscription_button.draw(self.screen)
            pygame.display.flip()  # Mettre à jour l'affichage
            self.clock.tick(60)  # Limiter le taux de rafraîchissement

        pygame.quit()



# Exemple d'utilisation
if __name__ == "__main__":
    interface = InterfaceGrafique()
    interface.run()
