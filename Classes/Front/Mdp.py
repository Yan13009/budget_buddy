import pygame 
from pygame.locals import *
from TextInput import TextInput
from Button import Button
import mysql.connector
import re


pygame.init()

class Mdp:
    def __init__(self):

        self.BK = pygame.display.set_mode((1000, 700))
        pygame.display.set_caption("Budget_buddy")
        self.image = pygame.image.load('Classes/Images/background.jpg')
        self.image = pygame.transform.scale(self.image, (1000, 700))
        self.font = pygame.font.Font(None, 30)

        self.N = (0, 0, 0)
        self.B = (255, 255, 255)
        self.R = (255, 0, 0)
        self.K = (55, 42, 59)
        self.M = (61, 54, 69)
        self.L = (97, 84, 105)

        self.x = 250
        self.y = 50
        self.width = 500
        self.height = 600

    def check_Mdp(self, password):
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
        if not self.check_Mdp(mot_de_passe):
            print("Le mot de passe ne satisfait pas aux critères de sécurité.")
            return

        try:
            print("Connecting to the database...")
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="Maysa1995@",
                database="budget_buddy"
            )

            if mydb.is_connected():
                print("Connected to the database!")

            mycursor = mydb.cursor()

            sql = "INSERT INTO user (nom, prenom, email, mot_de_passe) VALUES (%s, %s, %s, %s)"
            val = (nom, prenom, email, mot_de_passe)
            mycursor.execute(sql, val)

            mydb.commit()

            print("Utilisateur enregistré avec succès.")
        except Exception as e:
            print("Erreur lors de l'enregistrement de l'utilisateur :", e)
        finally:
            if mydb.is_connected():
                mydb.close()
                print("Database connection closed.")


    def create_text_inputs(self):
        # Définition des champs de texte
        self.nom_email_input = TextInput(350, 270, 290, 40, self.font, self.L, self.N, self.N)
        self.mdp_input = TextInput(350, 370, 290, 40, self.font, self.L, self.N, self.N)
        self.cmdp_input = TextInput(350, 470, 290, 40, self.font, self.L, self.N, self.N)

    def run(self):
        self.create_text_inputs()    

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                # Gérer les événements de texte pour les champs d'entrée
                self.nom_email_input.handle_event(event)
                self.mdp_input.handle_event(event)
                self.cmdp_input.handle_event(event)

                # Gérer les événements de clic de souris
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    # Vérifier si le clic est à l'intérieur des limites du bouton de connexion
                    if self.connexion_button.rect.collidepoint(mouse_pos):
                        # Récupérer les valeurs des champs de texte
                        nom = self.nom_email_input.get_text()
                        prenom = ""  # Ajoutez le champ de texte pour le prénom si nécessaire
                        email = ""   # Récupérez le champ de texte pour l'email
                        mdp = self.mdp_input.get_text()
                        cmdp = self.cmdp_input.get_text()

                        # Vérifier si les mots de passe correspondent et sont conformes
                        if mdp == cmdp and self.check_Mdp(mdp):
                            # Enregistrer l'utilisateur dans la base de données
                            self.register_user(nom, prenom, email, mdp)
                        else:
                            print("Les mots de passe ne correspondent pas ou ne satisfont pas aux critères de sécurité.") 

            self.BK.blit(self.image, (0, 0))
            pygame.draw.rect(self.BK, self.L, (self.x, self.y, self.width, self.height))

            # Création d'une surface de texte pour le titre "Créer un nouveau mot de passe"
            t_font_mdp = pygame.font.Font("Classes/Images/CFAzteques-Regular.ttf", 30)  # Choisir la police et la taille
            t_text_mdp = t_font_mdp.render("Créer un nouveau mot de passe", True, self.N)  # Couleur rouge (255, 0, 0)
            t_rect_mdp = t_text_mdp.get_rect(center=(505, 80))  # Centrez le texte horizontalement
            self.BK.blit(t_text_mdp, t_rect_mdp)

            image_logo = pygame.image.load('Classes/Images/icons8-money-box-48.png')
            n_width = 80
            n_height = 80
            image_logo = pygame.transform.scale(image_logo, (n_width, n_height))
            icon_rect = image_logo.get_rect()
            icon_rect.topleft = (460, 140)
            self.BK.blit(image_logo, icon_rect)

            # Affichage des étiquettes et des champs de texte
            label_nom_email = self.font.render("Nom ou Email", True, self.N)
            self.BK.blit(label_nom_email, (350, 240))
            self.nom_email_input.draw(self.BK)

            label_mdp = self.font.render("Mot de passe", True, self.N)
            self.BK.blit(label_mdp, (350, 340))
            self.mdp_input.draw(self.BK)

            label_cmdp = self.font.render("Confirmer Mot de passe", True, self.N)
            self.BK.blit(label_cmdp, (350, 440))
            self.cmdp_input.draw(self.BK)

            # Création du bouton de connexion
            self.connexion_button = Button(350, 580, 290, 50, self.N, "Confirmer", self.font)
            self.connexion_button.draw_button(self.BK)

            pygame.display.update()

mdp = Mdp()
mdp.run()

