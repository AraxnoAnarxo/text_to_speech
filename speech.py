# Чтение вслух
import os
import re
import pygame
from pygame.locals import *
import sys
import datetime
import time
from gtts import gTTS

mp3_name = '1.mp3'

#
# Открываем файл с текстом
f = open('lera_poem_1.txt', "r")
ss = f.read()


# Эта строка отправляет текст для озвучивания гуглу
tts = gTTS(text=ss, lang='ru')
# Получаем от гугла озвученный текст в виде mp3
tts.save(mp3_name)

f.close()

# небольшая программа на pygame для озвучивания текста

pygame.init()
display_window = pygame.display.set_mode((400, 400), 0, 32)
pygame.display.set_caption('Poem 1 by Lera')
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
DARKGREEN = (0, 155, 0)
FPS = 60 # frame per second
basic_font = pygame.font.SysFont(None, 16)
text = basic_font.render('Play', True, WHITE, RED)
text_rect = text.get_rect()
text_rect.centerx = display_window.get_rect().centerx
text_rect.centery = display_window.get_rect().centery

# загружаем файл для озвучивания
pygame.mixer.music.load('1.mp3')
main_clock = pygame.time.Clock()
musicPlay = False

# кнопка для озвучивания
play_button = pygame.Rect(180, 180, 40, 40)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == MOUSEBUTTONUP: # если мышь кликает на кнопку, то:
            mousex, mousey = event.pos
            if play_button.collidepoint((mousex, mousey)):
                if musicPlay: # если аудио играет, то нажатие на кнопку приводит к stop
                    pygame.mixer.music.stop()
                    musicPlay = False
                else: # если аудио не играет, то нажатие на кнопку приводит к play
                    pygame.mixer.music.play(0, 0.0)
                    musicPlay = True


        display_window.fill(BLACK) # черный экран

        # рисуем кпонку play
        pygame.draw.polygon(display_window, DARKGREEN, ((172, 150), (260, 200), (172, 250)))
        pygame.draw.rect(display_window, RED, play_button)
        display_window.blit(text, text_rect)

        pygame.display.update()
        main_clock.tick(FPS)

