# 021: Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.

import pygame
pygame.mixer.init()  # Inicializando o mixer PyGame

pygame.init()  # Iniciando o Pygame

pygame.mixer.music.load('ex01.mp3')
pygame.mixer.music.play()
pygame.event.wait()