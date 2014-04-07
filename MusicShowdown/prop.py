import pygame

class Prop(pygame.sprite.Sprite):
	def __init__(self, imagepath):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load(imagepath)
		self.rect = self.image.get_rect()
		self.rect.x = 2000
		self.xVel = 0
		self.yVel = 0