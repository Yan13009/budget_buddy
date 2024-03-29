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

# Pages
PAGE_LOGIN = "login"
PAGE_REGISTER = "register"
PAGE_RESET_PASSWORD = "reset_password"

# État actuel de la page
current_page = PAGE_LOGIN

# Variable pour suivre l'état de connexion de l'utilisateur
logged_in = False

# Variables pour suivre l'état des messages de succès et d'échec
success_message_displayed = False
failure_message_displayed = False

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

# Fonction pour afficher un message d'erreur à l'écran
def draw_error_message(error_message):
    if error_message:
        draw_text(error_message, RED, 20, 100)

# Fonction pour afficher un message de réussite à l'écran
def draw_success_message(message):
    draw_text(message, GREEN, 20, 150)

# Fonction pour afficher un message d'échec à l'écran
def draw_failure_message(message):
    draw_text(message, RED, 20, 150)

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
        self.color = self.color_inactive
        self.font = pygame.font.Font(None, 36)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = not self.active
            else:
                self.active = False
            self.color = self.color_active if self.active else self.color_inactive
        elif event.type == pygame.KEYDOWN and self.active:
            if event.key == pygame.K_RETURN:
                self.active = False
            elif event.key == pygame.K_BACKSPACE:
                self.text = self.text[:-1]
            else:
                self.text += event.unicode

    def update(self):
        text_surface = self.font.render(self.text, True, BLACK)
        width = max(200, text_surface.get_width() + 10)
        self.rect.w = width
        pygame.draw.rect(screen, self.color, self.rect, 2)
        screen.blit(text_surface, (self.rect.x + 5, self.rect.y + 5))

def is_valid_email(email):
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(email_regex, email) is not None

def is_unique_email(email):
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE email=?", (email,))
    result = c.fetchone()
    conn.close()
    return result is None

def is_valid_password(password):
    if len(password) < 10:
        return False, "Le mot de passe doit contenir au moins 10 caractères."
    
    has_lowercase = any(char.islower() for char in password)
    has_uppercase = any(char.isupper() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_special = any(char in '!@#$%^&*()_-+={[}]|:;"<,>.?/~' for char in password)
    
    if not all([has_lowercase, has_uppercase, has_digit, has_special]):
        return False, "Le mot de passe doit contenir des lettres minuscules, majuscules, des chiffres et des caractères spéciaux."

    return True, None

def reset_password(firstname, lastname, new_password):
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute("UPDATE users SET password=? WHERE firstname=? AND lastname=?", (new_password, firstname, lastname))
    conn.commit()
    conn.close()

def handle_register(input_boxes):
    firstname = input_boxes[0].text.strip()
    lastname = input_boxes[1].text.strip()
    email = input_boxes[2].text.strip()
    password = input_boxes[3].text.strip()
    
    if not all([firstname, lastname, email, password]):
        return "Erreur: Veuillez remplir tous les champs."
    
    if not is_valid_email(email):
        return "Erreur: L'adresse email n'est pas valide."
    
    if not is_unique_email(email):
        return "Erreur: Cette adresse email est déjà utilisée."
    
    is_valid, error_message = is_valid_password(password)
    if not is_valid:
        return f"Erreur: {error_message}"
    
    if register_user(firstname, lastname, email, password):
        return "Inscription réussie !"
    else:
        return "Erreur: Une erreur s'est produite lors de l'inscription."

def handle_login(input_boxes):
    global logged_in, success_message_displayed, failure_message_displayed  # Utiliser les variables globales
    email = input_boxes[0].text.strip()
    password = input_boxes[1].text.strip()

    if not email or not password:
        return "Erreur: Veuillez remplir tous les champs."
    
    if login_user(email, password):
        logged_in = True
        success_message_displayed = True  # Définir la variable de message de succès sur True
    else:
        failure_message_displayed = True  # Définir la variable de message d'échec sur True

def draw_login_page(input_boxes, buttons, error_message):
    screen.blit(background_image, (0, 0))
    for box in input_boxes:
        box.update()
    for button in buttons:
        button.draw()
    draw_text(error_message, RED, 20, 100)
    if success_message_displayed:
        draw_success_message("Connexion réussie !")  # Afficher le message de succès
    elif failure_message_displayed:
        draw_failure_message("Échec de la connexion. Vérifiez vos informations.")  # Afficher le message d'échec
    draw_text("Connexion", BLACK, 350, 100)
    draw_text("Email:", BLACK, 200, 200)
    draw_text("Mot de passe:", BLACK, 100, 300)
    pygame.display.flip()

def draw_register_page(input_boxes, buttons, error_message):
    screen.blit(background_image, (0, 0))
    for box in input_boxes:
        box.update()
    for button in buttons:
        button.draw()
    draw_text(error_message, RED, 20, 100)
    draw_text("Inscription", BLACK, 350, 100)
    pygame.display.flip()

def draw_reset_password_page(input_boxes, buttons, error_message):
    screen.blit(background_image, (0, 0))
    for box in input_boxes:
        box.update()
    for button in buttons:
        button.draw()
    draw_text(error_message, RED, 20, 100)
    draw_text("Réinitialisation du mot de passe", BLACK, 200, 50)
    draw_text("Nom:", BLACK, 200, 200)
    draw_text("Prénom:", BLACK, 200, 300)
    pygame.display.flip()

def main():
    clock = pygame.time.Clock()
    running = True
    error_message = ""
    
    login_input_boxes = [TextBox(300, 200, 200, 40), TextBox(300, 300, 200, 40)]
    login_button = Button(300, 400, 100, 50, GREEN, BLACK, "Se connecter", lambda: handle_login(login_input_boxes))
    register_input_boxes = [TextBox(300, 200, 200, 40), TextBox(300, 300, 200, 40), TextBox(300, 400, 200, 40), TextBox(300, 500, 200, 40)]
    register_button = Button(300, 550, 100, 50, GREEN, BLACK, "S'inscrire", lambda: handle_register(register_input_boxes))
    reset_password_input_boxes = [TextBox(300, 200, 200, 40), TextBox(300, 300, 200, 40)]
    reset_password_button = Button(300, 400, 100, 50, GREEN, BLACK, "Réinitialiser", lambda: reset_password(reset_password_input_boxes[0].text.strip(), reset_password_input_boxes[1].text.strip(), "NouveauMotDePasse"))
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

            # Gérer les événements de la page actuelle
            if current_page == PAGE_LOGIN:
                for box in login_input_boxes:
                    box.handle_event(event)
                login_button.handle_event(event)
            elif current_page == PAGE_REGISTER:
                for box in register_input_boxes:
                    box.handle_event(event)
                register_button.handle_event(event)
            elif current_page == PAGE_RESET_PASSWORD:
                for box in reset_password_input_boxes:
                    box.handle_event(event)
                reset_password_button.handle_event(event)
        
        # Dessiner la page actuelle
        if current_page == PAGE_LOGIN:
            draw_login_page(login_input_boxes, [login_button], error_message)
        elif current_page == PAGE_REGISTER:
            draw_register_page(register_input_boxes, [register_button], error_message)
        elif current_page == PAGE_RESET_PASSWORD:
            draw_reset_password_page(reset_password_input_boxes, [reset_password_button], error_message)

        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
