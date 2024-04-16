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
    bg_img_f = pg.transform.flip(bg_img, True, False)
    tmr1 = 0
    tmr2 = 1600
    bird_rct = img.get_rect()
    bird_rct.center = 300, 200
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        if tmr1<=-1600:
            tmr1=1600
            print("tmr1move")
        if tmr2<=-1600:
            tmr2=1600
            print("tmr2move")
        screen.blit(bg_img, [tmr1, 0])
        screen.blit(bg_img_f, [tmr2, 0])
        screen.blit(bird_img, bird_rct)
        print(tmr1,tmr2)
        pg.display.update()
        tmr1 -= 1
        tmr2 -= 1        
        clock.tick(200)
        key_lst = pg.key.get_pressed()
        if key_lst[pg.K_UP]:
            a = (-1, -1)
        elif key_lst[pg.K_DOWN]:
            a = (-1, 1)
        elif key_lst[pg.K_LEFT]:
            a = (-1, 0)
        elif key_lst[pg.K_RIGHT]:
            a = (2, 0)
        else:
            a = (-1, 0)
        bird_rct.move_ip(a)


if __name__ == "__main__":
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    pg.init()
    main()
    pg.quit()
    sys.exit()