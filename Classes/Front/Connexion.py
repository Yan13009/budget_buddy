import pygame
from pygame.locals import *
from Button import Button
from Compte import Compte
from TextInput import TextInput
import mysql.connector
from Transaction import  TransactionInterface
pygame.init()

class Connexion:
    def __init__(self):
        self.BK = pygame.display.set_mode((1000, 700))
        self.image = pygame.image.load('Classes/Images/background.jpg')
        self.image = pygame.transform.scale(self.image, (1000, 700))
        self.font = pygame.font.Font(None, 30)

        self.N = (0, 0, 0)
        self.L = (97, 84, 105)

        self.x = 550
        self.y = 75
        self.width = 400
        self.height = 600

        self.username_input = TextInput(570, 215, 250, 40, self.font, self.N, self.L, self.L)
        self.password_input = TextInput(570, 305, 250, 40, self.font, self.N, self.L, self.L)
        
        self.t_font = pygame.font.Font("Classes/Images/CFAzteques-Regular.ttf", 50)
        self.t_text = self.t_font.render("Budget-buddy", True, self.N)
        self.t_rect = self.t_text.get_rect(center=(750, 120))
        
        self.B_font = pygame.font.Font("Classes/Images/CFAzteques-Regular.ttf", 70)
        self.B_text = self.B_font.render("Bienvenue", True, self.N)
        self.B_rect = self.B_text.get_rect(topleft=(100, 300))
        
        self.image_logo = pygame.image.load('Classes/Images/icons8-accumulate-48.png')
        self.n_width = 80
        self.n_height = 80
        self.image_logo = pygame.transform.scale(self.image_logo, (self.n_width, self.n_height))
        self.icon_rect = self.image_logo.get_rect()
        self.icon_rect.topleft = (220, 400)
        
        self.facebook_logo = pygame.image.load('Classes/Images/facebook-48.png')
        self.google_logo = pygame.image.load('Classes/Images/google-48.png')
        self.logo_width = 40
        self.logo_height = 40
        self.facebook_logo = pygame.transform.scale(self.facebook_logo, (self.logo_width, self.logo_height))
        self.google_logo = pygame.transform.scale(self.google_logo, (self.logo_width, self.logo_height))
        self.facebook_rect = self.facebook_logo.get_rect(topleft=(680, 500))
        self.google_rect = self.google_logo.get_rect(topleft=(780, 500))

        self.connexion_button = Button(570, 400, 250, 40, self.N, "Se connecter", self.font)

    def login_user(self, email, mot_de_passe):
        try:
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="Maysa1995@",
                database="budget_buddy"
            )

            mycursor = mydb.cursor()

            sql = "SELECT * FROM user WHERE email = %s AND mot_de_passe = %s"
            val = (email, mot_de_passe)
            mycursor.execute(sql, val)

            user = mycursor.fetchone()

            if user:
                print("Connexion réussie !")
                # Ajoutez ici le code pour autoriser l'accès à l'utilisateur
            else:
                print("Nom d'utilisateur ou mot de passe incorrect.")

        except Exception as e:
            print("Erreur lors de l'authentification :", e)
    
    def creer_compte(self):
        compte = Compte()
        compte.run()

    def run(self):
        pygame.display.set_caption("Budget_buddy")
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                    

                # Gérer les événements pour les champs de texte
                self.username_input.handle_event(event)
                self.password_input.handle_event(event)

                # Gérer les événements pour le bouton de connexion
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.connexion_button.is_clicked(pygame.mouse.get_pos()):
                        interface = TransactionInterface()
                        interface.run()
                        print("Bouton de connexion cliqué !")
                        #self.login_user(self.username_input.get_text(), self.password_input.get_text())

                # Gérer les événements pour "Mot de passe oublié"
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if MDP_O_rect.collidepoint(pygame.mouse.get_pos()):
                        print("Mot de passe oublié cliqué !")
                        import Mdp
                        
                        # Ajoutez ici le code pour gérer le mot de passe oublié
 
                # Gérer les événements pour "Créer une compte"
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if CNC_rect.collidepoint(pygame.mouse.get_pos()):
                        print("Créer un compte cliqué !")
                        self.creer_compte()  
                                      

            self.BK.blit(self.image, (0, 0))

            pygame.draw.rect(self.BK, self.L, (self.x, self.y, self.width, self.height))
            pygame.draw.rect(self.BK, self.L, (self.x, self.y, 250, 30))
            text_surface = self.font.render("Nom ou Email", True, self.N)
            self.BK.blit(text_surface, (570, 179))
            pygame.draw.rect(self.BK, self.N, (570, self.y + 180, 290, 3))

            pygame.draw.rect(self.BK, self.L, (self.x, self.y + 120, 250, 30))
            text_surface = self.font.render("Mot de passe", True, self.N)
            self.BK.blit(text_surface, (570, 280))
            pygame.draw.rect(self.BK, self.N, (570, self.y + 270, 295, 3))

            self.connexion_button.draw_button(self.BK)

            MDP_O_font = pygame.font.Font(None, 20)
            MDP_O_text = MDP_O_font.render("Mot de passe oublié ?", True, self.N)
            MDP_O_rect = MDP_O_text.get_rect(topleft=(739, 355))
            self.BK.blit(MDP_O_text, MDP_O_rect)
            
            CNC_font = pygame.font.Font("Classes/Images/CFAzteques-Regular.ttf", 25)
            CNC_text = CNC_font.render("Créer un compte !", True, self.N)
            CNC_rect = CNC_text.get_rect(topleft=(620, 600))
            self.BK.blit(CNC_text, CNC_rect)
            
            self.BK.blit(self.t_text, self.t_rect)
            self.BK.blit(self.B_text, self.B_rect)
            self.BK.blit(self.image_logo, self.icon_rect)
            
            self.BK.blit(self.facebook_logo, self.facebook_rect)
            self.BK.blit(self.google_logo, self.google_rect)
            
            self.username_input.draw(self.BK)
            self.password_input.draw(self.BK)

            pygame.display.update()

connexion = Connexion()
connexion.run()
