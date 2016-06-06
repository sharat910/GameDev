from gameobject import *
import pygame,sys

screen = pygame.display.set_mode((800,600))

gameObjects = []

bg = Background("Sinistar/Nebula1.bmp",screen.get_width(),screen.get_height())
gameObjects.append(bg)

player = Player("Sinistar/Hunter1.bmp",2,(25,1,23,23))
player_rot = pygame.transform.rotate(player.image,30)
gameObjects.append(player)

enemy = Enemy("Sinistar/SpacStor.bmp",2,(101,13,91,59))
gameObjects.append(enemy)

asteroid = Asteroid("Sinistar/Rock2a.bmp",1,(6,3,80,67))
gameObjects.append(asteroid)

for obj in gameObjects:	
	screen.blit(obj.image,(obj.rect.x,obj.rect.y))

pygame.display.flip()

#Exit Loop
while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
