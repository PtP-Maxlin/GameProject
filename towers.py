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

        self.width = 90
        self.height = 90
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
        self.damage = 2
        self.range = 200
        self.tower_imgs = []
        self.archer_imgs = []
        self.archer_count = 0
        self.tower_imgs = tower_imgs1[:]
        self.archer_imgs = archer_imgs1[:]
        self.bullet = []
        self.width = 90
        self.height = 110

    def draw(self, win):
        img = self.tower_imgs[self.level - 1]
        win.blit(img, (self.x - img.get_width() / 2, self.y - img.get_height() / 2))
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
            self.archer_count += 3
            if self.archer_count >= len(self.archer_imgs) * 10:
                self.archer_count = 0
            first_enemy = enemy_inRange[0]
            if first_enemy.x > self.x and not (self.left):
                self.left = True
                for x, img in enumerate(self.archer_imgs):
                    self.archer_imgs[x] = pygame.transform.flip(img, True, False)
            elif self.left and first_enemy.x < self.x:
                self.left = False
                for x, img in enumerate(self.archer_imgs):
                    self.archer_imgs[x] = pygame.transform.flip(img, True, False)
            if self.archer_count == 30:
                self.bullet.append(ArcherBullet(self.x, self.y - 25, first_enemy))
        else:
            self.archer_count = 0
        for bullet in self.bullet:
            if bullet.move():
                if bullet.target.die(self.damage) and bullet.target in enemies:
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
        self.damage = 3
        self.attack_range = self.range
        self.bottom_imgs = turret_imgs1[:]
        self.top_imgs = turret_imgs2[:]
        self.tcount = 0
        self.bullet = []
        self.width = 90
        self.height = 90

    def draw(self, win):
        bottom = self.bottom_imgs[self.level - 1]
        win.blit(bottom, (self.x - bottom.get_width() / 2, self.y - bottom.get_height() / 2))
        top = self.top_imgs[self.level - 1]
        win.blit(top, (self.x - 45, (self.y - top.get_height() + 10 + self.count)))
        for bullet in self.bullet:
            bullet.draw(win)

    def attack(self, enemies):
        count = [0, 0]
        self.count += self.move
        if self.count >= 10 or self.count <= -10:
            self.move = -self.move
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
            if self.count == 10:
                self.bullet.append(TurretBullet(self.x, self.y, first_enemy))
        for bullet in self.bullet:
            if bullet.move():
                bullet.getAttackTarget(enemies, self.attack_range)
                for enemy in bullet.enemy_toAttack:
                    if enemy.die(self.damage):
                        if enemy in enemies:
                            enemies.remove(enemy)
                        count[0] += enemy.count_coin
                        count[1] += enemy.count_score
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
        enemy_inRange = []
        for enemy in enemies:
            x = enemy.x
            y = enemy.y
            dis = math.sqrt((self.x - x) ** 2 + (self.y - y) ** 2)  # distance
            if dis < self.range:
                enemy.v = enemy.original_v * self.slow
        return [0, 0]

class PoisonTower(Tower):

    def __init__(self, x, y):
        super().__init__(x, y)
        self.tower_img = pygame.transform.scale(pygame.image.load
                                                ("塔防游戏素材/防御塔/archer_towers/support/18.png"), (90, 90))

    def draw(self, win):
        img = self.tower_img
        win.blit(img, (self.x - img.get_width() / 2, self.y - img.get_height() / 2))

    def attack(self, enemies):
        for enemy in enemies:
            x = enemy.x
            y = enemy.y
            dis = math.sqrt((self.x - x) ** 2 + (self.y - y) ** 2)  # distance
            if dis < self.range:
                enemy.last = 500
        return [0, 0]
