import pygame

#from main_menu import Monsters


class Data:
    def __init__(self):
        font_lives = pygame.font.Font(None, 36)
        font_score = pygame.font.Font(None, 50)
        font_money = pygame.font.Font(None, 50)
        font_wave = pygame.font.Font(None, 50)
        #font_left = pygame.font.Font(None, 30)


        self.lives = self.getlives()
        self.score = self.getscore()
        self.money = self.getmoney()
        self.wave = self.getwave()
        #self.left = self.getleft()


        self.towers = []
        self.enemies = []

        self.lives_text = font_lives.render(str(self.lives), True, (255, 255, 255))
        self.score_text = font_score.render(str(self.score), True, (120, 255, 120))
        self.money_text = font_money.render(str(self.money), True, (255, 255, 120))
        self.wave_text = font_wave.render(str(self.wave), True, (255, 255, 200))
        #self.left_text = font_left.render(str(self.left), True, (0, 0, 0))

        



    def drawdata(self, num, win):
        if num == 1:
            win.blit(self.lives_text, [36, 24])
            win.blit(self.score_text, [1010, 15])
            win.blit(self.money_text, [1258, 15])
            win.blit(self.wave_text, [1235, 120])
            #win.blit(self.left_text, [1290, 140])
        elif num == 2:
            win.blit(self.lives_text, [61, 20])
            win.blit(self.score_text, [990, 15])
            win.blit(self.money_text, [1243, 15])
            win.blit(self.wave_text, [607, 20])
            #win.blit(self.left_text, [660, 45])
        elif num == 3:
            win.blit(self.lives_text, [33, 16])
            win.blit(self.score_text, [990, 15])
            win.blit(self.money_text, [1243, 15])
            win.blit(self.wave_text, [625, 25])
            #win.blit(self.left_text, [685, 45])
    #显示生命、分数、金钱、波数和剩余怪数

    '''计算游戏数据'''
    def getlives(self):
        self.lives = 5



        return self.lives

    def getscore(self):
        self.score = 0


        return self.score


    def getmoney(self):
        self.money = 1000


        return self.money

    def getwave(self):
        present = 4
        all = 20


        self.wave = str(present) + "  /  " + str(all)


        return self.wave














