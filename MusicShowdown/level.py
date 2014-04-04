import pygame, sys
from pygame.locals import *
from NusicShodown import character
from MusicShowdown import prop
from MusicShowdown import minion

class Level:
	def __init__(self, levelNum):
		filePath = 'data/level'+levelNum
		infile = open(filePath)
		self.levelSurfaceObject = pygame.image.load(infile.readline())
		self.character = character(infile.readline())
		
		curLine = infile.readline()
		self.minions = []
		while( curLine != '' ):
			minions.add(minion(curLine))
			curLine = infile.readline()

		self.objects = []
		curLine = infile.readline()
		while(curLine != ''):
			objects.add(prop(curLine))
		infile.close()
		
