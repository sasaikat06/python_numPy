import pygame
from time import sleep

pygame.init()
window = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
pygame.mixer.init()
pygame.mixer.music.load("E:\Media\Audio\0465. Spring - AShamaluevMusic.mp3")
pygame.mixer.music.play()
sleep(5)
pygame.mixer.music.load("E:\Media\Audio\0475. Flowering - AShamaluevMusic.mp3")
pygame.mixer.music.play()
sleep(1)

image = pygame.image.load("E:\Media\Canva\Images\Landscape Motivational Desktop Background.png")
window.blit(image,(200,300))
pygame.display.update()
sleep(3)