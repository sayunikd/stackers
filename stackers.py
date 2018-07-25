from sense_hat import SenseHat
from pygame.locals import *
import pygame
import random
import time
sense=SenseHat()
sense.clear()

class stack():		
	def __init__(self):
		pygame.init()
		pygame.display.set_mode((640, 480))
		self.gaming=True
	def startGame(self):
		row=0
		pygame.time.set_timer(USEREVENT +1, 200)
		while self.gaming:
			for event in pygame.event.get():
				if event.type == KEYDOWN:
					sense.set_pixel (row, 0, (0,0,255))
					self.gaming=False
				else:			
					sense.set_pixel(row,0, (0,0,255))
					time.sleep(0.2)
					sense.set_pixel (row,0, (0,0,0))
					row=(row+1)%8
				
if __name__ == "__main__":
	try:
		game = stack ()
		game.startGame()
	except KeyboardInterrupt:
		sense.clear()
		self.gaming=False
