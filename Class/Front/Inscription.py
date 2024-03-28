import pygame
import sqlite3
import re
from pygame.locals import *
from button import Button

# Initialiser Pygame
pygame.init()

# Définir les dimensions de la fenêtre
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Initialiser la fenêtre
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Interface d'inscription et de connexion")

# Charger l'image de fond
background_image = pygame.image.load('Images/4.jpg')  # Remplacez 'background.jpg' par le chemin de votre image
background_image = pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))

font = pygame.font.SysFont(None, 36)
# Couleurs
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Fonction pour vérifier si le mot de passe est sécurisé
def is_secure_password(password):
    if len(password) < 10:
        return False
    if not re.search("[a-z]", password):
        return False
    if not re.search("[A-Z]", password):
        return False
    if not re.search("[0-9]", password):
        return False
    if not re.search("[!@#$%^&*()_+{};:]", password):
        return False
    return True

# Fonction pour enregistrer un nouvel utilisateur
def register_user(firstname, lastname, email, password):
    if is_secure_password(password):
        conn = sqlite3.connect('users.db')
        c = conn.cursor()
        c.execute("INSERT INTO users (firstname, lastname, email, password) VALUES (?, ?, ?, ?)",
                  (firstname, lastname, email, password))
        conn.commit()
        conn.close()
        return True
    else:
        return False

# Fonction pour connecter un utilisateur
def login_user(email, password):
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE email=? AND password=?", (email, password))
    user = c.fetchone()
    conn.close()

    if user:
        return True
    else:
        return False

# Fonction pour afficher du texte à l'écran
def draw_text(text, color, x, y):
    surface = font.render(text, True, color)
    screen.blit(surface, (x, y))

# Classe pour créer des boutons

class Button:
    def __init__(self, x, y, width, height, color, text_color, text, action=None):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.text_color = text_color
        self.text = text
        self.action = action

    def draw(self):
        pygame.draw.rect(screen, self.color, self.rect)
        draw_text(self.text, self.text_color, self.rect.x + self.rect.width // 2 - 50, self.rect.y + self.rect.height // 2 - 15)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                if self.action:
                    self.action()

# Classe pour les champs de texte
class TextBox:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = ""

    def draw(self):
        pygame.draw.rect(screen, WHITE, self.rect, 2)
        draw_text(self.text, BLACK, self.rect.x + 5, self.rect.y + 5)

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                self.text = self.text[:-1]
            else:
                self.text += event.unicode

def handle_register(input_boxes):
    print("Inscription en cours...")

    # Récupération des valeurs des champs d'inscription
    firstname = input_boxes[0].text
    lastname = input_boxes[1].text
    email = input_boxes[2].text
    password = input_boxes[3].text
    
    # Validation des données saisies
    if not firstname or not lastname or not email or not password:
        print("Erreur: Veuillez remplir tous les champs.")
        return
    
    # Appel de la fonction register_user avec les données validées
    if register_user(firstname, lastname, email, password):
        print("Inscription réussie !")
    else:
        print("Erreur: Le mot de passe doit contenir au moins 10 caractères, dont des lettres minuscules, majuscules, des chiffres et des caractères spéciaux.")

def handle_login():
    print("Connexion en cours...")

    # Récupération des valeurs des champs de connexion
    email = input("Entrez votre adresse e-mail : ")
    password = input("Entrez votre mot de passe : ")

    # Validation des données saisies
    if not email or not password:
        print("Erreur: Veuillez remplir tous les champs.")
        return

    # Appel de la fonction login_user avec les données validées
    if login_user(email, password):
        print("Connexion réussie !")
    else:
        print("Erreur: La connexion a échoué.")

def main():
    clock = pygame.time.Clock()
    running = True  # Initialise la variable running à True

    is_register_page = True
    input_boxes = [TextBox(300, 200, 200, 40), TextBox(300, 300, 200, 40), TextBox(300, 400, 200, 40), TextBox(300, 500, 200, 40)]

    # Créer des boutons pour l'inscription et la connexion
    register_button = Button(300, 550, 100, 50, GREEN, BLACK, "S'inscrire", lambda: handle_register(input_boxes))
    login_button = Button(500, 550, 100, 50, RED, BLACK, "Se connecter", handle_login)

    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
            # Gérer les événements des boutons
            register_button.handle_event(event)
            login_button.handle_event(event)
            # Gérer les événements des champs de texte
            for box in input_boxes:
                box.handle_event(event)

        # Afficher l'animation de fond
        screen.blit(background_image, (0, 0))

        # Afficher les champs de texte
        for box in input_boxes:
            box.draw()

        # Afficher les boutons
        register_button.draw()
        login_button.draw()

        # Afficher le texte selon la page actuelle (inscription ou connexion)
        if is_register_page:
            draw_text("Inscription", BLACK, 350, 50)
            draw_text("Nom:", BLACK, 129, 200)
            draw_text("Prénom:", BLACK, 120, 300)
            draw_text("Email:", BLACK, 120, 400)
            draw_text("Mot de passe:", BLACK, 120, 500)
        else:
            draw_text("Connexion", BLACK, 350, 100)
            draw_text("Email:", BLACK, 200, 200)
            draw_text("Mot de passe:", BLACK, 200, 300)

        pygame.display.flip()
        clock.tick(60)  # Limite le nombre de frames par seconde

    # Quitter Pygame
    pygame.quit()

if __name__ == "__main__":
    main()
