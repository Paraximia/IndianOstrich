import pygame

class Boobs(pygame.sprite.Sprite):
	def __init__(self, imagepath, levelW, levelH, spawnPoint):
		pygame.sprite.Sprite.__init__(self)
		self.miniW = 96
		self.miniH = 192
		
		#health
		self.hit = 0
		
		self.sheet = pygame.image.load(imagepath)
		self.sheet.set_clip( pygame.Rect(0, 0, self.miniW, self.miniH) )
		self.image = self.sheet.subsurface( self.sheet.get_clip() )

		self.rect = self.image.get_rect()

		self.spawnPoint = spawnPoint

		self.rect.x = spawnPoint.x
		self.rect.y = spawnPoint.y - self.miniH - 42

		self.xVel = 0
		self.yVel = 0

		self.leftWalk = []
		self.rightWalk = []

		self.hitLeftWalk = []
		self.hitRightWalk = []

		self.getClips()

		self.frame = 0
		#true = right, false = left
		self.status = True

	def update(self, player):
		#self.chase(player)
		self.move()
		
		if (self.xVel != 0):
			self.frame += 1
		else:
			self.frame = 0
			
		#looping
		if( self.frame >= 4):
			self.frame = 0

		#check status and hit and change image
		if( self.status == True and self.hit == 0 ):
			self.image = self.rightWalk[self.frame]
			#self.rect = self.image.get_rect()
		elif( self.status == False and self.hit == 0 ):
			self.image = self.leftWalk[self.frame]

		#check status and hit and change image
		elif( self.status == True and self.hit == 1 ):
			self.image = self.hitRightWalk[self.frame]
			self.rect = self.image.get_rect()
		elif( self.status == False and self.hit == 1 ):
			self.image = self.hitLeftWalk[self.frame]

	def move(self):
		speed = 16
		if( self.rect.x + self.rect.w == self.spawnPoint.x + 768 or self.rect.x + self.rect.w == self.spawnPoint.x - 192 and self.hit == 0 ):
			self.status = not self.status
		if( self.rect.x + self.rect.w > self.spawnPoint.x - 192 and self.status == False and self.hit == 0):
			self.xVel = -speed
			self.rect.x += self.xVel
			#print self.rect.x + self.rect.w
		if( self.rect.x + self.rect.w < self.spawnPoint.x + 768 and self.status == True and self.hit == 0):
			self.xVel = speed
			self.rect.x += self.xVel

	"""def chase(self, player):
		if (player.rect.x - self.rect.x < 500):
			if (player.rect.x < self.rect.x):
				self.xVel = -self.rect.w/8
			elif(player.rect.x > self.rect.x):
				self.xVel = self.rect.w/8
			elif(player.rect.x == self.rect.x):
				self.xVel = 0
			#else:
				#give me out of vision minion code"""

	def getClips(self):
		#self.miniH *self.hit will jump the animation to the hit animation
		#all the rightwalks
		self.sheet.set_clip( pygame.Rect(0,0, self.miniW, self.miniH) )
		self.rightWalk.append( self.sheet.subsurface(self.sheet.get_clip()) )

		self.sheet.set_clip( pygame.Rect( self.miniW,0, self.miniW, self.miniH) )
		self.rightWalk.append( self.sheet.subsurface(self.sheet.get_clip()) )

		self.sheet.set_clip( pygame.Rect( self.miniW*2,0, self.miniW, self.miniH) )
		self.rightWalk.append( self.sheet.subsurface(self.sheet.get_clip()) )
		
		self.sheet.set_clip( pygame.Rect( self.miniW*3, 0, self.miniW, self.miniH) )
		self.rightWalk.append( self.sheet.subsurface(self.sheet.get_clip()) )


		#get all the leftwalks
		self.sheet.set_clip( pygame.Rect(0, self.miniH, self.miniW, self.miniH) )
		self.leftWalk.append( self.sheet.subsurface(self.sheet.get_clip()) )

		self.sheet.set_clip( pygame.Rect( self.miniW, self.miniH, self.miniW, self.miniH) )
		self.leftWalk.append( self.sheet.subsurface(self.sheet.get_clip()) )

		self.sheet.set_clip( pygame.Rect( self.miniW*2, self.miniH, self.miniW, self.miniH) )
		self.leftWalk.append( self.sheet.subsurface(self.sheet.get_clip()) )
		
		self.sheet.set_clip( pygame.Rect( self.miniW*3, self.miniH, self.miniW, self.miniH) )
		self.leftWalk.append( self.sheet.subsurface(self.sheet.get_clip()) )

		#right hitwalks
		self.sheet.set_clip( pygame.Rect(0,2*self.miniH, self.miniW, self.miniH) )
		self.hitRightWalk.append( self.sheet.subsurface(self.sheet.get_clip()) )

		self.sheet.set_clip( pygame.Rect( self.miniW,2*self.miniH, self.miniW, self.miniH) )
		self.hitRightWalk.append( self.sheet.subsurface(self.sheet.get_clip()) )

		self.sheet.set_clip( pygame.Rect( self.miniW*2,2*self.miniH, self.miniW, self.miniH) )
		self.hitRightWalk.append( self.sheet.subsurface(self.sheet.get_clip()) )
		
		self.sheet.set_clip( pygame.Rect( self.miniW*3, 2*self.miniH, self.miniW, self.miniH) )
		self.hitRightWalk.append( self.sheet.subsurface(self.sheet.get_clip()) )

		#left hitwalks
		self.sheet.set_clip( pygame.Rect(0, 3*self.miniH, self.miniW, self.miniH) )
		self.hitLeftWalk.append( self.sheet.subsurface(self.sheet.get_clip()) )

		self.sheet.set_clip( pygame.Rect( self.miniW, 3*self.miniH, self.miniW, self.miniH) )
		self.hitLeftWalk.append( self.sheet.subsurface(self.sheet.get_clip()) )

		self.sheet.set_clip( pygame.Rect( self.miniW*2, 3*self.miniH, self.miniW, self.miniH) )
		self.hitLeftWalk.append( self.sheet.subsurface(self.sheet.get_clip()) )
		
		self.sheet.set_clip( pygame.Rect( self.miniW*3, 3*self.miniH, self.miniW, self.miniH) )
		self.hitLeftWalk.append( self.sheet.subsurface(self.sheet.get_clip()) )
