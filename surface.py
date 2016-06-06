import pygame

screen = pygame.display.set_mode((800,600))
screen.fill((255,255,255))
while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
	
	newSurface = pygame.Surface((200,200))
	newSurface.set_colorkey((0,0,0))
	pygame.draw.circle(newSurface,(0,0,255),(100,100),100,4)
	screen.blit(newSurface,(400,300))
	pygame.display.flip()
