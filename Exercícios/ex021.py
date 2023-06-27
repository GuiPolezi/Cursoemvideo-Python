# Desafio 21 - Tocando um mp3

"""
Faça um programa em python que abra e reproduza o aúdio de um arquivo MP3.
"""

import pygame

# Inicializando o mixer Pygame
pygame.mixer.init()

# Iniciando o Pygame
pygame.init()

pygame.mixer.music.load('ex021.mp3')
pygame.mixer.music.play(loops=0, start=0.0)
pygame.event.wait()