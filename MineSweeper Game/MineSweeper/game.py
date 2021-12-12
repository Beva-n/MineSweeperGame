
from MineSweeper.base_game import BaseGame

class Game(BaseGame):

    def create(self) -> None:
        from MineSweeper.title_view import TitleView
        self.current_view = TitleView()
    