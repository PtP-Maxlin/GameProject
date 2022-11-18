import pygame
import os
import math


class Bullet:

    def __init__(self, x, y, target):
        self.g = 10
        self.v = 10
        self.img = pygame.Surface((50, 50), flags=pygame.HWSURFACE)
        self.x = x
        self.y = y
        self.level = 1
        self.target = target

    def draw(self, win):
        pass

    def move(self):
        dirn = (self.target.x - self.x, self.target.y - self.y)
        length = math.sqrt(math.pow(dirn[0], 2) + math.pow(dirn[1], 2))
        if length <= 2 * self.v:
            return True
        dirn = (dirn[0] / length, dirn[1] / length)
        self.x += dirn[0] * self.v
        self.y += dirn[1] * self.v
        return False


bullet_imgs1 = []
bullet_imgs1.append(pygame.transform.scale(
        pygame.image.load(os.path.join("塔防游戏素材/防御塔/投石塔", "35.png")),
        (30, 30)))
bullet_imgs1.append(pygame.transform.scale(
        pygame.image.load(os.path.join("塔防游戏素材/防御塔/投石塔", "40.png")),
        (30, 30)))
bullet_imgs1.append(pygame.transform.scale(
        pygame.image.load(os.path.join("塔防游戏素材/防御塔/投石塔", "45.png")),
        (30, 30)))


class TurretBullet(Bullet):
    def __init__(self, x, y, target):
        super().__init__(x, y, target)
        self.enemy_toAttack = []

    def getAttackTarget(self, enemies, attack_range):
        for enemy in enemies:
            x = enemy.x
            y = enemy.y
            dis = math.sqrt((self.target.x - x) ** 2 + (self.target.y - y) ** 2)
            if dis < attack_range:
                self.enemy_toAttack.append(enemy)

    def draw(self, win):
        self.img = bullet_imgs1[self.level - 1]
        win.blit(self.img, (self.x, self.y))

bullet_imgs2 = []
bullet_imgs2.append(pygame.transform.scale(
        pygame.image.load(os.path.join("塔防游戏素材/防御塔/archer_towers/archer_top", "35.png")),
        (30, 30)))


class ArcherBullet(Bullet):
    def __init__(self, x, y, target):
        super().__init__(x, y, target)

    def draw(self, win):
        self.img = bullet_imgs2[self.level - 1]
        win.blit(self.img, (self.x, self.y))