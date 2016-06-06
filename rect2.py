import sys,pygame

'''

Movable Rectangle.
Use arrow keys.

'''

screen = pygame.display.set_mode((800,600))
screen.fill( (200,200,255) )

rect = pygame.Rect(400,300,60,40)
rectlast = (0,0,0,0)

clock =pygame.time.Clock()
lastTick = pygame.time.get_ticks()
totalTime = pygame.time.get_ticks()

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()

	#Process Player Input
	timeChange = pygame.time.get_ticks() -totalTime
	totalTime = pygame.time.get_ticks()
	vel = timeChange / 16

	up = pygame.key.get_pressed()[pygame.K_UP]
	down = pygame.key.get_pressed()[pygame.K_DOWN]
	right = pygame.key.get_pressed()[pygame.K_RIGHT]
	left = pygame.key.get_pressed()[pygame.K_LEFT]

	#Updating Game State Logic
	if up:
		rect.y += -3*vel
	if down:
		rect.y += +3*vel
	if right:
		rect.x += +3*vel
	if left:
		rect.x += -3*vel

	if rect.x<0:
		rect.x = 0
	if rect.y<0:
		rect.y = 0
	if rect.x > screen.get_width() - rect.width:
		rect.x = screen.get_width() - rect.width
	if rect.y > screen.get_height() - rect.height:
		rect.y = screen.get_height() - rect.height

	#Rendering	
	pygame.draw.rect(screen,(200,200,255),rectlast)
	pygame.draw.rect(screen,(255,255,255),rect)
	pygame.display.flip()
	clock.tick(60)
	rectlast = pygame.Rect(rect.x,rect.y,rect.width,rect.height)