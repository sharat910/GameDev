import sys,pygame

screen = pygame.display.set_mode((800,600))

r = 0
rdir = 1

g = 0
gdir = 1

b = 0
bdir = 1

while True:
	g += 1 * gdir
	b += 2 * bdir
	r += 3 * rdir
	if r>=255:
		r = 255
		rdir = -1
	elif r<=0:
		r = 0
		rdir = 1
	if g>=255:
		g = 255
		gdir = -1
	elif g<=0:
		g = 0
		gdir = 1
	if b>=255:
		b = 255	
		bdir = -1
	elif b<=0:
		b = 0
		bdir = 1

	screen.fill((r,g,b))
	pygame.display.flip()

	pygame.time.delay(10)

