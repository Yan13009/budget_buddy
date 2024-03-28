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

# Créer une classe Transaction
class Transaction:
    def __init__(self, name, description, amount, transaction_type):
        self.name = name
        self.description = description
        self.amount = amount
        self.transaction_type = transaction_type

# Fonction pour afficher les transactions à l'écran
def display_transactions(transactions, screen):
    screen.fill(WHITE)
    for i, transaction in enumerate(transactions):
        text = f"Transaction {i+1}: {transaction.name} - {transaction.description} - Montant: {transaction.amount} - Type: {transaction.transaction_type}"
        font = pygame.font.SysFont(None, 24)
        text_surface = font.render(text, True, BLACK)
        screen.blit(text_surface, (50, 50 + i * 30))
    pygame.display.flip()

# Fonction principale
def main():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Gestion financière")

    # Créer quelques transactions de test
    transactions = [
        Transaction("Achat", "Courses alimentaires", 50.0, "Dépense"),
        Transaction("Salaire", "Salaire mensuel", 1500.0, "Revenu"),
        Transaction("Facture", "Electricité", 80.0, "Dépense"),
    ]

    # Boucle principale
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False

        # Afficher les transactions
        display_transactions(transactions)

    pygame.quit()

if __name__ == "__main__":
    main()
