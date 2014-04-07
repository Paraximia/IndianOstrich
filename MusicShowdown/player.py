import pygame

class Player(pygame.sprite.Sprite):
	def __init__(self, imagepath, playerW, playerH):
		pygame.sprite.Sprite.__init__(self)
		self.sheet = pygame.image.load(imagepath)
		self.playerW = playerW
		self.playerH = playerH

		#initial image
		self.sheet.set_clip( pygame.Rect(0, 0, playerW, playerH) )
		self.image = self.sheet.subsurface( self.sheet.get_clip() )
		self.rect = self.image.get_rect()

		#velocitites
		self.xVel = 0
		self.yVel = 0

		#left = l or right = r
		self.status = 'r'
		
		#current frame
		self.frame = 0
		self.leftWalk = []
		self.rightWalk = []
		self.getClips()

	def update(self):
		#if it's moving left 
		if( self.xVel < 0 ):
			#change status to left
			self.status = 'l'
			#go to next frame
			self.frame += 1
		elif( self.xVel > 0 ):
			#change status to right
			self.status = 'r'
			#go to next frame
			self.frame +=1
		#if standing
		else:
			#reset the animation
			self.frame = 0
		#looping
		if( self.frame >= 3):
			self.frame = 0

		#check status and change image
		if( self.status == 'r' ):
			self.image = self.rightWalk[self.frame]
			self.rect = self.image.get_rect()
		elif( self.status == 'l' ):
			self.image = self.leftWalk[self.frame]
			self.rect = self.image.get_rect()
		self.move()

	def move(self):
		self.rect.x += self.xVel
		self.rect.y += self.yVel

	def getClips(self):
		#all the rightwalks
		self.sheet.set_clip( pygame.Rect(0, 0, self.playerW, self.playerH) )
		self.rightWalk.append( self.sheet.subsurface(self.sheet.get_clip()) )

		self.sheet.set_clip( pygame.Rect( self.playerW, 0, self.playerW, self.playerH) )
		self.rightWalk.append( self.sheet.subsurface(self.sheet.get_clip()) )

		self.sheet.set_clip( pygame.Rect( self.playerW*2, 0, self.playerW, self.playerH) )
		self.rightWalk.append( self.sheet.subsurface(self.sheet.get_clip()) )

		#4th animation
		#self.sheet.set_clip( pygame.Rect( self.playerW*3, 0, self.playerW, self.playerH) )
		#self.rightWalk.append( self.sheet.subsurface(self.sheet.get_clip()) )


		#get all the leftwalks
		self.sheet.set_clip( pygame.Rect(0, self.playerH, self.playerW, self.playerH) )
		self.leftWalk.append( self.sheet.subsurface(self.sheet.get_clip()) )

		self.sheet.set_clip( pygame.Rect( self.playerW, self.playerH, self.playerW, self.playerH) )
		self.leftWalk.append( self.sheet.subsurface(self.sheet.get_clip()) )

		self.sheet.set_clip( pygame.Rect( self.playerW*2, self.playerH, self.playerW, self.playerH) )
		self.leftWalk.append( self.sheet.subsurface(self.sheet.get_clip()) )

		#4th animation
		#self.sheet.set_clip( pygame.Rect( self.playerW*3, self.playerH, self.playerW, self.playerH) )
		#self.leftWalk.append( self.sheet.subsurface(self.sheet.get_clip()) )




	def handleInput(self, event):
		#deal with left events
		if( event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT ):
			self.xVel -= self.rect.w/8
		elif( event.type == pygame.KEYUP and event.key == pygame.K_LEFT ):
			self.xVel += self.rect.w/8

		#deal with right events
		if( event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT ):
			self.xVel += self.rect.w/8
		elif( event.type == pygame.KEYUP and event.key == pygame.K_RIGHT ):
			self.xVel -= self.rect.w/8

		#deal with up events
		if( event.type == pygame.KEYDOWN and event.key == pygame.K_UP ):
			self.yVel -= self.rect.w/8
		elif( event.type == pygame.KEYUP and event.key == pygame.K_UP ):
			self.yVel += self.rect.w/8

		#deal with down events
		if( event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN ):
			self.yVel += self.rect.w/8
		elif( event.type == pygame.KEYUP and event.key == pygame.K_DOWN ):
			self.yVel -= self.rect.w/8