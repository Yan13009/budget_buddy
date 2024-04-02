import pygame 
from pygame.locals import *

from TextInput import TextInput

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
M = (61, 54, 69)
L = (97, 84, 105)

x = 250
y = 50
width = 500
height = 600

# Définition des champs de texte
nom_email_input = TextInput(350, 270, 290, 40, font, L, N, N)
mdp_input = TextInput(350, 370, 290, 40, font, L, N, N)
cmdp_input = TextInput(350, 470, 290, 40, font, L, N, N)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Gérer les événements de texte pour les champs d'entrée
        nom_email_input.handle_event(event)
        mdp_input.handle_event(event)
        cmdp_input.handle_event(event)    
    
    BK.blit(image, (0, 0))
    pygame.draw.rect(BK, L, (x, y, width, height))

    # Création d'une surface de texte pour le titre "Créer un nouveau mot de passe"
    t_font_mdp = pygame.font.Font("Classes/Images/CFAzteques-Regular.ttf", 30)  # Choisir la police et la taille
    t_text_mdp = t_font_mdp.render("Créer un nouveau mot de passe", True, N)  # Couleur rouge (255, 0, 0)
    t_rect_mdp = t_text_mdp.get_rect(center=(505, 80))  # Centrez le texte horizontalement
    BK.blit(t_text_mdp, t_rect_mdp)

    image_logo = pygame.image.load('Classes/Images/icons8-money-box-48.png')
    n_width = 80
    n_height = 80
    image_logo = pygame.transform.scale(image_logo, (n_width, n_height))
    icon_rect = image_logo.get_rect()
    icon_rect.topleft = (460, 140)
    BK.blit(image_logo, icon_rect)


    # Affichage des étiquettes et des champs de texte
    label_nom_email = font.render("Nom ou Email", True, N)
    BK.blit(label_nom_email, (350, 240))
    nom_email_input.draw(BK)

    label_mdp = font.render("Mot de passe", True, N)
    BK.blit(label_mdp, (350, 340))
    mdp_input.draw(BK)

    label_cmdp = font.render("Confirmer Mot de passe", True, N)
    BK.blit(label_cmdp, (350, 440))
    cmdp_input.draw(BK)

    pygame.display.flip()
