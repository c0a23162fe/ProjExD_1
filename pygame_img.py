import os
import sys
import pygame as pg

def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")
    img = pg.image.load("fig/3.png")
    bird_img = pg.transform.flip(img, True, False)
    tmr1 = 0
    bird_rct = img.get_rect()
    bird_rct.center = 300, 200
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        screen.blit(bg_img, [tmr1, 0])
        screen.blit(bird_img, bird_rct)
        clock.tick(200)


if __name__ == "__main__":
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    pg.init()
    main()
    pg.quit()
    sys.exit()