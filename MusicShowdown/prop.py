import pygame

class Prop(pygame.sprite.Sprite):
	def __init__(self, imagepath):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load(imagepath)
		self.rect = self.image.get_rect()
		self.xVel = 0
		self.yVel = 0