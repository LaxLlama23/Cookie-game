import pygame
pygame.init()

class Button:
    def __init__(self, x, y, image, scale=1):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def draw(self, suface):
        action = False
        pos = pygame.mouse.get_pos()
        suface.blit(self.image, (self.rect.x, self.rect.y))
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True
            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False
        return action

class Text:
    def __init__(self, font_path, font_size=33):
        self.font = pygame.font.Font(font_path, font_size)

    def draw(self, text, color, x, y, screen):
        img = self.font.render(text, True, color)
        screen.blit(img, (x, y))
