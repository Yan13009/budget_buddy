import pygame
from button import Button
from input_field import InputField
import re

class RegistrationInterface:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Registration")
        self.clock = pygame.time.Clock()

        # Initialization of the input fields
        self.name_input = InputField("Name", 300, 200, 200, 30)
        self.email_input = InputField("Email", 300, 250, 200, 30)
        self.password_input = InputField("Password", 300, 300, 200, 30)

        # Initialization of the registration button
        self.register_button = Button("Register", 300, 350, 200, 50, (0, 0, 255), (0, 0, 200))

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.register_button.is_hover(pygame.mouse.get_pos()):
                        # Action to perform when the user clicks on the register button
                        name = self.name_input.get_text()
                        email = self.email_input.get_text()
                        password = self.password_input.get_text()

                        # Validate the registration information
                        if self.validate_registration(name, email, password):
                            # Register the user
                            self.register_user(name, email, password)
                            # Go to the main interface
                            running = False
                            MainInterface().run()
                        else:
                            # Display an error message if the registration information is invalid
                            print("Invalid registration information")

            # Handle keyboard input for the input fields
            self.name_input.handle_event(event)
            self.email_input.handle_event(event)
            self.password_input.handle_event(event)

            # Draw the input fields and button
            self.screen.fill((255, 255, 255))
            self.name_input.draw(self.screen)
            self.email_input.draw(self.screen)
            self.password_input.draw(self.screen)
            self.register_button.draw(self.screen)
            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()

    def validate_registration(self, name, email, password):
        # Validate the registration information
        if len(name) < 2 or not re.match(r"[^@]+@[^@]+\.[^@]+", email) or len(password) < 8:
            return False
        return True

    def register_user(self, name, email, password):
        # Register the user (you need to implement this)
        print("User registered successfully")

class MainInterface:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Main Interface")
        self.clock = pygame.time.Clock()

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            # Draw the main interface
            self.screen.fill((255, 255, 255))
            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()

if __name__ == "__main__":
    RegistrationInterface().run()
