import pygame

pygame.init()
pygame.mixer.music.load('exe021_tocar_mp3.mp3')

pygame.mixer.music.play()

pygame.event.wait()
