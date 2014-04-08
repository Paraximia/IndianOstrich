import pygame
class Bullet(pygame.sprite.Sprite):
	def __init__(self, player):
		pygame.sprite.Sprite.__init__(self)

		self.image = pygame.Surface([4, 10])
		self.image.fill(pygame.Color(0,0,0))

		self.rect = self.image.get_rect()
		self.rect.x = player.rect.x
		self.rect.y = player.rect.y

	def update(self):
		self.rect.x += 5