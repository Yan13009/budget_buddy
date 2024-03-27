import pygame
import sqlite3
from pygame.locals import *

# Initialiser Pygame
pygame.init()

# Définir les dimensions de la fenêtre
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Initialiser la fenêtre
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Interface d'inscription et de connexion")

# Charger l'image de fond
background_image = pygame.image.load('background.jpg')  # Remplacez 'background.jpg' par le chemin de votre image
background_image = pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))

font = pygame.font.SysFont(None, 36)
# Couleurs
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Fonction pour enregistrer un nouvel utilisateur
def register_user(firstname, lastname, email, password):
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute("INSERT INTO users (firstname, lastname, email, password) VALUES (?, ?, ?, ?)",
              (firstname, lastname, email, password))
    conn.commit()
    conn.close()
    return True

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

class TextBox:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = ""
        self.active = False
        self.color_inactive = GRAY
        self.color_active = WHITE
        self.color = self.color_inactive  # Ajout de l'attribut color
        self.font = pygame.font.Font(None, 36)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Vérifier si le clic de la souris est à l'intérieur de la zone de texte
            if self.rect.collidepoint(event.pos):
                self.active = not self.active
            else:
                self.active = False
            # Modifier la couleur du rectangle selon l'état actif ou inactif
            self.color = self.color_active if self.active else self.color_inactive
        elif event.type == pygame.KEYDOWN and self.active:
            if event.key == pygame.K_RETURN:
                # Désactiver le champ de texte lorsqu'on appuie sur Entrée
                self.active = False
            elif event.key == pygame.K_BACKSPACE:
                # Supprimer le dernier caractère lorsqu'on appuie sur Retour arrière
                self.text = self.text[:-1]
            else:
                # Ajouter le caractère entré à la chaîne de texte
                self.text += event.unicode

    def update(self):
        # Créer une surface de texte avec la chaîne actuelle
        text_surface = self.font.render(self.text, True, BLACK)
        # Ajuster la largeur de la boîte de texte pour s'adapter au texte
        width = max(200, text_surface.get_width() + 10)
        # Mettre à jour la taille et la position de la boîte de texte
        self.rect.w = width
        # Dessiner le rectangle de la boîte de texte
        pygame.draw.rect(screen, self.color, self.rect, 2)
        # Dessiner la surface de texte
        screen.blit(text_surface, (self.rect.x + 5, self.rect.y + 5))


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

def handle_login(input_boxes):
    print("Connexion en cours...")

    # Récupération des valeurs des champs de connexion (email et mot de passe)
    email = input_boxes[0].text
    password = input_boxes[1].text

    # Validation des données saisies
    if not email or not password:
        print("Erreur: Veuillez remplir tous les champs.")
        return
    # Appel de la fonction login_user avec les données validées
    if login_user(email, password):
        print("Connexion réussie !")
    else:
        print("Erreur: La connexion a échoué.")


def handle_events(input_boxes, register_button, login_button):
    for event in pygame.event.get():
        if event.type == QUIT:
            return False
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                return False
        # Gérer les événements des boutons
        register_button.handle_event(event)
        login_button.handle_event(event)
        # Gérer les événements des champs de texte
        for box in input_boxes:
            box.handle_event(event)
    return True

def draw_elements(input_boxes, register_button, login_button):
    # Afficher l'animation de fond
    screen.blit(background_image, (0, 0))

    # Afficher les champs de texte
    for box in input_boxes:
        box.update()

    # Afficher les boutons
    register_button.draw()
    login_button.draw()

def draw_page_text(is_register_page):
    if is_register_page:
        draw_text("Inscription", BLACK, 350, 100)
        draw_text("Nom:", BLACK, 200, 200)
        draw_text("Prénom:", BLACK, 200, 300)
        draw_text("Email:", BLACK, 200, 400)
        draw_text("Mot de passe:", BLACK, 130, 500)
    else:
        draw_text("Connexion", BLACK, 350, 100)
        draw_text("Email:", BLACK, 200, 200)
        draw_text("Mot de passe:", BLACK, 130, 300)

def main():
    clock = pygame.time.Clock()
    running = True  # Initialise la variable running à True

    is_register_page = True
    input_boxes = [TextBox(300, 200, 200, 40), TextBox(300, 300, 200, 40), TextBox(300, 400, 200, 40), TextBox(300, 500, 200, 40)]

    # Créer des boutons pour l'inscription et la connexion
    register_button = Button(300, 550, 100, 50, GREEN, BLACK, "S'inscrire", lambda: handle_register(input_boxes))
    login_button = Button(500, 550, 100, 50, RED, BLACK, "Se connecter", lambda: handle_login(input_boxes))

    while running:
        running = handle_events(input_boxes, register_button, login_button)

        draw_elements(input_boxes, register_button, login_button)

        draw_page_text(is_register_page)

        pygame.display.flip()
        clock.tick(60)  # Limite le nombre de frames par seconde

    # Quitter Pygame
    pygame.quit()

if __name__ == "__main__":
    main()

