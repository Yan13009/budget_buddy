import pygame 
from pygame.locals import *
from Button import Button
from EyeButton import EyeButton
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

# Création des objets TextInput pour le nom d'utilisateur et le mot de passe
username_input = TextInput(570, 215, 250, 40, font, N, L, L)
password_input = TextInput(570, 305, 250, 40, font, N, L, L)

while True:
    mouse_pos = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        elif event.type == MOUSEBUTTONDOWN:
            if connexion_button.is_clicked(mouse_pos):
                pass
            # Gérer les clics de souris pour les interactions avec les champs d'entrée
            elif event.type == MOUSEBUTTONDOWN:
                if event.button == 1:  # Clic gauche
                    if 800 < event.pos[0] < 850 and 255 < event.pos[1] < 305:
                        # Si le clic est sur le bouton de l'œil
                        eye_button.toggle_password_visibility()
        # Gérer les événements pour les champs de texte
        username_input.handle_event(event)
        password_input.handle_event(event)
 
    
        """
        elif event.type == MOUSEBUTTONDOWN:
            if connexion_button.is_clicked(mouse_pos):
                pass
            # Gérer les clics de souris pour les interactions avec les champs d'entrée
            elif event.type == MOUSEBUTTONDOWN:
                if event.button == 1:  # Clic gauche
                    if 800 < event.pos[0] < 850 and 255 < event.pos[1] < 305:
                        # Si le clic est sur le bouton de l'œil
                        eye_button.toggle_password_visibility()
        """
    
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
    icon_rect = image_logo.get_rect()
    icon_rect.topleft = (220, 400)  # Position sous le texte "Bienvenue"


    # Charger les images des yeux
    open_eye_image = pygame.image.load('Classes/Images/eye-24.png')
    closed_eye_image = pygame.image.load('Classes/Images/closed-eye-24.png')

    # Créer l'objet EyeButton
    eye_button = EyeButton(840, 320, 50, 50, open_eye_image, closed_eye_image, BK)

    BK.blit(image, (0, 0))       
    pygame.draw.rect(BK, L, (x, y, width, height))
    # Dessiner les champs d'entrée et les étiquettes
    pygame.draw.rect(BK, L, (x, y, 250, 30))  # Rectangle pour le nom d'utilisateur
    text_surface = font.render("Nom ou Email", True, N)  # Étiquette pour le nom d'utilisateur
    BK.blit(text_surface, (570, 179))
    pygame.draw.rect(BK, N, (570, y + 180, 290, 3))  # Dessiner une ligne sous le texte "Nom ou Email"
    
    pygame.draw.rect(BK, L, (x, y + 120, 250, 30))  # Rectangle pour le mot de passe
    text_surface = font.render("Mot de passe", True, N)  # Étiquette pour le mot de passe
    BK.blit(text_surface, (570, 280))
    pygame.draw.rect(BK, N, (570, y + 270, 295, 3))  # Dessiner une ligne sous le texte "Mot de passe"
    connexion_button = Button(570, 400, 250, 40, N, "Se connecter", font)
    connexion_button.draw_button(BK)

    # Création du bouton "Mot de passe oublié ?"
    MDP_O_font = pygame.font.Font(None, 20)
    MDP_O_text = MDP_O_font.render("Mot de passe oublié ?", True, N)
    MDP_O_rect = MDP_O_text.get_rect(topleft=(739, 355))
    BK.blit(MDP_O_text, MDP_O_rect)

    # Création du bouton "Créer un nouveau compte"
    CNC_font = pygame.font.Font("Classes/Images/CFAzteques-Regular.ttf", 25)
    CNC_text = CNC_font.render("Créer une compte !", True, N)
    CNC_rect = CNC_text.get_rect(topleft=(620, 600))
    BK.blit(CNC_text, CNC_rect)

    # Charger les logos de Facebook et Google
    facebook_logo = pygame.image.load('Classes/Images/facebook-48.png')
    google_logo = pygame.image.load('Classes/Images/google-48.png')

    # Ajuster la taille des logos si nécessaire
    logo_width = 40
    logo_height = 40
    facebook_logo = pygame.transform.scale(facebook_logo, (logo_width, logo_height))
    google_logo = pygame.transform.scale(google_logo, (logo_width, logo_height))

    # Positionner les logos en dessous du bouton "Se connecter"
    facebook_rect = facebook_logo.get_rect(topleft=(680, 500))
    google_rect = google_logo.get_rect(topleft=(780, 500)) 




    # Affichage du titre à l'écran
    BK.blit(t_text, t_rect)
    # Affichage du mot "Bienvenue" à l'écran
    BK.blit(B_text, B_rect)
    # Afficher l'image du bouton
    BK.blit(image_logo, icon_rect)
    # Afficher les logos
    BK.blit(facebook_logo, facebook_rect)
    BK.blit(google_logo, google_rect)
    # Dessiner le bouton de l'œil
    eye_button.draw()

    # Dessiner les champs de texte
    username_input.draw(BK)
    password_input.draw(BK)

    pygame.display.update()
