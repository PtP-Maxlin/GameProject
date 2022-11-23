import pygame


class Hole:
    def __init__(self, x, y):
        self.hole = pygame.image.load('塔防游戏素材/按钮/坑1.jpg')
        self.hole_menu = pygame.image.load('塔防游戏素材/按钮/建造2.png')
        self.hole_menu_tower1 = pygame.image.load('塔防游戏素材/按钮/选项1.png')
        self.hole_menu_tower2 = pygame.image.load('塔防游戏素材/按钮/选项2.png')
        self.hole_menu_tower3 = pygame.image.load('塔防游戏素材/按钮/选项3.png')
        self.hole_menu_tower4 = pygame.image.load('塔防游戏素材/按钮/选项4.png')

        self.hole = pygame.transform.smoothscale(self.hole, (130, 58))
        self.hole_menu = pygame.transform.smoothscale(self.hole_menu, (150, 130))
        self.hole_menu_tower1 = pygame.transform.smoothscale(self.hole_menu_tower1, (46, 40))
        self.hole_menu_tower2 = pygame.transform.smoothscale(self.hole_menu_tower2, (46, 40))
        self.hole_menu_tower3 = pygame.transform.smoothscale(self.hole_menu_tower3, (46, 40))
        self.hole_menu_tower4 = pygame.transform.smoothscale(self.hole_menu_tower4, (46, 40))

        self.hole_rect = self.hole.get_rect()
        self.hole_menu_rect = self.hole_menu.get_rect()
        self.hole_menu_tower1_rect = self.hole_menu_tower1.get_rect()
        self.hole_menu_tower2_rect = self.hole_menu_tower2.get_rect()
        self.hole_menu_tower3_rect = self.hole_menu_tower3.get_rect()
        self.hole_menu_tower4_rect = self.hole_menu_tower4.get_rect()
        # x, y 改一下
        self.hole_rect.x = x
        self.hole_rect.y = y
        self.hole_menu_rect.x = self.hole_rect.x - 5
        self.hole_menu_rect.y = self.hole_rect.y - 130
        self.hole_menu_tower1_rect.x = self.hole_rect.x - 1
        self.hole_menu_tower1_rect.y = self.hole_rect.y - 115
        self.hole_menu_tower2_rect.x = self.hole_rect.x + 96
        self.hole_menu_tower2_rect.y = self.hole_rect.y - 115
        self.hole_menu_tower3_rect.x = self.hole_rect.x - 1
        self.hole_menu_tower3_rect.y = self.hole_rect.y - 42
        self.hole_menu_tower4_rect.x = self.hole_rect.x + 96
        self.hole_menu_tower4_rect.y = self.hole_rect.y - 42

        self.menu = True
        self.lock = True
        self.bool = True
        self.selected = [False, False, False, False]

    def draw(self, win):
        win.blit(self.hole, self.hole_rect)

    def drawmenu(self, win):
        win.blit(self.hole_menu, self.hole_menu_rect)
        win.blit(self.hole_menu_tower1, self.hole_menu_tower1_rect)
        win.blit(self.hole_menu_tower2, self.hole_menu_tower2_rect)
        win.blit(self.hole_menu_tower3, self.hole_menu_tower3_rect)
        win.blit(self.hole_menu_tower4, self.hole_menu_tower4_rect)

    def click_tower1(self, mouse_pos):
        click = self.hole_menu_tower1_rect.collidepoint(mouse_pos)
        if click:
            return True
        else:
            return False

    def click_tower2(self, mouse_pos):
        click = self.hole_menu_tower2_rect.collidepoint(mouse_pos)
        if click:
            return True
        else:
            return False

    def click_tower3(self, mouse_pos):
        click = self.hole_menu_tower3_rect.collidepoint(mouse_pos)
        if click:
            return True
        else:
            return False

    def click_tower4(self, mouse_pos):
        click = self.hole_menu_tower4_rect.collidepoint(mouse_pos)
        if click:
            return True
        else:
            return False

    def click_hole(self, mouse_pos):
        hole = self.hole_rect.collidepoint(mouse_pos)
        if hole:
            self.menu = not self.menu
            self.bool = self.menu
        elif not self.click_menu(mouse_pos):
            self.bool = True
            self.menu = True
        elif self.click_menu(mouse_pos) and True not in self.selected:
            self.bool = True
            self.menu = True

    def click_menu(self, mouse_pos):
        if not self.bool:
            menu = self.hole_menu_rect.collidepoint(mouse_pos)
            if menu:
                self.menu = not self.menu
                self.selected = [self.click_tower1(mouse_pos), self.click_tower2(mouse_pos),
                                 self.click_tower3(mouse_pos), self.click_tower4(mouse_pos)]

        return self.menu

    def flush(self):
        self.menu = True
        self.lock = True
        self.bool = True
        self.selected = [False, False, False, False]


class Hole2:
    def __init__(self, x, y):
        self.hole = pygame.image.load('塔防游戏素材/按钮/坑2.png')
        self.hole_menu = pygame.image.load('塔防游戏素材/按钮/建造2.png')
        self.hole_menu_tower1 = pygame.image.load('塔防游戏素材/按钮/选项1.png')
        self.hole_menu_tower2 = pygame.image.load('塔防游戏素材/按钮/选项2.png')
        self.hole_menu_tower3 = pygame.image.load('塔防游戏素材/按钮/选项3.png')
        self.hole_menu_tower4 = pygame.image.load('塔防游戏素材/按钮/选项4.png')

        self.hole = pygame.transform.smoothscale(self.hole, (75, 58))
        self.hole_menu = pygame.transform.smoothscale(self.hole_menu, (150, 130))
        self.hole_menu_tower1 = pygame.transform.smoothscale(self.hole_menu_tower1, (46, 40))
        self.hole_menu_tower2 = pygame.transform.smoothscale(self.hole_menu_tower2, (46, 40))
        self.hole_menu_tower3 = pygame.transform.smoothscale(self.hole_menu_tower3, (46, 40))
        self.hole_menu_tower4 = pygame.transform.smoothscale(self.hole_menu_tower4, (46, 40))

        self.hole_rect = self.hole.get_rect()
        self.hole_menu_rect = self.hole_menu.get_rect()
        self.hole_menu_tower1_rect = self.hole_menu_tower1.get_rect()
        self.hole_menu_tower2_rect = self.hole_menu_tower2.get_rect()
        self.hole_menu_tower3_rect = self.hole_menu_tower3.get_rect()
        self.hole_menu_tower4_rect = self.hole_menu_tower4.get_rect()
        # x, y 改一下
        self.hole_rect.x = x
        self.hole_rect.y = y
        self.hole_menu_rect.x = self.hole_rect.x - 35
        self.hole_menu_rect.y = self.hole_rect.y - 130
        self.hole_menu_tower1_rect.x = self.hole_rect.x - 31
        self.hole_menu_tower1_rect.y = self.hole_rect.y - 115
        self.hole_menu_tower2_rect.x = self.hole_rect.x + 66
        self.hole_menu_tower2_rect.y = self.hole_rect.y - 115
        self.hole_menu_tower3_rect.x = self.hole_rect.x - 31
        self.hole_menu_tower3_rect.y = self.hole_rect.y - 42
        self.hole_menu_tower4_rect.x = self.hole_rect.x + 66
        self.hole_menu_tower4_rect.y = self.hole_rect.y - 42

        self.menu = True
        self.lock = True
        self.bool = True
        self.selected = [False, False, False, False]

    def draw(self, win):
        win.blit(self.hole, self.hole_rect)

    def drawmenu(self, win):
        win.blit(self.hole_menu, self.hole_menu_rect)
        win.blit(self.hole_menu_tower1, self.hole_menu_tower1_rect)
        win.blit(self.hole_menu_tower2, self.hole_menu_tower2_rect)
        win.blit(self.hole_menu_tower3, self.hole_menu_tower3_rect)
        win.blit(self.hole_menu_tower4, self.hole_menu_tower4_rect)

    def click_tower1(self, mouse_pos):
        click = self.hole_menu_tower1_rect.collidepoint(mouse_pos)
        if click:
            return True
        else:
            return False

    def click_tower2(self, mouse_pos):
        click = self.hole_menu_tower2_rect.collidepoint(mouse_pos)
        if click:
            return True
        else:
            return False

    def click_tower3(self, mouse_pos):
        click = self.hole_menu_tower3_rect.collidepoint(mouse_pos)
        if click:
            return True
        else:
            return False

    def click_tower4(self, mouse_pos):
        click = self.hole_menu_tower4_rect.collidepoint(mouse_pos)
        if click:
            return True
        else:
            return False

    def click_hole(self, mouse_pos):
        hole = self.hole_rect.collidepoint(mouse_pos)
        if hole:
            self.menu = not self.menu
            self.bool = self.menu
        elif not self.click_menu(mouse_pos):
            self.bool = True
            self.menu = True
        elif self.click_menu(mouse_pos) and True not in self.selected:
            self.bool = True
            self.menu = True

    def click_menu(self, mouse_pos):
        if not self.bool:
            menu = self.hole_menu_rect.collidepoint(mouse_pos)
            if menu:
                self.menu = not self.menu
                self.selected = [self.click_tower1(mouse_pos), self.click_tower2(mouse_pos),
                                 self.click_tower3(mouse_pos), self.click_tower4(mouse_pos)]

        return self.menu

    def flush(self):
        self.menu = True
        self.lock = True
        self.bool = True
        self.selected = [False, False, False, False]


class Hole3:
    def __init__(self, x, y):
        self.hole = pygame.image.load('塔防游戏素材/按钮/坑3改.png')
        self.hole_menu = pygame.image.load('塔防游戏素材/按钮/建造2.png')
        self.hole_menu_tower1 = pygame.image.load('塔防游戏素材/按钮/选项1.png')
        self.hole_menu_tower2 = pygame.image.load('塔防游戏素材/按钮/选项2.png')
        self.hole_menu_tower3 = pygame.image.load('塔防游戏素材/按钮/选项3.png')
        self.hole_menu_tower4 = pygame.image.load('塔防游戏素材/按钮/选项4.png')

        self.hole = pygame.transform.smoothscale(self.hole, (80, 60))
        self.hole_menu = pygame.transform.smoothscale(self.hole_menu, (150, 130))
        self.hole_menu_tower1 = pygame.transform.smoothscale(self.hole_menu_tower1, (46, 40))
        self.hole_menu_tower2 = pygame.transform.smoothscale(self.hole_menu_tower2, (46, 40))
        self.hole_menu_tower3 = pygame.transform.smoothscale(self.hole_menu_tower3, (46, 40))
        self.hole_menu_tower4 = pygame.transform.smoothscale(self.hole_menu_tower4, (46, 40))

        self.hole_rect = self.hole.get_rect()
        self.hole_menu_rect = self.hole_menu.get_rect()
        self.hole_menu_tower1_rect = self.hole_menu_tower1.get_rect()
        self.hole_menu_tower2_rect = self.hole_menu_tower2.get_rect()
        self.hole_menu_tower3_rect = self.hole_menu_tower3.get_rect()
        self.hole_menu_tower4_rect = self.hole_menu_tower4.get_rect()
        # x, y 改一下
        self.hole_rect.x = x
        self.hole_rect.y = y + 10
        self.hole_menu_rect.x = self.hole_rect.x - 32
        self.hole_menu_rect.y = self.hole_rect.y - 130
        self.hole_menu_tower1_rect.x = self.hole_rect.x - 28
        self.hole_menu_tower1_rect.y = self.hole_rect.y - 115
        self.hole_menu_tower2_rect.x = self.hole_rect.x + 69
        self.hole_menu_tower2_rect.y = self.hole_rect.y - 115
        self.hole_menu_tower3_rect.x = self.hole_rect.x - 28
        self.hole_menu_tower3_rect.y = self.hole_rect.y - 42
        self.hole_menu_tower4_rect.x = self.hole_rect.x + 69
        self.hole_menu_tower4_rect.y = self.hole_rect.y - 42

        self.menu = True
        self.lock = True
        self.bool = True
        self.selected = [False, False, False, False]

    def draw(self, win):
        win.blit(self.hole, self.hole_rect)

    def drawmenu(self, win):
        win.blit(self.hole_menu, self.hole_menu_rect)
        win.blit(self.hole_menu_tower1, self.hole_menu_tower1_rect)
        win.blit(self.hole_menu_tower2, self.hole_menu_tower2_rect)
        win.blit(self.hole_menu_tower3, self.hole_menu_tower3_rect)
        win.blit(self.hole_menu_tower4, self.hole_menu_tower4_rect)

    def click_tower1(self, mouse_pos):
        click = self.hole_menu_tower1_rect.collidepoint(mouse_pos)
        if click:
            return True
        else:
            return False

    def click_tower2(self, mouse_pos):
        click = self.hole_menu_tower2_rect.collidepoint(mouse_pos)
        if click:
            return True
        else:
            return False

    def click_tower3(self, mouse_pos):
        click = self.hole_menu_tower3_rect.collidepoint(mouse_pos)
        if click:
            return True
        else:
            return False

    def click_tower4(self, mouse_pos):
        click = self.hole_menu_tower4_rect.collidepoint(mouse_pos)
        if click:
            return True
        else:
            return False

    def click_hole(self, mouse_pos):
        hole = self.hole_rect.collidepoint(mouse_pos)
        if hole:
            self.menu = not self.menu
            self.bool = self.menu
        elif not self.click_menu(mouse_pos):
            self.bool = True
            self.menu = True
        elif self.click_menu(mouse_pos) and True not in self.selected:
            self.bool = True
            self.menu = True

    def click_menu(self, mouse_pos):
        if not self.bool:
            menu = self.hole_menu_rect.collidepoint(mouse_pos)
            if menu:
                self.menu = not self.menu
                self.selected = [self.click_tower1(mouse_pos), self.click_tower2(mouse_pos),
                                 self.click_tower3(mouse_pos), self.click_tower4(mouse_pos)]

        return self.menu

    def flush(self):
        self.menu = True
        self.lock = True
        self.bool = True
        self.selected = [False, False, False, False]
