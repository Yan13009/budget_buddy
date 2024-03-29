import pygame
import sqlite3
import re

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

# Fonction pour réinitialiser un mot de passe
def reset_password(firstname, lastname, new_password):
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute("UPDATE users SET password=? WHERE firstname=? AND lastname=?", (new_password, firstname, lastname))
    conn.commit()
    conn.close()

# Fonction pour afficher du texte à l'écran
def draw_text(text, color, x, y):
    surface = font.render(text, True, color)
    screen.blit(surface, (x, y))

# Fonction pour afficher un message d'erreur à l'écran
def draw_error_message(error_message):
    if error_message:
        draw_text(error_message, RED, 200, 50)

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

def is_valid_email(email):
    # Vérifie si l'email est valide en utilisant une expression régulière
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(email_regex, email) is not None

def is_unique_email(email):
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE email=?", (email,))
    result = c.fetchone()
    conn.close()
    print("Résultat de la recherche pour", email, ":", result)  
    return result is None

def is_valid_password(password):
    # Vérifie si le mot de passe a au moins 10 caractères
    if len(password) < 10:
        return False, "Le mot de passe doit contenir au moins 10 caractères."
    
    # Vérifie si le mot de passe contient des lettres minuscules, majuscules, des chiffres et des caractères spéciaux
    has_lowercase = any(char.islower() for char in password)
    has_uppercase = any(char.isupper() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_special = any(char in '!@#$%^&*()_-+={[}]|:;"<,>.?/~' for char in password)
    
    if not all([has_lowercase, has_uppercase, has_digit, has_special]):
        return False, "Le mot de passe doit contenir des lettres minuscules, majuscules, des chiffres et des caractères spéciaux."

    return True, None

def handle_register(input_boxes):
    # Récupération des valeurs des champs d'inscription
    firstname = input_boxes[0].text.strip()
    lastname = input_boxes[1].text.strip()
    email = input_boxes[2].text.strip()
    password = input_boxes[3].text.strip()
    
    # Validation des données saisies
    if not all([firstname, lastname, email, password]):
        return "Erreur: Veuillez remplir tous les champs."
    
    # Validation de l'email
    if not is_valid_email(email):
        return "Erreur: L'adresse email n'est pas valide."
    
    # Vérification de l'unicité de l'email
    if not is_unique_email(email):
        return "Erreur: Cette adresse email est déjà utilisée."
    
    # Validation du mot de passe
    is_valid, error_message = is_valid_password(password)
    if not is_valid:
        return f"Erreur: {error_message}"
    
    # Appel de la fonction register_user avec les données validées
    if register_user(firstname, lastname, email, password):
        return "Inscription réussie !"
    else:
        return "Erreur: Une erreur s'est produite lors de l'inscription."

def handle_login(input_boxes):
    # Récupération des valeurs des champs de connexion (email et mot de passe)
    email = input_boxes[2].text.strip()  # Le troisième champ est l'email
    password = input_boxes[3].text.strip()  # Le quatrième champ est le mot de passe

    # Validation des données saisies
    if not email or not password:
        return "Erreur: Veuillez remplir tous les champs."
    
    # Appel de la fonction login_user avec les données validées
    if login_user(email, password):
        return "Connexion réussie !"
    else:
        return "Erreur: La connexion a échoué."

def handle_reset_password(input_boxes):
    # Récupération des valeurs des champs de nom et prénom
    firstname = input_boxes[0].text.strip()
    lastname = input_boxes[1].text.strip()

    # Vérification si le nom et le prénom sont valides (non vides)
    if not firstname or not lastname:
        print("Veuillez fournir votre nom et prénom pour réinitialiser le mot de passe.")
        return

    # Demande à l'utilisateur de saisir un nouveau mot de passe
    new_password = input("Veuillez saisir votre nouveau mot de passe : ")

    # Mise à jour du mot de passe dans la base de données
    reset_password(firstname, lastname, new_password)
    print("Mot de passe réinitialisé avec succès !")

def handle_events(input_boxes, register_button, login_button, reset_button):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                return False
        # Gérer les événements des boutons
        if event.type == pygame.MOUSEBUTTONDOWN:
            if register_button.rect.collidepoint(event.pos):
                print(handle_register(input_boxes))
            elif login_button.rect.collidepoint(event.pos):
                print(handle_login(input_boxes))
            elif reset_button.rect.collidepoint(event.pos):
                handle_reset_password(input_boxes)
        # Gérer les événements des champs de texte
        for box in input_boxes:
            box.handle_event(event)
            # Désactiver tous les champs de texte sauf ceux de l'email et du mot de passe lors de la connexion
            if login_button.rect.collidepoint(pygame.mouse.get_pos()):
                if box != input_boxes[2] and box != input_boxes[3]:
                    box.active = False
                    box.color = box.color_inactive
    return True

def draw_elements(input_boxes, register_button, login_button, reset_button, is_register_page, error_message=""):
    # Afficher l'animation de fond
    screen.blit(background_image, (0, 0))

    # Afficher les champs de texte
    for box in input_boxes:
        box.update()

    # Afficher les boutons
    register_button.draw()
    login_button.draw()
    reset_button.draw()

    # Afficher le texte de la page
    draw_page_text(is_register_page)

    # Afficher le message d'erreur
    draw_text(error_message, RED, 20, 100)

    # Si ce n'est pas la page d'inscription, effacer visuellement le nom et le prénom
    if not is_register_page:
        draw_text("Nom:", WHITE, 200, 200)
        draw_text("Prénom:", WHITE, 200, 300)

    pygame.display.flip()

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
    running = True
    is_register_page = True  # Initialise la variable is_register_page à True
    error_message = ""  # Initialiser le message d'erreur à une chaîne vide

    # Initialisation des autres éléments de l'interface
    input_boxes = [TextBox(300, 200, 200, 40), TextBox(300, 300, 200, 40), TextBox(300, 400, 200, 40), TextBox(300, 500, 200, 40)]
    register_button = Button(300, 550, 100, 50, GREEN, BLACK, "S'inscrire")
    login_button = Button(500, 550, 100, 50, RED, BLACK, "Se connecter")
    reset_button = Button(600, 550, 100, 30, GRAY, BLACK, "Réinitialiser MDP")

    while running:
        # Appel des fonctions pour gérer les événements, dessiner les éléments et mettre à jour l'affichage
        error_message = ""  # Réinitialiser le message d'erreur à chaque boucle
        running = handle_events(input_boxes, register_button, login_button, reset_button)  # Mettre à jour la variable running
        draw_elements(input_boxes, register_button, login_button, reset_button, is_register_page, error_message)

        pygame.display.flip()
        clock.tick(60)  # Limite le nombre de frames par seconde
        
    pygame.quit()

if __name__ == "__main__":
    main()
