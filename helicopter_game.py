import pygame

pygame.init()

szer = 600
wys = 600

screen = pygame.display.set_mode((szer, wys))

def napisz(tekst, x, y, rozmiar):
    czcionka = pygame.font.SysFont("Arial", rozmiar)
    rend = czcionka.render(tekst, 1, (255,100,100))
    screen.blit(rend, (x,y))  # this line is use to put render text in graphic window


while True:                                     # This loop close game window
    for event in pygame.event.get():
        pygame.quit()
        quit()

    napisz("Nacisnij spacje zeby zaczac", 80, 150, 20)
    pygame.display.update()


