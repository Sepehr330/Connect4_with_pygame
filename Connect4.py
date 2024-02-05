import pygame , sys , os
import pygame.display
import pygame.event
import pygame.time
import pygame.image
import pygame.transform
import pygame.surface
import pygame.mouse
import pygame.font
import pygame.time
import copy
from math import *
#start RY ---- > 160 + 70k  ,,,,, 162 + 70k : arrows
#End -----> 558 -70k
pygame.init()

# global variables-----
disp = 0
V = 0
Isred = True
Arrows = []
reds = []
yellows = []
ARR = []
ALL = []
YELLOW = (255 , 255 , 0)
WHITE = (255,255,255)
GREY = (230 , 230 , 230)
GREEN = (0 , 255, 0)
DARKGREEN = (0,170,0)
RED = (225 , 0 , 0)
L_RED = (250 , 50, 50)
BLUE = (0 , 0 , 128)
L_BLUE = (50 , 50 , 250)
BLACK = (0,0,0)
FPS = 120

#Fonts-----
font = pygame.font.SysFont("Arial" , 50)
Font = pygame.font.SysFont("Arial" , 80)

#uploading files----
text = font.render("Red turn" , True , RED)
text1 = font.render("Yellow turn" , True , YELLOW)
winred = Font.render("Red wins" , True , RED)
winyell = Font.render("Yellow wins" , True , YELLOW)
Tie = Font.render("DRAW" , True , BLUE)
screen = pygame.display.set_mode((800,650))
THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
background = pygame.image.load(os.path.join(THIS_FOLDER, 'A_Connect\Back.jpg'))
background = pygame.transform.scale(background , (800,800))
Board = pygame.image.load(os.path.join(THIS_FOLDER, 'A_Connect\Board.png'))
Red = pygame.image.load(os.path.join(THIS_FOLDER, 'A_Connect\Red.png'))
Red = pygame.transform.scale(Red , (60,60))
Yellow = pygame.image.load(os.path.join(THIS_FOLDER, 'A_Connect\Yellow.png'))
Yellow = pygame.transform.scale(Yellow , (70,70))
Green = pygame.image.load(os.path.join(THIS_FOLDER, 'A_Connect\L_green.png'))
Green = pygame.transform.scale(Green , (69,69))
Gren = pygame.image.load(os.path.join(THIS_FOLDER, 'A_Connect\green.png'))
Gren = pygame.transform.scale(Gren , (69,69))
arrow = pygame.image.load(os.path.join(THIS_FOLDER, 'A_Connect\D_arrow.png'))
arrow = pygame.transform.scale(arrow , (50,80))

#Reset the game
class Reset():
    def __init__(self ,x,y):
        self.x = x
        self.y = y
        self.text = font.render("RESTART" , True , GREEN)
        self.size = self.text.get_size()
        self.surface = pygame.Surface(self.size)
        self.surface.fill(BLACK)
        self.surface.blit(self.text , (0,0))
    def show(self):
        screen.blit(self.surface , (self.x , self.y))
    def button(self):
        global Isred
        global V
        global disp
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if (self.x + 200 > mouse[0] > self.x) and (self.y + 50 > mouse[1] > self.y) :
            self.surface.fill(L_BLUE)
            self.surface.blit(self.text , (0,0))
            if click[0] == 1 :
                disp = 0
                V = 0
                Isred = True
                reds.clear()
                yellows.clear()
                ALL.clear()
                ARR.clear()
                return 1
        else :
            self.surface.fill(BLACK)
            self.surface.blit(self.text , (0,0))
        return 0
    
#Arrows for choosing the column
class ARROW :
    def __init__(self , x , y , index):
        self.x = x
        self.y = y
        self.index = index
    def show(self):
        screen.blit(arrow , (self.x , self.y))
    def button(self):
        global Isred
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if (self.x + 50 > mouse[0] > self.x) and (self.y + 80 > mouse[1] > self.y) :
            if click[0] == 1 :
                if  Isred : 
                    for i in range(6):
                        if reds == [] or checkarr(self.index , i) :
                            reds.append(Red_bead(self.index , i))
                            ALL.append(reds[-1])
                            Isred = False
                            pygame.time.delay(130)
                            break
                else :
                    for i in range(6):
                        if  checkarr(self.index , i) :
                            yellows.append(Yellow_bead(self.index , i))
                            ALL.append(yellows[-1])
                            Isred = True
                            pygame.time.delay(130)
                            break

#RED_BEADS
class Red_bead :
    def __init__(self , x ,y , color = "red", Isin = False) :
        self.arr = (x,y)
        self.color = color
        self.p = [160 + 70*x , 0]
        self.place = (160 + 70*x , 558 - 70*y)
        self.isin = Isin
    def show(self):
        global disp
        global V
        if self.p[1] < self.place[1]:
            disp += V
            V += 0.15
            self.p[1] += disp
        if int(self.p[1]) >= self.place[1] and self.isin == False:
            V = 0
            disp = 0
            self.p[1] = self.place[1]
            self.isin = True
        screen.blit(Red , (int(self.p[0]),int(self.p[1])))

#Yellow_BEADS ----- 
class Yellow_bead :
    def __init__(self,x,y , color = "yellow" , Isin = False):
        self.arr = (x,y)
        self.color = color
        self.p = [155 + 70*x , 0]
        self.place = (155 + 70*x , 556 - 70*y)
        self.isin = Isin
    def show(self):
        global disp
        global V
        if self.p[1] < self.place[1]:
            disp += V
            V += 0.15
            self.p[1] += disp
        if int(self.p[1]) >= self.place[1] and self.isin == False:
            V = 0
            disp = 0
            self.p[1] = self.place[1]
            self.isin = True
        screen.blit(Yellow , (int(self.p[0]),int(self.p[1])))
clock = clock = pygame.time.Clock()
pygame.display.set_caption("Connect four")

#animation for winning
def green_win():
    for red in reds :
        for i in range(4):
            if red.arr == ARR[0][i] :
                screen.blit(Green , (red.place[0] - 5 , red.place[1]-5))
    for yellow in yellows :
        for i in range(4):
            if yellow.arr == ARR[0][i] :
                screen.blit(Gren , (yellow.place[0] + 1 , yellow.place[1] - 3))

#Check rows-------
def row():
    SATR = []
    row = []
    for i in range(6):
        for j in range(4):
            for k in range(4):
                row.append((j+k , i))
            SATR.append(row)
            row = []
    return SATR

#Check columns ----- 
def column():
    SOTON = []
    column = []
    for i in range(7):
        for j in range(3):
            for k in range(4):
                column.append((i , j+k))
            SOTON.append(column)
            column = []
    return SOTON

#Check diagonals ------
def dia():
    DIA = []
    dia = []
    for i in range(4):
        for j in range(3):
            for k in range(4):
                dia.append((i+k,j+k))
            DIA.append(dia)
            dia = []
    dia = []
    for i in range(3,7):
        for j in range(3):
            for k in range(4):
                dia.append((i-k , j+k))
            DIA.append(dia)
            dia = []
    return DIA

#check if the game is end=----
def checkend():
    global ARR
    C1 = 0
    for Dia in  row():
        for R in Dia:
            for red in reds :
                if red.arr == R :
                    C1 += 1
                if C1 == 4 :
                    ARR.append(Dia)
                    return 1
        C1 = 0
    C1 = 0
    for Dia in  row():
        for R in Dia:
            for ye in yellows :
                if ye.arr == R :
                    C1 += 1
                if C1 == 4 :
                    ARR.append(Dia)
                    return 2
        C1 = 0
    C1 = 0
    for Dia in  column():
        for R in Dia:
            for red in reds :
                if red.arr == R :
                    C1 += 1
                if C1 == 4 :
                    ARR.append(Dia)
                    return 4
        C1 = 0
    C1 = 0
    for Dia in  column():
        for R in Dia:
            for ye in yellows :
                if ye.arr == R :
                    C1 += 1
                if C1 == 4 :
                    ARR.append(Dia)
                    return 5
        C1 = 0
    #Diagonal _____________________________
    C1 = 0
    for Dia in  dia():
        for R in Dia:
            for red in reds :
                if red.arr == R :
                    C1 += 1
                if C1 == 4 :
                    ARR.append(Dia)
                    return 7
        C1 = 0
    C1 = 0
    for Dia in  dia():
        for R in Dia:
            for ye in yellows :
                if ye.arr == R :
                    C1 += 1
                if C1 == 4 :
                    ARR.append(Dia)
                    return 8
        C1 = 0
    if len(ALL) == 42 :
        return 3
    return 0


def checkarr(a , b) :
    for all in ALL :
        if all.arr == (a,b):
            return False
    return True

#show beads
def show_RY():
    for red in reds :
        red.show()
    for yellow in yellows :
        yellow.show()

#insert and show arrows
def insert_arrows():
    for i in range(7) :
        Arrows.append(ARROW(163 + 70*i , 100 , i))
def show_arrows():
    for i in range(7):
        Arrows[i].show()
    for i in range(7):
        Arrows[i].button()


insert_arrows()
reset = Reset(600,30)
blink  = 0
while True :
    while True :
        run = True
        for event in pygame.event.get() :
            if event.type == pygame.QUIT :
                pygame.quit()
                sys.exit()
        screen.blit(background , (0,0))
        if V == 0 :
            show_arrows()
        show_RY()
        if checkend() != 0 :
            break
        if Isred :
            screen.blit(text , (290 , 0))
        else :
            screen.blit(text1 , (290,0))
        screen.blit(Board , (155 ,200))
        pygame.display.update()
        clock.tick(FPS)
    while run :
        for event in pygame.event.get() :
            if event.type == pygame.QUIT :
                pygame.quit()
                sys.exit()
        blink += 1
        if blink > 140:
            blink = 0
        screen.blit(background , (0,0))
        show_RY()
        if checkend() %3 == 1 :
            screen.blit(winred , (250 , 0))
        if checkend()%3 == 2 :
            screen.blit(winyell , (250 , 0))
        if checkend()%3 == 0:
            screen.blit(Tie , (250 , 0))
        reset.show()
        if reset.button() == 1:
            run = False
        screen.blit(Board , (155 ,200))
        if ARR != [] and blink<70 :
            green_win()
        pygame.display.update()
        clock.tick(FPS)