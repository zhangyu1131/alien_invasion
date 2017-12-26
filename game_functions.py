import sys
import pygame
from bullet import Bullet

def check_keydown_events(event,ship,ai_settings,screen,bullets):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key==pygame.K_SPACE:
        new_bullet=Bullet(ai_settings,screen,ship)
        bullets.add(new_bullet)

def check_keyup_events(event,ship,ai_settings,screen,bullets):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_events(ship,ai_settings,screen,bullets):
    '''响应按键事件'''
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
        #按键事件
        elif event.type==pygame.KEYDOWN:
            check_keydown_events(event,ship,ai_settings,screen,bullets)
        elif event.type==pygame.KEYUP:
            check_keyup_events(event,ship,ai_settings,screen,bullets)

def update_screen(ai_settings,screen,ship,bullets):
    screen.fill(ai_settings.bg_color)
    for bullet in bullets:
        bullet.draw_bullet()
    ship.blitme()
    pygame.display.flip()