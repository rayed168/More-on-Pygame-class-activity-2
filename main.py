import pygame as pg
pg.init()
screen=pg.display.set_mode((400,400))
screen.fill((255,255,255))
blue=(0,0,255)
pg.draw.circle(screen,blue,(200,200),50)
red=(255,3,0)
pg.draw.circle(screen,red,(100,100),50,5)
pg.display.update()
while True:
    for event in pg.event.get():
        if event.type==pg.QUIT:
            pg.quit()