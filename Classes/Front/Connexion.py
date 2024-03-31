import pygame 
from pygame.locals import *

from Button import Button 
pygame.init()

BK = pygame.display.set_mode((1000, 700))
pygame.display.set_caption("Budget_buddy")
image = pygame.image.load('Classes/Images/background.jpg')
image = pygame.transform.scale(image, (1000, 700))
font = pygame.font.Font(None, 30)

N = (0, 0, 0)
B = (255, 255, 255)
R = (255, 0, 0)
K = (55, 42, 59)
L = (97, 84, 105)
M = (61, 54, 69)


# Variables pour les champs d'entrée
username = ""
password = ""

x = 550
y = 75
width = 400
height = 600

class Connexion:
    def __init__(self):
        pass

    # Fonction pour vérifier l'authentification de l'utilisateur
    def login_user():
        pass
        # Insérer ici le code pour vérifier l'authentification de l'utilisateur

    # Fonction pour créer un nouveau compte
    def signup_page():
        pass
        # Insérer ici le code pour ouvrir la page de création de compte
    
connexion = Connexion()

while True:
    mouse_pos = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        elif event.type == MOUSEBUTTONDOWN:
            if connexion_button.is_clicked(mouse_pos):
                pass
            # Gérer les clics de souris pour les interactions avec les champs d'entrée
    
    
    # Création d'une surface de texte pour le titre "Budget buddy"
    t_font = pygame.font.Font("Classes/Images/CFAzteques-Regular.ttf", 50)  # Choisir la police et la taille
    t_text = t_font.render("Budget-buddy", True, N)  # Couleur rouge (255, 0, 0)
    t_rect = t_text.get_rect(center=(750, 120))  # Centrez le texte horizontalement

    # Création d'une surface de texte pour le mot "Bienvenue"
    B_font = pygame.font.Font("Classes/Images/CFAzteques-Regular.ttf", 70)  # Choisir la police et la taille
    B_text = B_font.render("Bienvenue", True, N)  # Couleur rouge (255, 0, 0)
    B_rect = B_text.get_rect(topleft=(100, 300))  # Position en haut à gauche

    # Charger l'image du bouton
    image_logo = pygame.image.load('Classes/Images/icons8-accumulate-48.png')
    n_width = 80
    n_height = 80
    image_logo = pygame.transform.scale(image_logo, (n_width, n_height))  # Ajuster la taille au besoin

    # Créer un rectangle pour le bouton
    google_rect = image_logo.get_rect()
    google_rect.topleft = (250, 400)  # Position sous le texte "Bienvenue"

    

    BK.blit(image, (0, 0))       
    pygame.draw.rect(BK, L, (x, y, width, height))
    # Dessiner les champs d'entrée et les étiquettes
    pygame.draw.rect(BK, L, (x, y, 250, 40))  # Rectangle pour le nom d'utilisateur
    text_surface = font.render("Nom ou Email", True, (0, 0, 0))  # Étiquette pour le nom d'utilisateur
    BK.blit(text_surface, (570, 205))
    pygame.draw.rect(BK, N, (570, y + 180, 250, 3))  # Dessiner une ligne sous le texte "Nom ou Email"
    pygame.draw.rect(BK, L, (x, y, 250, 40))  # Rectangle pour le mot de passe
    text_surface = font.render("Mot de passe", True, (0, 0, 0))  # Étiquette pour le mot de passe
    BK.blit(text_surface, (570, 300))
    pygame.draw.rect(BK, N, (570, y + 270, 250, 3))  # Dessiner une ligne sous le texte "Mot de passe"
    connexion_button = Button(570, 400, 250, 40, N, "Se connecter", font)
    
    connexion_button.draw_button(BK)
    # Affichage du titre à l'écran
    BK.blit(t_text, t_rect)
    # Affichage du mot "Bienvenue" à l'écran
    BK.blit(B_text, B_rect)
    # Afficher l'image du bouton
    BK.blit(image_logo, google_rect)
    pygame.display.update()
