import pygame, sys, loader
from math import sin, cos

pygame.init()
zenék = ["music/chop.mp3", "music/chop2.mp3", "music/chop3.mp3", "music/chop4.mp3", "music/chop5.mp3", "music/chop6.mp3", "music/chop7.mp3", "music/chop8.mp3", "music/chop9.mp3", ]
playmusic = 1
increase = 0
decrease = 0
kijelző = pygame.display.set_mode((1000, 800))
pygame.display.set_caption("válassz nyelvet/choose language")
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

def onclick(x=0,y=0,sz=0,m=0):
    return pygame.mouse.get_pos()[0] > x and pygame.mouse.get_pos()[0] < x+sz and pygame.mouse.get_pos()[1] > y and pygame.mouse.get_pos()[1] < y+m

nyelv = ""
choosing = 1
zeneszám = 0
mutató = 1
akció = 1
alapkör = keringő([500, 400, 20, 20, [255,0,0]], [100, 100, 50, 50, [0,0,0]], 200, 0, 1)
körökbe = []

while choosing == 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    kijelző.blit(loader.images["magyar"], (20, 300))
    kijelző.blit(pygame.font.SysFont("Arial", 24).render("magyar", False, (255,255,255)), (120, 500))
    kijelző.blit(loader.images["english"], (700, 300))
    kijelző.blit(pygame.font.SysFont("Arial", 24).render("english", False, (255,255,255)), (810, 500))
    if event.type == pygame.MOUSEBUTTONDOWN:
        if onclick(20,300,300,150):
            nyelv = "magyar"
        if onclick(700,300,285,150):
            nyelv = "english"  
        print(f"chosen language: {nyelv}")
        if onclick(490,550,80,50):
            choosing = 0
    if nyelv:   
        pygame.draw.rect(kijelző,(255,255,255),(470, 550, 80, 50), 5)
        pygame.draw.rect(kijelző,(0,0,0),(470, 500, 80, 50))
        kijelző.blit(pygame.font.SysFont("Arial", 24).render(nyelv, False, (255,255,255)), (470, 500))      
        kijelző.blit(pygame.font.SysFont("Arial", 24).render("OK", False, (255,255,255)), (490, 560))      
    pygame.display.update()

if nyelv == "magyar":
    from textHU import caption, instructions, variables, fps
if nyelv == "english":
    from textEN import caption, instructions, variables, fps

pygame.display.set_caption(caption)
kijelző.fill((0,0,0))
kijelző.blit(pygame.font.SysFont("Arial", 24).render(instructions[0], False, (255,255,255)), (400, 50)) #irányítások
kijelző.blit(pygame.font.SysFont("Arial", 24).render(instructions[1], False, (255,255,255)), (200, 150)) #space
kijelző.blit(pygame.font.SysFont("Arial", 24).render(instructions[2], False, (255,255,255)), (200, 200)) #jobbegérgomb
kijelző.blit(pygame.font.SysFont("Arial", 24).render(instructions[3], False, (255,255,255)), (200, 250)) #balegérgomb
kijelző.blit(pygame.font.SysFont("Arial", 24).render(instructions[4], False, (255,255,255)), (200, 300)) #középső egérgomb
kijelző.blit(pygame.font.SysFont("Arial", 24).render(instructions[5], False, (255,255,255)), (200, 350)) #fel
kijelző.blit(pygame.font.SysFont("Arial", 24).render(instructions[6], False, (255,255,255)), (200, 400)) #le
pygame.draw.rect(kijelző,(255,255,255),(420, 550, 80, 50), 5)
kijelző.blit(pygame.font.SysFont("Arial", 24).render("OK", False, (255,255,255)), (440, 560)) 

while mutató == 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if onclick(420,550,80,50):
                mutató = 0
    pygame.display.update()

while True: 
    if increase == 1:
        if akció == 1:
            alapkör.sebesség += 0.5
        if akció == 2:
            alapkör.keringőnégyzet.szélesség += 1
            alapkör.keringőnégyzet.magasság += 1
        if akció == 3:
            alapkör.sugár += 1
        if akció == 4:
            if alapkör.keringőnégyzet.szín.r < 255:
                alapkör.keringőnégyzet.szín.r += 1
        if akció == 5:
            if alapkör.keringőnégyzet.szín.g < 255:
                alapkör.keringőnégyzet.szín.g += 1
        if akció == 6:
            if alapkör.keringőnégyzet.szín.b < 255:
                alapkör.keringőnégyzet.szín.b += 1

    if decrease == 1:
        if akció == 1:
            alapkör.sebesség -= 0.5
        if akció == 2:
            if alapkör.keringőnégyzet.szélesség > 1 and alapkör.keringőnégyzet.magasság > 1:
                alapkör.keringőnégyzet.szélesség -= 1
                alapkör.keringőnégyzet.magasság -= 1
        if akció == 3:
            alapkör.sugár -= 1
        if akció == 4:
            if alapkör.keringőnégyzet.szín.r > 0:
                alapkör.keringőnégyzet.szín.r -= 1
        if akció == 5:
            if alapkör.keringőnégyzet.szín.g > 0:
                    alapkör.keringőnégyzet.szín.g -= 1
        if akció == 6:
            if alapkör.keringőnégyzet.szín.b > 0:
                alapkör.keringőnégyzet.szín.b -= 1

    if playmusic == -1:
        pygame.mixer.music.stop()
    else:
        if not pygame.mixer.music.get_busy():
            if zeneszám > len(zenék)-1:
                zeneszám = 0
            pygame.mixer.music.load(zenék[zeneszám])
            pygame.mixer.music.play()
            zeneszám += 1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if onclick(930,160,50,50):
                playmusic *= -1
            if onclick(20, 660,50,50):
                print("fel")
                increase = 1
            if onclick(20, 730,50,50):
                print("le")
                decrease = 1
            if onclick(90,660,50,50):
                print("piros")
                akció = 4
            if onclick(160,660,50,50):
                print("zöld")
                akció = 5
            if onclick(230,660,50,50):
                print("kék")
                akció = 6
            if onclick(90,730,50,50):
                print("sebesség")
                akció = 1
            if onclick(160,730,50,50):
                print("sugár")
                akció = 3
            if onclick(230,730,50,50):
                print("méret")
                akció = 2
            if onclick(930,660,50,50):
                print("plusz")
                körökbe.append(keringő([alapkör.középnégyzet.x, alapkör.középnégyzet.y, alapkör.középnégyzet.szélesség, alapkör.középnégyzet.magasság,[alapkör.középnégyzet.szín.r,alapkör.középnégyzet.szín.g,alapkör.középnégyzet.szín.b]], [alapkör.keringőnégyzet.x, alapkör.keringőnégyzet.y, alapkör.keringőnégyzet.szélesség, alapkör.keringőnégyzet.magasság,[alapkör.keringőnégyzet.szín.r,alapkör.keringőnégyzet.szín.g,alapkör.keringőnégyzet.szín.b]], alapkör.sugár, alapkör.szög, alapkör.sebesség))
            if onclick(930,730,50,50):
                print("mínusz")
                if körökbe:
                    körökbe.pop()
            if onclick(930,20,50,50):
                print("kuka")
                körökbe = []
            if onclick(300,730,50,50):
                print("reset")
                alapkör = keringő([500, 400, 20, 20, [255,0,0]], [100, 100, 50, 50, [0,0,0]], 200, 0, 1)
                
            
            if event.button == 3:
                if körökbe:
                    körökbe.pop()
            if event.button == 2: #sebesség,méret,sugár,r,g,b
                akció += 1
            if akció == 1:  #sebesség
                if event.button == 4:
                    alapkör.sebesség += 0.1
                if event.button == 5:
                    alapkör.sebesség -= 0.1
            if akció == 2:  #méret
                if event.button == 4:
                    alapkör.keringőnégyzet.szélesség += 0.1
                    alapkör.keringőnégyzet.magasság += 0.1
                if event.button == 5:
                    if alapkör.keringőnégyzet.szélesség > 0.1 and alapkör.keringőnégyzet.magasság > 0.1:
                        alapkör.keringőnégyzet.szélesség -= 0.1
                        alapkör.keringőnégyzet.magasság -= 0.1
            if akció == 3:  #sugár
                if event.button == 4:
                    alapkör.sugár += 0.1
                if event.button == 5:
                    alapkör.sugár -= 0.1
            if akció == 4:  #r
                if event.button == 4:
                    if alapkör.keringőnégyzet.szín.r < 255:
                        alapkör.keringőnégyzet.szín.r += 1
                if event.button == 5:
                    if alapkör.keringőnégyzet.szín.r > 0:
                        alapkör.keringőnégyzet.szín.r -= 1
            if akció == 5:  #g
                if event.button == 4:
                    if alapkör.keringőnégyzet.szín.g < 255:
                        alapkör.keringőnégyzet.szín.g += 1
                if event.button == 5:
                    if alapkör.keringőnégyzet.szín.g > 0:
                        alapkör.keringőnégyzet.szín.g -= 1
            if akció == 6:  #b
                if event.button == 4:
                    if alapkör.keringőnégyzet.szín.b < 255:
                        alapkör.keringőnégyzet.szín.b += 1
                if event.button == 5:
                    if alapkör.keringőnégyzet.szín.b > 0:
                        alapkör.keringőnégyzet.szín.b -= 1
            if akció == 7:
                akció = 0
        
        if event.type == pygame.MOUSEBUTTONUP:
            increase = 0
            decrease = 0
        if event.type == pygame.KEYDOWN:
            if pygame.key.name(event.key) == "space":
                körökbe.append(keringő([alapkör.középnégyzet.x, alapkör.középnégyzet.y, alapkör.középnégyzet.szélesség, alapkör.középnégyzet.magasság,[alapkör.középnégyzet.szín.r,alapkör.középnégyzet.szín.g,alapkör.középnégyzet.szín.b]], [alapkör.keringőnégyzet.x, alapkör.keringőnégyzet.y, alapkör.keringőnégyzet.szélesség, alapkör.keringőnégyzet.magasság,[alapkör.keringőnégyzet.szín.r,alapkör.keringőnégyzet.szín.g,alapkör.keringőnégyzet.szín.b]], alapkör.sugár, alapkör.szög, alapkör.sebesség))

    szöveg = [
        f"{variables[0]}{alapkör.sebesség}{variables[1]}",
        f"{variables[2]}{alapkör.keringőnégyzet.szélesség}{variables[3]}",
        f"{variables[4]}{alapkör.sugár}{variables[5]}",
        f"{variables[6]}{alapkör.keringőnégyzet.szín.r}{variables[7]}",
        f"{variables[8]}{alapkör.keringőnégyzet.szín.g}{variables[9]}",
        f"{variables[10]}{alapkör.keringőnégyzet.szín.b}{variables[11]}",
        f"{variables[12]}"
    ]

    kijelző.fill((25, 205, 240))
    for kör in körökbe:
        kör.vakolás()
        kör.interakció()

    if óra.get_fps() > 10:
        kijelző.blit(pygame.font.SysFont("Arial", 20).render(f"{fps}{óra.get_fps()}", False, (15, 180, 190)), (20, 20))
    elif óra.get_fps() > 5:
        kijelző.blit(pygame.font.SysFont("Arial", 40).render(f"{fps}{óra.get_fps()}", False, (205,0,0)), (20, 20))
    else:
        kijelző.blit(pygame.font.SysFont("Arial", 100).render(str(int(óra.get_fps())), False, (205,0,0)), (450, 350))
    kijelző.blit(pygame.font.SysFont("Arial", 24).render(str(szöveg[akció-1]), False, (60,60,60)), (20, 600))

    kijelző.blit(loader.images["increase"], (20, 660))
    kijelző.blit(loader.images["decrease"], (20, 730))
    if nyelv == "magyar":
        kijelző.blit(loader.images["piros"], (90,660))
        kijelző.blit(loader.images["zöld"], (160,660))
        kijelző.blit(loader.images["kék"], (230,660))
    elif nyelv == "english":
        kijelző.blit(loader.images["red"], (90,660))
        kijelző.blit(loader.images["green"], (160,660))
        kijelző.blit(loader.images["blue"], (230,660))
    kijelző.blit(loader.images["speed"], (90,730))
    kijelző.blit(loader.images["distance"], (160,730))
    kijelző.blit(loader.images["size"], (230,730))
    kijelző.blit(loader.images["add"], (930,660))
    kijelző.blit(loader.images["remove"], (930,730))
    kijelző.blit(loader.images["trash"], (930,20))
    kijelző.blit(loader.images["reset"], (300,730))
    pygame.draw.rect(kijelző, (alapkör.keringőnégyzet.szín.r, alapkör.keringőnégyzet.szín.g, alapkör.keringőnégyzet.szín.b), (300, 660, 50, 50))

    if playmusic == 1:
        kijelző.blit(loader.images["musicplaying"], (930,160))
    else:
        kijelző.blit(loader.images["mute"], (930,160))
    pygame.display.update()
    óra.tick(60)