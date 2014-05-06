import pygame

class Mackle(pygame.sprite.Sprite):
	def __init__(self, imagepath, levelW, levelH, spawnPoint):
		pygame.sprite.Sprite.__init__(self)
		self.miniW = 192
		self.miniH = 256

		self.sheet = pygame.image.load(imagepath)
		self.sheet.set_clip( pygame.Rect(0, 0, self.miniW, self.miniH) )
		self.image = self.sheet.subsurface( self.sheet.get_clip() )

		self.rect = self.image.get_rect()

		self.spawnPoint = spawnPoint
		self.rect.x = spawnPoint
		self.rect.y = levelH - self.miniW - 64

		self.xVel = 0
		self.yVel = 0

		self.leftWalk = []
		self.rightWalk = []

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
		
		#if( self.xVel < 0 ):
			#change status to left
			#self.status = False
			#go to next frame
			#self.frame += 1
		#elif( self.xVel > 0 ):
			#change status to right
			#self.status = True
			#go to next frame
			#self.frame +=1
		#if standing
		#else:
			#reset the animation
			#self.frame = 0
		#looping
		if( self.frame >= 4):
			self.frame = 0

		#check status and change image
		if( self.status == True ):
			self.image = self.rightWalk[self.frame]
			#self.rect = self.image.get_rect()
		elif( self.status == False ):
			self.image = self.leftWalk[self.frame]

	def move(self):
		speed = 32
		if( self.rect.x + self.rect.w == self.spawnPoint + 768 or self.rect.x + self.rect.w == self.spawnPoint - 192 ):
			self.status = not self.status
		if( self.rect.x + self.rect.w > self.spawnPoint - 192 and self.status == False):
			self.xVel = -speed
			self.rect.x += self.xVel
			#print self.rect.x + self.rect.w
		if( self.rect.x + self.rect.w < self.spawnPoint + 768 and self.status == True):
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
		#all the rightwalks
		self.sheet.set_clip( pygame.Rect(0, 0, self.miniW, self.miniH) )
		self.rightWalk.append( self.sheet.subsurface(self.sheet.get_clip()) )

		self.sheet.set_clip( pygame.Rect( self.miniW, 0, self.miniW, self.miniH) )
		self.rightWalk.append( self.sheet.subsurface(self.sheet.get_clip()) )

		self.sheet.set_clip( pygame.Rect( self.miniW*2, 0, self.miniW, self.miniH) )
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
