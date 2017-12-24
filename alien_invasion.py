import sys
import pygame
from settings import Settings
from ship import Ship

def run_game():
    #初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings=Settings()

    screen=pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    ship = Ship(screen)
    #游戏主循环
    while True:
        #监视鼠标键盘
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sys.exit()
        #设置背景色
        screen.fill(ai_settings.bg_color)
        #画飞船
        ship.blitme()
        #使屏幕可见
        pygame.display.flip()

run_game()

