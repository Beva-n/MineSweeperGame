import pygame

class Method_Library:
 
    global clock, upperbar, flag, bigflag, size_25_text, size_35_text
    bigflag = pygame.image.load("img/bigflag.png")
    flag = pygame.image.load("img/flag.png")
    clock = pygame.image.load("img/clock.png")
    upperbar = pygame.Rect(0, 0, 600, 50)

    def __init__(self) -> None:
        pygame.font.init()
        self.size_22_text = pygame.font.Font("font/ReadexPro-Regular.ttf", 22)
        self.size_30_text = pygame.font.Font("font/ReadexPro-Regular.ttf", 30)
        self.size_50_text = pygame.font.Font("font/ReadexPro-Regular.ttf", 50)
        self.size_16_text = pygame.font.Font("font/ReadexPro-Regular.ttf", 16)

    def draw_stat_display(self, screen, time: int, remaining_flags: int):
        pygame.draw.rect(screen, (34,139,34), upperbar)
        screen.blit(clock, (150, 5))
        screen.blit(bigflag, (350, 5))
        text_surface = self.size_30_text.render(f"{time}", False, (255, 255, 255))
        screen.blit(text_surface, (205, 5))
        text_surface = self.size_30_text.render(f"{remaining_flags}", False, (255,255,255))
        screen.blit(text_surface, (395, 5))
    
    def draw_basic_board(self, screen, board):
        screen.fill((255, 255, 255))
        for i in range(24):
            for j in range(20):
                if board.arr[i][j].revealed:
                    if i % 2 ==  j%2:
                        RGB = (255,255,255) #white
                    else:
                        RGB = (192,192,192) #sliver
                else:
                    if i % 2 == j % 2:
                        RGB = (0, 255, 0)
                    else:
                        RGB = (50,205,50)
                pygame.draw.rect(screen, RGB, board.arr[i][j].rect)
                if board.arr[i][j].flag:
                    screen.blit(flag, (board.arr[i][j].rect.left, board.arr[i][j].rect.top))
        for i in range(24):
            for j in range(20):
                if board.arr[i][j].revealed and board.arr[i][j].value >= 1 and board.arr[i][j].value <= 8:
                    textsurface = self.size_22_text.render(f'{board.arr[i][j].value}', False, (0, 0, 0))
                    screen.blit(textsurface, (board.arr[i][j].rect.left + 5, board.arr[i][j].rect.top-3))
    
    def draw_bombs(self, screen, board):
        for i in range(24):
             for j in range(20):
                 if board.arr[i][j].value == -999 and board.arr[i][j].flag == False:
                     pygame.draw.circle(screen, (255, 0, 0), board.arr[i][j].rect.center, 10)
    
    def draw_ending_screen(self, screen, time: int, highscore: int):
        pygame.draw.rect(screen, (136, 209, 241), (125, 125, 350, 250))
        BG = pygame.image.load("img/yuki.png")
        screen.blit(BG, (135, 135))
        BG = pygame.image.load("img/clock.png")
        screen.blit(BG, (300, 175))
        BG = pygame.image.load("img/trophy.png")
        screen.blit(BG, (300, 240))
        if time == 0:
            text_surface = self.size_30_text.render(f"-", False, (255,255,255))
        else:    
            text_surface = self.size_30_text.render(f"{time}", False, (255,255,255))
        screen.blit(text_surface, (370, 175))
        
        if highscore == 0:
            text_surface = self.size_30_text.render(f"-", False, (255,255,255))
        else:    
            text_surface = self.size_30_text.render(f"{highscore}", False, (255,255,255))
        screen.blit(text_surface, (370, 240))

        pygame.draw.rect(screen, (0, 57, 169), (150, 400, 300, 50))
        text_surface = self.size_22_text.render("Restart", False, (255,255,255))
        screen.blit(text_surface, (260, 408))
    
    def draw_title_view(self, screen):
        screen.fill((119, 118, 196))
        welcome_text = self.size_22_text.render("Welcome to", False, (0, 0, 0))
        title_text = self.size_50_text.render(f"Name TBD", False, (0, 0,0))
        instruction_text = self.size_16_text.render("Press any key to continue", False, (0, 0, 0))
        screen.blit(welcome_text, (210, 220))
        screen.blit(title_text, (170, 240))
        screen.blit(instruction_text, (184, 300))

    def draw_menu_view(self, screen):
        screen.fill((119, 118, 196))
        title_text = self.size_30_text.render(f"Name TBD", False, (0, 0,0))
        screen.blit(title_text, (220, 10))
        for i in range(4):
            pygame.draw.rect(screen, (51, 214, 81), (50, 65 + 110*i, 500, 95))
        minesweeper_png = pygame.image.load("img/minesweeper.png")
        screen.blit(minesweeper_png, (60, 72.5))


    