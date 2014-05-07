import pygame

class Player(pygame.sprite.Sprite):
	def __init__(self, imagepath, levelW, levelH, spawnPoint):
		pygame.sprite.Sprite.__init__(self)
		self.sheet = pygame.image.load(imagepath)
		self.playerW = 192/2
		self.playerH = 384/2
		self.levelW = levelW
		self.levelH = levelH

		#initial image
		self.sheet.set_clip(pygame.Rect(self.playerW*4, 0, self.playerW, self.playerH))
		self.image = self.sheet.subsurface( self.sheet.get_clip() )
		self.rect = self.image.get_rect()
		self.spawnPoint = spawnPoint
		self.rect.y = spawnPoint.y - self.playerH - 42
		#velocitites
		self.gravity = 4.5
		self.xVel = 0
		self.yVel = self.gravity
		self.xSpeed = self.rect.w/4
		self.ySpeed = 55

		#jump state
		self.jumping = False


		#attacking status 'n' = not, 'a' = attacking
		self.attack = 'n'
		self.health = 100

		#left = l or right = r
		self.status = 'r'

		#current frame
		self.frame = 0
		self.leftWalk = []
		self.rightWalk = []
		self.punch = []
		self.jumpA = []
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

		elif( self.status == 'l' ):
			self.image = self.leftWalk[self.frame]

		if( self.attack == 'a' and self.status == 'r'):
			self.image = self.punch[0]
			self.attack = 'n'

		elif( self.attack == 'a' and self.status == 'l'):
			self.image = self.punch[1]
			self.attack = 'n'

		if( self.jumping == True and self.status == 'l'):
			self.image = self.jumpA[0]

		if( self.jumping == True and self.status == 'r'):
			self.image = self.jumpA[1]

	def move(self):
		self.rect.x += self.xVel  

		#check if it's gone too far to the right or left
		if( (self.rect.x < 0 ) or (self.rect.x + self.rect.w > self.levelW) ):
			#move it back
			self.rect.x -= self.xVel

		if( self.jumping == True):
			self.rect.y += self.yVel
			self.yVel += self.gravity
			
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

		#get jump
		self.sheet.set_clip( pygame.Rect(self.playerW*3, self.playerH*2, self.playerW, self.playerH) )
		self.jumpA.append( self.sheet.subsurface(self.sheet.get_clip()) )

		self.sheet.set_clip( pygame.Rect(self.playerW*2, self.playerH*2, self.playerW, self.playerH) )
		self.jumpA.append( self.sheet.subsurface(self.sheet.get_clip()) )

		#get punch
		self.sheet.set_clip( pygame.Rect(0, self.playerH*2, self.playerW, self.playerH) )
		self.punch.append( self.sheet.subsurface(self.sheet.get_clip()) )

		self.sheet.set_clip( pygame.Rect(self.playerW, self.playerH*2, self.playerW, self.playerH) )
		self.punch.append( self.sheet.subsurface(self.sheet.get_clip()) )


	def handleInput(self, event):
		#deal with left events
		if( event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT ):
			self.xVel -= self.xSpeed
		elif( event.type == pygame.KEYUP and event.key == pygame.K_LEFT ):
			self.xVel += self.xSpeed

		#deal with right events
		if( event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT ):
			self.xVel += self.xSpeed
		elif( event.type == pygame.KEYUP and event.key == pygame.K_RIGHT ):
			self.xVel -= self.xSpeed

		#deal with up events
		if( (event.type == pygame.KEYDOWN and event.key == pygame.K_UP) and self.jumping == False):
			self.yVel -= self.ySpeed
			self.jumping = True

		#deal with attack events
		if (event.type == pygame.KEYDOWN and event.key == pygame.K_a):
			self.attack = 'a'
			self.frame = 0
