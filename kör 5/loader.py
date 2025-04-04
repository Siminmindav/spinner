import pygame, os
pygame.init()

images = {}

for i in os.listdir("images"):
    path = os.path.join("images", i)
    key = os.path.splitext(i)[0]
    if i not in ["magyar.png", "english.png","espanyol.svg","performance.png"]:
        img = pygame.transform.scale(pygame.image.load(path), (50,50))
    elif i == "performance.png":
        img = pygame.transform.scale(pygame.image.load(path), (10,10))
    else:
        img = pygame.transform.scale(pygame.image.load(path),(300, 150))
    images[key] = img

for i in images:
    images[i].set_colorkey((240,240,240))
