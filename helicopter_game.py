import pygame
import os

pygame.init()

szer = 600
wys = 600

screen = pygame.display.set_mode((szer, wys))

def napisz(tekst, x, y, rozmiar):
    czcionka = pygame.font.SysFont("Arial", rozmiar)
    rend = czcionka.render(tekst, 1, (255,100,100))
    screen.blit(rend, (x,y))  # this line is use to put render text in graphic window

copokazuje = "menu"

class Przeszkoda():
    def __init__(self, x, szerokosc):
        self.x=x
        self.szerokosc = szerokosc
        self.y_gora = y
        self.wys_gora = random.randint(150, 250)
        self.odstep = 200
        self.y_dol = self.wys_gora + self.odstep

while True:                                     # This loop close game window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
    if copokazuje == "menu":
            napisz("Nacisnij spacje zeby zaczac", 80, 150, 20)
            grafika = pygame.image.load(os.path.join("helicoper.png"))
            screen.blit(grafika, (80, 30))
    
    pygame.display.update()


