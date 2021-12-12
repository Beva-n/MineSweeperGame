import pygame
from pygame import draw
from pygame.constants import MOUSEBUTTONUP
from pygame.locals import KEYDOWN, K_w, K_a, K_s, K_d
from typing import List
from MineSweeper.method_library import Method_Library
from MineSweeper.base_view import BaseView
from MineSweeper.board import Board
from MineSweeper.end_view import EndView
from MineSweeper.game import Game

class PlayView(BaseView):


    def __init__(self):
        self.start_tick = pygame.time.get_ticks()
        self.remaining_flags = 99
        #0 = game ongoing 1 = game lost 2 = game won
        self.state = 0
        self.drawing = Method_Library()
        self.upperbar = pygame.Rect(0, 0, 600, 50)
        self.board = Board()
        self.time = 0

    def event_loop(self, events: List[pygame.event.Event]) -> None:
        for event in events:
            if event.type == KEYDOWN:
                pass
            if event.type == MOUSEBUTTONUP:                
                posX, posY =  pygame.mouse.get_pos()
                if self.upperbar.collidepoint(pygame.mouse.get_pos()):
                    continue
                posX = int((posX - (posX%25))/25)
                posY = int((posY - (posY%25) - 50)/25)
                if(event.button == 1):
                    if self.board.generated == False:
                        self.board.generate(posX, posY)
                        self.start_tick = pygame.time.get_ticks()
                        self.time = round((pygame.time.get_ticks()-self.start_tick)/1000)
                    elif self.board.arr[posX][posY].flag == True:
                        continue
                    elif self.board.arr[posX][posY].value == -999:
                        self.state = 1
                        new_view = EndView(self)
                        Game.set_current_view(new_view)
                    else:
                        self.board.reveal(posX, posY)
                        if self.board.check_win():
                            self.state = 2
                            new_view = EndView(self)
                            Game.set_current_view(new_view)

                if(event.button == 3):
                    if self.board.arr[posX][posY].revealed == True:
                        continue
                    elif self.board.arr[posX][posY].flag == True:
                        self.board.arr[posX][posY].flag = False
                        self.remaining_flags += 1
                    else:
                        self.board.arr[posX][posY].flag = True
                        self.remaining_flags -= 1
    

    def update(self) -> None:
        if self.state == 0 and self.board.generated == True:
            self.time = round((pygame.time.get_ticks()-self.start_tick)/1000)
        
    
    def draw(self, screen: pygame.Surface) -> None:
        self.drawing.draw_basic_board(screen, self.board)
        self.drawing.draw_stat_display(screen, self.time, self.remaining_flags)
        if self.state == 1:
            self.drawing.draw_bombs(screen, self.board)


pygame.font.init()