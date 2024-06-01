"""
GameBoard
"""

# Remzi Alpaslan

import numpy as np
import random


class gameBoard:
    def __init__(self, gameRow, gameCol, numberOfMines):
        # creat the board
        self.gameRow = gameRow
        self.gameCol = gameCol
        self.numberOfMines = numberOfMines
        gameboard = np.full((gameRow, gameCol), "0")

        # add the mine
        gameBoardIndexs = []
        for r in range(self.gameRow):
            for c in range(self.gameCol):
                gameBoardIndexs.append([r, c])
        mineIndexs = []
        for i in range(self.numberOfMines):
            chose = random.choice(gameBoardIndexs)
            mineIndexs.append(chose)
            gameBoardIndexs.remove(chose)
        for i in mineIndexs:
            gameboard[i[0], i[1]] = "9"

        # add the number
        for r in range(self.gameRow):
            for c in range(self.gameCol):
                if gameboard[r][c] != "9":
                    howManyMine = 0
                    for i in (-1, 0, 1):
                        for j in (-1, 0, 1):
                            if 0 <= r + i <= self.gameRow - 1 and 0 <= c + j <= self.gameCol - 1:
                                if gameboard[r + i, c + j] == "9":
                                    howManyMine += 1
                    gameboard[r, c] = str(howManyMine)
        self.gameboard = gameboard


