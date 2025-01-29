import pygame

class Player(pygame.Sprite.Sprite):
  def __init__(self, POS):
    super().__init__()
    self.image = pygame.image.load('../graphics/blue.png').convert_alpha()
    self.rect = self.image.get_react(midbottom = POS)
    