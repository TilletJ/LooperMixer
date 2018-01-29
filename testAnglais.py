# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""

import pygame
import pygame.event as ev
import pygame.mixer as mix
import os
import time
import numpy as np
from threading import Timer

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
COLORS = (RED, GREEN, BLUE)
BASS = ()
BRASS = (39, 74, 74)
DRUMS = (39, 74, 60)
FX = (39, 74, 48)
GUITAR = (44, 74, 39)
KEYS = (57, 74, 39)
PERCUSSIONS = (74, 39, 39)
SEQUENCES = (74, 39, 53)

COLORS_USED = [DRUMS, GUITAR, SEQUENCES]

color_index = 0
NB_BUTTONS = 5
loop_duration = 1.92
total_time = 10



class Bouton():
    def __init__(self, pos, size, sound_path, color):
        self.rect = pygame.Rect(pos, size)
        self.surf = pygame.Surface(self.rect.size)
        self.sound = mix.Sound(sound_path)
        self.isplaying = False
        self.color = 1.8*np.array(color)
        self.surf.fill(list(0.7*self.color))

    def toggle(self):
        if self.isplaying:
            self.sound.stop()
            self.surf.fill(list(0.8*self.color))
        else:
            self.sound.play(loops=-1)
            self.surf.fill(list(self.color))
        self.isplaying = not self.isplaying


if __name__=='__main__':
    mix.pre_init(frequency=44100, size=-16, channels=2, buffer=4096)
    
    pygame.init()

    width = 650
    height = 550

    fenetre = pygame.display.set_mode((width, height))
    image_fond = pygame.image.load("01_Colordrilos_-_DJ_Sliver.jpg")
    fond = image_fond.convert()
    fenetre.blit(fond,(0,0))

    print(mix.get_init())
   
    continuer = 1  # Variable de boucle

    listDir = []

    listDir.append(os.path.join("samples","Drums"))
    listDir.append(os.path.join("samples", "Bass"))
    listDir.append(os.path.join("samples", "Melodies"))
    
    buttons = []


    for i in range(len(listDir)):
        d = listDir[i]
        files = os.listdir(d)
        step = width/len(files)
        
        for j in range(len(files)) :
            try:
                file = files[j]
                pos = (step*j, 50*i)
                size = (step-2, 50-2)
                sound_path = os.path.join(d, file)
                buttons.append(Bouton(pos, size, sound_path, color=COLORS_USED[i]))
            except:
                pass


    start = time.time()
    while continuer:
        for event in ev.get():
            #Quitter
            if event.type == pygame.QUIT:
                continuer = 0
            elif event.type == pygame.MOUSEBUTTONUP:  # quand je relache le bouton
                if event.button == 1:  # 1= clique gauche
                    for button in buttons:
                        if button.rect.collidepoint(event.pos):
                            # Lancer le son
                            Timer(loop_duration-(time.time()-start)%loop_duration, button.toggle, ()).start()
                            break
    
    
        #fenetre.fill(0)  # On efface tout l'écran
        for button in buttons:
            fenetre.blit(button.surf, button.rect)
        pygame.display.flip()
    
    
    pygame.quit()
    
    
    
    
