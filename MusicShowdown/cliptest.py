import pygame

pygame.init()

screen = pygame.display.set_mode((800, 640))

screen.fill(pygame.Color(255,255,255))

sheet = pygame.image.load('data/player.png')
clock = pygame.time.Clock()
running = True

while running:
	clock.tick(9)
	for event in pygame.event.get():
		if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
			running = False
	sheet.set_clip( pygame.Rect(0, 0, 384, 192) )
	screen.blit( sheet, (192,384) )