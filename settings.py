class Settings():
    '''存储设置'''
    def __init__(self):
        self.screen_width=1200
        self.screen_height=600
        self.bg_color=(230,230,230)
        #飞船的设置
        self.ship_limit=1
        #子弹设置
        self.bullet_width=3
        self.bullet_height=15
        self.bullet_color=(60,60,60)
        self.bullets_allowed=10
        #外星人速度设置
        self.fleet_drop_speed=10
        self.score_scale=1.5

        #游戏节奏加快速度
        self.speedup_scale=1.1
        #动态设置
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        '''设置飞船子弹外星人的速度，以及外星人移动方向'''
        self.ship_speed_factor = 1
        self.alien_speed_factor = 1
        self.bullet_speed_factor = 3
        self.fleet_direction = 1
        #外星人分数
        self.alien_points=50

    def increase_speed(self):
        self.ship_speed_factor*=self.speedup_scale
        self.alien_speed_factor*=self.speedup_scale
        self.bullet_speed_factor*=self.speedup_scale
        self.alien_points=int(self.alien_points*self.score_scale)
