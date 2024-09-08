import pygame, sys
from math import sin, cos

pygame.init()
screen = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()

Center = [400, 400, 20, 20]
rect = [100, 100, 50, 50]
deg = 0
diameter = 200
írd = -1
katt = 0
speed = 1

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if pygame.mouse.get_pos()[0] < Center[0]+Center[2]/2 and pygame.mouse.get_pos()[0] > Center[0]-Center[2]/2 and pygame.mouse.get_pos()[1] < Center[1]+Center[3]/2 and pygame.mouse.get_pos()[1] > Center[1]-Center[3]/2:
                    katt = 1
                    Center[0], Center[1] = pygame.mouse.get_pos()
            if event.button == 3:
                írd *= -1
            if event.button == 2:
                speed = 1
            if event.button == 5:
                speed -= 1
            if event.button == 4:
                speed += 1           
        if event.type == pygame.MOUSEMOTION:
            if katt == 1:
                Center[0], Center[1] = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONUP:
            katt = 0

    deg += speed
    if deg != 0:
        radian = 3.14159/180*deg
    else:
        radian = 0
    if -360 > deg or deg> 360:
        deg = 0
    sinus = sin(radian)
    cosinus = cos(radian)

    rect[0] = int(Center[0] + sinus*(diameter)-rect[2]/2)
    rect[1] = int(Center[1] + cosinus*(diameter)-rect[3]/2)
    screen.fill((25, 205, 240))
    pygame.draw.rect(screen, (255,0,0),(Center[0]-Center[2]/2, Center[1]-Center[3]/2, Center[2], Center[3]))
    pygame.draw.rect(screen, (0,0,0), rect)
    if írd == 1:
        screen.blit(pygame.font.SysFont("Arial", 24).render(f"Radián: {radian/3} pi", False, (0,0,0)), (20, 20))
        screen.blit(pygame.font.SysFont("Arial", 24).render(f"Fok: {deg}˚", False, (0,0,0)), (20, 40))
        screen.blit(pygame.font.SysFont("Arial", 24).render(f"Hely: {rect[0], rect[1]}", False, (0,0,0)), (20, 60))
        screen.blit(pygame.font.SysFont("Arial", 24).render(f"Sebesség: {speed}", False, (0,0,0)), (20, 80))
        screen.blit(pygame.font.SysFont("Arial", 24).render(f"Képkocka másodpercenként: {clock.get_fps()}", False, (0,0,0)), (20, 760))
        
    pygame.display.update()
    clock.tick(40)