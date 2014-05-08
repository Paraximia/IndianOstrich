import pygame
#game imports
from player import Player
from minion import Minion
from prop import Prop
from random import randint
from mackle import Mackle 

import math

#constants  using caps and underscores to differentiate them from other vars
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

def main():
	pygame.init()

	#caption
	pygame.display.set_caption("This is a game we made, it's cool")

	#create screen
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	#setup music
	pygame.mixer.init()
	pygame.mixer.music.load("data/music/thrift.ogg")

	#make a floor sprite
	floorSpawn = pygame.Rect(0, BG_HEIGHT - 64, 0, 0)
	floor = Prop("data/floor.png", BG_WIDTH, BG_HEIGHT, spawnPoint=floorSpawn)

	#initialise sprite and render it
	player = Player("data/player.png", BG_WIDTH, BG_HEIGHT, spawnPoint=floorSpawn)
	setCamera(player)

	#initialize minion objects here
	minion1 = Minion("data/moo1.png", BG_WIDTH, BG_HEIGHT, spawnPoint=pygame.Rect(692, floorSpawn.y, 0, 0))
	minion2 = Minion("data/moo1.png", BG_WIDTH, BG_HEIGHT, spawnPoint=pygame.Rect(1500, floorSpawn.y, 0, 0))
	minion3 = Minion("data/moo1.png", BG_WIDTH, BG_HEIGHT, spawnPoint=pygame.Rect(2000, floorSpawn.y, 0, 0))
	#minion4 = Minion("data/moo1.png", BG_WIDTH, BG_HEIGHT, spawnPoint=pygame.Rect(2700, floorSpawn.y, 0, 0))
	#minion list
	minions = [minion1, minion2, minion3]
	#macklemore
	mackle = Mackle("data/boo.png", BG_WIDTH, BG_HEIGHT, spawnPoint=floorSpawn)

	#initialize prop objects here
	prop1 = Prop("data/poo.png", BG_WIDTH, BG_HEIGHT, pygame.Rect(1700, BG_WIDTH - 192 - 64, 0, 0))
	#prop list
	props = [prop1]

	#make pipes
	pipes = pygame.sprite.Sprite()
	pipes.image = pygame.image.load("data/Flappy Bird/FlappyBirdPipe1.png")


	#renders all the sprites
	playersprite = pygame.sprite.RenderPlain(player)
	minionsprites = pygame.sprite.RenderPlain(minions)
	propsprites = pygame.sprite.RenderPlain(props)
	floorsprite = pygame.sprite.RenderPlain(floor)
	macklesprite = pygame.sprite.RenderPlain(mackle)
	pipesprite = pygame.sprite.RenderPlain(pipes)



	#initialise clock
	clock = pygame.time.Clock()

	screen.fill(pygame.Color(0,0,0))

	#dialogue setup
	scene1Text = ["Player: What the fuck are you guys doing?",
	"Devs: Uhh......",
	"Player: You're supposed to be making a game!",
	"Devs: OH SHIT!",
	"Surya: Guys, let's rewrite the whole thing",
	"John: Yeah! How's this?" ]
	scene1Count = 0

	#scene2
	scene2Text = [ "Austin: We can't do this! Don't be idiots",
	"Surya: I promised them music features!",
	"Surya: We NEED music features!",
	"James: These aren't music features!"
	"John: Let's just... Give the player some boobs?", 
	"John: People like boobs!"
	]
	scene2Count = 0

	#setup sound effects
	effects = []
	effects.append(pygame.mixer.Sound('data/music/99c.ogg'))
	effects.append(pygame.mixer.Sound('data/music/brand.ogg'))

	#play music
	#pygame.mixer.music.play(start=3)
	kills = 0

	#font for health and other stupid stuff we write
	pygame.font.init()
	myfont = pygame.font.SysFont("monospace", 20)

	running = True
	while running:
		print player.rect.x
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

		#handle playerfloor collisions:
		playerFloorColls = (pygame.sprite.spritecollide(playersprite.sprites()[0], floorsprite, False))
		if( playerFloorColls ):
			player.jumping = False
			player.rect.y -= player.yVel
			player.frame = 0
			player.yVel = 0

		#get player-minion collisions
		playerMinionColls = ( pygame.sprite.spritecollide(playersprite.sprites()[0], minionsprites, False) )
		#if there are any
		if( playerMinionColls ):
			#check if player.x < minion.x
			for coll in playerMinionColls:
				#kill the minion if the player is attacking it and it's in front
				if coll.rect.x > player.rect.x and player.attack == 'a':
					player.health += 10
					#remove it -- TODO HEALTH
					minionsprites.remove(playerMinionColls[0])
					kills += 1
					#kick in the beat if the player gets his first kill
					if( kills == 1):
						pygame.mixer.music.play(-1, 43.5)
				#take away from the player's health otherwise
				elif(player.health > 0):
					player.health -= 5
					
					pygame.mixer.music.pause()
					effects[0].play()
				elif(player.health <= 0):
					playersprite.sprites()[0].rect.x = 0
					player.health = 100
		#debug
		if(event.type == pygame.KEYDOWN and event.key == pygame.K_s):
			player.rect.x = 3000
		#cutscene1
		if( player.rect.x >= 3072 and player.rect.x <= 4080):
			#where the text shows up
			textPos = pygame.Rect(player.rect.x, player.rect.y - 500, 0,0)
			#textbox
			textbox = pygame.Surface((600, 100), flags=0)
			#loop through the dialogue
			text = myfont.render(scene1Text[scene1Count], 1, (255,255,0))
			if(scene1Count < len(scene1Text) and (event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE)):
				scene1Count += 1
			#blit the textbox and the text
			screen.blit(textbox, (textPos.x - camera.x, textPos.y - camera.y))
			screen.blit(text, (textPos.x - camera.x, textPos.y - camera.y))
			#start the flappy bird
			if( scene1Count == 6):
				player.rect.x = 5088
				player.rect.y = 500

		#FLAPPYBIRDSCENE
		if( player.rect.x >= 5088 and player.rect.x <= 6500):
			player.jumping = True
			#kill player if he hits the floor
			if( playerFloorColls ):
				player.rect.x = 5088
				player.rect.y = 500
			#let player jump around and shitz
			if(event.type == pygame.KEYDOWN and event.key == pygame.K_UP):
				player.yVel -= 16
				print player.rect.y
			#cap the height--broken af
			if( player.rect.y < 100 ):
				player.rect.y == 100

		#BOOBSSCENE
		#move the player over
		if(player.rect.x >= 6000 and player.rect.x <= 7000):
			player.rect.x = 7300

		#dialogue
		if(player.rect.x >= 7300 and player.rect.x <= 7500):
			#where the text shows up
			textPos = pygame.Rect(player.rect.x, player.rect.y - 500, 0,0)
			#textbox
			textbox = pygame.Surface((600, 100), flags=0)
			#loop through the dialogue
			text = myfont.render(scene2Text[scene2Count], 1, (255,255,0))

			if(scene2Count < len(scene2Text) - 1 and (event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE)):
				scene2Count += 1
			#blit the textbox and the text
			screen.blit(textbox, (textPos.x - camera.x, textPos.y - camera.y))
			screen.blit(text, (textPos.x - camera.x, textPos.y - camera.y))

		playersprite.update()
		minionsprites.update(player)
		macklesprite.update(player)
		propsprites.update()
		#draw sprites
		screen.blit(player.image, (player.rect.x - camera.x, player.rect.y - camera.y))
		screen.blit(mackle.image, (mackle.rect.x - camera.x, mackle.rect.y - camera.y))
		
		for minion in minionsprites.sprites():
			screen.blit( minion.image, ( minion.rect.x - camera.x, minion.rect.y - camera.y))

		screen.blit(pipesprite.sprites()[0].image, (5200 - camera.x,200 - camera.y,0,0))
		label = myfont.render("Health:" + str(player.health), 1, (255,255,0))
		label2 = myfont.render("Macklemore Health:" + str(mackle.health), 1, (255,255,0))
		screen.blit(label, (0,0))
		screen.blit(label2, (SCREEN_WIDTH - label.get_rect().w - 250, 0))
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
