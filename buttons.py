import pygame

''' 游戏开始的按钮类 '''
''' 设定按钮的大小，初始位置等属性'''


class PlayButton:
    def __init__(self):
        self.play_button = pygame.image.load('塔防游戏素材/按钮/开始游戏.png')
        self.width = 441
        self.height = 133
        self.play_button = pygame.transform.scale(self.play_button, (self.width, self.height))
        self.rect = self.play_button.get_rect()
        self.rect.midbottom = (700, 750 - 2 * self.height)

    ''' 渲染按钮图标 '''

    def draw(self, win):
        win.blit(self.play_button, self.rect)


''' 退出界面的按钮类 '''


class ExitButton:
    def __init__(self):
        self.exit_button = pygame.image.load('塔防游戏素材/按钮/退出.png')
        self.width = self.exit_button.get_width()
        self.height = self.exit_button.get_height()
        self.play_button = pygame.transform.scale(self.exit_button, (self.width, self.height))
        self.rect = self.exit_button.get_rect()
        self.rect.midbottom = (700, 750 - self.height + 50)

    def draw(self, win):
        win.blit(self.exit_button, self.rect)


''' 开关音乐的按钮类 '''


class MusicButton:
    def __init__(self):
        self.music_on_button = pygame.image.load('塔防游戏素材/按钮/button_sound.png')
        self.music_on_button = pygame.transform.smoothscale(self.music_on_button, (64, 65))
        self.music_off_button = pygame.image.load('塔防游戏素材/按钮/button_sound_off.png')
        self.music_off_button = pygame.transform.smoothscale(self.music_off_button, (64, 65))
        ''' 检验音乐按钮处于开或关状态的变量 '''
        self.music_paused = True
        if self.music_paused:
            self.music_rect = self.music_on_button.get_rect()
        else:
            self.music_rect = self.music_off_button.get_rect()
        self.music_rect.x = 150
        self.music_rect.y = 0

    ''' 检测音乐开关情况并渲染对应的图标 '''

    def draw(self, win):
        if self.music_paused:
            win.blit(self.music_on_button, self.music_rect)
        else:
            win.blit(self.music_off_button, self.music_rect)

    ''' 检验鼠标对音乐按钮的点击 '''

    def click_music_on_button(self, mouse_pos):
        button_on_clicked = self.music_rect.collidepoint(mouse_pos)
        if button_on_clicked:
            self.music_paused = not self.music_paused
            if self.music_paused:
                pygame.mixer.music.unpause()
            else:
                pygame.mixer.music.pause()




''' 控制游戏是否暂停的按钮 '''
''' 实现原理类似于音乐开关按钮 '''


class ContinuePauseButton:
    def __init__(self):
        self.continue_button = pygame.image.load('塔防游戏素材/按钮/暂停.png')
        self.continue_button = pygame.transform.smoothscale(self.continue_button, (75, 75))
        self.pause_button = pygame.image.load('塔防游戏素材/按钮/继续.png')
        self.pause_button = pygame.transform.smoothscale(self.pause_button, (75, 75))
        self.game_paused = True
        if self.game_paused:
            self.rect = self.continue_button.get_rect()
        else:
            self.rect = self.pause_button.get_rect()
        self.rect.x = 215
        self.rect.y = -6

    def draw(self, win):
        if self.game_paused:
            win.blit(self.continue_button, self.rect)
        else:
            win.blit(self.pause_button, self.rect)

    def click_continue_button(self, mouse_pos):
        button_on_clicked = self.rect.collidepoint(mouse_pos)
        if button_on_clicked:
            self.game_paused = not self.game_paused
        return self.game_paused


''' 返回上个界面的按钮 '''


class ReturnButton:
    def __init__(self):
        self.return_button = pygame.image.load('塔防游戏素材/按钮/返回.png')
        self.rect = self.return_button.get_rect()
        self.rect.midbottom = (700, 667)


    def draw(self, win):
        win.blit(self.return_button, self.rect)


''' 控制选关的按钮 '''


class NumberButton:
    def __init__(self):
        self.number_button1 = pygame.image.load('塔防游戏素材/按钮/1.png')
        self.number_button2 = pygame.image.load('塔防游戏素材/按钮/2.png')
        self.number_button3 = pygame.image.load('塔防游戏素材/按钮/3.png')
        self.rect1 = self.number_button1.get_rect()
        self.rect2 = self.number_button2.get_rect()
        self.rect3 = self.number_button3.get_rect()
        self.rect1.topleft = (450, 300)
        self.rect2.topleft = (630, 300)
        self.rect3.topleft = (810, 300)

    def draw(self, win):
        win.blit(self.number_button1, self.rect1)
        win.blit(self.number_button2, self.rect2)
        win.blit(self.number_button3, self.rect3)


''' 通过关卡后进入下一关的按钮 '''


class NextButton:
    def __init__(self):
        self.Next_button = pygame.image.load('塔防游戏素材/按钮/下一关.png')
        self.rect = self.Next_button.get_rect()
        self.rect.midbottom = (1100, 667)

    def draw(self, win):
        win.blit(self.Next_button, self.rect)


''' 通过关卡后重新开始的按钮 '''


class RestartButton:
    def __init__(self):
        self.Restart_button = pygame.image.load('塔防游戏素材/按钮/重新开始.png')
        self.rect = self.Restart_button.get_rect()
        self.rect.midbottom = (700, 667)

    def draw(self, win):
        win.blit(self.Restart_button, self.rect)


class BackButton:
    def __init__(self):
        self.Back_button = pygame.image.load('塔防游戏素材/按钮/back_button.png')
        self.Back_button = pygame.transform.smoothscale(self.Back_button, (68, 63))
        self.width = self.Back_button.get_width()
        self.height = self.Back_button.get_height()
        self.back_rect = self.Back_button.get_rect()
        self.back_rect.x = 90
        self.back_rect.y = 0

    def draw(self, win):
        win.blit(self.Back_button, self.back_rect)