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
				r = random.randint(0,255)
				g = random.randint(0,255)
				b = random.randint(0,255)
				sense.set_pixel(row,0, (r,g,b))
				time.sleep(0.2)
				sense.set_pixel (row,0, (0,0,0))
				row=(row+1)%8
if __name__ == "__main__":
	try:
		game = stack ()
		game.startGame()
	except KeyboardInterrupt:
		sense.clear()
