from MineSweeper.base_view import BaseView
import pygame
from pygame.locals import MOUSEBUTTONUP, KEYUP
from MineSweeper.game import Game
from MineSweeper.menu_view import MenuView
from typing import List
from MineSweeper.method_library import Method_Library


class TitleView(BaseView):

    def __init__(self):
        self.drawing = Method_Library()
    
    def event_loop(self, events: List[pygame.event.Event]) -> None:
         for event in events:
            if event.type == MOUSEBUTTONUP or event.type == KEYUP:
                Game.set_current_view(MenuView())
    
    def update(self) -> None:
        pass

    def draw(self, surface: pygame.Surface) -> None:
        self.drawing.draw_title_view(surface)


