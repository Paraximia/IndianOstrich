import pygame

class Player(pygame.sprite.Sprite):
	def __init__(self, imagepath):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load(imagepath)
		self.rect = self.image.get_rect()
		self.xVel = 0
		self.yVel = 0

	def update(self):
		self.move()

	def move(self):
		self.rect.x += self.xVel
		self.rect.y += self.yVel


	def handleInput(self, event):
		#deal with left events
		if( event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT ):
			self.xVel -= self.rect.w/4
		elif( event.type == pygame.KEYUP and event.key == pygame.K_LEFT ):
			self.xVel += self.rect.w/4

		#deal with right events
		if( event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT ):
			self.xVel += self.rect.w/4
		elif( event.type == pygame.KEYUP and event.key == pygame.K_RIGHT ):
			self.xVel -= self.rect.w/4

		#deal with up events
		if( event.type == pygame.KEYDOWN and event.key == pygame.K_UP ):
			self.yVel -= self.rect.w/4
		elif( event.type == pygame.KEYUP and event.key == pygame.K_UP ):
			self.yVel += self.rect.w/4

			#down events should be crouch not downward movement
			
		#deal with down events
		if( event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN ):
			self.yVel += self.rect.w/4
		elif( event.type == pygame.KEYUP and event.key == pygame.K_DOWN ):
			self.yVel -= self.rect.w/4