import pygame

class Prop(pygame.sprite.Sprite):
	def __init__(self, imagepath, levelW, levelH, spawnPoint):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load(imagepath)
		self.rect = self.image.get_rect()
		self.xVel = 0
		self.yVel = 0
		#self.kind = kind
		self.levelW = levelW
		self.levelH = levelH
		self.propW = self.rect.w
		self.propH = self.rect.h
		self.spawnPoint = spawnPoint

		self.rect.x = spawnPoint
		self.rect.y = levelH - self.propW - 64