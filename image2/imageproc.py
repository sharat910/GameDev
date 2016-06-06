import pygame,sys

lena = pygame.image.load("lena.bmp")
screen = pygame.display.set_mode((lena.get_width(),lena.get_height()))

lenaPixelArray = pygame.PixelArray(lena)

while True:
	#Exit Loop
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()

	#ImageProcessing
	for x in range(0,lena.get_height()):
		for y in range(0,lena.get_width()):
			#screen.fill(lenaPixelArray[x,y])
			pixel = lenaPixelArray[x,y]
			if pixel > 0x444444:
				lenaPixelArray[x,y] = 0xFFFFFF
	screen.blit(lenaPixelArray.make_surface(),(0,0))
	pygame.display.flip()
	#Rendering
	#screen.blit(pygame.transform.laplacian(lena),(0,0))
	# screen.fill(pygame.transform.average_color(lena))
	# pygame.display.flip()