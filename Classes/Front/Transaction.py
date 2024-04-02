import pygame
from pygame.locals import *
from Button import Button
from TextInput import TextInput
import mysql.connector
from datetime import datetime

class TransactionInterface:
    def __init__(self):
        pygame.init()

        self.BK = pygame.display.set_mode((1000, 700))
        self.image = pygame.image.load('Classes/Images/background.jpg')
        self.image = pygame.transform.scale(self.image, (1000, 700))
        pygame.display.set_caption("Budget_buddy")

        self.font = pygame.font.Font(None, 30)
        self.N = (0, 0, 0)
        self.L = (97, 84, 105)

        self.text_inputs = {
            "Nom": TextInput(570, 115, 250, 40, self.font, self.N, self.L, self.L),
            "Description": TextInput(570, 205, 250, 40, self.font, self.N, self.L, self.L),
            "Montant": TextInput(570, 295, 250, 40, self.font, self.N, self.L, self.L),
            "Type": TextInput(570, 385, 250, 40, self.font, self.N, self.L, self.L),
            "Utilisateur ID": TextInput(570, 475, 250, 40, self.font, self.N, self.L, self.L)
        }

        self.ajouter_button = Button(570, 565, 250, 40, self.N, "Ajouter", self.font)

    def ajouter_transaction(self):
        nom = self.text_inputs["Nom"].get_text()
        description = self.text_inputs["Description"].get_text()
        montant_str = self.text_inputs["Montant"].get_text()
        type_transaction = self.text_inputs["Type"].get_text()
        utilisateur_id_str = self.text_inputs["Utilisateur ID"].get_text()

        try:
            montant = float(montant_str)
            utilisateur_id = int(utilisateur_id_str)

            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="Maysa1995@",
                database="budget_buddy"
            )

            mycursor = mydb.cursor()

            sql = "INSERT INTO transactions (nom, description, montant, type, date, utilisateur_id) VALUES (%s, %s, %s, %s, %s, %s)"
            date_transaction = datetime.now().date()
            val = (nom, description, montant, type_transaction, date_transaction, utilisateur_id)
            mycursor.execute(sql, val)

            mydb.commit()

            print("Transaction ajoutée avec succès.")
        except ValueError:
            print("Erreur: Le montant ou l'identifiant utilisateur n'est pas un nombre valide.")
        except Exception as e:
            print("Erreur lors de l'ajout de la transaction :", e)
        finally:
            try:
                if mydb.is_connected():
                    mydb.close()
                    print("Connexion à la base de données fermée.")
            except NameError:
                pass

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                # Gérer les événements pour les champs de texte
                for text_input in self.text_inputs.values():
                    text_input.handle_event(event)

                # Gérer les événements pour le bouton Ajouter
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.ajouter_button.is_clicked(pygame.mouse.get_pos()):
                        print("Bouton Ajouter cliqué !")
                        self.ajouter_transaction()

            self.BK.blit(self.image, (0, 0))

            for text_input in self.text_inputs.values():
                text_input.draw(self.BK)

            self.ajouter_button.draw_button(self.BK)

            pygame.display.update()

        pygame.quit()

if __name__ == "__main__":
    interface = TransactionInterface()
    interface.run()


