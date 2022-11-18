import pygame


class Hole_1_1:
    def __init__(self):
        self.hole = pygame.image.load('塔防游戏素材/按钮/坑1.jpg')
        self.hole_menu = pygame.image.load('塔防游戏素材/按钮/建造2.png')
        self.hole = pygame.transform.smoothscale(self.hole, (130, 58))
        self.hole_menu = pygame.transform.smoothscale(self.hole_menu, (150, 130))
        self.hole_menu_rect = self.hole_menu.get_rect()
        self.hole_rect = self.hole.get_rect()
        self.hole_menu_rect.x = 20
        self.hole_menu_rect.y = 310
        self.hole_rect.x = 25
        self.hole_rect.y = 435
        self.menu = True

    def draw(self, win):
        win.blit(self.hole, self.hole_rect)

    def drawmenu(self, win):
        win.blit(self.hole_menu, self.hole_menu_rect)

    def click_hole(self, mouse_pos):
        hole = self.hole_rect.collidepoint(mouse_pos)
        if hole:
            self.menu = not self.menu
        return self.menu

    def click_menu(self, mouse_pos):
        menu = self.hole_menu_rect.collidepoint(mouse_pos)
        if menu:
            self.menu = not self.menu
        return self.menu


    def flush(self):
        self.menu = True


class Hole_1_2:
    def __init__(self):
        self.hole = pygame.image.load('塔防游戏素材/按钮/坑1.jpg')
        self.hole_menu = pygame.image.load('塔防游戏素材/按钮/建造2.png')
        self.hole = pygame.transform.smoothscale(self.hole, (130, 58))
        self.hole_menu = pygame.transform.smoothscale(self.hole_menu, (150, 130))
        self.hole_menu_rect = self.hole_menu.get_rect()
        self.hole_rect = self.hole.get_rect()
        self.hole_menu_rect.x = 280
        self.hole_menu_rect.y = 286
        self.hole_rect.x = 285
        self.hole_rect.y = 411
        self.menu = True

    def draw(self, win):
        win.blit(self.hole, self.hole_rect)

    def drawmenu(self, win):
        win.blit(self.hole_menu, self.hole_menu_rect)

    def click_hole(self, mouse_pos):
        hole = self.hole_rect.collidepoint(mouse_pos)
        if hole:
            self.menu = not self.menu
        return self.menu

    def click_menu(self, mouse_pos):
        menu = self.hole_menu_rect.collidepoint(mouse_pos)
        if menu:
            self.menu = not self.menu
        return self.menu

    def flush(self):
        self.menu = True

class Hole_1_3:
    def __init__(self):
        self.hole = pygame.image.load('塔防游戏素材/按钮/坑1.jpg')
        self.hole_menu = pygame.image.load('塔防游戏素材/按钮/建造2.png')
        self.hole = pygame.transform.smoothscale(self.hole, (130, 58))
        self.hole_menu = pygame.transform.smoothscale(self.hole_menu, (150, 130))
        self.hole_menu_rect = self.hole_menu.get_rect()
        self.hole_rect = self.hole.get_rect()
        self.hole_menu_rect.x = 507
        self.hole_menu_rect.y = 50
        self.hole_rect.x = 512
        self.hole_rect.y = 175
        self.menu = True

    def draw(self, win):
        win.blit(self.hole, self.hole_rect)

    def drawmenu(self, win):
        win.blit(self.hole_menu, self.hole_menu_rect)

    def click_hole(self, mouse_pos):
        hole = self.hole_rect.collidepoint(mouse_pos)
        if hole:
            self.menu = not self.menu
        return self.menu

    def click_menu(self, mouse_pos):
        menu = self.hole_menu_rect.collidepoint(mouse_pos)
        if menu:
            self.menu = not self.menu
        return self.menu

    def flush(self):
        self.menu = True

class Hole_1_4:
    def __init__(self):
        self.hole = pygame.image.load('塔防游戏素材/按钮/坑1.jpg')
        self.hole_menu = pygame.image.load('塔防游戏素材/按钮/建造2.png')
        self.hole = pygame.transform.smoothscale(self.hole, (130, 58))
        self.hole_menu = pygame.transform.smoothscale(self.hole_menu, (150, 130))
        self.hole_menu_rect = self.hole_menu.get_rect()
        self.hole_rect = self.hole.get_rect()
        self.hole_menu_rect.x = 736
        self.hole_menu_rect.y = 256
        self.hole_rect.x = 741
        self.hole_rect.y = 381
        self.menu = True

    def draw(self, win):
        win.blit(self.hole, self.hole_rect)

    def drawmenu(self, win):
        win.blit(self.hole_menu, self.hole_menu_rect)

    def click_hole(self, mouse_pos):
        hole = self.hole_rect.collidepoint(mouse_pos)
        if hole:
            self.menu = not self.menu
        return self.menu

    def click_menu(self, mouse_pos):
        menu = self.hole_menu_rect.collidepoint(mouse_pos)
        if menu:
            self.menu = not self.menu
        return self.menu

    def flush(self):
        self.menu = True

class Hole_1_5:
    def __init__(self):
        self.hole = pygame.image.load('塔防游戏素材/按钮/坑1.jpg')
        self.hole_menu = pygame.image.load('塔防游戏素材/按钮/建造2.png')
        self.hole = pygame.transform.smoothscale(self.hole, (130, 58))
        self.hole_menu = pygame.transform.smoothscale(self.hole_menu, (150, 130))
        self.hole_menu_rect = self.hole_menu.get_rect()
        self.hole_rect = self.hole.get_rect()
        self.hole_menu_rect.x = 949
        self.hole_menu_rect.y = 59
        self.hole_rect.x = 954
        self.hole_rect.y = 184
        self.menu = True

    def draw(self, win):
        win.blit(self.hole, self.hole_rect)

    def drawmenu(self, win):
        win.blit(self.hole_menu, self.hole_menu_rect)

    def click_hole(self, mouse_pos):
        hole = self.hole_rect.collidepoint(mouse_pos)
        if hole:
            self.menu = not self.menu
        return self.menu

    def click_menu(self, mouse_pos):
        menu = self.hole_menu_rect.collidepoint(mouse_pos)
        if menu:
            self.menu = not self.menu
        return self.menu

    def flush(self):
        self.menu = True

class Hole_1_6:
    def __init__(self):
        self.hole = pygame.image.load('塔防游戏素材/按钮/坑1.jpg')
        self.hole_menu = pygame.image.load('塔防游戏素材/按钮/建造2.png')
        self.hole = pygame.transform.smoothscale(self.hole, (130, 58))
        self.hole_menu = pygame.transform.smoothscale(self.hole_menu, (150, 130))
        self.hole_menu_rect = self.hole_menu.get_rect()
        self.hole_rect = self.hole.get_rect()
        self.hole_menu_rect.x = 1003
        self.hole_menu_rect.y = 293
        self.hole_rect.x = 1008
        self.hole_rect.y = 418
        self.menu = True

    def draw(self, win):
        win.blit(self.hole, self.hole_rect)

    def drawmenu(self, win):
        win.blit(self.hole_menu, self.hole_menu_rect)

    def click_hole(self, mouse_pos):
        hole = self.hole_rect.collidepoint(mouse_pos)
        if hole:
            self.menu = not self.menu
        return self.menu

    def click_menu(self, mouse_pos):
        menu = self.hole_menu_rect.collidepoint(mouse_pos)
        if menu:
            self.menu = not self.menu
        return self.menu

    def flush(self):
        self.menu = True

class Hole_1_7:
    def __init__(self):
        self.hole = pygame.image.load('塔防游戏素材/按钮/坑1.jpg')
        self.hole_menu = pygame.image.load('塔防游戏素材/按钮/建造2.png')
        self.hole = pygame.transform.smoothscale(self.hole, (130, 58))
        self.hole_menu = pygame.transform.smoothscale(self.hole_menu, (150, 130))
        self.hole_menu_rect = self.hole_menu.get_rect()
        self.hole_rect = self.hole.get_rect()
        self.hole_menu_rect.x = 960
        self.hole_menu_rect.y = 515
        self.hole_rect.x = 965
        self.hole_rect.y = 640
        self.menu = True

    def draw(self, win):
        win.blit(self.hole, self.hole_rect)

    def drawmenu(self, win):
        win.blit(self.hole_menu, self.hole_menu_rect)

    def click_hole(self, mouse_pos):
        hole = self.hole_rect.collidepoint(mouse_pos)
        if hole:
            self.menu = not self.menu
        return self.menu

    def click_menu(self, mouse_pos):
        menu = self.hole_menu_rect.collidepoint(mouse_pos)
        if menu:
            self.menu = not self.menu
        return self.menu

    def flush(self):
        self.menu = True
