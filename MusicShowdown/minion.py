import pygame

class Minion(pygame.sprite.Sprite):
	def __init__(self, imagepath):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load(imagepath)
		self.rect = self.image.get_rect()
		self.xVel = 0
		self.yVel = 0

	def update(self, Player player):
		self.chase(player)
		self.move()

	def move(self):
		self.rect.x += self.xVel
		self.rect.y += self.yVel

	def chase(self, Player player):
		if (player.x < self.x):
			self.xVel -= self.rect.w/4
		elif(player.x > self.x):
			self.xVel += self.rect.w/4