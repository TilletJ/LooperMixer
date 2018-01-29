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
from threading import Timer

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
COLORS = (RED, GREEN, BLUE)
color_index = 0
NB_BUTTONS = 5
loop_duration = 2
total_time = 10

 

class Bouton():
    def __init__(self, pos, size, sound_path):
        self.rect = pygame.Rect(pos, size)
        self.surf = pygame.Surface(self.rect.size)
        self.sound = mix.Sound(sound_path)
        self.isplaying = False
        self.surf.fill(RED)
       
    def toggle(self):
        if self.isplaying:
            self.sound.stop()
            self.surf.fill(RED)
        else:
            self.sound.play(loops=-1)
            self.surf.fill(GREEN)
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

    listDir.append(os.path.join("samples","drum"))
    listDir.appent(os.path.join("samples", "bass"))
    listDir.append(os.path.join("samples", "melody"))
    
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
                buttons.append(Bouton(pos, size, sound_path))
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
    
    
    
    
