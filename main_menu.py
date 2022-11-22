import sys

from buttons import *
from holes import *

from scenes import *
from towers import *

from monsters import *
import time
import random

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
        self.help_button = HelpButton()
        self.Help1Scene = Help1Scene()
        self.Help2Scene = Help2Scene()
        self.TurnLeftButton = TurnLeftButton()
        self.TurnRightButton = TurnRightButton()
        self.change_help_number = 1

        self.holes = [Hole(25, 435), Hole(285, 411), Hole(512, 175), Hole(741, 381),
                      Hole(954, 184), Hole(1008, 418), Hole(965, 640)]
        self.holes2 = [Hole2(127, 268), Hole2(190, 435), Hole2(221, 629), Hole2(402, 300), Hole2(413, 484),
                       Hole2(576, 130), Hole2(621, 584),
                       Hole2(843, 582), Hole2(735, 462), Hole2(905, 175), Hole2(1095, 265), Hole2(1168, 451),
                       Hole2(1167, 584)]
        self.holes3 = [Hole3(65, 190), Hole3(189, 190), Hole3(311, 190), Hole3(65, 586), Hole3(189, 586),
                       Hole3(311, 586), Hole3(504, 101), Hole3(504, 266), Hole3(504, 477), Hole3(504, 652),
                       Hole3(788, 101), Hole3(788, 266), Hole3(788, 477), Hole3(788, 652), Hole3(993, 176),
                       Hole3(1127, 176), Hole3(1247, 176), Hole3(1007, 378), Hole3(1133, 378), Hole3(995, 586),
                       Hole3(1133, 586), Hole3(1263, 586), Hole3(189, 378), Hole3(311, 378)]
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
        self.count = 0

        self.current_wave = []
        self.timer = time.time()
        self.timer2 = time.time()
        self.clock = pygame.time.Clock()

        self.font_lives = pygame.font.Font(None, 36)
        self.font_score = pygame.font.Font(None, 50)
        self.font_money = pygame.font.Font(None, 50)
        self.font_wave = pygame.font.Font(None, 40)

        self.lives = 9
        self.score = 0
        self.money = 300
        self.wave = 0
        self.waves = []

        self.price_archer = 100
        self.price_turret = 200
        self.price_slower = 150

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
                if self.help_button.click_help_button:

                    if self.change_help_number == 1:
                        self.TurnRightButton.draw(self.win)
                        self.Help1Scene.draw(self.win)
                    elif self.change_help_number == 2:
                        self.TurnLeftButton.draw(self.win)
                        self.Help2Scene.draw(self.win)
                else:
                    self.draw_main_menu()

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
                    pygame.mixer.music.play(-1)
                self.waves = [[5, 0], [5, 3], [3, 5], [5, 5], [10, 10], [0, 8], [5, 8], [10, 5], [10, 8], [15, 15]]
                self.draw_battle_scene1()

            elif self.change_scene_number == 4:
                self.battle_scene_number = 2
                if sound4 and self.music_button.music_paused:
                    pygame.mixer.init()
                    pygame.mixer.music.load('塔防游戏素材/音乐/丛林地图.mp3')
                    sound4 = False
                    sound1, sound3, sound5, sound6, sound7 = True, True, True, True, True
                    pygame.mixer.music.play(-1)
                self.waves = [[5, 0, 0, 0, 0, 0, 0, 0],
                              [5, 0, 0, 0, 5, 0, 0, 0],
                              [0, 5, 0, 0, 0, 5, 0, 0],
                              [3, 3, 0, 0, 3, 3, 0, 0],
                              [5, 5, 3, 0, 5, 5, 3, 0],
                              [3, 3, 3, 0, 3, 3, 3, 0],
                              [5, 3, 5, 3, 3, 5, 3, 3],
                              [5, 3, 5, 5, 3, 3, 5, 5],
                              [10, 8, 8, 8, 8, 8, 8, 10],
                              [15, 15, 15, 15, 15, 15, 15, 15]]
                self.draw_battle_scene2()

            elif self.change_scene_number == 5:
                self.battle_scene_number = 3
                if sound5 and self.music_button.music_paused:
                    pygame.mixer.init()
                    pygame.mixer.music.load('塔防游戏素材/音乐/沙漠地图.mp3')
                    sound5 = False
                    sound1, sound3, sound4, sound6, sound7 = True, True, True, True, True
                    pygame.mixer.music.play(-1)
                self.waves = [[1]]
                self.draw_battle_scene3()

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
        self.help_button.draw(self.win)

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

    def click_help_buttton(self, mouse_pos):
        help_button_clicked = self.help_button.rect.collidepoint(mouse_pos)
        if help_button_clicked:
            self.help_button.click_help_button = not self.help_button.click_help_button

    def click_turn_left_buttton(self, mouse_pos):
        turn_left_buttton_clicked = self.TurnLeftButton.rect.collidepoint(mouse_pos)
        if turn_left_buttton_clicked:
            if self.change_help_number != 1:
                self.change_help_number -= 1

    def click_turn_right_buttton(self, mouse_pos):
        turn_right_buttton_clicked = self.TurnRightButton.rect.collidepoint(mouse_pos)
        if turn_right_buttton_clicked:
            if self.change_help_number != 2:
                self.change_help_number += 1

    ''' 以下部分为检测不同场景中发生事件的函数 '''
    ''' 开始界面检测开始游戏和退出按钮的点击，选关界面检测选关1,2,3以及返回按钮的点击；
        地图1,2,3界面检测音乐，暂停按钮的点击，以及键盘是否输入esc键，如输入则返回选关界面 
        成功界面检测是否进入下一关或返回选关界面的按钮点击，失败界面检测是否重新开始或返回选关 '''

    def check_scene1(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if self.help_button.click_help_button == False:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    self.music_button.click_music_on_button(mouse_pos)
                    self.click_play_button(mouse_pos)
                    self.click_exit_button(mouse_pos)
                    self.click_help_buttton(mouse_pos)
            else:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    self.click_help_buttton(mouse_pos)
                    self.click_turn_right_buttton(mouse_pos)
                    self.click_turn_left_buttton(mouse_pos)

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

    def check_battle_scene(self, num):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self.music_button.click_music_on_button(mouse_pos)
                self.click_back_button(mouse_pos)
                self.pause_button.click_continue_button(mouse_pos)

                if num == 1:
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

                elif num == 2:
                    for hole in self.holes2:
                        hole.bool = hole.click_hole(mouse_pos)
                        if not hole.bool:
                            hole.bool = hole.click_menu(mouse_pos)
                            hole.selected = [hole.click_tower1(mouse_pos), hole.click_tower2(mouse_pos),
                                             hole.click_tower3(mouse_pos), hole.click_tower4(mouse_pos)]
                        if hole.selected[0] and hole.lock and self.money >= self.price_archer:
                            self.towers.append(ArchTower(hole.hole_rect.x + 45, hole.hole_rect.y + 8))
                            self.money -= self.price_archer
                            hole.lock = False
                        if hole.selected[1] and hole.lock and self.money >= self.price_turret:
                            self.towers.append(TurretTower(hole.hole_rect.x + 45, hole.hole_rect.y + 8))
                            self.money -= self.price_turret
                            hole.lock = False
                        if hole.selected[2] and hole.lock and self.money >= self.price_slower:
                            self.towers.append(SlowTower(hole.hole_rect.x + 45, hole.hole_rect.y + 8))
                            self.money -= self.price_slower
                            hole.lock = False

                elif num == 3:
                    for hole in self.holes3:
                        hole.bool = hole.click_hole(mouse_pos)
                        if not hole.bool:
                            hole.bool = hole.click_menu(mouse_pos)
                            hole.selected = [hole.click_tower1(mouse_pos), hole.click_tower2(mouse_pos),
                                             hole.click_tower3(mouse_pos), hole.click_tower4(mouse_pos)]
                        if hole.selected[0] and hole.lock and self.money >= self.price_archer:
                            self.towers.append(ArchTower(hole.hole_rect.x + 42, hole.hole_rect.y + 25))
                            self.money -= self.price_archer
                            hole.lock = False
                        if hole.selected[1] and hole.lock and self.money >= self.price_turret:
                            self.towers.append(TurretTower(hole.hole_rect.x + 40, hole.hole_rect.y + 25))
                            self.money -= self.price_turret
                            hole.lock = False
                        if hole.selected[2] and hole.lock and self.money >= self.price_slower:
                            self.towers.append(SlowTower(hole.hole_rect.x + 42, hole.hole_rect.y + 22))
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

    def draw_battle_scene1(self):
        self.battle_scene1.draw(self.win)
        self.music_button.draw(self.win)
        self.pause_button.draw(self.win)
        self.back_button.draw(self.win)
        self.draw_holes()
        self.draw_towers()
        self.draw_enemies()
        self.towers_attack()
        self.drawdata(1, self.win)
        self.check_battle_scene(1)
        self.get_waves_enemies(self.waves, [Ntr(path_1_1), Goblin(path_1_1)], 1)

    def draw_battle_scene2(self):
        self.battle_scene2.draw(self.win)
        self.music_button.draw(self.win)
        self.pause_button.draw(self.win)
        self.back_button.draw(self.win)
        self.draw_holes2()
        self.draw_towers()
        self.draw_enemies()
        self.towers_attack()
        self.drawdata(2, self.win)
        self.check_battle_scene(2)
        self.get_waves_enemies(self.waves,
                               [Reaper(path_2_1), Reaper(path_2_2), Reaper(path_2_3), Reaper(path_2_4),
                                Wraith(path_2_1), Wraith(path_2_2), Wraith(path_2_3),
                                Wraith(path_2_4)], 4)

    def draw_battle_scene3(self):
        self.battle_scene3.draw(self.win)
        self.music_button.draw(self.win)
        self.pause_button.draw(self.win)
        self.back_button.draw(self.win)
        self.draw_holes3()
        self.draw_towers()
        self.draw_enemies()
        self.towers_attack()
        self.drawdata(3, self.win)
        self.check_battle_scene(3)
        self.get_waves_enemies(self.waves, [BatMonster(path_3_2)], 4)  # 出一波敌人

    def get_waves_enemies(self, waves, wave_enemies, number):  # 每一关的波数和对应的小怪种类、数量, 每一关、每个出怪口都是不同的
        if self.pause_button.game_paused:
            self.count += 1
            if self.count >= random.randrange(50, 100):
                self.count = 0
                if sum(self.current_wave) == 0:
                    if len(self.enemies) == 0:
                        self.wave += 1
                        if self.wave > len(waves):
                            # 跳到成功界面
                            pygame.time.wait(1000)
                            self.change_scene_number = 6
                        else:
                            self.current_wave = waves[self.wave - 1]
                            self.pause_button.game_paused = False
                else:
                    for i in range((len(self.current_wave) // number)):
                        flag = False
                        for x in range(number):
                            if self.current_wave[number * i + x] != 0:
                                flag = True
                                self.enemies.append(wave_enemies[number * i + x])
                                self.current_wave[number * i + x] -= 1
                        if flag:
                            break



    # 渲染敌人
    def draw_enemies(self):  # target表示进门的坐标
        for en in self.enemies:
            if self.pause_button.game_paused:
                en.move()
            if en.path[len(en.path) - 1][0] - 5 <= en.x <= en.path[len(en.path) - 1][0] + 5 and \
                    en.path[len(en.path) - 1][1] - 5 <= en.y <= en.path[len(en.path) - 1][1] + 5:
                self.lives -= en.damage
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
        if self.pause_button.game_paused:
            for tower in self.towers:
                count = tower.attack(self.enemies)
                self.money += count[0]
                self.score += count[1]

    # 渲染生命，分数，金钱和波数
    def drawdata(self, num, win):
        lives_text = self.font_lives.render(str(self.lives), True, (255, 255, 255))
        score_text = self.font_score.render(str(self.score), True, (120, 255, 120))
        money_text = self.font_money.render(str(self.money), True, (255, 255, 120))
        wave_text = self.font_wave.render("wave:" + str(self.wave) + " / 10 ", True, (255, 255, 200))

        if num == 1:
            win.blit(lives_text, [36, 24])
            win.blit(score_text, [1030, 15])
            win.blit(money_text, [1275, 15])
            win.blit(wave_text, [1220, 122])

        elif num == 2:
            win.blit(lives_text, [61, 20])
            win.blit(score_text, [1015, 18])
            win.blit(money_text, [1265, 18])
            win.blit(wave_text, [587, 18])

        elif num == 3:
            win.blit(lives_text, [33, 16])
            win.blit(score_text, [1010, 15])
            win.blit(money_text, [1265, 15])
            win.blit(wave_text, [612, 29])

        elif num == 4:
            win.blit(score_text, [670, 385])

        elif num == 5:
            win.blit(score_text, [675, 400])

    def draw_holes(self):
        for hole in self.holes:
            hole.draw(self.win)
            if not hole.bool and hole.lock:
                hole.drawmenu(self.win)

    def draw_holes2(self):
        for hole in self.holes2:
            hole.draw(self.win)
            if not hole.bool and hole.lock:
                hole.drawmenu(self.win)

    def draw_holes3(self):
        for hole in self.holes3:
            hole.draw(self.win)
            if not hole.bool and hole.lock:
                hole.drawmenu(self.win)

    def flushdata(self):
        self.pause_button.flush_button()

        for hole in self.holes:
            hole.flush()
        for hole in self.holes2:
            hole.flush()
        for hole in self.holes3:
            hole.flush()
        self.pause_button.game_paused = True
        self.enemies.clear()
        self.towers.clear()
        self.lives = 9
        self.score = 0
        self.money = 300
        self.wave = 0
        self.waves.clear()
        self.current_wave.clear()  # 重新加载数据
        self.count = 0
