import pygame
import os
from pygame import mixer
from pygame.locals import *

WIDTH, HEIGHT = 900,500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Spartakus:Storm of the November Days")

#orginala bild dimensions men +1 på båda
coolSpaceShipWidth, coolSpaceShipHeight = 274,132

coolSpaceShipImage =pygame.image.load(
os.path.join('Assets', 'spaceshipPygame.JPG'))
coolSpaceShip = pygame.transform.rotate(pygame.transform.scale(
coolSpaceShipImage, (coolSpaceShipWidth,coolSpaceShipHeight)),90)

mixer.init()
mixer.music.load('assets/Spaceship.wav')
mixer.music.play()

VEL = 5

def draw_window(spaceship):
    white = (255,255,255)   

    #WIN.FILL((R,G,B)) - kan använda tuples som input
    WIN.fill((white))

    #måste komma efter vi fyller skärmen med bakgrunds!
    WIN.blit(coolSpaceShip,(spaceship.x,spaceship.y))

    #OBS pygame behöver uppdatera för att visa detta!
    pygame.display.update()

def spaceship_handle_movement(keysPressed, spaceship):
    #tar hand om rymdraketens rörelse
    if keysPressed[pygame.K_LEFT]: 
        spaceship.x -= VEL
    if keysPressed[pygame.K_RIGHT]: 
        spaceship.x += VEL
    if keysPressed[pygame.K_UP]: 
        spaceship.y -= VEL
    if keysPressed[pygame.K_DOWN]: 
        spaceship.y += VEL

def main():
    #frames per second
    FPS = 60
    #kollar om spellet spelas
    gameRunning = True

    #clock object som tar hand om tid inom pygame
    clock = pygame.time.Clock()

    #position av rymdskeppet - rect betyder rectangle av rymdskeppet
    spaceship = pygame.Rect(100,100, coolSpaceShipWidth, coolSpaceShipHeight)

    #events in the game - vår gameplay loop
    while gameRunning:
        #kallar till clock objektet som är några rader övanpå här
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                #lol glöm inte ändra denna också
                gameRunning = False

        keysPressed = pygame.key.get_pressed()
        spaceship_handle_movement(keysPressed, spaceship)

        draw_window(spaceship)
        
    pygame.quit()

#Om namnet på filen är main så kör vi filen
if __name__ == "__main__":
    main()