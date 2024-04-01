import pygame
import re
import mysql.connector

class Mdp:
    def __init__(self):
        pygame.init()
        self.BK = pygame.display.set_mode((1000, 700))
        pygame.display.set_caption("Mot de passe")
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
                    if self.validate_password(self.password):
                        print("Mot de passe valide")
                        #self.register_user("John", "Doe", "john@example.com", self.password)
                    else:
                        print("Mot de passe non valide")

                else:
                    self.password += event.unicode

    def validate_password(self, password):
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

    def register_user(self, nom, prenom, email, mot_de_passe):
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
        running = True
        while running:
            self.handle_events()

            # Dessiner l'interface utilisateur
            self.BK.fill((255, 255, 255))
            pygame.draw.rect(self.BK, (17, 86, 95), (100, 100, 400, 50))
            text_surface = self.font.render(self.password, True, (255, 255, 255))
            self.BK.blit(text_surface, (110, 110))
            pygame.display.flip()

            self.clock.tick(60)

if __name__ == "__main__":
    password_page = Mdp()
    password_page.run()