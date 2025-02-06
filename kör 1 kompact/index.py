'''
filter value: f0f0f0
'''
import pygame, sys, random, math, os
from math import sin, cos, sqrt

pygame.init()

images = {}

for i in os.listdir("images"):
    path = os.path.join("images", i)
    key = os.path.splitext(i)[0]
    if i not in ["magyar.png", "english.png"]:
        img = pygame.transform.scale(pygame.image.load(path), (50,50))
    else:
        img = pygame.image.load(path)
    images[key] = img

for i in images:
    images[i].set_colorkey((240,240,240))

zenék = ["zene.mp3"]
showSettings = -1
pencilcase = 0
playmusic = 1
középnégyzetmód = 1
increase = 0
decrease = 0
hide = 1
stop = -1
mentés = []
stáblistaBe = -1
kijelző = pygame.display.set_mode((665, 400))
pygame.display.set_caption("válassz nyelvet/choose language")
óra = pygame.time.Clock()

def stáblista():
    pygame.draw.rect(kijelző, (0,0,0), (225, 185, 534, 360))
    pygame.draw.rect(kijelző, (110,110,110), (230, 190, 525, 350))
    kijelző.blit(pygame.font.SysFont("Arial", 24).render(developer[0], False, (255,255,255)), (240, 200))
    kijelző.blit(pygame.font.SysFont("Arial", 24).render(developer[1], False, (255,255,255)), (240, 225))
    kijelző.blit(pygame.font.SysFont("Arial", 24).render(developer[2], False, (255,255,255)), (240, 250))
    kijelző.blit(pygame.font.SysFont("Arial", 24).render(developer[3], False, (255,255,255)), (240, 275))
    kijelző.blit(pygame.font.SysFont("Arial", 24).render(developer[4], False, (255,255,255)), (240, 300))
    kijelző.blit(pygame.font.SysFont("Arial", 24).render(developer[5], False, (255,255,255)), (240, 325))
    kijelző.blit(pygame.font.SysFont("Arial", 24).render(developer[6], False, (255,255,255)), (290, 350))
    kijelző.blit(pygame.font.SysFont("Arial", 24).render(developer[7], False, (255,255,255)), (290, 375))
    kijelző.blit(pygame.font.SysFont("Arial", 24).render(developer[8], False, (255,255,255)), (290, 400))
    kijelző.blit(pygame.font.SysFont("Arial", 24).render(developer[9], False, (255,255,255)), (290, 425))
    pygame.draw.rect(kijelző,(255,255,255),(452, 470, 80, 50), 5)
    kijelző.blit(pygame.font.SysFont("Arial", 24).render("OK", False, (255,255,255)), (472, 480)) 

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
        if stop == -1:
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
        if középnégyzetmód == 1 and hide == 1:
            pygame.draw.rect(kijelző, (self.középnégyzet.szín.r, self.középnégyzet.szín.g, self.középnégyzet.szín.b),(self.középnégyzet.x-self.középnégyzet.szélesség/2, self.középnégyzet.y-self.középnégyzet.magasság/2, self.középnégyzet.szélesség, self.középnégyzet.magasság))
        pygame.draw.rect(kijelző, (self.keringőnégyzet.szín.r,self.keringőnégyzet.szín.g,self.keringőnégyzet.szín.b), (self.keringőnégyzet.x, self.keringőnégyzet.y, self.keringőnégyzet.szélesség, self.keringőnégyzet.magasság))
        if középnégyzetmód == 1 and hide == -1:
            pygame.draw.rect(kijelző, (self.középnégyzet.szín.r, self.középnégyzet.szín.g, self.középnégyzet.szín.b),(self.középnégyzet.x-self.középnégyzet.szélesség/2, self.középnégyzet.y-self.középnégyzet.magasság/2, self.középnégyzet.szélesség, self.középnégyzet.magasság))

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
    kijelző.blit(pygame.font.SysFont("Arial", 24).render("Válassz egy nyelvet! / Choose a language!", False, (255,255,255)), (110, 20))
    kijelző.blit(images["magyar"], (20,100))
    kijelző.blit(pygame.font.SysFont("Arial", 24).render("magyar", False, (255,255,255)), (130, 250))
    kijelző.blit(images["english"], (360, 100))
    kijelző.blit(pygame.font.SysFont("Arial", 24).render("english", False, (255,255,255)), (470, 250))
    if event.type == pygame.MOUSEBUTTONDOWN:
        if onclick(20,100,300,150):
            nyelv = "magyar"
        if onclick(360,100,285,150):
            nyelv = "english"  
        print(f"chosen language: {nyelv}")
        if onclick(300,300,80,50):
            choosing = 0
    if nyelv:   
        pygame.draw.rect(kijelző,(255,255,255),(300, 300, 80, 50), 5)
        pygame.draw.rect(kijelző,(0,0,0),(300, 250, 80, 50))
        kijelző.blit(pygame.font.SysFont("Arial", 24).render(nyelv, False, (255,255,255)), (300, 250))      
        kijelző.blit(pygame.font.SysFont("Arial", 24).render("OK", False, (255,255,255)), (320, 310))      
    pygame.display.update()

if nyelv == "magyar":
    caption = "Végtelen spirál"
    fps = f"Képkockák másodpercenként: "

    instructions = [
        "---Irányítások---",
        "Szóköz:                      Új négyzetet hoz létre.",
        "Bal egérgomb:             Elhúzza a középső négyzetet.",
        "Középső egérgomb:     Vált változók között.",
        "Görgő fel:                    Az adott változót növeli.",
        "Görgő le:                     Az adott változót csökkenti.",
        "Jobb egérgomb:          Törli az előzőleg létre hozott négyzetet.",
        "OK"
        ]

    variables = [
        "Sebesség: ",
        " fok/képkocka",
        "Méret: ",
        " px^2",
        "Sugár: ",
        " px",
        "Piros: ",
        " színérték",
        "Zöld: ",
        " színérték",
        "Kék: ",
        " színérték",
        "Semmi"
    ]

    developer = [
        "Tervezte: Siminmin",
        "Készítette: Siminmin",
        "Programozta: Siminmin",
        "Rajzolta: Siminmin",
        "Zenét szerezte: Frédéric Chopin",
        "Zenét előadta:",
        "Alfonso Bertazzi -- Tristan Hudson",
        "Chiara Bertoglio -- Pantelis Assimakopoulos",
        "John Robson -- George Vosgerichian",
        "Ken Sasaki -- Joseph Renouf",
    ]
if nyelv == "english":
    caption = "Infinite spiral"
    fps = f"Frames per second: "

    instructions = [
        "---Controls---",
        "Space:                               Makes a new square.",
        "Left mouse button:             Drags the middle square.",
        "Middle mouse button:         Changes the changable variable.",
        "Mouse wheel up:                Increases the selected variable.",
        "Mouse wheel down:            Decreases the selected variable.",
        "Right mouse button:            Deletes the last summoned square.",
        "OK"
        ]

    variables = [
        "Speed: ",
        " degree/frame",
        "Size: ",
        " px^2",
        "Radius: ",
        " px",
        "Red: ",
        " color value",
        "Green: ",
        " color value",
        "Blue: ",
        " color value",
        "Nothing"
    ]

    developer = [
        "Planned by: Siminmin",
        "Developed by: Siminmin",
        "Programmed by: Siminmin",
        "Drawed by: Siminmin",
        "Music written by: Frédéric Chopin",
        "Music preformed by:",
        "Alfonso Bertazzi -- Tristan Hudson",
        "Chiara Bertoglio -- Pantelis Assimakopoulos",
        "John Robson -- George Vosgerichian",
        "Ken Sasaki -- Joseph Renouf",
    ]

kijelző = pygame.display.set_mode((1000, 800))
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
            if showSettings == 1:
                if onclick(860,370,50,50):
                    print(mentés)
                    for kör in körökbe:
                        rész1 = kör.__dict__
                        for k, i in rész1.items():
                            print(f"{k}: {i}")
                            if hasattr(i, "__dict__"): #ha van olyan tulajdonsága az elemnek
                                rész2 = i.__dict__
                                for k2, i2 in rész2.items():
                                    print(f"\t{k2}: {i2}")
                                    if hasattr(i2, "__dict__"):
                                        rész3 = i2.__dict__
                                        for k3, i3 in rész3.items():
                                            print(f"\t\t{k3}: {i3}")
                        print(" ")
                if onclick(790,300,50,50):
                    print("mentés")
                    mentés = körökbe[:]
                if onclick(860,300,50,50):
                    print("írás")
                    körökbe = mentés[:]
                if onclick(860,230,50,50):
                    print("mutató kapcsoló")
                    középnégyzetmód *= -1
                if onclick(790,230,50,50):
                    print("tüntető kapcsoló")
                    hide *= -1
                if onclick(860,160,50,50):
                    print("zene kapcsoló")
                    playmusic *= -1
                if onclick(790,370,50,50):
                    print("példák") #keringő([xhely, yhely, méretx, mérety, [r, g, b]], [xhely, yhely, méretx, mérety, [r, g, b]], sugár, szög, sebesség)
                    körökbe = []
                    pencilcase += 1
                    if pencilcase == 9:
                        pencilcase = 1
                    match pencilcase:
                        case 1:
                            print("1")
                            körökbe.append(keringő([200, 450, 0, 0, [0, 0, 0]], 
                                                    [100, 100, 50, 50, [0, 0, 0]],
                                                    10, 0, 1))
                            körökbe.append(keringő([250, 500, 0, 0, [0, 0, 0]], 
                                                    [100, 100, 50, 50, [0, 0, 0]],
                                                    10, 0, 1))
                            körökbe.append(keringő([300, 500, 0, 0, [0, 0, 0]], 
                                                    [100, 100, 50, 50, [0, 0, 0]],
                                                    10, 0, 1))
                            körökbe.append(keringő([350, 500, 0, 0, [0, 0, 0]], 
                                                    [100, 100, 50, 50, [0, 0, 0]],
                                                    10, 0, 1))
                            körökbe.append(keringő([400, 450, 0, 0, [0, 0, 0]], 
                                                    [100, 100, 50, 50, [0, 0, 0]],
                                                    10, 0, 1))
                            körökbe.append(keringő([250, 350, 0, 0, [0, 0, 0]], 
                                                    [100, 100, 50, 50, [0, 0, 0]],
                                                    10, 0, 1))
                            körökbe.append(keringő([350, 350, 0, 0, [0, 0, 0]], 
                                                    [100, 100, 50, 50, [0, 0, 0]],
                                                    10, 0, 1))
                            
                        case 2:
                            print("2")
                            körökbe.append(keringő([150, 450, 100, 100, [254, 243, 117]], 
                                                    [100, 100, 8, 8, [169, 169, 169]],
                                                    100, 90, 0.2))
                            körökbe.append(keringő([150, 450, 100, 100, [254, 243, 117]], 
                                                    [100, 100, 12, 12, [210, 180, 140]],
                                                    110, 90, 0.15))
                            körökbe.append(keringő([150, 450, 100, 100, [254, 243, 117]], 
                                                    [100, 100, 14, 14, [0, 102, 204]],
                                                    150, 90, 0.13))
                            körökbe.append(keringő([150, 450, 100, 100, [254, 243, 117]], 
                                                    [100, 100, 10, 10, [188, 39, 50]],
                                                    180, 90, 0.18))
                            for _ in range(200):
                                rot = random.randint(0, 360)
                                size = random.randint(1, 4)
                                speed = round(random.uniform(0.2, 0.3), 2)
                                color = [random.randint(50, 200), random.randint(50, 200), random.randint(50, 200)]
                                körökbe.append(keringő([150, 450, 100, 100, [254, 243, 117]], 
                                                        [100, 100, size, size, color], 
                                                        random.randint(200, 360), rot, speed))
                            for _ in range(3000):
                                radius = random.randint(170, 950)
                                rot = random.randint(0, 360)
                                size = random.randint(1, 3)
                                speed = round(random.uniform(0.2, 0.9), 2)
                                color = [random.randint(50, 200), random.randint(50, 200), random.randint(50, 200)]
                                körökbe.append(keringő([150, 450, 100, 100, [254, 243, 117]], 
                                                        [100, 100, size, size, color], 
                                                        radius, rot, speed/(radius/200)))
                            for _ in range(50):
                                rot = random.randint(0, 360)
                                size = random.randint(1, 2)
                                speed = round(random.uniform(0.2, 0.4), 2)
                                color = [random.randint(50, 200), random.randint(50, 200), random.randint(50, 200)]
                                körökbe.append(keringő([150, 450, 100, 100, [254, 243, 117]], 
                                                        [100, 100, size, size, color], 
                                                        random.randint(90, 180), rot, speed))
                            körökbe.append(keringő([150, 450, 100, 100, [254, 243, 117]], 
                                                    [100, 100, 30, 30, [184, 134, 11]],
                                                    350, 90, 0.05))
                            körökbe.append(keringő([150, 450, 100, 100, [254, 243, 117]], 
                                                    [100, 100, 25, 25, [210, 180, 140]],
                                                    500, 90, 0.06))
                            körökbe.append(keringő([150, 450, 100, 100, [254, 243, 117]], 
                                                    [100, 100, 20, 20, [173, 216, 230]],
                                                    650, 90, 0.07))
                            körökbe.append(keringő([150, 450, 100, 100, [254, 243, 117]], 
                                                    [100, 100, 18, 18, [25, 25, 112]],
                                                    800, 90, 0.08))
                        case 3:
                            print("3")
                            for _ in range(15000):
                                radius = random.randint(1, 1275)
                                rot = random.randint(0, 360)
                                size = random.randint(1, 2)
                                speed = round(random.uniform(0.7, 0.15), 2)
                                color = [random.randint(50, 200), random.randint(50, 200), random.randint(50, 200)]
                                körökbe.append(keringő([500, 400, 10, 10, [0,0,0]], 
                                                        [100, 100, size*(radius/200)*3, size*(radius/200)*3, color], 
                                                        radius, rot, speed/(radius/200)))
                        case 4:
                            print("4")
                            for _ in range(20000):
                                    radius = random.randint(1, 1300)
                                    rot = random.randint(0, 360)
                                    size = random.randint(10, 50)
                                    speed = round(random.uniform(0.7, 0.15), 2)
                                    color = [random.randint(50, 200), random.randint(50, 200), random.randint(50, 200)]
                                    körökbe.append(keringő([500, 400, 10, 10, [0, 0, 0]], 
                                                            [100, 100, size, size, color], 
                                                            radius, rot, speed/(radius/200)))
                        case 5:
                            print("5")
                            for i in range(1,1300):
                                radius = i+1
                                rot = i*137.5
                                rot = rot % 360
                                size = sqrt(i)*3.5
                                speed = 0.2         #*sqrt(i) optikai illuziót keltő
                                color = [0,55,0]
                                körökbe.append(keringő([500, 400, 10, 10, [0, 0, 0]], 
                                                        [100, 100, size, size, color], 
                                                        radius, rot, speed))
                                size *= 0.8
                                color = [0,255,0]
                                körökbe.append(keringő([500, 400, 10, 10, [0, 0, 0]], 
                                                        [100, 100, size, size, color], 
                                                        radius, rot, speed))
                        case 6:
                            print("6")
                            for ű in range(1, 10):
                                for é in range(1, 9):
                                    speed = 0.1*random.randint(-é,é)
                                    if speed == 0:
                                        speed = 0.1
                                    for i in range(10,13*ű):
                                        radius = i*2+ű**2.60
                                        rot = (é*360/8+ű*390) % 360
                                        size = 40*ű*sqrt(i)/40
                                        color = [155,155,0]
                                        körökbe.append(keringő([500, 400, 10, 10, [0, 0, 0]], 
                                                                [100, 100, size, size, color], 
                                                                radius, rot, speed))
                                        size -= 5
                                        color = [255,255,0]
                                        körökbe.append(keringő([500, 400, 10, 10, [0, 0, 0]], 
                                                                [100, 100, size, size, color], 
                                                                radius, rot, speed))
                        case 7:
                            print("7")
                            for u in range(1, 10):
                                for e in range(1, 9):
                                    for i in range(10, 15*u):
                                        z_depth = u * 20 
                                        radius = (i * 2 + u**3)/2
                                        angle = math.radians(e * 360/8 + u * 370)
                                        x = 500 + radius * math.cos(angle) * (1 - z_depth/200)
                                        y = 400 + radius * math.sin(angle) * (1 - z_depth/200)
                                        base_size = 40 * u * math.sqrt(i) / 50 * (1 - z_depth/400)
                                        speed = 0.1 * (1 + z_depth/100)
                                        depth_factor = 1 - z_depth/200
                                        dark_color = [0, int(55 * depth_factor), 0]
                                        bright_color = [0, int(255 * depth_factor), 0]
                                        körökbe.append(
                                            keringő(
                                                [x, y, 0, 0, [0, 0, 0]],
                                                [100, 100, base_size, base_size, dark_color],
                                                radius, math.degrees(angle), speed
                                            )
                                        )
                                        körökbe.append(
                                            keringő(
                                                [x * 1.05, y * 1.05, 0, 0, [0, 0, 0]],
                                                [100, 100, base_size * 0.9, base_size * 0.9, bright_color],
                                                radius * 0.95, math.degrees(angle) + 5, speed * 1.1
                                            )
                                        )   
                        case 8:
                            print("8")
                            for i in range(1, 1300):
                                radius = i * 1.1  # Slightly adjusted for better spacing
                                rot = (i * 137.5) % 360  # Maintains Fibonacci-like rotation
                                size = math.sqrt(i) * 3.5  # Controls object size
                                speed = 0.15 + 0.05 * math.sqrt(i)  # Slight variation for optical illusion
                                color = [0, int(100 + 100 * (i / 1300)), int(255 * (i / 1300))]  # Blue to cyan gradient

                                körökbe.append(keringő(
                                    [500, 400, 10, 10, [0, 0, 0]],  
                                    [100, 100, size, size, color],  
                                    radius, rot, speed
                                ))

                                # Smaller secondary object for depth effect
                                size *= 0.85
                                color = [15, int(255 * (i / 1300)), 230]  # Brighter cyan hue 25, 205, 240
                                körökbe.append(keringő(
                                    [500, 400, 10, 10, [0, 0, 0]],  
                                    [100, 100, size, size, color],  
                                    radius * 1.05, rot + 10, speed * 1.1  
                                ))                         
                if onclick(790,440,50,50):
                    print("fejlesztői adatok")
                    stáblistaBe *= -1
                if onclick(860,440,50,50):
                    print("kilépés")
                    pygame.quit()
                    sys.exit()
                if onclick(790,160,50,50):
                    print("futási kapcsoló")
                    stop *= -1
            if onclick(930, 160,50,50):
                print("beállítások")
                showSettings *= -1
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
                    alapkör.sugár += 1
                if event.button == 5:
                    alapkör.sugár -= 1
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

    kijelző.blit(images["increase"], (20, 660))
    kijelző.blit(images["decrease"], (20, 730))
    if nyelv == "magyar":
        kijelző.blit(images["piros"], (90,660))
        kijelző.blit(images["zöld"], (160,660))
        kijelző.blit(images["kék"], (230,660))
    elif nyelv == "english":
        kijelző.blit(images["red"], (90,660))
        kijelző.blit(images["green"], (160,660))
        kijelző.blit(images["blue"], (230,660))
    kijelző.blit(images["speed"], (90,730))
    kijelző.blit(images["distance"], (160,730))
    kijelző.blit(images["size"], (230,730))
    kijelző.blit(images["add"], (930,660))
    kijelző.blit(images["remove"], (930,730))
    kijelző.blit(images["trash"], (930,20))
    kijelző.blit(images["reset"], (300,730))
    pygame.draw.rect(kijelző, (alapkör.keringőnégyzet.szín.r, alapkör.keringőnégyzet.szín.g, alapkör.keringőnégyzet.szín.b), (300, 660, 50, 50))
    kijelző.blit(images["settings"], (930,160))
    if stáblistaBe == 1:
        stáblista()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if onclick(452, 470, 80, 50):
                print("fejlesztői adatok")
                stáblistaBe *= -1

    if showSettings == 1:
        pygame.draw.rect(kijelző, (0,0,0), (775, 145, 150, 360))
        pygame.draw.rect(kijelző, (110,110,110), (780, 150, 140, 350))
        kijelző.blit(images["save"], (790,300))
        kijelző.blit(images["info"], (860,370))
        kijelző.blit(images["book"], (790,370))
        kijelző.blit(images["import"], (860,300))
        kijelző.blit(images["heart"], (790,440))
        kijelző.blit(images["exit"], (860,440))
        if stop == 1:
            kijelző.blit(images["stop"], (790,160))
        else:
            kijelző.blit(images["play"], (790,160))
        if középnégyzetmód == 1:
            kijelző.blit(images["show"], (860,230))
        else:
            kijelző.blit(images["dontshow"], (860,230))
        if hide == 1:
            kijelző.blit(images["behind"], (790,230))
        else:
            kijelző.blit(images["ontop"], (790,230))
        if playmusic == 1:
            kijelző.blit(images["musicplaying"], (860,160))
        else:
            kijelző.blit(images["mute"], (860,160))

    pygame.display.update()
    óra.tick(60)