import pygame
import os
import math


class Tower:

    def __init__(self, x, y):  # 在哪个点建造
        # 属性
        self.x = x
        self.y = y
        self.level = 1

        self.width = 0
        self.height = 0
        self.sell_price = [0, 0, 0]  # 需要花费的价钱
        self.price = [0, 0, 0]
        self.number = 1  # 建造的序号
        self.bottom_imgs = []
        self.top_imgs = []
        self.damage = 1
        self.tower_imgs = []
        self.archer_imgs = []
        self.archer_count = 0
        self.range = 150
        self.original_range = self.range

    def draw(self, win):  # 每个防御塔不一样
        pass


tower_imgs1 = []
for x in range(7, 10):
    tower_imgs1.append(pygame.transform.scale(
            pygame.image.load(os.path.join("塔防游戏素材/防御塔/archer_towers/archer_1", str(x) + ".png")),
            (90, 90)))
archer_imgs1 = []
for x in range(38, 50):
    archer_imgs1.append(
        pygame.image.load(os.path.join("塔防游戏素材/防御塔/archer_towers/archer_top", str(x) + ".png")))


class ArchTower(Tower):

    def __init__(self, x, y):
        super().__init__(x, y)
        self.tower_imgs = tower_imgs1[:]
        self.archer_imgs = archer_imgs1[:]

    def draw(self, win):
        img = self.tower_imgs[self.level - 1]
        win.blit(img, (self.x - img.get_width() / 2, self.y - img.get_height() / 2))
        # 这里后面改成攻击才动
        self.archer_count += 1
        if self.archer_count >= len(self.archer_imgs) * 10:
            self.archer_count = 0
        archer = self.archer_imgs[self.archer_count // 10]
        win.blit(archer, ((self.x - 25), (self.y - archer.get_height() - 25)))
        
     def attack(self, enemies):
        count = [0, 0]
        self.inRange = False
        enemy_inRange = []
        for enemy in enemies:
            x = enemy.x
            y = enemy.y
            dis = math.sqrt((self.x - x) ** 2 + (self.y - y) ** 2)  # distance
            if dis < self.range:
                self.inRange = True
                enemy_inRange.append(enemy)

        # 选定最近的一个敌人攻击
        enemy_inRange.sort(key=lambda x: -x.distance)
        if len(enemy_inRange) > 0:
            first_enemy = enemy_inRange[0]
            if time.time() - self.timer >= 0.5:
                self.timer = time.time()
                if first_enemy.die(self.damage):
                    count[0] = first_enemy.count_coin
                    count[1] = first_enemy.count_score
                    enemies.remove(first_enemy)
            # if first_enemy.x > self.x and not self.left:
            #     self.left = True
            #     for x, img in enumerate(self.archer_imgs):
            #         self.archer_imgs[x] = pygame.transform.flip(img, True, False)
            # elif self.left and first_enemy.x < self.x:
            #     self.left = False
            #     for x, img in enumerate(self.archer_imgs):
            #         self.archer_imgs[x] = pygame.transform.flip(img, True, False)

        return count
