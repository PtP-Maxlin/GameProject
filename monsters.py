import pygame
import os
import math


class Monsters:
    def __init__(self, path):
        # 移动路径
        self.path = path
        # x y当前的坐标，沿路径移动  底部中间
        self.x = self.path[0][0]
        self.y = self.path[0][1]
        # 放到第几张图片，以达到gif的效果
        self.animation_count = 0
        #
        # 基本属性，每个怪不一样
        self.width = 78
        self.height = 63  # 体积
        self.images = []
        self.img = pygame.Surface((50, 50), flags=pygame.HWSURFACE)  # 图组
        self.max_health = 10
        self.health = self.max_health  # 血量
        self.count_coin = 0  # 金币
        self.count_score = 0  # 分数
        self.v = 1  # 移动速度

        self.original_v = self.v
        self.damage = 1

        #
        # 移动相关
        self.path_pos = 0
        self.move_count = 0
        self.move_step_dis = 0
        self.distance = 0

    def move(self):  # 移动
        self.animation_count += 1
        if self.animation_count >= len(self.images):
            self.animation_count = 0

        x1, y1 = self.path[self.path_pos]
        if self.path_pos + 1 >= len(self.path):
            x2, y2 = (9999, 9999)  # 进家
        else:
            x2, y2 = self.path[self.path_pos + 1]
        dirn = ((x2 - x1) * 2, (y2 - y1) * 2)
        length = math.sqrt((dirn[0]) ** 2 + (dirn[1]) ** 2)
        dirn = (dirn[0] / length, dirn[1] / length)
        move_x, move_y = ((self.x + dirn[0] * self.v), (self.y + dirn[1] * self.v))
        self.distance += self.v
        self.x = move_x
        self.y = move_y
        if dirn[0] >= 0:
            if dirn[1] >= 0:
                if self.x >= x2 and self.y >= y2:
                    self.x, self.y = self.path[self.path_pos + 1]
                    self.path_pos += 1
            else:
                if self.x >= x2 and self.y <= y2:
                    self.x, self.y = self.path[self.path_pos + 1]
                    self.path_pos += 1
        else:
            if dirn[1] >= 0:
                if self.x <= x2 and self.y >= y2:
                    self.x, self.y = self.path[self.path_pos + 1]
                    self.path_pos += 1
            else:
                if self.x <= x2 and self.y >= y2:
                    self.x, self.y = self.path[self.path_pos + 1]
                    self.path_pos += 1
        self.v = self.original_v

    def die(self, damage):  # 敌人死亡  与防御塔关联
        self.health -= damage
        if self.health <= 0:
            return True
        return False

    def getpath(self, path):  # 路径，一个精灵组用一个路径
        self.path = path

    def draw(self, win):  # 怪物＋血条
        self.img = pygame.transform.scale(self.images[self.animation_count], (self.width, self.height))
        win.blit(self.img, (self.x - self.width / 2, self.y - self.height / 2))
        self.draw_health_bar(win)

    def draw_health_bar(self, win):  # 血条
        length = 50
        loseHP = length / self.max_health
        health_bar = loseHP * self.health
        pygame.draw.rect(win, (255, 0, 0), (self.x - self.width / 4 - 6, self.y - self.height * 3 / 4 - 6, length, 6),
                         0)
        pygame.draw.rect(win, (0, 255, 0),
                         (self.x - self.width / 4 - 6, self.y - self.height * 3 / 4 - 6, health_bar, 6), 0)


imgs1 = []
for x in range(18):
    add_str = str(x)
    if x < 10:
        add_str = "0" + add_str
    add_str = "0" + add_str
    imgs1.append(pygame.transform.scale(
        pygame.image.load(os.path.join("塔防游戏素材/怪物/牛头人/Walking", "Satyr_03_Walking_" + add_str + ".png")),
        (78, 63)))


class Ntr(Monsters):
    def __init__(self, path):  # def __init__(self, path)  self.path = path
        super().__init__(path)
        self.path = path
        self.max_health = 10
        self.health = self.max_health
        self.images = imgs1[:]
        self.count_coin = 5
        self.count_score = 20
        self.v = 1.2

        self.original_v = self.v


imgs2 = []
for x in range(24):
    add_str = str(x)
    if x < 10:
        add_str = "0" + add_str
    add_str = "0" + add_str
    imgs2.append(pygame.transform.scale(
        pygame.image.load(os.path.join("塔防游戏素材/怪物/哥布林/Walking", "0_Goblin_Walking_" + add_str + ".png")),
        (75, 75)))


class Goblin(Monsters):
    def __init__(self, path):  # def __init__(self, path)  self.path = path
        super().__init__(path)
        self.width = 75
        self.height = 75  # 体积
        self.max_health = 20
        self.health = self.max_health  # 血量
        self.count_coin = 10  # 金币
        self.count_score = 30  # 分数
        self.v = 1  # 移动速度
        self.path = path
        self.images = imgs2[:]
        self.original_v = self.v


imgs3 = []
for x in range(12):
    add_str = str(x)
    if x < 10:
        add_str = "0" + add_str
    add_str = "0" + add_str
    imgs3.append(pygame.transform.scale(
        pygame.image.load(
            os.path.join("塔防游戏素材/怪物/漂浮幽灵/Walking", "Wraith_01_Moving Forward_" + add_str + ".png")),
        (78, 63)))


class Wraith(Monsters):
    def __init__(self, path):  # def __init__(self, path)  self.path = path
        super().__init__(path)
        self.width = 78
        self.height = 63  # 体积
        self.max_health = 10
        self.health = self.max_health  # 血量
        self.count_coin = 15  # 金币
        self.count_score = 60  # 分数
        self.v = 2  # 移动速度

        self.original_v = self.v

        self.path = path
        self.images = imgs3[:]


imgs4 = []
for x in range(12):
    add_str = str(x)
    if x < 10:
        add_str = "0" + add_str
    add_str = "0" + add_str
    imgs4.append(pygame.transform.scale(
        pygame.image.load(
            os.path.join("塔防游戏素材/怪物/第二关boss/Running", "0_Reaper_Man_Running_" + add_str + ".png")),
        (75, 75)))


class Reaper(Monsters):
    def __init__(self, path):
        super().__init__(path)
        self.width = 75
        self.height = 75  # 体积
        self.max_health = 20
        self.health = self.max_health  # 血量
        self.count_coin = 15  # 金币
        self.count_score = 50  # 分数
        self.v = 1.5  # 移动速度

        self.original_v = self.v

        self.path = path
        self.images = imgs4[:]


imgs5 = []
for x in range(31):
    add_str = str(x)
    if x < 10:
        add_str = "0" + add_str
    add_str = "0" + add_str
    imgs5.append(pygame.transform.scale(
        pygame.image.load(
            os.path.join("塔防游戏素材/怪物/BatMonster/Walking", "Troll_03_1_WALK_" + add_str + ".png")),
        (250, 200)))


class BatMonster(Monsters):
    def __init__(self, path):
        super().__init__(path)
        self.width = 250
        self.height = 200  # 体积
        self.max_health = 200
        self.health = self.max_health  # 血量
        self.count_coin = 200  # 金币
        self.count_score = 500  # 分数
        self.v = 1  # 移动速度
        self.damage = 10

        self.original_v = self.v

        self.path = path
        self.images = imgs5[:]

    def draw(self, win):  # 怪物＋血条
        self.img = pygame.transform.scale(self.images[self.animation_count], (self.width, self.height))
        win.blit(self.img, (self.x - self.width / 2, self.y - self.height / 2-50))
        self.draw_health_bar(win)

    def draw_health_bar(self, win):  # 血条
        length = 135
        loseHP = length / self.max_health
        health_bar = loseHP * self.health
        pygame.draw.rect(win, (255, 0, 0), (self.x - self.width / 4 - 6, self.y - self.height * 3 / 4 +30, length, 6),
                         0)
        pygame.draw.rect(win, (0, 255, 0),
                         (self.x - self.width / 4 - 6, self.y - self.height * 3 / 4 + 30, health_bar, 6), 0)


imgs6 = []
for x in range(24):
    add_str = str(x)
    if x < 10:
        add_str = "0" + add_str
    add_str = "0" + add_str
    imgs6.append(pygame.transform.scale(
        pygame.image.load(
            os.path.join("塔防游戏素材/怪物/白色小怪/Walking", "0_Fallen_Angels_Walking_" + add_str + ".png")),
        (75, 75)))


class Angel(Monsters):
    def __init__(self, path):
        super().__init__(path)
        self.width = 75
        self.height = 75  # 体积
        self.max_health = 20
        self.health = self.max_health  # 血量
        self.count_coin = 15  # 金币
        self.count_score = 50  # 分数
        self.v = 1.5  # 移动速度

        self.original_v = self.v

        self.path = path
        self.images = imgs6[:]

imgs7 = []
for x in range(18):
    add_str = str(x)
    if x < 10:
        add_str = "0" + add_str
    add_str = "0" + add_str
    imgs7.append(pygame.transform.scale(
        pygame.image.load(
            os.path.join("塔防游戏素材/怪物/光头小怪/Walking", "Golem_03_Walking_" + add_str + ".png")),
        (75, 75)))


class Gollem(Monsters):
    def __init__(self, path):
        super().__init__(path)
        self.width = 75
        self.height = 75  # 体积
        self.max_health = 20
        self.health = self.max_health  # 血量
        self.count_coin = 15  # 金币
        self.count_score = 50  # 分数
        self.v = 1.5  # 移动速度

        self.original_v = self.v

        self.path = path
        self.images = imgs7[:]

imgs8 = []
for x in range(24):
    add_str = str(x)
    if x < 10:
        add_str = "0" + add_str
    add_str = "0" + add_str
    imgs8.append(pygame.transform.scale(
        pygame.image.load(
            os.path.join("塔防游戏素材/怪物/火小怪/Walking", "0_Golem_Walking_" + add_str + ".png")),
        (75, 75)))


class Fire(Monsters):
    def __init__(self, path):
        super().__init__(path)
        self.width = 75
        self.height = 75  # 体积
        self.max_health = 20
        self.health = self.max_health  # 血量
        self.count_coin = 15  # 金币
        self.count_score = 50  # 分数
        self.v = 1.5  # 移动速度

        self.original_v = self.v

        self.path = path
        self.images = imgs8[:]


imgs9 = []
for x in range(18):
    add_str = str(x)
    if x < 10:
        add_str = "0" + add_str
    add_str = "0" + add_str
    imgs9.append(pygame.transform.scale(
        pygame.image.load(
            os.path.join("塔防游戏素材/怪物/海盗/Walking", "Minotaur_02_Walking_" + add_str + ".png")),
        (75, 75)))


class Minotaur(Monsters):
    def __init__(self, path):
        super().__init__(path)
        self.width = 75
        self.height = 75  # 体积
        self.max_health = 20
        self.health = self.max_health  # 血量
        self.count_coin = 15  # 金币
        self.count_score = 50  # 分数
        self.v = 1.5  # 移动速度

        self.original_v = self.v

        self.path = path
        self.images = imgs9[:]

imgs10 = []
for x in range(10):
    add_str = str(x)
    if x < 10:
        add_str = "0" + add_str
    add_str = "0" + add_str
    imgs10.append(pygame.transform.scale(
        pygame.image.load(
            os.path.join("塔防游戏素材/怪物/最终boss/Walking", "Walk_" + add_str + ".png")),
        (200, 120)))


class Final(Monsters):
    def __init__(self, path):
        super().__init__(path)
        self.width = 200
        self.height = 120  # 体积
        self.max_health = 200
        self.health = self.max_health  # 血量
        self.count_coin = 200  # 金币
        self.count_score = 500  # 分数
        self.v = 0.5  # 移动速度
        self.damage = 10

        self.original_v = self.v

        self.path = path
        self.images = imgs10[:]

    def draw(self, win):  # 怪物＋血条
        self.img = pygame.transform.scale(self.images[self.animation_count], (self.width, self.height))
        win.blit(self.img, (self.x - self.width / 2, self.y - self.height / 2-50))
        self.draw_health_bar(win)

    def draw_health_bar(self, win):  # 血条
        length = 135
        loseHP = length / self.max_health
        health_bar = loseHP * self.health
        pygame.draw.rect(win, (255, 0, 0), (self.x - self.width / 4 - 47, self.y - self.height * 3 / 4 - 18, length, 6),
                         0)
        pygame.draw.rect(win, (0, 255, 0),
                         (self.x - self.width / 4 - 47, self.y - self.height * 3 / 4 - 18, health_bar, 6), 0)
