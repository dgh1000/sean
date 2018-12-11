import pygame as P
import os

#os.environ['SDL_VIDEO_WINDOW_POS'] = "250,500"

g_width = 1024
g_height = 768

g_white = (255, 255, 255)
g_blue_light = (0, 191, 255)
g_black = (0, 0, 0)
g_blue_midnight = (25, 25, 112)


def checkQuit(evts):
    for e in evts:
        if e.type == P.QUIT:
            return True
        elif e.type == P.KEYDOWN and e.key == P.K_ESCAPE:
            return True
    return False

class RectSprite(P.sprite.Sprite):

    def __init__(self, x, y, width, height, color):
        P.sprite.Sprite.__init__(self)
        self.color = color
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.image = P.Surface((self.width, self.height))
        self.image.fill(self.color)

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y


class Moving(RectSprite):

    def __init__(self, x, y, xv, yv, width, height, color):
        RectSprite.__init__(self, x, y, width, height, color)
        self.xPos = float(x)
        self.yPos = float(y)
        self.xVel = float(xv)
        self.yVel = float(yv)
        
    def update(self):
        self.xPos += self.xVel
        self.yPos += self.yVel
        self.detectWallCollision()
        self.rect.x = int(self.xPos)
        self.rect.y = int(self.yPos)

    def collideUpdate(self, group):
        if P.sprite.spritecollide(self, group, False):
            self.xVel = -self.xVel
            self.yVel = -self.yVel

    def detectWallCollision(self):
        if not (0 <= self.xPos <= g_width):
            self.xVel = -self.xVel
        if not (0 <= self.yPos <= g_height):
            self.yVel = -self.yVel
            

def main():

    # initializion
    P.init()
    P.time.set_timer(24, 16)
    screen = P.display.set_mode((g_width, g_height))
    clock = P.time.Clock()
    # lastTime = P.time.get_ticks()
    v1 = Moving(10, 10, 6.0, 6.0, 60, 60, (255, 255, 255))
    h1 = Moving(200, 200, -6.0, -2.0, 60, 60, (255, 255, 255))
    groupH = P.sprite.Group([h1])
    groupV = P.sprite.Group([v1])
    bg = P.Surface(screen.get_size())
    bg = bg.convert()
    bg.fill((0, 0, 0))
    

    # create all the sprites and groups
    going = True
    while going:
        clock.tick(60)
        evts = P.event.get()
        for e in evts:
            if e.type == 24:
                groupH.update()
                groupV.update()
                    
        # here check events to see if we're still going.
        if checkQuit(evts):
            break
        v1.collideUpdate(groupH)
        h1.collideUpdate(groupV)
        screen.blit(bg, (0, 0))
        groupH.draw(screen)
        groupV.draw(screen)
        P.display.flip()

    P.quit()


if __name__ == '__main__':
    main()
