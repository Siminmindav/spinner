import pygame, sys, time
from math import sin, cos

pygame.init()
kijelző = pygame.display.set_mode((1000, 800))
pygame.display.set_caption("Infinite spiral")
óra = pygame.time.Clock()

class keringő:
    def __init__(self, középnégyzet = [400, 400, 20, 20, [255,0,0]], keringőnégyzet = [100, 100, 50, 50, [0,0,0]], sugár = 200, szög = 0, sebesség = 0):
        self.középnégyzet = self.középnégyzet(*középnégyzet)
        self.keringőnégyzet = self.keringőnégyzet(*keringőnégyzet)
        self.sugár = sugár
        self.szög = szög
        self.sebesség = sebesség
    
    class középnégyzet:
        def __init__(self, x, y, szélesség, magasság, szín, katt = 0):
            self.x = x
            self.y = y
            self.szélesség = szélesség
            self.magasság = magasság
            self.szín = self.szín(*szín)
            self.katt = katt

        class szín:
            def __init__(self, r, g, b):
                self.r = r
                self.g = g
                self.b = b

    class keringőnégyzet:
        def __init__(self, x, y, szélesség, magasság, szín):
            self.x = x
            self.y = y
            self.szélesség = szélesség
            self.magasság = magasság
            self.szín = self.szín(*szín)

        class szín:
            def __init__(self, r, g, b):
                self.r = r
                self.g = g
                self.b = b
        

    def interakció(self):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if pygame.mouse.get_pos()[0] < self.középnégyzet.x+self.középnégyzet.szélesség/2 and pygame.mouse.get_pos()[0] > self.középnégyzet.x-self.középnégyzet.szélesség/2 and pygame.mouse.get_pos()[1] < self.középnégyzet.y+self.középnégyzet.magasság/2 and pygame.mouse.get_pos()[1] > self.középnégyzet.y-self.középnégyzet.magasság/2:
                    self.középnégyzet.katt = 1  
                
        if event.type == pygame.MOUSEMOTION:
            if self.középnégyzet.katt == 1:
                self.középnégyzet.x, self.középnégyzet.y = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONUP:
            self.középnégyzet.katt = 0

    def vakolás(self):
        self.szög += self.sebesség

        if self.szög != 0:
            radián = 3.14159/180*self.szög
        else:
            radián = 0
        if -360 > self.szög or self.szög > 360:
            self.szög = 0
        sinus = sin(radián)
        cosinus = cos(radián)

        self.keringőnégyzet.x = int(self.középnégyzet.x + sinus*(self.sugár)-self.keringőnégyzet.szélesség/2)
        self.keringőnégyzet.y = int(self.középnégyzet.y + cosinus*(self.sugár)-self.keringőnégyzet.magasság/2)
        pygame.draw.rect(kijelző, (self.középnégyzet.szín.r, self.középnégyzet.szín.g, self.középnégyzet.szín.b),(self.középnégyzet.x-self.középnégyzet.szélesség/2, self.középnégyzet.y-self.középnégyzet.magasság/2, self.középnégyzet.szélesség, self.középnégyzet.magasság))
        pygame.draw.rect(kijelző, (self.keringőnégyzet.szín.r,self.keringőnégyzet.szín.g,self.keringőnégyzet.szín.b), (self.keringőnégyzet.x, self.keringőnégyzet.y, self.keringőnégyzet.szélesség, self.keringőnégyzet.magasság))

mutató = 1
akció = 1
alapkör = keringő([500, 100, 20, 20, [255,0,0]], [100, 100, 50, 50, [0,0,0]], 200, 0, 1)
körökbe = []

kijelző.blit(pygame.font.SysFont("Arial", 24).render("---Controls---", False, (255,255,255)), (400, 50))
kijelző.blit(pygame.font.SysFont("Arial", 24).render("Space:                               Makes a new square.", False, (255,255,255)), (200, 150)) 
kijelző.blit(pygame.font.SysFont("Arial", 24).render("Left mouse button:             Drags the middle square.", False, (255,255,255)), (200, 200))
kijelző.blit(pygame.font.SysFont("Arial", 24).render("Middle mouse button:         Changes the changable variable.", False, (255,255,255)), (200, 250)) 
kijelző.blit(pygame.font.SysFont("Arial", 24).render("Mouse wheel up:                Increases the selected variable.", False, (255,255,255)), (200, 300)) 
kijelző.blit(pygame.font.SysFont("Arial", 24).render("Mouse wheel down:            Decreases the selected variable.", False, (255,255,255)), (200, 350)) 
kijelző.blit(pygame.font.SysFont("Arial", 24).render("Right mouse button:            Deletes the last summoned square.", False, (255,255,255)), (200, 400)) 
pygame.draw.rect(kijelző,(255,255,255),(420, 550, 80, 50), 5)
kijelző.blit(pygame.font.SysFont("Arial", 24).render("OK", False, (255,255,255)), (440, 560)) 
while mutató == 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pos()[0] > 420 and pygame.mouse.get_pos()[0] < 420+80 and pygame.mouse.get_pos()[1] > 550 and pygame.mouse.get_pos()[1] < 550+50:
                mutató = 0

    pygame.display.update()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 3:
                if körökbe:
                    körökbe.pop()
            if event.button == 2: 
                akció += 1
            if akció == 1: 
                if event.button == 4:
                    alapkör.sebesség += 0.5
                if event.button == 5:
                    alapkör.sebesség -= 0.5
            if akció == 2:  
                if event.button == 4:
                    alapkör.keringőnégyzet.szélesség += 1
                    alapkör.keringőnégyzet.magasság += 1
                if event.button == 5:
                    if alapkör.keringőnégyzet.szélesség > 1 and alapkör.keringőnégyzet.magasság > 1:
                        alapkör.keringőnégyzet.szélesség -= 1
                        alapkör.keringőnégyzet.magasság -= 1
            if akció == 3:  
                if event.button == 4:
                    alapkör.sugár += 1
                if event.button == 5:
                    alapkör.sugár -= 1
            if akció == 4: 
                if event.button == 4:
                    if alapkör.keringőnégyzet.szín.r < 255:
                        alapkör.keringőnégyzet.szín.r += 1
                if event.button == 5:
                    if alapkör.keringőnégyzet.szín.r > 0:
                        alapkör.keringőnégyzet.szín.r -= 1
            if akció == 5: 
                if event.button == 4:
                    if alapkör.keringőnégyzet.szín.g < 255:
                        alapkör.keringőnégyzet.szín.g += 1
                if event.button == 5:
                    if alapkör.keringőnégyzet.szín.g > 0:
                        alapkör.keringőnégyzet.szín.g -= 1
            if akció == 6:  
                if event.button == 4:
                    if alapkör.keringőnégyzet.szín.b < 255:
                        alapkör.keringőnégyzet.szín.b += 1
                if event.button == 5:
                    if alapkör.keringőnégyzet.szín.b > 0:
                        alapkör.keringőnégyzet.szín.b -= 1
            if akció == 7:
                akció = 0


        if event.type == pygame.KEYDOWN:
            körökbe.append(keringő([alapkör.középnégyzet.x, alapkör.középnégyzet.y, alapkör.középnégyzet.szélesség, alapkör.középnégyzet.magasság,[alapkör.középnégyzet.szín.r,alapkör.középnégyzet.szín.g,alapkör.középnégyzet.szín.b]], [alapkör.keringőnégyzet.x, alapkör.keringőnégyzet.y, alapkör.keringőnégyzet.szélesség, alapkör.keringőnégyzet.magasság,[alapkör.keringőnégyzet.szín.r,alapkör.keringőnégyzet.szín.g,alapkör.keringőnégyzet.szín.b]], alapkör.sugár, alapkör.szög, alapkör.sebesség))

    szöveg = [f"Speed: {alapkör.sebesség} degree/frame", f"Size: {alapkör.keringőnégyzet.szélesség} px^2", f"radius: {alapkör.sugár} px", f"Red: {alapkör.keringőnégyzet.szín.r} color value", f"Green: {alapkör.keringőnégyzet.szín.g} color value", f"Blue: {alapkör.keringőnégyzet.szín.b} color value", "Nothing is selected"]

    kijelző.fill((25, 205, 240))
    for kör in körökbe:
        kör.vakolás()
        kör.interakció()

    if óra.get_fps() > 10:
        kijelző.blit(pygame.font.SysFont("Arial", 20).render(f"Frames per second: {óra.get_fps()}", False, (15, 180, 190)), (20, 20))
    elif óra.get_fps() > 5:
        kijelző.blit(pygame.font.SysFont("Arial", 40).render(f"Frames per second: {óra.get_fps()}", False, (205,0,0)), (20, 20))
    else:
        kijelző.blit(pygame.font.SysFont("Arial", 100).render(str(int(óra.get_fps())), False, (205,0,0)), (450, 350))
    kijelző.blit(pygame.font.SysFont("Arial", 24).render(str(szöveg[akció-1]), False, (60,60,60)), (20, 750))
    pygame.display.update()
    óra.tick(60)