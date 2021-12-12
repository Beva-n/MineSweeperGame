from abc import ABC, abstractmethod

import pygame
from pygame.locals import K_ESCAPE, KEYDOWN, QUIT

from MineSweeper.base_view import BaseView


class BaseGame(ABC):
    game: 'BaseGame' = None

    def __init__(self):
        BaseGame.game = self

        pygame.init()
        pygame.font.init()

        WIDTH = 24*25
        HEIGHT = 20*25 + 50
        SIZE = (WIDTH, HEIGHT)

        self.screen = pygame.display.set_mode(SIZE)
        self.clock = pygame.time.Clock()

        self.current_view = None
        self.high_score = 0

        self.create()
    
    @staticmethod
    def set_current_view(view: BaseView):
        BaseGame.game.current_view = view
    
    def set_high_score(score: int):
        BaseGame.game.high_score = score
    
    def get_high_score() -> int:
        return BaseGame.game.high_score


    @abstractmethod
    def create(self) -> None: ...

    def run(self) -> None:
        running = True
        while running:
            # EVENT HANDLING
            events = pygame.event.get()
            for event in events:
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
                elif event.type == QUIT:
                    running = False
            
            self.current_view.event_loop(events)
            self.current_view.update()
            self.current_view.draw(self.screen)
            

            # Must be the last two lines
            # of the game loop
            pygame.display.flip()
            self.clock.tick(30)
            #---------------------------


        pygame.quit()