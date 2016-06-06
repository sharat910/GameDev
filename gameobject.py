import pygame
from imgload import *

class Background(pygame.sprite.Sprite):
	
	def __init__(self,image,width,height):
		self.origAsset = pygame.image.load(image)
		self.image = pygame.transform.scale(self.origAsset,(width,height))
		self.rect = self.image.get_rect()

class Player(pygame.sprite.Sprite):
	def __init__(self,image,scale,clip):
		self.image = imageLoader(image,scale,clip)
		self.image.set_colorkey((0,0,0))
		self.rect = self.image.get_rect()
		self.rect.x = 400
		self.rect.y = 300

class Enemy(pygame.sprite.Sprite):
	def __init__(self,image,scale,clip):
		self.image = imageLoader(image,scale,clip)
		self.image.set_colorkey(0x454e5b)
		self.rect = self.image.get_rect()
		self.rect.x = 200
		self.rect.y = 500

class Asteroid(pygame.sprite.Sprite):
	def __init__(self,image,scale,clip):
		self.image = imageLoader(image,scale,clip)
		self.image.set_colorkey(0x454e5b)
		self.rect = self.image.get_rect()
		self.rect.x = 100
		self.rect.y = 400