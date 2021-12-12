import pygame
from pygame.constants import MOUSEBUTTONUP
from pygame.locals import KEYDOWN, K_w, K_a, K_s, K_d
from typing import List
from MineSweeper.method_library import Method_Library
from MineSweeper.base_view import BaseView
from MineSweeper.game import Game

class EndView(BaseView):

    
    def __init__(self, parent: BaseView):
        self.next_view = None
        self.parent = parent
        self.drawing = Method_Library()
        self.restart_button = pygame.Rect(150, 400, 300, 50)
        # self.flag_cnt = flag_cnt
        # self.time = time
        # self.win = win
        # self.highscore = highscore

    def event_loop(self, events: List[pygame.event.Event]) -> None:
        for event in events:
            if event.type == MOUSEBUTTONUP:
                if self.restart_button.collidepoint(pygame.mouse.get_pos()):
                    from MineSweeper.play_view import PlayView
                    Game.set_current_view(PlayView())
    
    def update(self) -> None:
        pass

    def draw(self, screen: pygame.Surface) -> None:
        # Draw parent screen
        self.parent.draw(screen)

        # Draw overlay
        overlay = pygame.Surface(screen.get_size(), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 200))
        screen.blit(overlay, (0, 0))
        
        if self.parent.state == 1:
            self.drawing.draw_ending_screen(screen, 0, Game.get_high_score())
        else:
            self.drawing.draw_ending_screen(screen, self.parent.time, Game.get_high_score())