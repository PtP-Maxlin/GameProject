import pygame
from buttons import NumberButton
from buttons import ReturnButton
from buttons import ContinuePauseButton
from buttons import NextButton
from buttons import RestartButton



''' 此处是游戏所有的界面类  '''


'''  进入选关时的界面    '''
'''  初始化选关背景图，返回按钮，选关按钮 '''
class LevelSelection:

    def __init__(self):
        self.win = pygame.display.set_mode((1400, 750))
        self.bg = pygame.image.load('塔防游戏素材/地图/关卡选择.jpg')      #
        self.select_bg = pygame.image.load('塔防游戏素材/按钮/关卡面板.png')
        self.number_button = NumberButton()
        self.return_button = ReturnButton()

    ''' 分别渲染背景，选关面板，按钮  '''
    def draw(self, win):
        win.blit(self.bg, (0, 0))
        win.blit(self.select_bg, (350, 100))
        self.number_button.draw(win)
        self.return_button.draw(win)


''' 以下为三个关卡的界面 '''
class BattleScene1:
    def __init__(self):
        self.win = pygame.display.set_mode((1400, 750))
        self.bg = pygame.image.load('塔防游戏素材/地图/第一关.png')
        #self.continue_pause_button = ContinuePauseButton()

    def draw(self, win):
        win.blit(self.bg, (0, 0))
        #self.continue_pause_button.draw(win)


class BattleScene2:
    def __init__(self):
        self.win = pygame.display.set_mode((1400, 750))
        self.bg = pygame.image.load('塔防游戏素材/地图/第二关.png')
        #self.continue_pause_button = ContinuePauseButton()

    def draw(self, win):
        win.blit(self.bg, (0, 0))
        #self.continue_pause_button.draw(win)



class BattleScene3:
    def __init__(self):
        self.win = pygame.display.set_mode((1400, 750))
        self.bg = pygame.image.load('塔防游戏素材/地图/第三关.png')
        #self.continue_pause_button = ContinuePauseButton()

    def draw(self, win):
        win.blit(self.bg, (0, 0))
        #self.continue_pause_button.draw(win)


''' 失败界面 '''
''' 初始化返回按钮，重新开始按钮以及失败背景图 '''
class FailureScene:
    def __init__(self):
        self.win = pygame.display.set_mode((1400, 750))
        self.bg = pygame.image.load('塔防游戏素材/地图/失败.png')
        self.RestartButton= RestartButton()
        self.ReturnButton= ReturnButton()
        self.ReturnButton.rect.midbottom = (450, 667)
        self.RestartButton = RestartButton()
        self.RestartButton.rect.midbottom = (950, 667)

    def draw(self, win):
        win.blit(self.bg, (0, 0))
        self.RestartButton.draw(win)
        self.ReturnButton.draw(win)


''' 胜利界面 '''
''' 初始化重新开始按钮，下一关的按钮以及胜利背景图 '''
class VictoryScene:
    def __init__(self):
        self.win = pygame.display.set_mode((1400, 750))
        self.bg = pygame.image.load('塔防游戏素材/地图/胜利.png')
        self.RestartButton = RestartButton()
        self.ReturnButton = ReturnButton()
        self.ReturnButton.rect.midbottom = (300, 667)
        self.NextButton = NextButton()

    def draw(self, win):
        win.blit(self.bg, (0, 0))
        self.RestartButton.draw(win)
        self.ReturnButton.draw(win)
        self.NextButton.draw(win)



