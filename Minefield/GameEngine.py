"""
GameEngine
"""

# Remzi Alpaslan

import numpy as np
import GameBoard


class gameEngine:
    def __init__(self, gameBoard):
        self.win = None
        self.gb = gameBoard
        self.gameRow = gameBoard.shape[0]
        self.gameCol = gameBoard.shape[1]
        self.ib = np.full(gameBoard.shape, "#")
        self.index = []

    def openSquare(self, openRow, openCol):
        if self.gb[openRow, openCol] == "9":
            self.win = False
            for r in range(self.gameRow):
                for c in range(self.gameCol):
                    if self.gb[r, c] == "9":
                        self.index.append([r, c])


        elif self.gb[openRow, openCol] == "0":
            zeros = [[openRow, openCol]]
            doesZeros = []
            while zeros:
                for i in ([-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]):
                    if 0 <= zeros[0][0] + i[0] <= self.gameRow - 1 and 0 <= zeros[0][1] + i[1] <= self.gameCol - 1:
                        if [zeros[0][0] + i[0], zeros[0][1] + i[1]] not in zeros:
                            if self.gb[zeros[0][0] + i[0], zeros[0][1] + i[1]] == "0":
                                if [zeros[0][0] + i[0], zeros[0][1] + i[1]] not in doesZeros:
                                    zeros.append([zeros[0][0] + i[0], zeros[0][1] + i[1]])

                if zeros[0] not in doesZeros:
                    doesZeros.append(zeros[0])
                zeros.pop(0)
            for zero in doesZeros:
                for i in ([-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 0], [0, 1], [1, -1], [1, 0], [1, 1]):
                    if 0 <= zero[0] + i[0] <= self.gameRow - 1 and 0 <= zero[1] + i[1] <= self.gameCol - 1:
                        if [zero[0] + i[0], zero[1] + i[1]] not in self.index:
                            self.index.append([zero[0] + i[0], zero[1] + i[1]])
        else:
            self.index.append([openRow, openCol])

        for i in self.index:
            self.ib[i[0], i[1]] = self.gb[i[0], i[1]]
