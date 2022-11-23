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

        '''新增菜单'''
        self.level = 1
        self.upgrade_price = 100
        self.sell_price = 50
        self.rect = pygame.Rect(x, y, 90, 90)

        self.menu = pygame.image.load("塔防游戏素材/按钮/菜单2.png")
        self.menu = pygame.transform.smoothscale(self.menu, (160, 90))
        self.menu_rect = self.menu.get_rect()
        self.upgrade = pygame.image.load("塔防游戏素材/按钮/升级.png")
        self.upgrade = pygame.transform.smoothscale(self.upgrade, (46, 40))
        self.upgrade_rect = self.upgrade.get_rect()
        self.sell = pygame.image.load("塔防游戏素材/按钮/拆除.png")
        self.sell = pygame.transform.smoothscale(self.sell, (46, 40))
        self.sell_rect = self.sell.get_rect()
        self.bool = True
        self.selected = [False, False]
        self.menu_on = True

    def draw(self, win):  # 每个防御塔不一样
        pass

    def draw_menu(self, win, x2, y2):
        self.menu_rect.x = x2 - 5
        self.menu_rect.y = y2 + 50
        self.upgrade_rect.x = self.menu_rect.x + 55
        self.upgrade_rect.y = self.menu_rect.y + 0
        self.sell_rect.x = self.menu_rect.x + 55
        self.sell_rect.y = self.menu_rect.y + 50

        win.blit(self.menu, self.menu_rect)
        win.blit(self.upgrade, self.upgrade_rect)
        win.blit(self.sell, self.sell_rect)

    def click_tower(self, mouse_pos, rect):
        click = rect.collidepoint(mouse_pos)
        if click:
            self.menu_on = not self.menu_on
            self.bool = self.menu_on
        elif not self.click_menu(mouse_pos):
            self.bool = True
            self.menu_on = True
        elif self.click_menu(mouse_pos) and True not in self.selected:
            self.bool = True
            self.menu_on = True

    def click_menu(self, mouse_pos):
        if not self.bool:
            menu_on = self.menu_rect.collidepoint(mouse_pos)
            if menu_on:
                self.menu_on = not self.menu_on
                self.selected = [self.click_upgrade(mouse_pos), self.click_sell(mouse_pos)]

        return self.menu_on

    def click_upgrade(self, mouse_pos):
        click = self.upgrade_rect.collidepoint(mouse_pos)
        if click:
            return True
        else:
            return False

    def click_sell(self, mouse_pos):
        click = self.sell_rect.collidepoint(mouse_pos)
        if click:
            return True
        else:
            return False

    def flush(self):
        self.menu_on = True
        self.bool = True
        self.selected = [False, False]


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

        self.upgrade_price = 100
        self.sell_price = 50

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
            self.archer_count += 1
            if self.archer_count >= len(self.archer_imgs) * 10:
                self.archer_count = 0
            first_enemy = enemy_inRange[0]
            if time.time() - self.timer >= 0.5:
                self.timer = time.time()
                self.bullet.append(ArcherBullet(self.x, self.y, first_enemy))
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
        self.damage = 5
        self.attack_range = self.range
        self.bottom_imgs = turret_imgs1[:]
        self.top_imgs = turret_imgs2[:]
        self.bullet = []

        self.upgrade_price = 100
        self.sell_price = 50

    def draw(self, win):
        bottom = self.bottom_imgs[self.level - 1]
        win.blit(bottom, (self.x - bottom.get_width() / 2, self.y - bottom.get_height() / 2))
        # 这里后面改成攻击才动
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
            if time.time() - self.timer >= 2:
                self.timer = time.time()
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
                                                ("塔防游戏素材/防御塔/冰霜塔/冰霜塔1.png"), (100, 90))
        self.tower_img2 = pygame.transform.scale(pygame.image.load
                                                ("塔防游戏素材/防御塔/冰霜塔/冰霜塔2.png"), (100, 100))
        self.slow = 0.5

        self.upgrade_price = 100
        self.sell_price = 50

    def draw(self, win):
        if self.level == 1:
            img = self.tower_img
        else:
            img = self.tower_img2
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
                                                ("塔防游戏素材/防御塔/毒/毒气塔.png"), (90, 90))
        self.tower_img2 = pygame.transform.scale(pygame.image.load
                                                ("塔防游戏素材/防御塔/毒/毒气塔2.png"), (90, 100))

        self.upgrade_price = 100
        self.sell_price = 50

    def draw(self, win):
        if self.level == 1:
            img = self.tower_img
        else:
            img = self.tower_img2
        win.blit(img, (self.x - img.get_width() / 2, self.y - img.get_height() / 2))

    def attack(self, enemies):
        count = [0, 0]
        enemies_in = []
        for enemy in enemies:
            x = enemy.x
            y = enemy.y
            dis = math.sqrt((self.x - x) ** 2 + (self.y - y) ** 2)  # distance
            if dis <= self.range:
                enemies_in.append(enemy)
            if dis > self.range and enemy in enemies_in:
                enemies_in.remove(enemy)

        for enemy in enemies:
            self.damage = enemy.max_health / 10
            if time.time() - self.timer > 1:
                self.timer = time.time()
                for e in enemies_in:
                    if e.die(self.damage):
                        if e in enemies:
                            enemies.remove(e)
                            enemies_in.remove(e)
                            count[0] += e.count_coin
                            count[1] += e.count_score

        return count
