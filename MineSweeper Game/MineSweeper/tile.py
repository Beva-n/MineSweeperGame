import pygame

class Tile:
    def __init__(self, x: int, y: int, reveal: bool = False, value: int = -1):
        self.value = value
        self.flag = False
        self.rect = pygame.Rect(x*25, y*25+50, 25, 25)
        self.revealed = reveal
    
    def __str__(self):
        return f"left:{self.rect.left} top:{self.rect.top}"
    

    
    
    
