import pygame
from pygame.locals import *
from Button import Button
from EyeButton import EyeButton
from TextInput import TextInput
pygame.init()

class Connexion:
    def __init__(self):
        self.BK = pygame.display.set_mode((1000, 700))
        self.image = pygame.image.load('Classes/Images/background.jpg')
        self.image = pygame.transform.scale(self.image, (1000, 700))
        self.font = pygame.font.Font(None, 30)

        self.N = (0, 0, 0)
        self.B = (255, 255, 255)
        self.R = (255, 0, 0)
        self.K = (55, 42, 59)
        self.L = (97, 84, 105)
        self.M = (61, 54, 69)

        self.x = 550
        self.y = 75
        self.width = 400
        self.height = 600

        self.username_input = TextInput(570, 215, 250, 40, self.font, self.N, self.L, self.L)
        self.password_input = TextInput(570, 305, 250, 40, self.font, self.N, self.L, self.L)
        
        # Création d'une surface de texte pour le titre "Budget buddy"
        self.t_font = pygame.font.Font("Classes/Images/CFAzteques-Regular.ttf", 50) # Choisir la police et la taille
        self.t_text = self.t_font.render("Budget-buddy", True, self.N)
        self.t_rect = self.t_text.get_rect(center=(750, 120)) # Centrez le texte horizontalement
        
        # Création d'une surface de texte pour le mot "Bienvenue"
        self.B_font = pygame.font.Font("Classes/Images/CFAzteques-Regular.ttf", 70) # Choisir la police et la taille
        self.B_text = self.B_font.render("Bienvenue", True, self.N)
        self.B_rect = self.B_text.get_rect(topleft=(100, 300)) # Position en haut à gauche
        
        # Charger l'image
        self.image_logo = pygame.image.load('Classes/Images/icons8-accumulate-48.png')
        self.n_width = 80
        self.n_height = 80
        self.image_logo = pygame.transform.scale(self.image_logo, (self.n_width, self.n_height))
        self.icon_rect = self.image_logo.get_rect()
        self.icon_rect.topleft = (220, 400) # Position sous le texte "Bienvenue"
        
        # Charger les images des yeux
        self.open_eye_image = pygame.image.load('Classes/Images/eye-24.png')
        self.closed_eye_image = pygame.image.load('Classes/Images/closed-eye-24.png')
        # Créer l'objet EyeButton
        self.eye_button = EyeButton(840, 320, 50, 50, self.open_eye_image, self.closed_eye_image, self.BK, self)
        
        # Charger les logos de Facebook et Google
        self.facebook_logo = pygame.image.load('Classes/Images/facebook-48.png')
        self.google_logo = pygame.image.load('Classes/Images/google-48.png')
        # Ajuster la taille des logos si nécessaire
        self.logo_width = 40
        self.logo_height = 40
        self.facebook_logo = pygame.transform.scale(self.facebook_logo, (self.logo_width, self.logo_height))
        self.google_logo = pygame.transform.scale(self.google_logo, (self.logo_width, self.logo_height))
        # Positionner les logos en dessous du bouton "Se connecter"
        self.facebook_rect = self.facebook_logo.get_rect(topleft=(680, 500))
        self.google_rect = self.google_logo.get_rect(topleft=(780, 500))

        self.connexion_button = Button(570, 400, 250, 40, self.N, "Se connecter", self.font)
    
    def toggle_password_visibility(self):
        # Inversez l'état de visibilité du mot de passe
        self.password_input.toggle_visibility()

    def connexion_button_click_action(self):
        # Mettez ici le code à exécuter lorsque le bouton de connexion est cliqué
        print("Button 'Se connecter' clicked!")    

    def run(self):
        pygame.display.set_caption("Budget_buddy")
        while True:
            mouse_pos = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()

                elif event.type == MOUSEBUTTONDOWN:
                    if self.connexion_button.is_clicked(mouse_pos):
                        if event.button == 1:
                            # Vérifiez si le clic est sur le bouton de l'œil
                            if self.eye_button.rect.collidepoint(event.pos):
                                self.toggle_password_visibility()
                    elif event.type == MOUSEBUTTONDOWN:
                        if event.button == 1:  # Clic gauche
                            if 800 < event.pos[0] < 850 and 255 < event.pos[1] < 305:
                                # Si le clic est sur le bouton de l'œil
                                self.eye_button.toggle_password_visibility()
                # Gérer les événements pour les champs de texte
                self.username_input.handle_event(event)
                self.password_input.handle_event(event)
            self.eye_button.draw()
            self.BK.blit(self.image, (0, 0))

            pygame.draw.rect(self.BK, self.L, (self.x, self.y, self.width, self.height))
            # Dessiner les champs d'entrée et les étiquettes
            pygame.draw.rect(self.BK, self.L, (self.x, self.y, 250, 30)) # Rectangle pour le nom d'utilisateur
            text_surface = self.font.render("Nom ou Email", True, self.N) # Étiquette pour le nom d'utilisateur
            self.BK.blit(text_surface, (570, 179))
            pygame.draw.rect(self.BK, self.N, (570, self.y + 180, 290, 3)) # Dessiner une ligne sous le texte "Nom ou Email"

            pygame.draw.rect(self.BK, self.L, (self.x, self.y + 120, 250, 30)) # Rectangle pour le mot de passe
            text_surface = self.font.render("Mot de passe", True, self.N) # Étiquette pour le mot de passe
            self.BK.blit(text_surface, (570, 280))
            pygame.draw.rect(self.BK, self.N, (570, self.y + 270, 295, 3)) # Dessiner une ligne sous le texte "Mot de passe"

            self.connexion_button.draw_button(self.BK)

            # Création du bouton "Mot de passe oublié ?"
            MDP_O_font = pygame.font.Font(None, 20)
            MDP_O_text = MDP_O_font.render("Mot de passe oublié ?", True, self.N)
            MDP_O_rect = MDP_O_text.get_rect(topleft=(739, 355))
            self.BK.blit(MDP_O_text, MDP_O_rect)
            
            # Création du bouton "Créer un nouveau compte"
            CNC_font = pygame.font.Font("Classes/Images/CFAzteques-Regular.ttf", 25)
            CNC_text = CNC_font.render("Créer une compte !", True, self.N)
            CNC_rect = CNC_text.get_rect(topleft=(620, 600))
            self.BK.blit(CNC_text, CNC_rect)
            
            # Affichage du titre à l'écran
            self.BK.blit(self.t_text, self.t_rect)
            # Affichage du mot "Bienvenue" à l'écran
            self.BK.blit(self.B_text, self.B_rect)
            # Afficher l'image du bouton
            self.BK.blit(self.image_logo, self.icon_rect)

            self.eye_button.draw()
            
            # Afficher les logos
            self.BK.blit(self.facebook_logo, self.facebook_rect)
            self.BK.blit(self.google_logo, self.google_rect)
            
            # Dessiner les champs de texte
            self.username_input.draw(self.BK)
            self.password_input.draw(self.BK)

            pygame.display.update()

connexion = Connexion()
connexion.run()
