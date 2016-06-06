import pygame,sys

def imageLoader(image,scale,clip):
	asset = pygame.image.load(image)
	surface = pygame.Surface((clip[2],clip[3]))
	surface.blit(asset,(0,0),clip)
	scaledAssetdim = (clip[2] * scale,clip[3] * scale)
	scaledAsset = pygame.transform.scale(surface,scaledAssetdim)
	return scaledAsset
