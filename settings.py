class Settings():
    '''存储设置'''
    def __init__(self):
        self.screen_width=1200
        self.screen_height=600
        self.bg_color=(230,230,230)
        #飞船的设置
        self.ship_speed_factor=1
        self.ship_limit=1
        #子弹设置
        self.bullet_speed_factor=3
        self.bullet_width=3
        self.bullet_height=15
        self.bullet_color=(60,60,60)
        self.bullets_allowed=10
        #外星人速度设置
        self.alien_speed_factor = 1
        self.fleet_drop_speed=10
        self.fleet_direction=1
