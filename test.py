import pygame
import pygame.mixer as mix
import time

#
# mix.pre_init(44100, -32, 2, 4096)
# pygame.init()


import pygame

import time

tic = time.time()

name2Sound = {}
playing_now = []
to_be_played = []
to_be_removed = []


def add_sample(name, sample_filename):
    name2Sound[name] = pygame.mixer.Sound(sample_filename)


def remove_sample(name):
    name2Sound.remove(name)


def play_sample(name):
    to_be_played.append(name)


def stop_sample(name):
    to_be_removed.append(name)


pygame.mixer.pre_init(44100, -16, 2, 4096)
# pygame.mixer.init()
pygame.init()

fenetre = pygame.display.set_mode((30,30))

add_sample("drums", "drums.wav")
add_sample("piano", "piano.wav")

play_sample("drums")

loop_duration = 3
total_time = 10
toc = time.time()

while toc - tic < total_time:
    loop_tic = loop_tac = time.time()
    if loop_tac - loop_tic < loop_duration:
        for sample in to_be_played:
            if sample in playing_now:
                print sample, "already being played"
            else:
                playing_now.append(sample)
                name2Sound[sample].play(loops=-1)
                print sample, "is now playing"
        to_be_played = []

        for sample in to_be_removed:
            if sample in playing_now:
                playing_now.remove(sample)
                name2Sound[sample].stop()
                print sample, "is now stopping"
            else:
                print sample, "is not being played"
        to_be_removed = []

    events = pygame.event.get()
    for event in events:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                play_sample("piano")
            if event.key == pygame.K_RIGHT:
                stop_sample("piano")

    toc = time.time()

pygame.quit()
