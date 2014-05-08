import pygame
#game imports
from player import Player
from minion import Minion
from boobs import Boobs
from prop import Prop
from random import randint
from mackle import Mackle 
from dialogue import Dialogue

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
	minion4 = Boobs("data/boobs.png", BG_WIDTH, BG_HEIGHT, spawnPoint=pygame.Rect(9200, floorSpawn.y, 0, 0))
	minion5 = Boobs("data/boobs.png", BG_WIDTH, BG_HEIGHT, spawnPoint=pygame.Rect(9700, floorSpawn.y, 0, 0))
	minion6 = Boobs("data/boobs.png", BG_WIDTH, BG_HEIGHT, spawnPoint=pygame.Rect(10300, floorSpawn.y, 0, 0))
	#minion list
	minions = [minion1, minion2, minion3, minion4, minion5, minion6]
	#macklemore
	mackle = Mackle("data/boo.png", BG_WIDTH, BG_HEIGHT, spawnPoint=pygame.Rect(13000,floorSpawn.y,0,0))

	#initialize prop objects here
	upPipe = Prop("data/uppipe.png", BG_WIDTH, BG_HEIGHT, pygame.Rect(5640, 700, 0, 0))
	downPipe = Prop("data/downpipe.png", BG_WIDTH, BG_HEIGHT, pygame.Rect(5640, 0, 0, 0))

	upPipe2 = Prop("data/uppipe.png", BG_WIDTH, BG_HEIGHT, pygame.Rect(6200, 700, 0, 0))
	downPipe2 = Prop("data/downpipe.png", BG_WIDTH, BG_HEIGHT, pygame.Rect(6200, 0, 0, 0))

	upPipe3 = Prop("data/uppipe.png", BG_WIDTH, BG_HEIGHT, pygame.Rect(6450, 700, 0, 0))
	downPipe3 = Prop("data/downpipe.png", BG_WIDTH, BG_HEIGHT, pygame.Rect(6450, 0, 0, 0))

	upPipe4 = Prop("data/uppipe.png", BG_WIDTH, BG_HEIGHT, pygame.Rect(6700, 700, 0, 0))
	downPipe4 = Prop("data/downpipe.png", BG_WIDTH, BG_HEIGHT, pygame.Rect(6700, 0, 0, 0))


	#prop list
	pipes = [upPipe, downPipe, upPipe2, downPipe2, upPipe3, downPipe3, upPipe4, downPipe4]

	#renders all the sprites
	playersprite = pygame.sprite.RenderPlain(player)
	minionsprites = pygame.sprite.RenderPlain(minions)
	floorsprite = pygame.sprite.RenderPlain(floor)
	macklesprite = pygame.sprite.RenderPlain(mackle)
	pipesprites = pygame.sprite.RenderPlain(pipes)



	#initialise clock
	clock = pygame.time.Clock()

	screen.fill(pygame.Color(0,0,0))

	#dialogue setup
	scene1Text = [Dialogue("Player: What the f**k are you guys doing?", pygame.mixer.Sound("data/lines/playerLine1.ogg")),
	Dialogue("Devs: Uhh......", pygame.mixer.Sound("data/lines/playerLine4.ogg")),
	Dialogue("Player: You're supposed to be making a game!", pygame.mixer.Sound("data/lines/playerLine2.ogg")),
	Dialogue("Devs: OH SHIT!",pygame.mixer.Sound("data/lines/playerLine4.ogg")),
	Dialogue("Surya: Guys, let's rewrite the whole thing", pygame.mixer.Sound("data/lines/suryaLine1.ogg")),
	Dialogue("John: Yeah! How's this?", pygame.mixer.Sound("data/lines/johnLine1.ogg")) ]
	scene1Count = 0

	#scene2
	scene2Text = [ Dialogue("Austin: We can't do this! Don't be idiots", pygame.mixer.Sound("data/lines/austinLine1.ogg")),
	Dialogue("Surya: I promised them music features!", pygame.mixer.Sound("data/lines/suryaLine2.ogg")),
	Dialogue("Surya: We NEED music features!", pygame.mixer.Sound("data/lines/suryaLine3.ogg")),
	Dialogue("Surya: We NEED music features!", pygame.mixer.Sound("data/music/shmashup.ogg")),
	Dialogue("James: These aren't music features!", pygame.mixer.Sound("data/lines/jamesLine1.ogg")),
	Dialogue("John: Let's just... Give the player some boobs?", pygame.mixer.Sound("data/lines/johnLine2.ogg")), 
	Dialogue("James: People like boobs!", pygame.mixer.Sound("data/lines/jamesLine2.ogg"))
	]
	scene2Count = 0

	#scene3
	scene3Text = [ Dialogue("Player: ???", pygame.mixer.Sound("data/lines/playerLine3.ogg")),
	Dialogue("John: I gave you boobs, leave us alone.", pygame.mixer.Sound("data/lines/johnLine3.ogg")),
	Dialogue("Player: Your ideas are bad and you should feel bad.", pygame.mixer.Sound("data/lines/playerLine4.ogg")),
	Dialogue("James: He's right, This is awful!", pygame.mixer.Sound("data/music/jamesLine3.ogg")),
	Dialogue("James: Just do a boss fight instead!", pygame.mixer.Sound("data/lines/jamesLine4.ogg")),
	]
	scene3Count = 0

	scene4Text = [Dialogue("Austin: Dude... He's walking backwards", pygame.mixer.Sound("data/lines/austinLine3.ogg")), 
	Dialogue("John: Screw it! There's no time!", pygame.mixer.Sound("data/lines/johnLine4.ogg"))
	]
	scene4Count = 0

	#setup sound effects
	flappyStart = pygame.mixer.Sound('data/music/flappyEffect.ogg')
	flappyCoin = pygame.mixer.Sound('data/music/flappyCoin.ogg')
	flappyDeath = pygame.mixer.Sound('data/music/flappyDeath.ogg')
	flappyFlap = pygame.mixer.Sound('data/music/flappyFlap.ogg')
	effects = []
	effects.append(pygame.mixer.Sound('data/music/99c.ogg'))
	effects.append(pygame.mixer.Sound('data/music/brand.ogg'))

	#play music
	#pygame.mixer.music.play(start=3)
	#kills on thriftshop
	thriftkills = 0
	#kills for tdfw
	tdfwkills = 0
	tdfwplaying = False
	mackleFight = False

	#font for health and other stupid stuff we write
	pygame.font.init()
	myfont = pygame.font.SysFont("monospace", 20)

	running = True
	while running:
		#print player.rect.x
		if( pygame.mixer.music.get_pos() >= 5000 and thriftkills == 0 and not tdfwplaying):
			pygame.mixer.music.play(start=3)

		if( pygame.mixer.music.get_pos() >= 12534 and tdfwkills == 0 and tdfwplaying ):
			pygame.mixer.music.play(start=0.225)

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
				#if tdfw playing and mini not hit
				if (((coll.rect.x > player.rect.x and player.status == 'r') or (coll.rect.x < player.rect.x and player.status == 'l'))
				 and player.attack == 'a' and tdfwplaying and coll.hit == 0):
					coll.hit = 1
					tdfwkills += 1
					#kick in the beat if the player gets his first kill
					if( tdfwkills == 1):
						pygame.mixer.music.play(-1, 18)

				#if the player is attacking it and it's in front and tdfw  playing and mini hit
				elif (((coll.rect.x > player.rect.x and player.status == 'r') or (coll.rect.x < player.rect.x and player.status == 'l')) and 
				player.attack == 'a' and tdfwplaying and coll.hit == 1):
					player.health += 10
					#remove it -- TODO HEALTH
					minionsprites.remove(playerMinionColls[0])

				#kill the minion if the player is attacking it and it's in front and tdfw not playing
				elif (((coll.rect.x > player.rect.x and player.status == 'r') or (coll.rect.x < player.rect.x and player.status == 'l')) and 
				player.attack == 'a' and not tdfwplaying):
					player.health += 10
					#remove it -- TODO HEALTH
					minionsprites.remove(playerMinionColls[0])
					thriftkills += 1
					#kick in the beat if the player gets his first kill
					if( thriftkills == 1):
						pygame.mixer.music.play(-1, 43.5)
				
				#take away from the player's health otherwise
				elif(player.health > 0):
					player.health -= 5
				elif(player.health <= 0):
					if( tdfwplaying ):
						playersprite.sprites()[0].rect.x = 8500
					if( mackleFight ):
						playersprite.sprites()[0].rect.x = 12800
					else:
						playersprite.sprites()[0].rect.x = 0
					player.health = 100
		playerMackleColls = ( pygame.sprite.spritecollide(playersprite.sprites()[0], macklesprite, False) )
		if( playerMackleColls):
			if (((macklesprite.sprites()[0].rect.x > player.rect.x and player.status == 'r') or (macklesprite.sprites()[0].rect.x < player.rect.x and player.status == 'l'))
				 and player.attack == 'a'):
				macklesprite.sprites()[0].health -= 5
				if(macklesprite.sprites()[0].health <= 0):
					macklesprite.remove(macklesprite.sprites()[0])
			elif(player.health > 0):
				player.health -= 5
			elif(player.health <= 0):
				playersprite.sprites()[0].rect.x = 12800
				player.health = 100 



		#debug
		if(event.type == pygame.KEYDOWN and event.key == pygame.K_f):
			player.rect.x = 11000
		if(event.type == pygame.KEYDOWN and event.key == pygame.K_s):
			player.rect.x = 7300
		if(event.type == pygame.KEYDOWN and event.key == pygame.K_d):
			player.rect.x = 3072
		#cutscene1
		if( player.rect.x >= 3072 and player.rect.x <= 4080 and scene1Count < len(scene1Text)):
			pygame.mixer.music.stop()
			#where the text shows up
			textPos = pygame.Rect(player.rect.x, player.rect.y - 500, 0,0)
			#textbox
			textbox = pygame.Surface((600, 100), flags=0)
			#loop through the dialogue
			text = myfont.render(scene1Text[scene1Count].text, 1, (255,255,0))
			if( not pygame.mixer.get_busy() and not scene1Text[scene1Count].played):
				scene1Text[scene1Count].sound.play()
				scene1Text[scene1Count].played = True

			if(event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE):
				scene1Count += 1
			#blit the textbox and the text
			screen.blit(textbox, (textPos.x - camera.x, textPos.y - camera.y))
			screen.blit(text, (textPos.x - camera.x, textPos.y - camera.y))
			#start the flappy bird
			if( scene1Count == 6):
				flappyStart.play()
				player.rect.x = 5088
				player.rect.y = 500

		#FLAPPYBIRDSCENE
		if( player.rect.x >= 5088 and player.rect.x <= 7200):
			player.jumping = True
			#kill player if he hits the floor or touches pipe
			playerPipeColls = ( pygame.sprite.spritecollide(playersprite.sprites()[0], pipesprites, False) )
			if( playerFloorColls or playerPipeColls):
				flappyDeath.play()
				player.rect.x = 5088
				player.rect.y = 500

			#let player jump around and shitz
			if(event.type == pygame.KEYDOWN and event.key == pygame.K_UP):
				flappyFlap.play()
				player.yVel -= 16
				print player.rect.y

			if((player.rect.x >= 5544 and player.rect.x <= 5568) or 
				(player.rect.x >= 6200 and player.rect.x <= 6220) or 
				(player.rect.x >= 6450 and player.rect.x <= 6470) or 
				(player.rect.x >= 6700 and player.rect.x <= 6720)):
				flappyCoin.play()
			#cap the height--broken af
			if( player.rect.y < 100 ):
				player.rect.y == 100

		#BOOBSSCENE
		#move the player over
		if(player.rect.x >= 6900 and player.rect.x <= 7400):
			player.rect.x = 8500
			pygame.mixer.music.stop()
			scene2Text[0].sound.play()
			scene2Text[0].played = True

		#cutscene2
		if(player.rect.x >= 8500 and player.rect.x <= 8700 and scene2Count < len(scene2Text)):
			pygame.mixer.music.stop()
			#where the text shows up
			textPos = pygame.Rect(player.rect.x, player.rect.y - 500, 0,0)
			#textbox
			textbox = pygame.Surface((600, 100), flags=0)
			#loop through the dialogue
			text = myfont.render(scene2Text[scene2Count].text, 1, (255,255,0))
			if( not pygame.mixer.get_busy() and not scene2Text[scene2Count].played):
				scene2Text[scene2Count].sound.play()
				scene2Text[scene2Count].played = True

			if(event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE):
				scene2Count += 1
			#blit the textbox and the text
			screen.blit(textbox, (textPos.x - camera.x, textPos.y - camera.y))
			screen.blit(text, (textPos.x - camera.x, textPos.y - camera.y))

			if( scene2Count == 4 and not scene2Text[4].played):
				pygame.mixer.stop()
				scene2Text[4].sound.play()
				scene2Text[4].played = True
		elif scene2Text[6].played and not tdfwplaying:
			pygame.mixer.music.load("data/music/tdfw.ogg")
			pygame.mixer.music.play(start=0.225)
			tdfwplaying = True

		#cutscene3
		if(player.rect.x >= 11000 and player.rect.x <= 12500 and scene3Count < len(scene3Text)):
			pygame.mixer.music.stop()
			#where the text shows up
			textPos = pygame.Rect(player.rect.x, player.rect.y - 500, 0,0)
			#textbox
			textbox = pygame.Surface((600, 100), flags=0)
			#loop through the dialogue
			text = myfont.render(scene3Text[scene3Count].text, 1, (255,255,0))
			if( not pygame.mixer.get_busy() and not scene3Text[scene3Count].played):
				scene3Text[scene3Count].sound.play()
				scene3Text[scene3Count].played = True

			if(event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE):
				scene3Count += 1

			if( scene3Text[4].played ):
				mackleFight = True
				player.rect.x = 12800
			#blit the textbox and the text
			screen.blit(textbox, (textPos.x - camera.x, textPos.y - camera.y))
			screen.blit(text, (textPos.x - camera.x, textPos.y - camera.y))


		playersprite.update()
		minionsprites.update(player)
		if(player.rect.x >= 12800):
			macklesprite.update(player)
		#draw sprites
		screen.blit(player.image, (player.rect.x - camera.x, player.rect.y - camera.y))
		if(mackle.health > 0):
			screen.blit(mackle.image, (mackle.rect.x - camera.x, mackle.rect.y - camera.y))
		
		for minion in minionsprites.sprites():
			screen.blit( minion.image, ( minion.rect.x - camera.x, minion.rect.y - camera.y))

		#render upPipes
		for pipe in pipesprites.sprites() :
			screen.blit(pipe.image, (pipe.rect.x - camera.x,pipe.rect.y - camera.y,0,0))

		label = myfont.render("Health:" + str(player.health), 1, (255,255,0))
		if( player.rect.x >= 12800 and mackle.health > 0):
			label2 = myfont.render("Macklemore Health:" + str(mackle.health), 1, (255,255,0))	
			screen.blit(label2, (SCREEN_WIDTH - label.get_rect().w - 250, 0))		
		screen.blit(label, (0,0))

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
