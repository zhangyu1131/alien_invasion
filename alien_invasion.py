import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from alien import Alien
from game_stats import  GameStats
from button import Button
from scoreboard import Scoreboard

def run_game():
    #初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings=Settings()

    screen=pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    ship = Ship(screen,ai_settings)
    #创建一个用于存储子弹的编组
    bullets=Group()
    #创建外星人群
    aliens=Group()
    gf.create_fleet(ai_settings,screen,aliens,ship)
    #创建游戏统计实例
    stats=GameStats(ai_settings)
    #创建play按钮
    play_button=Button(ai_settings,screen,"Play")
    #创建存储游戏分数的类实例
    sb=Scoreboard(ai_settings,screen,stats)
    #游戏主循环
    while True:
        #监视鼠标键盘
        gf.check_events(ship,ai_settings,screen,bullets,stats,play_button,aliens)
        if stats.game_active:
            #移动飞船
            ship.update()
            #子弹更新
            gf.update_bullets(bullets,aliens,ai_settings,screen,ship,stats,sb)
            #外星人更新
            gf.update_aliens(aliens,ai_settings,ship,stats,screen,bullets)

        #更新屏幕
        gf.update_screen(ai_settings,screen,ship,bullets,aliens,stats,play_button,sb)

run_game()

