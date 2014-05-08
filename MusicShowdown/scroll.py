import pygame
class Scrolling(pygame.sprite.Sprite):
	def __init__(self, imagepath, xVel, yVel, spawnPointX, spawnPointY):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load(imagepath)
		self.xVel = xVel
		self.yVel = yVel
		self.rect = self.image.get_rect()
		self.rect.x = spawnPointX
		self.rect.y = spawnPointY

	def update(self):
		self.rect.x += self.xVel
		self.rect.y += self.yVel