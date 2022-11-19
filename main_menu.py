import sys

from buttons import *
from holes import *

from scenes import LevelSelection
from scenes import BattleScene1
from scenes import BattleScene2
from scenes import BattleScene3
from scenes import FailureScene
from scenes import VictoryScene
from towers import *

from monsters import *
import time
import random

"""
        需要初始化的变量
        waves[][]  第几关、第几个口
        path[][]  第几关、第几个口
        wave_enemies[][] 第几关、第几个口 每个里面path一样
"""
path_1_1 = [(1, 580), (115, 579), (194, 534), (214, 464), (232, 394), (305, 341), (391, 317), (430, 248), (457, 173),
            (512, 119), (560, 105), (773, 108), (782, 106), (820, 91), (845, 90), (867, 94), (915, 108), (1041, 107),
            (1108, 130), (1118, 123), (1145, 168), (1149, 245), (1100, 311), (1029, 329), (966, 373),
            (936, 442), (955, 505), (1001, 545), (1070, 573), (1101, 572), (1110, 582)]

path_2_1 = [(1, 374), (247, 374), (247, 99), (1025, 99), (1025, 546), (673, 546), (673, 393)]

path_2_2 = [(1399, 388), (1125, 388), (1125, 660), (355, 660), (358, 223), (673, 223), (673, 308)]

path_2_3 = [(1399, 220), (1025, 220), (1025, 545), (673, 545), (673, 393)]

path_2_4 = [(1, 556), (355, 556), (355, 225), (675, 225), (673, 308)]

path_3_1 = [(0, 86), (449, 86), (449, 188), (924, 188), (924, 275), (1290, 275), (1290, 354)]

path_3_2 = [(1399, 88), (925, 88), (925, 185), (450, 185), (450, 290), (128, 290), (128, 340)]

path_3_3 = [(0, 675), (444, 675), (444, 575), (923, 575), (923, 477), (1293, 477), (1293, 395)]

path_3_4 = [(1399, 677), (923, 677), (923, 575), (445, 575), (445, 477), (127, 477), (127, 387)]

'''游戏的菜单类'''
''' 初始化各种按钮以及界面背景图'''
''' 以数字1,2,3,4,5分别指代开始菜单，选关菜单以及1,2,3关的菜单'''


class MainMenu:
    def __init__(self, win):
        self.width = 1400
        self.height = 750
        self.bg = pygame.image.load('塔防游戏素材/地图/开始界面.png')
        self.bg = pygame.transform.scale(self.bg, (self.width, self.height))
        self.win = win

        self.play_button = PlayButton()
        self.exit_button = ExitButton()
        self.music_button = MusicButton()
        self.number_button = NumberButton()
        self.pause_button = ContinuePauseButton()
        self.restart_button = RestartButton()
        self.next_button = NextButton()
        self.back_button = BackButton()

        self.holes = [Hole(25, 435), Hole(285, 411), Hole(512, 175), Hole(741, 381),
                      Hole(954, 184), Hole(1008, 418), Hole(965, 640)]

        self.level_scene = LevelSelection()
        self.battle_scene1 = BattleScene1()
        self.battle_scene2 = BattleScene2()
        self.battle_scene3 = BattleScene3()
        self.change_scene_number = 1
        self.battle_scene_number = 1
        self.FailureScene = FailureScene()
        self.VictoryScene = VictoryScene()

        self.towers = []

        self.enemies = []
        self.clicks = []

        self.current_wave = []
        self.timer = time.time()
        self.timer2 = time.time()
        self.clock = pygame.time.Clock()

        self.font_lives = pygame.font.Font(None, 36)
        self.font_score = pygame.font.Font(None, 50)
        self.font_money = pygame.font.Font(None, 50)
        self.font_wave = pygame.font.Font(None, 50)

        self.lives = 9
        self.score = 0
        self.money = 5000
        self.wave = 0
        self.waves = []

        self.price_archer = 100
        self.price_turret = 200
        self.price_slower = 150

        self.pause = True

    ''' 启动游戏的菜单 '''
    ''' 界面变化后音乐也要变更,开始与选关界面为sound1,123关分别对应sound345,sound6为控制失败音乐，sound7为控制成功音乐 '''

    def run_game(self):
        sound1, sound3, sound4, sound5, sound6, sound7 = True, True, True, True, True, True

        ''' 不同菜单类的切换 '''
        while True:
            if self.change_scene_number == 1:
                if sound1 and self.music_button.music_paused:
                    pygame.mixer.init()
                    pygame.mixer.music.load('塔防游戏素材/音乐/开始界面 The 7 Seas.mp3')
                    sound1 = False
                    sound3, sound4, sound5, sound6, sound7 = True, True, True, True, True
                    pygame.mixer.music.play()
                self.draw_main_menu()
                self.check_scene1()

            elif self.change_scene_number == 2:
                if sound1 and self.music_button.music_paused:
                    pygame.mixer.init()
                    pygame.mixer.music.load('塔防游戏素材/音乐/开始界面 The 7 Seas.mp3')
                    sound1 = False
                    sound3, sound4, sound5, sound6, sound7 = True, True, True, True, True
                    pygame.mixer.music.play()
                self.level_scene.draw(self.win)
                self.music_button.draw(self.win)
                self.check_scene2()
                self.flushdata()

            elif self.change_scene_number == 3:
                self.battle_scene_number = 1
                if sound3 and self.music_button.music_paused:
                    pygame.mixer.init()
                    pygame.mixer.music.load('塔防游戏素材/音乐/沼泽地图.mp3')
                    sound3 = False
                    sound1, sound4, sound5, sound6, sound7 = True, True, True, True, True
                    pygame.mixer.music.play()
                self.battle_scene1.draw(self.win)
                self.music_button.draw(self.win)
                self.pause_button.draw(self.win)
                self.back_button.draw(self.win)

                self.drawdata(1, self.win)
                self.check_battle_scene()
                self.draw_holes()

                # 测试代码
                self.waves = [[5, 2], [5, 3], [10, 4]]

                if self.pause:
                    if time.time() - self.timer >= random.randrange(1, 6) / 2:
                        self.timer = time.time()
                        self.get_waves_enemies(self.waves, [Ntr(path_1_1), Goblin(path_1_1)])  # 出一波敌人

                self.draw_enemies((1110, 582))
                self.draw_towers()
                self.towers_attack()

                # event = pygame.event.wait()
                # if event.type == pygame.MOUSEBUTTONDOWN:
                #     self.clicks.append(event.pos)
                #     print(self.clicks)

            elif self.change_scene_number == 4:
                self.battle_scene_number = 2
                if sound4 and self.music_button.music_paused:
                    pygame.mixer.init()
                    pygame.mixer.music.load('塔防游戏素材/音乐/丛林地图.mp3')
                    sound4 = False
                    sound1, sound3, sound5, sound6, sound7 = True, True, True, True, True
                    pygame.mixer.music.play()
                self.battle_scene2.draw(self.win)
                self.music_button.draw(self.win)
                self.pause_button.draw(self.win)
                self.back_button.draw(self.win)
                self.drawdata(2, self.win)
                self.check_battle_scene()

                self.waves = [[5, 5]]

                if self.pause:
                    if time.time() - self.timer >= random.randrange(1, 6):
                        self.timer = time.time()
                        self.get_waves_enemies(self.waves, [Goblin(path_2_4), Wraith(path_2_4)])  # 出一波敌人

                self.draw_enemies((673, 308))
                self.draw_towers()
                self.towers_attack()

                # event = pygame.event.wait()
                # if event.type == pygame.MOUSEBUTTONDOWN:
                #     self.clicks.append(event.pos)
                #     print(self.clicks)

            elif self.change_scene_number == 5:
                self.battle_scene_number = 3
                self.clock.tick(100)
                if sound5 and self.music_button.music_paused:
                    pygame.mixer.init()
                    pygame.mixer.music.load('塔防游戏素材/音乐/沙漠地图.mp3')
                    sound5 = False
                    sound1, sound3, sound4, sound6, sound7 = True, True, True, True, True
                    pygame.mixer.music.play()
                self.battle_scene3.draw(self.win)
                self.music_button.draw(self.win)
                self.pause_button.draw(self.win)
                self.back_button.draw(self.win)
                self.drawdata(3, self.win)
                self.check_battle_scene()

                self.waves = [[1, 2]]

                if self.pause:
                    if time.time() - self.timer >= random.randrange(1, 6):
                        self.timer = time.time()
                        self.get_waves_enemies(self.waves, [Goblin(path_3_4), Wraith(path_3_4)])  # 出一波敌人

                self.draw_enemies((127, 387))
                self.draw_towers()
                self.towers_attack()

                # event = pygame.event.wait()
                # if event.type == pygame.MOUSEBUTTONDOWN:
                #     self.clicks.append(event.pos)
                #     print(self.clicks)

            elif self.change_scene_number == 6:
                self.clock.tick(100)
                if sound6 and self.music_button.music_paused:
                    pygame.mixer.init()
                    pygame.mixer.music.load('塔防游戏素材/音乐/成功音效.wav')
                    sound6 = False
                    sound1, sound3, sound4, sound5, sound7 = True, True, True, True, True
                    pygame.mixer.music.play()
                self.VictoryScene.draw(self.win)
                self.next_button.draw(self.win)
                self.check_Victory_scene()
                self.drawdata(4, self.win)

            elif self.change_scene_number == 7:
                self.clock.tick(100)
                if sound7 and self.music_button.music_paused:
                    pygame.mixer.init()
                    pygame.mixer.music.load('塔防游戏素材/音乐/失败音效.mp3')
                    sound7 = False
                    sound1, sound3, sound4, sound5, sound6 = True, True, True, True, True
                    pygame.mixer.music.play()
                self.FailureScene.draw(self.win)
                self.check_Failure_scene()
                self.drawdata(5, self.win)

            pygame.display.update()

    ''' 主菜单的渲染 '''

    def draw_main_menu(self):
        self.win.blit(self.bg, (0, 0))
        self.play_button.draw(self.win)
        self.exit_button.draw(self.win)
        self.music_button.draw(self.win)

    ''' 不同按钮功能的实现 '''
    ''' 开始菜单选择开始游戏将进入选关界面，即场景2，选择退出按钮会退出游戏 
        在选关界面选择返回将会回到开始菜单，选择关卡1,2,3将分别进入对应关卡场景，即场景3，4，5 '''

    def click_play_button(self, mouse_pos):
        play_button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if play_button_clicked:
            self.change_scene_number = 2

    def click_return_button(self, mouse_pos):
        return_button_clicked = self.level_scene.return_button.rect.collidepoint(mouse_pos)
        if return_button_clicked:
            self.change_scene_number = 1

    def click_exit_button(self, mouse_pos):
        exit_button_clicked = self.exit_button.rect.collidepoint(mouse_pos)
        if exit_button_clicked:
            pygame.quit()
            sys.exit()

    def click_number_button(self, mouse_pos):
        number1_button_clicked = self.number_button.rect1.collidepoint(mouse_pos)
        number2_button_clicked = self.number_button.rect2.collidepoint(mouse_pos)
        number3_button_clicked = self.number_button.rect3.collidepoint(mouse_pos)
        if number1_button_clicked:
            self.change_scene_number = 3
        elif number2_button_clicked:
            self.change_scene_number = 4
        elif number3_button_clicked:
            self.change_scene_number = 5

    def click_back_button(self, mouse_pos):
        back_button_clicked = self.back_button.back_rect.collidepoint(mouse_pos)
        if back_button_clicked:
            self.change_scene_number = 2

    ''' 以下部分为检测不同场景中发生事件的函数 '''
    ''' 开始界面检测开始游戏和退出按钮的点击，选关界面检测选关1,2,3以及返回按钮的点击；
        地图1,2,3界面检测音乐，暂停按钮的点击，以及键盘是否输入esc键，如输入则返回选关界面 
        成功界面检测是否进入下一关或返回选关界面的按钮点击，失败界面检测是否重新开始或返回选关 '''

    def check_scene1(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self.music_button.click_music_on_button(mouse_pos)
                self.click_play_button(mouse_pos)
                self.click_exit_button(mouse_pos)

    def check_scene2(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self.music_button.click_music_on_button(mouse_pos)
                self.click_number_button(mouse_pos)
                self.click_return_button(mouse_pos)

    def check_battle_scene(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self.music_button.click_music_on_button(mouse_pos)
                self.click_back_button(mouse_pos)
                self.pause = self.pause_button.click_continue_button(mouse_pos)

                for hole in self.holes:
                    hole.bool = hole.click_hole(mouse_pos)
                    if not hole.bool:
                        hole.bool = hole.click_menu(mouse_pos)
                        hole.selected = [hole.click_tower1(mouse_pos), hole.click_tower2(mouse_pos),
                                         hole.click_tower3(mouse_pos), hole.click_tower4(mouse_pos)]
                    if hole.selected[0] and hole.lock and self.money >= self.price_archer:
                        self.towers.append(ArchTower(hole.hole_rect.x + 65, hole.hole_rect.y))
                        self.money -= self.price_archer
                        hole.lock = False
                    if hole.selected[1] and hole.lock and self.money >= self.price_turret:
                        self.towers.append(TurretTower(hole.hole_rect.x + 65, hole.hole_rect.y))
                        self.money -= self.price_turret
                        hole.lock = False
                    if hole.selected[2] and hole.lock and self.money >= self.price_slower:
                        self.towers.append(SlowTower(hole.hole_rect.x + 65, hole.hole_rect.y))
                        self.money -= self.price_slower
                        hole.lock = False



            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.change_scene_number = 2

    def check_Failure_scene(self):
        '''失败界面的按钮判定，加在3，4,5界面的后面'''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if self.FailureScene.ReturnButton.rect.collidepoint(mouse_pos):
                    self.change_scene_number = 2
                    self.flushdata()

                elif self.FailureScene.RestartButton.rect.collidepoint(mouse_pos):
                    self.change_scene_number = self.battle_scene_number + 2
                    self.flushdata()

                    '''重新渲染界面'''

    def check_Victory_scene(self):
        '''成功界面的按钮判定，加在3，4,5界面的后面'''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if self.VictoryScene.NextButton.rect.collidepoint(mouse_pos):
                    self.change_scene_number = self.battle_scene_number + 3
                    if self.battle_scene_number == 3:
                        self.change_scene_number = 3
                    self.flushdata()

                elif self.VictoryScene.ReturnButton.rect.collidepoint(mouse_pos):
                    self.change_scene_number = 2
                elif self.VictoryScene.RestartButton.rect.collidepoint(mouse_pos):
                    self.change_scene_number = self.battle_scene_number + 2
                    self.flushdata()

                    '''重新渲染界面'''

    def get_waves_enemies(self, waves, wave_enemies):  # 每一关的波数和对应的小怪种类、数量, 每一关、每个出怪口都是不同的
        """
        eg
        waves[][] = [[10], [20], [25], [40]]
        wave_enemies = [Ntr(path[][]), Boss(path[][])]
        """
        if sum(self.current_wave) == 0:
            if len(self.enemies) == 0:
                self.wave += 1
                if self.wave > len(waves):
                    # 跳到成功界面
                    pygame.time.wait(1500)
                    self.change_scene_number = 6
                else:
                    self.current_wave = waves[self.wave - 1]
        else:
            for x in range(len(self.current_wave)):
                if self.current_wave[x] != 0:
                    self.enemies.append(wave_enemies[x])
                    self.current_wave[x] = self.current_wave[x] - 1
                    break

    # 渲染敌人
    def draw_enemies(self, target):  # target表示进门的坐标
        for en in self.enemies:
            if self.pause:
                en.move()
            if target[0] - 5 <= en.x <= target[0] + 5 and target[1] - 5 <= en.y <= target[1] + 5:
                self.lives -= 1
                self.enemies.remove(en)
                if self.lives <= 0:
                    # 跳到失败界面
                    pygame.time.wait(1500)
                    self.change_scene_number = 7

        for en in self.enemies:
            en.draw(self.win)

    def draw_towers(self):
        for tower in self.towers:
            tower.draw(self.win)

    def towers_attack(self):
        if self.pause:
            for tower in self.towers:
                count = tower.attack(self.enemies)
                self.money += count[0]
                self.score += count[1]

    # 渲染生命，分数，金钱和波数
    def drawdata(self, num, win):
        lives_text = self.font_lives.render(str(self.lives), True, (255, 255, 255))
        score_text = self.font_score.render(str(self.score), True, (120, 255, 120))
        money_text = self.font_money.render(str(self.money), True, (255, 255, 120))
        wave_text = self.font_wave.render(str(self.wave), True, (255, 255, 200))

        if num == 1:
            win.blit(lives_text, [36, 24])
            win.blit(score_text, [1010, 15])
            win.blit(money_text, [1258, 15])
            win.blit(wave_text, [1245, 120])

        elif num == 2:
            win.blit(lives_text, [61, 20])
            win.blit(score_text, [990, 15])
            win.blit(money_text, [1243, 15])
            win.blit(wave_text, [607, 20])

        elif num == 3:
            win.blit(lives_text, [33, 16])
            win.blit(score_text, [990, 15])
            win.blit(money_text, [1243, 15])
            win.blit(wave_text, [625, 25])

        elif num == 4:
            win.blit(score_text, [670, 385])

        elif num == 5:
            win.blit(score_text, [675, 400])

    def draw_holes(self):
        for hole in self.holes:
            hole.draw(self.win)
            if not hole.bool and hole.lock:
                hole.drawmenu(self.win)


    def flushdata(self):
        self.pause_button.flush_button()

        for hole in self.holes:
            hole.flush()
            hole.bool = True
            hole.selected = [False, False, False, False]
        self.pause = True
        self.enemies.clear()
        self.towers.clear()
        self.lives = 9
        self.score = 0
        self.money = 5000
        self.wave = 0
        self.waves.clear()
        self.current_wave.clear()  # 重新加载数据