from MineSweeper.tile import Tile
from typing import List
import random 
from collections import deque

class Board:

    global dir
    dir = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (-1, 1), (1, -1), (-1, -1)]
       
    def __init__(self):
        self.arr = [[0 for i in range(20)] for j in range(24)]
        self.generated = False
        for i in range(24):
            for j in range(20):
                self.arr[i][j] = Tile(i, j)

    def generate(self, x: int, y: int):
        """
        bfs through all tiles around the starting tile
        giving each tile a (10 - dist*4) chance to be another empty tile 
        and running bfs on the tile that is determined to be a empty tile
        to create a starting empty area with random size and shape
        """
        vis=[[0 for _ in range(20)] for _ in range(24)]
        dis=[[-1 for _ in range(20)] for _ in range(24)]
        q=deque([(x,y)])
        vis[x][y] = 1
        dis[x][y] = 0
        self.arr[x][y] = Tile(x, y, reveal = True, value = 0)
        while q:
            x, y = q.popleft()
            for nxt in dir:
                addX, addY = nxt[0], nxt[1]
                newX = x + addX
                newY = y + addY
                if newX < 0 or newX > 23:
                    continue
                if newY < 0 or newY > 19:
                    continue
                if vis[newX][newY] == 0:
                    vis[newX][newY] = 1
                    dis[newX][newY] = dis[x][y] + 1
                    luck_number = random.randint(1, 10)
                    if luck_number <= (10 - dis[newX][newY]*4):
                        self.arr[newX][newY].revealed = True
                        self.arr[newX][newY].value = 0
                        q.append((newX, newY))
        self.plantMines()
        self.assign_values()
        self.reveal(x, y)
        self.generated = True
    
    def can_be_planted(self, x: int, y: int) -> bool:
        """
        returns false if the tile itself is already a mine or if it is around a tile is that determined to be of value 0
        returns true otherwise
        """
        if self.arr[x][y].value == -999:
            return False
        for nxt in dir:
            addX, addY = nxt[0], nxt[1]
            newX = x + addX
            newY = y + addY
            if newX < 0 or newX > 23:
                continue
            if newY < 0 or newY > 19:
                continue
            if self.arr[newX][newY].value == 0:
                return False
        return True


    def plantMines(self):
        """
        continously loops through all tiles on the board
        checking if it is a plantable tile and giving it a 5% chance to plant the mines there
        exits after all 99 mines have been successfully planted 
        """
        cnt = 99
        while True:
            for i in range(24):
                for j in range(20):
                    if self.can_be_planted(i, j):
                        luck_number = random.randint(1, 20)
                        if luck_number == 17:
                            self.arr[i][j].value = -999
                            cnt -= 1
                            if cnt == 0:
                                return
    
    def assign_values(self):
        """
        for all the tiles that is not a mine or value 0, it assigns it a value based on how many mines is around that tile
        """
        for i in range(24):
            for j in range(20):
                if self.arr[i][j].value == -1:
                    cnt = 0
                    for nxt in dir:
                        addX, addY = nxt[0], nxt[1]
                        newX = i + addX
                        newY = j + addY
                        if newX < 0 or newX > 23:
                            continue
                        if newY < 0 or newY > 19:
                            continue
                        if self.arr[newX][newY].value == -999:
                            cnt += 1
                    self.arr[i][j].value = cnt
    
    def reveal(self, x: int, y: int):
        """
        reveal the tile on the board, if the tile revealed is a mine, game ends
        if the tile is of value 0, it reveals all the around that tile as well as all the ajacent tile that has a value of 0
        """
        self.arr[x][y].revealed = True
        if self.arr[x][y].value == 0:
            vis=[[0 for _ in range(20)] for _ in range(24)]
            q=deque([(x,y)])
            vis[x][y] = 1
            while q:
                x, y = q.popleft()
                for nxt in dir:
                    addX, addY = nxt[0], nxt[1]
                    newX = x + addX
                    newY = y + addY
                    if newX < 0 or newX > 23:
                        continue
                    if newY < 0 or newY > 19:
                        continue
                    if vis[newX][newY] == 0:
                        vis[newX][newY] = 1
                        self.arr[newX][newY].revealed = True
                        if self.arr[newX][newY].value == 0:
                            q.append((newX, newY))
    
    def check_win(self) -> bool:
        """
        if all the tiles that are not a mine had been revealed return true
        else return false
        """
        for i in range(24):
            for j in range(20):
                if self.arr[i][j].value == -999:
                    continue
                if self.arr[i][j].revealed == False:
                    return False
        return True


