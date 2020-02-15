import pygame
import os
import random

pygame.init()

szer = 600
wys = 600

screen = pygame.display.set_mode((szer, wys))

def napisz(tekst, x, y, rozmiar):
    czcionka = pygame.font.SysFont("Arial", rozmiar)
    rend = czcionka.render(tekst, 1, (255,100,100))
    screen.blit(rend, (x, y))  # this line is use to put render text in graphic window

copokazuje = "rozgrywka"

class Helicopter():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.wysokosc = 30
        self.szerokosc = 50
        self.ksztalt = pygame.Rect(self.x, self.y, self.szerokosc, self.wysokosc)
        self.grafika = pygame.image.load(os.path.join("heli.png"))
    def rysuj (self):
        screen.blit(self.grafika, (self.x, self.y))
    def ruch (self, v):
        self.y = self.y + v
        self.ksztalt = pygame.Rect(self.x, self.y, self.szerokosc, self.wysokosc)
        

class Przeszkoda():
    def __init__(self, x, szerokosc):
        self.x = x
        self.szerokosc = szerokosc
        self.y_gora = 0
        self.wys_gora = random.randint(150, 250)
        self.odstep = 200
        self.y_dol = self.wys_gora + self.odstep
        self.wys_dol = wys - self.y_dol
        self.kolor = (160, 140, 190)
        self.ksztalt_gora = pygame.Rect(self.x, self.y_gora, self.szerokosc, self.wys_gora)
        self.ksztalt_dol = pygame.Rect(self.x, self.y_dol, self.szerokosc, self.wys_dol)
    def rysuj(self):
        pygame.draw.rect(screen, self.kolor, self.ksztalt_gora, 0)
        pygame.draw.rect(screen, self.kolor, self.ksztalt_dol, 0)
    def ruch(self, v):
        self.x = self.x - v
        self.ksztalt_gora = pygame.Rect(self.x, self.y_gora, self.szerokosc, self.wys_gora)
        self.ksztalt_dol = pygame.Rect(self.x, self.y_dol, self.szerokosc, self.wys_dol)
    def kolizja(self, player):
        if self.ksztalt_gora.colliderect(player) or self.ksztalt_dol.colliderect(player):
            return True
        else:
            return False
                                

przeszkody = []
for i in range(21):
    przeszkody.append(Przeszkoda(i*szer/20, szer/20))

gracz = Helicopter(250, 275)
dy = 0

while True:                                     # This loop close game window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                dy = -1
            if event.key == pygame.K_DOWN:
                dy = 1
                    
    screen.fill((0, 0, 0))
    if copokazuje == "menu":
            napisz("Nacisnij spacje zeby zaczac", 80, 150, 20)
            grafika = pygame.image.load(os.path.join("helicoper.png"))
            screen.blit(grafika, (80, 30))
    elif copokazuje == "rozgrywka":
        for p in przeszkody:
            p.ruch(1)
            p.rysuj()
            if p.kolizja(gracz.ksztalt):
                copokazuje = "koniec"
        for p in przeszkody:
            if p.x <= -p.szerokosc:
                przeszkody.remove(p)
                przeszkody.append((Przeszkoda(szer, szer/20)))

        gracz.rysuj()
        gracz.ruch(dy)
    
    pygame.display.update()


