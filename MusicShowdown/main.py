import pygame
from player import Player
from minion import Minion
from prop import Prop
from random import randint
from mackle import Mackle
import math

#constants -- using caps and underscores to differentiate them from other vars
#get the background
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 960
SCALEFACTOR = 1
bg = pygame.image.load("data/level1.png")
bg = pygame.transform.scale(bg, (bg.get_rect().w*SCALEFACTOR, bg.get_rect().h*SCALEFACTOR))
BG_WIDTH = bg.get_rect().w
BG_HEIGHT = bg.get_rect().h
#initialise the camera
camera = pygame.Rect(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT)
bullets_array = []

#this is gross as fucks
class Bullet(pygame.sprite.Sprite):
    def __init__(self, surface, x_coord, y_coord):
    	pygame.sprite.Sprite.__init__(self)
        self.image = surface
        self.rect = self.image.get_rect()
        self.rect.x = x_coord
        self.rect.y = y_coord
        return

    def update(self, x_amount=50):
        self.rect.x -= x_amount
        self.image.set_at((self.rect.x, self.rect.y),(255,255,255))
        return

def main():
	pygame.init()

	#caption
	pygame.display.set_caption("This is a game we made, it's cool")

	#create screen
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	#setup music
	pygame.mixer.init()
	pygame.mixer.music.load("data/thrift/thrift.ogg")

	#initialise sprites and render it
	player = Player("data/player.png", BG_WIDTH, BG_HEIGHT, scaleFactor=1)
	setCamera(player)

	#initialize minion objects here
	minion1 = Minion("data/moo.png", SCREEN_WIDTH, SCREEN_HEIGHT, spawnPoint=692)
	minion2 = Minion("data/moo.png", SCREEN_WIDTH, SCREEN_HEIGHT, spawnPoint=1500)
	minion3 = Minion("data/moo.png", SCREEN_WIDTH, SCREEN_HEIGHT, spawnPoint=2000)
	minion4 = Minion("data/moo.png", SCREEN_WIDTH, SCREEN_HEIGHT, spawnPoint=2700)
	#minion list
	minions = [minion1, minion2, minion3, minion4]

	#macklemore
	mackle = Mackle("data/boo.png", SCREEN_WIDTH, SCREEN_HEIGHT, spawnPoint=500)

	#initialize prop objects here
	prop1 = Prop("data/poo.png", SCREEN_WIDTH, SCREEN_HEIGHT, spawnPoint=2800)
	#prop list
	props = [prop1]

	bulletGross = Bullet(bg, 50000000, 50000000)
	#renders all the sprites
	playersprite = pygame.sprite.RenderPlain(player)
	minionsprites = pygame.sprite.RenderPlain(minions)
	macklesprite = pygame.sprite.RenderPlain(mackle)
	bulletGroup = pygame.sprite.RenderPlain(bulletGross)
	propsprites = pygame.sprite.RenderPlain(props)

	#initialise clock
	clock = pygame.time.Clock()

	screen.fill(pygame.Color(0,0,0))
	running = True
	#setup sound effects
	effects = []
	effects.append(pygame.mixer.Sound('data/thrift/99c.ogg'))
	effects.append(pygame.mixer.Sound('data/thrift/brand.ogg'))

	#play music
	pygame.mixer.music.play(start=3)
	kills = 0

	#font for health
	pygame.font.init()
	myfont = pygame.font.SysFont("monospace", 15)

	while running:
		if( player.rect.x - mackle.rect.x <= 200 and len(bullets_array) <= 6):
			bullets_array.append(Bullet(bg, mackle.rect.x, mackle.rect.y))
			#GROSS
			for bullet in bullets_array :
				bulletGroup.add(bullet)

		for bullet in bullets_array:
			bullet.update()

		if( pygame.mixer.music.get_pos() >= 5000 and kills == 0):
			pygame.mixer.music.play(start=3)

		if( not pygame.mixer.get_busy() ):
			pygame.mixer.music.unpause()

		clock.tick(9) #9 fps
		for event in pygame.event.get():
			if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
				running = False
			else:
				player.handleInput(event)
		setCamera(player)
		#draw bg
		bg.set_clip( pygame.Rect(camera.x, camera.y, SCREEN_WIDTH, SCREEN_HEIGHT) )
		screen.blit(bg.subsurface(bg.get_clip()), (0,0))
		#bullet player collisions
		bulletPlayerColls = pygame.sprite.groupcollide(playersprite, bulletGroup, False, True)
		#get player-minion collisions
		playerMinionColls = ( pygame.sprite.spritecollide(playersprite.sprites()[0], minionsprites, False) )
		#if there are any
		if( playerMinionColls ):
			#check if player.x < minion.x
			#todo--loop for all collisions
			if playerMinionColls[0].rect.x > player.rect.x and player.attack == 'a':
				minionsprites.remove(playerMinionColls[0])
				kills += 1
				if( kills == 1):
					pygame.mixer.music.play(-1, 43.5)
			elif(player.health > 0):
				player.health -= 5
				if(player.rect.x - 500 >= 0):
					player.rect.x -= 500
				else:
					player.rect.x = 0
				pygame.mixer.music.pause()
				effects[0].play()
			elif(player.health <= 0):
				playersprite.sprites()[0].rect.x = 0
				player.health = 100

		"""#get player-prop collisions
		playerPropColls = ( pygame.sprite.spritecollide(playersprite.sprites()[0], propsprites, False) )
		#if there are any
		if( playerPropColls ):
			#first checks if player is to the left of object
			if((player.rect.x + player.rect.w) > playerPropColls[0].rect.x and player.status == 'r' ):
				#checks if the player is still trying to move right
				if(player.xVel > 0):
					player.rect.x -= player.xVel
			#then checks if player is to the right of object
			elif(player.rect.x < (playerPropColls[0].rect.x + playerPropColls[0].rect.w) and player.status == 'l' ):
				#checks if the player is still trying to move left
				if(player.xVel < 0):
					player.rect.x -= player.xVel
			#lastly checks if player is above the object
			elif(player.rect.y >= playerPropColls[0].rect.y):
				#checks if the player is still falling
				if(player.yVel != 0):
					player.yVel = 0
					player.rect.y == playerPropColls[0].rect.h"""	

		playersprite.update()
		minionsprites.update(player)
		propsprites.update()
		macklesprite.update(player)
		#draw sprites
		screen.blit(player.image, (player.rect.x - camera.x, player.rect.y - camera.y))
		screen.blit(mackle.image, (mackle.rect.x - camera.x, mackle.rect.y - camera.y))
		for minion in minionsprites.sprites():
			screen.blit( minion.image, ( minion.rect.x - camera.x, minion.rect.y - camera.y))
		label = myfont.render("Health:" + str(player.health), 1, (255,255,0))
		screen.blit(label, (0,0))
		#for prop in propsprites.sprites():
			#screen.blit( prop.image, (prop.rect.x - camera.x, prop.rect.y - camera.y))
		pygame.display.flip()

def setCamera(player):
	#center it over player
	camera.x = (player.rect.x + player.rect.w/2) - (SCREEN_WIDTH/ 2)
	camera.y = (player.rect.y + player.rect.h/2)  - (SCREEN_HEIGHT/2)

	#keep it in bounds
	if( camera.x < 0 ):
		camera.x = 0

	if( camera.y < 0 ):
		camera.y = 0

	if( camera.x > BG_WIDTH - camera.w ):
		camera.x = BG_WIDTH - camera.w

	if( camera.y > BG_HEIGHT - camera.h ):
		camera.y = BG_HEIGHT - camera.h

#run the main function if this file is run
if __name__=="__main__":
	main()
