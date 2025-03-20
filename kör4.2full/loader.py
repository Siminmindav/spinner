import pygame, os
pygame.init()

images = {}

for i in os.listdir("progrm/python/kör/images"):
    path = os.path.join("progrm/python/kör/images", i)
    key = os.path.splitext(i)[0]
    if i not in ["magyar.png", "english.png","performance.png"]:
        img = pygame.transform.scale(pygame.image.load(path), (50,50))
    elif i == "performance.png":
        img = pygame.transform.scale(pygame.image.load(path), (10,10))
    else:
        img = pygame.image.load(path)
    images[key] = img

for i in images:
    images[i].set_colorkey((240,240,240))
