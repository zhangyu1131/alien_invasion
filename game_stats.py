class GameStats():
    '''跟踪游戏统计信息'''
    def __init__(self,ai_settings):
        self.ai_settings=ai_settings
        self.reset_stats()
        self.game_active=False
        self.high_score=0
        self.level=1

    def reset_stats(self):
        self.ships_left=self.ai_settings.ship_limit
        #得分
        self.score=0