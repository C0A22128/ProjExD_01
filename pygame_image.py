import sys
import pygame as pg


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("ex01-20230613/fig/pg_bg.jpg")
    bg_imgs = pg.transform.flip(bg_img, True, False)
    
    kk_img = pg.image.load("ex01-20230613/fig/3.png")
    kk_img = pg.transform.flip(kk_img, True, False)
    kk_imgs = [kk_img, pg.transform.rotozoom(kk_img, 10, 1.0)]

    kk2_img = pg.image.load("ex01-20230613/fig/4.png")
    kk2_img = pg.transform.flip(kk2_img, True, False)
    kk_img = [kk2_img, pg.transform.rotate(kk2_img, 10)]
    

    x = 0
    x2 = 0

    tmr = 0



    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        screen.blit(bg_img, [-x, 0])
        screen.blit(bg_img, [1600-x2, 0])
        screen.blit(bg_img, [3200-x2, 0])
        screen.blit(kk_imgs[tmr % 2], [300, 200])
        if tmr <= 40:
            screen.blit(kk_img[0], [300, 200])
        else:
            screen.blit(kk_img[1], [300, 200])

        pg.display.update()
        tmr += 1   

        if tmr >= 80:
            tmr = 0
        x += 1
        if x >= 1600:
            x = 0
        x2 += 1
        if x2 >= 32000:
            x2 -= 32000 


        clock.tick(100)
        clock.tick(200)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()

     
    
    

        
        