import pygame
from main_menu import MainMenu
''' 游戏的启动界面 '''
if __name__ == '__main__':
    pygame.init()
    win = pygame.display.set_mode((1400, 750))
    mainMenu = MainMenu(win)
    mainMenu.run_game()