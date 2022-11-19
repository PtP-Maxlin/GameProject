import pygame
import os
import math
import time
from bullet import *


class Tower:

    def __init__(self, x, y):  # 在哪个点建造
        # 属性
        self.x = x
        self.y = y
        self.level = 1
        self.timer = time.time()

        self.width = 0
        self.height = 0
        self.sell_price = [0, 0, 0]  # 需要花费的价钱
        self.price = [0, 0, 0]
        self.number = 1  # 建造的序号
        self.bottom_imgs = []
        self.top_imgs = []
        self.damage = 2
        self.range = 150
        self.original_range = self.range
        self.left = True

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
        self.tower_imgs = []
        self.archer_imgs = []
        self.archer_count = 0
        self.tower_imgs = tower_imgs1[:]
        self.archer_imgs = archer_imgs1[:]
        self.bullet = []

    def draw(self, win):
        img = self.tower_imgs[self.level - 1]
        win.blit(img, (self.x - img.get_width() / 2, self.y - img.get_height() / 2))
        # 这里后面改成攻击才动
        self.archer_count += 1
        if self.archer_count >= len(self.archer_imgs) * 10:
            self.archer_count = 0
        archer = self.archer_imgs[self.archer_count // 10]
        win.blit(archer, ((self.x - 25), (self.y - archer.get_height() - 25)))
        for bullet in self.bullet:
            bullet.draw(win)

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
                self.bullet.append(ArcherBullet(self.x, self.y, first_enemy))
        for bullet in self.bullet:
            if bullet.move():
                if bullet.target.die(self.damage):
                    count[0] = bullet.target.count_coin
                    count[1] = bullet.target.count_score
                    enemies.remove(bullet.target)
                self.bullet.remove(bullet)
        return count


turret_imgs1 = []
for x in range(5, 8):
    turret_imgs1.append(pygame.transform.scale(
        pygame.image.load(os.path.join("塔防游戏素材/防御塔/投石塔", str(x) + ".png")),
        (90, 90)))
turret_imgs2 = []
for x in range(12, 15):
    turret_imgs2.append(pygame.transform.scale(
        pygame.image.load(os.path.join("塔防游戏素材/防御塔/投石塔", str(x) + ".png")),
        (90, 90)))


class TurretTower(Tower):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.count = 0
        self.move = 0.5
        self.damage = 10
        self.attack_range = self.range / 3
        self.bottom_imgs = turret_imgs1[:]
        self.top_imgs = turret_imgs2[:]
        self.bullet = []

    def draw(self, win):
        bottom = self.bottom_imgs[self.level - 1]
        win.blit(bottom, (self.x - bottom.get_width() / 2, self.y - bottom.get_height() / 2))
        # 这里后面改成攻击才动
        self.count += self.move
        if self.count >= 10 or self.count <= -10:
            self.move = -self.move
        top = self.top_imgs[self.level - 1]
        win.blit(top, (self.x - 45, (self.y - top.get_height() + 10 + self.count)))
        for bullet in self.bullet:
            bullet.draw(win)

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
            if time.time() - self.timer >= 2:
                self.timer = time.time()
                self.bullet.append(TurretBullet(self.x, self.y, first_enemy))
        for bullet in self.bullet:
            if bullet.move():
                bullet.getAttackTarget(enemies, self.attack_range)
                for enemy in bullet.enemy_toAttack:
                    if enemy.die(self.damage):
                        count[0] = enemy.count_coin
                        count[1] = enemy.count_score
                        enemies.remove(enemy)
                self.bullet.remove(bullet)
        return count

    
class SlowTower(Tower):

    def __init__(self, x, y):
        super().__init__(x, y)
        self.tower_img = pygame.transform.scale(pygame.image.load
                                                ("塔防游戏素材/防御塔/archer_towers/support/18.png"), (90, 90))
        self.slow = 0.5

    def draw(self, win):
        img = self.tower_img
        win.blit(img, (self.x - img.get_width() / 2, self.y - img.get_height() / 2))

    def attack(self, enemies):
        for enemy in enemies:
            x = enemy.x
            y = enemy.y
            dis = math.sqrt((self.x - x) ** 2 + (self.y - y) ** 2)  # distance
            if dis < self.range:
                enemy.v = enemy.original_v * self.slow
            else:
                enemy.v = enemy.original_v
        return [0, 0]
