import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group

def run_game():
    #初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings=Settings()

    screen=pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    ship = Ship(screen,ai_settings)
    #创建一个用于存储子弹的编组
    bullets=Group()

    #游戏主循环
    while True:
        #监视鼠标键盘
        gf.check_events(ship,ai_settings,screen,bullets)
        #移动飞船
        ship.update()
        bullets.update()
        #删除已消失的子弹
        for bullet in bullets:
            if bullet.rect.bottom<=0:
                bullets.remove(bullet)
        print(len(bullets))
        #更新屏幕
        gf.update_screen(ai_settings,screen,ship,bullets)

run_game()

