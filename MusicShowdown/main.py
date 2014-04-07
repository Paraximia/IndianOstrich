import pygame
from player import Player
from minion import Minion
from prop import Prop

#constants -- using caps and underscores to differentiate them from other vars
#get the background
bg = pygame.image.load("data/level1.png")
BG_WIDTH = bg.get_rect().w
BG_HEIGHT = bg.get_rect().h
#coordinates of where the ground is
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 320
PLAYERW = 64
PLAYERH = 128
#initialise the camera
camera = pygame.Rect(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT)

def main():
	pygame.init()

	#caption
	pygame.display.set_caption("This is a game we made, it's cool")

	#create screen
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

	#initialise sprites and render it
	player = Player("data/player.png", PLAYERW, PLAYERH, BG_WIDTH, BG_HEIGHT) 

	#initialize minion objects here
	minion1 = Minion("data/boo.png")
	#minion list
	minions = [minion1]

	#initialize prop objects here
	prop1 = Prop("data/poo.png")
	#prop list
	props = [prop1]

	#renders all the sprites
	playersprite = pygame.sprite.RenderPlain(player)
	minionsprites = pygame.sprite.RenderPlain(minions)
	propsprites = pygame.sprite.RenderPlain(props)

	#initialise clock
	clock = pygame.time.Clock()

	running = True
	while running:
		clock.tick(60) #60 fps
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
			else:
				player.handleInput(event)
		setCamera(player)
		#draw bg
		screen.fill(pygame.Color(255,255,255))
		bg.set_clip( pygame.Rect(camera.x, camera.y, SCREEN_WIDTH, SCREEN_HEIGHT) )
		screen.blit(bg.subsurface(bg.get_clip()), (0,0))
		#check for collisions
		#TODO COLLISION CHECK
		#update sprites
		playersprite.update()
		minionsprites.update(player)
		propsprites.update()
		#draw sprites
		screen.blit(player.image, (player.rect.x - camera.x, player.rect.y - camera.y))
		minionsprites.draw(screen)
		propsprites.draw(screen)
		pygame.display.flip()

def setCamera(player):
	#center it over player
	camera.x = ( player.rect.x + player.rect.w/ 2 ) - ( SCREEN_WIDTH/ 2 )
	camera.y = ( (player.rect.y + player.rect.h/2) - (SCREEN_HEIGHT/2) ) 

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