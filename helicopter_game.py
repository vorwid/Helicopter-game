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

class Pszeszkoda():
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

pszeszkody = []
for i in range(21):
    pszeszkody.append(Pszeszkoda(i*szer/20, szer/20))

while True:                                     # This loop close game window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
    if copokazuje == "menu":
            napisz("Nacisnij spacje zeby zaczac", 80, 150, 20)
            grafika = pygame.image.load(os.path.join("helicoper.png"))
            screen.blit(grafika, (80, 30))
    elif copokazuje == "rozgrywka":
        for p in pszeszkody:
            p.rysuj()
    
    pygame.display.update()


