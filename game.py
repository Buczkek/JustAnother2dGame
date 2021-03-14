import pygame
from Config import Config

CONFIG = Config()
print(CONFIG["resolution"])
SCREEN = pygame.display.set_mode(list(map(int, CONFIG["resolution"].split('x'))))
