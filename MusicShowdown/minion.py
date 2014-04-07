import pygame

class Minion(pygame.sprite.Sprite):
	def __init__(self, imagepath):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load(imagepath)
		self.rect = self.image.get_rect()
		self.xVel = 0
		self.yVel = 0

	def update(self, player):
		self.chase(player)
		self.move()

	def move(self):
		self.rect.x += self.xVel
		self.rect.y += self.yVel

	def chase(self, player):
		if (player.rect.x < self.rect.x):
			self.xVel -= self.rect.w/4
		elif(player.rect.x > self.rect.x):
			self.xVel += self.rect.w/4