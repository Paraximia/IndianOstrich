import pygame

class Player(pygame.sprite.Sprite):
	def __init__(self, imagepath, levelW, levelH, scaleFactor):
		pygame.sprite.Sprite.__init__(self)
		self.sheet = pygame.image.load(imagepath)
		self.playerW = 192
		self.playerH = 384
		self.levelW = levelW
		self.levelH = levelH

		#initial image
		self.sheet.set_clip(pygame.Rect(self.playerW*4, 0, self.playerW, self.playerH))
		imageOrig = self.sheet.subsurface( self.sheet.get_clip() )
		self.image = pygame.transform.scale(imageOrig, (imageOrig.get_rect().w*scaleFactor,
			imageOrig.get_rect().h*scaleFactor))
		self.rect = self.image.get_rect()
		self.spawnPoint = (0, levelH - self.playerH - 64)
		self.rect.y = self.spawnPoint[1]
		#velocitites
		self.xVel = 0
		self.yVel = 0

		#jump state 
		self.onGround = True
		self.jumping = False
		self.gravity = 3

		#attacking status 'n' = not, 'a' = attacking
		self.attack = 'n'

		#left = l or right = r
		self.status = 'r'

		#current frame
		self.frame = 0
		self.leftWalk = []
		self.rightWalk = []
		self.getClips()

	def update(self):
		self.move()
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
		if( self.frame >= 5):
			self.frame = 0

		#check status and change image
		if( self.status == 'r' ):
			self.image = self.rightWalk[self.frame]
			#self.rect = self.image.get_rect()
		elif( self.status == 'l' ):
			self.image = self.leftWalk[self.frame]
			#self.rect = self.image.get_rect()

	def move(self):
		self.rect.x += self.xVel  

		#check if it's gone too far to the right or left
		if( (self.rect.x < 0 ) or (self.rect.x + self.rect.w > self.levelW) ):
			#move it back
			self.rect.x -= self.xVel

		if( self.jumping == True):
			if( self.rect.y + self.yVel < self.spawnPoint[1] ):
				self.rect.y += self.yVel
				self.yVel += self.gravity
				print self.yVel
			else:
				self.yVel = 0
				self.jumping = False
				self.onGround = True

	def getClips(self):
		#all the rightwalks
		self.sheet.set_clip( pygame.Rect( self.playerW*4, 0, self.playerW, self.playerH) )
		self.rightWalk.append( self.sheet.subsurface(self.sheet.get_clip()) )

		self.sheet.set_clip( pygame.Rect(0, 0, self.playerW, self.playerH) )
		self.rightWalk.append( self.sheet.subsurface(self.sheet.get_clip()) )

		self.sheet.set_clip( pygame.Rect( self.playerW, 0, self.playerW, self.playerH) )
		self.rightWalk.append( self.sheet.subsurface(self.sheet.get_clip()) )

		self.sheet.set_clip( pygame.Rect( self.playerW*2, 0, self.playerW, self.playerH) )
		self.rightWalk.append( self.sheet.subsurface(self.sheet.get_clip()) )
		
		self.sheet.set_clip( pygame.Rect( self.playerW*3, 0, self.playerW, self.playerH) )
		self.rightWalk.append( self.sheet.subsurface(self.sheet.get_clip()) )



		#get all the leftwalks
		self.sheet.set_clip( pygame.Rect( self.playerW*4, self.playerH, self.playerW, self.playerH) )
		self.leftWalk.append( self.sheet.subsurface(self.sheet.get_clip()) )

		self.sheet.set_clip( pygame.Rect(0, self.playerH, self.playerW, self.playerH) )
		self.leftWalk.append( self.sheet.subsurface(self.sheet.get_clip()) )

		self.sheet.set_clip( pygame.Rect( self.playerW, self.playerH, self.playerW, self.playerH) )
		self.leftWalk.append( self.sheet.subsurface(self.sheet.get_clip()) )

		self.sheet.set_clip( pygame.Rect( self.playerW*2, self.playerH, self.playerW, self.playerH) )
		self.leftWalk.append( self.sheet.subsurface(self.sheet.get_clip()) )
		
		self.sheet.set_clip( pygame.Rect( self.playerW*3, self.playerH, self.playerW, self.playerH) )
		self.leftWalk.append( self.sheet.subsurface(self.sheet.get_clip()) )


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
		if( (event.type == pygame.KEYDOWN and event.key == pygame.K_UP) and self.onGround == True and self.jumping == False):
			self.yVel -= 42
			self.jumping = True
			self.onGround = False

		#deal with attack events
		if (event.type == pygame.KEYDOWN and event.key == pygame.K_a):
			self.attack = 'a'
		if (event.type == pygame.KEYUP and event.key == pygame.K_a):
			self.attack = 'n'
