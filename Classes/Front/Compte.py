import re
import pygame 
from pygame.locals import *
from Button import Button 
from TextInput import TextInput
import mysql.connector
pygame.init()

class Compte:
    def __init__(self):
        self.BK = pygame.display.set_mode((1000, 700))
        pygame.display.set_caption("Budget_buddy")
        self.image = pygame.image.load('Classes/Images/background.jpg')
        self.image = pygame.transform.scale(self.image, (1000, 700))
        self.font = pygame.font.Font(None, 30)

        self.N = (0, 0, 0)
        self.L = (97, 84, 105)

        self.Nom_input = TextInput(80, 140, 290, 40, self.font, self.L, self.N, self.N)
        self.Prenom_input = TextInput(80, 235, 290, 40, self.font, self.L, self.N, self.N)
        self.email_input = TextInput(80, 330, 290, 40, self.font, self.L, self.N, self.N)
        self.Mdp_input = TextInput(80, 425, 290, 40, self.font, self.L, self.N, self.N)
        self.Cmdp_input = TextInput(80, 520, 290, 40, self.font, self.L, self.N, self.N)

        self.x = 50
        self.y = 40
        self.width = 475
        self.height = 650

    def check__Mdp(self, password):
        # Vérifie si le mot de passe satisfait aux critères requis
        if len(password) < 10:
            return False
        if not re.search(r'[A-Z]', password):
            return False
        if not re.search(r'[a-z]', password):
            return False
        if not re.search(r'[0-9]', password):
            return False
        if not re.search(r'[!@#$%^&*()-_+=]', password):
            return False
        return True    
    
    def register_user(self, nom, prenom, email, mot_de_passe):
        # Vérifie d'abord la force du mot de passe
        if not self.check__Mdp(mot_de_passe):
            print("Le mot de passe ne satisfait pas aux critères de sécurité.")
            return
        try:
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="maysa1995",
                database="budget_buddy"
            )

            mycursor = mydb.cursor()

            sql = "INSERT INTO compte (nom, prenom, email, mot_de_passe) VALUES (%s, %s, %s, %s)"
            val = (nom, prenom, email, mot_de_passe)
            mycursor.execute(sql, val)

            mydb.commit()

            print("Utilisateur enregistré avec succès.")
        except Exception as e:
            print("Erreur lors de l'enregistrement de l'utilisateur :", e)

    
    def run(self):
        while True:
            mouse_pos = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()
                elif event.type == MOUSEBUTTONDOWN:
                    # Gérer les clics de souris pour les interactions avec les champs d'entrée
                    self.Nom_input.handle_event(event)
                    self.Prenom_input.handle_event(event)
                    self.email_input.handle_event(event)
                    self.Mdp_input.handle_event(event)
                    self.Cmdp_input.handle_event(event)
                elif event.type == KEYDOWN:  # Gérer les événements de touche en entrée de texte
                    self.Nom_input.handle_event(event)
                    self.Prenom_input.handle_event(event)
                    self.email_input.handle_event(event)
                    self.Mdp_input.handle_event(event)
                    self.Cmdp_input.handle_event(event)    



            B_font = pygame.font.Font("Classes/Images/CFAzteques-Regular.ttf", 70)
            B_text = B_font.render("Bienvenue", True, self.N)
            B_rect = B_text.get_rect(topleft=(620, 120))
            
            # Création d'une surface de texte pour le titre "Budget buddy"
            t_font = pygame.font.Font("Classes/Images/CFAzteques-Regular.ttf", 50)  # Choisir la police et la taille
            t_text = t_font.render("Créer un compte", True, self.N)  # Couleur rouge (255, 0, 0)
            t_rect = t_text.get_rect(center=(720, 250))  # Centrez le texte horizontalement

            image_logo = pygame.image.load('Classes/Images/icons8-accumulate-48.png')
            n_width = 80
            n_height = 80
            image_logo = pygame.transform.scale(image_logo, (n_width, n_height))
            icon_rect = image_logo.get_rect()
            icon_rect.topleft = (720, 300)

            facebook_logo = pygame.image.load('Classes/Images/facebook-48.png')
            google_logo = pygame.image.load('Classes/Images/google-48.png')
            logo_width = 40
            logo_height = 40
            facebook_logo = pygame.transform.scale(facebook_logo, (logo_width, logo_height))
            google_logo = pygame.transform.scale(google_logo, (logo_width, logo_height))
            facebook_rect = facebook_logo.get_rect(topleft=(150, 580))
            google_rect = google_logo.get_rect(topleft=(240, 580))

            self.BK.blit(self.image, (0, 0))       
            pygame.draw.rect(self.BK, self.L, (self.x, self.y, self.width, self.height))

            # Champ pour l'identifiant
            pygame.draw.rect(self.BK, self.L, (self.x, self.y, 290, 40))  
            text_surface = self.font.render("Nom", True, self.N)  
            self.BK.blit(text_surface, (80, 110))
            pygame.draw.rect(self.BK, self.N, (80, self.y + 120, 290, 3)) 

            # Dessiner les champs d'entrée et les étiquettes
            pygame.draw.rect(self.BK, self.L, (self.x, self.y, 290, 40))  # Rectangle pour le nom d'utilisateur
            text_surface = self.font.render("Prénom", True, self.N)  # Étiquette pour le nom d'utilisateur
            self.BK.blit(text_surface, (80, 205))
            pygame.draw.rect(self.BK, self.N, (80, self.y + 215, 290, 3))  # Dessiner une ligne sous le texte "Nom ou Email"

            pygame.draw.rect(self.BK, self.L, (self.x, self.y, 290, 40))  # Rectangle pour le mot de passe
            text_surface = self.font.render("Email", True, self.N)  # Étiquette pour le mot de passe
            self.BK.blit(text_surface, (80, 300))
            pygame.draw.rect(self.BK, self.N, (80, self.y + 310, 290, 3))  # Dessiner une ligne sous le texte "Mot de passe"

            # Champ de mot de passe
            pygame.draw.rect(self.BK, self.L, (self.x, self.y, 290, 40))  
            text_surface = self.font.render("mot de passe", True, self.N)  
            self.BK.blit(text_surface, (80, 390))
            pygame.draw.rect(self.BK, self.N, (80, self.y + 400, 290, 3)) 

            # Champ de confirmation du mot de passe
            pygame.draw.rect(self.BK, self.L, (self.x, self.y, 290, 40))  
            text_surface = self.font.render("Confirmer mot de passe", True, self.N)  
            self.BK.blit(text_surface, (80, 480))
            pygame.draw.rect(self.BK, self.N, (80, self.y + 490, 290, 3))   

            connexion_button = Button(80, 630, 290, 50, self.N, "Se connecter", self.font)
            
            connexion_button.draw_button(self.BK)
            # Affichage du titre à l'écran
            self.BK.blit(t_text, t_rect)
            self.BK.blit(B_text, B_rect)
            self.BK.blit(image_logo, icon_rect)

            self.BK.blit(facebook_logo, facebook_rect)
            self.BK.blit(google_logo, google_rect)

            # Dessiner les champs de texte
            self.Nom_input.draw(self.BK)
            self.Prenom_input.draw(self.BK)
            self.email_input.draw(self.BK)
            self.Mdp_input.draw(self.BK)
            self.Cmdp_input.draw(self.BK)


            pygame.display.update() 

if __name__ == "__main__":
    compte = Compte()
    compte.run()

