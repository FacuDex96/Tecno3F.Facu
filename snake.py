import pygame, sys, time, random # type: ignore

speed = 14

#windows sizes

frame_size_x = 720
frame_size_y = 480

check_errors = pygame.init()

if(check_errors[1] > 0):
    print("Error" + check_errors[1])
else:
    print("Game Succesfully initialized")
    
    #initialise game window
    
    pygame.display.set.caption("Snake game")
    
    
    