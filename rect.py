import sys,pygame

'''

Movable Rectangle.
Use arrow keys.

'''

screen = pygame.display.set_mode((800,600))
screen.fill((200,200,255))
pygame.display.flip()
rect = pygame.Rect(400,300,60,40)
pygame.draw.rect(screen,(255,255,255),rect)
pygame.display.flip()

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()

	#Process Player Input
	up = pygame.key.get_pressed()[pygame.K_UP]
	down = pygame.key.get_pressed()[pygame.K_DOWN]
	right = pygame.key.get_pressed()[pygame.K_RIGHT]
	left = pygame.key.get_pressed()[pygame.K_LEFT]

	#Updating Game State Logic
	if up:
		rect.y += -1
	if down:
		rect.y += +1
	if right:
		rect.x += +1
	if left:
		rect.x += -1

	if rect.x<0:
		rect.x = 0
	if rect.y<0:
		rect.y = 0
	if rect.x > screen.get_width() - rect.width:
		rect.x = screen.get_width() - rect.width
	if rect.y > screen.get_height() - rect.height:
		rect.y = screen.get_height() - rect.height

	#Rendering
	screen.fill((200,200,255))
	pygame.draw.rect(screen,(255,255,255),rect)
	pygame.display.flip()
