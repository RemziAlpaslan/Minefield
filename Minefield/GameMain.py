"""
GameMain
"""

# Remzi Alpaslan
import pygame as p
from GameBoard import gameBoard
from GameEngine import gameEngine
import numpy as np

DIMENSION = 10# dimension of a cheese board are 8x8
SQ_SIZE = 40
WIDTH = HEIGHT = DIMENSION * SQ_SIZE  # 400 is another option
MAX_FPS = 15  # for animations later on
IMAGES = {}


def board(userRow, userCol, dimension):
    mines = int((dimension * dimension) / 5)
    gb = gameBoard(dimension, dimension, mines)
    while gb.gameboard[userRow, userCol] != "0":
        gb = gameBoard(dimension, dimension, mines)
    return gb.gameboard



"""
Initialize a global dictionary of images. This will be called exactly once in the main
"""


def loadImages():
    pieces = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "F"]
    for piece in pieces:
        IMAGES[piece] = p.transform.scale(p.image.load("images/" + piece + ".png"), (SQ_SIZE, SQ_SIZE))
        # Note: we can access an image by saying"IMAGES["wp"]"


"""
The main driver for our code. This will handle user input and updating the graphics.
"""


def main():
    stop = True
    i_board = np.full((DIMENSION, DIMENSION), "#")
    p.init()
    screen = p.display.set_mode((WIDTH, HEIGHT))
    clock = p.time.Clock()
    screen.fill(p.Color("white"))
    ge = gameEngine

    loadImages()  # only do this once, before the while loop
    running = True
    sqSelected = ()
    playerClicks = []  # keep track of player clicks (tuples[(6, 4),(4, 4)])

    while running:
        left, middle, right = p.mouse.get_pressed()
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
            # mouse handler

            elif right:
                location = p.mouse.get_pos()  # (x ,y) location of mouse
                col = location[0] // SQ_SIZE
                row = location[1] // SQ_SIZE
                if sqSelected == (row, col):  # the user clicked the same square twice
                    sqSelected = ()  # deselect
                    playerClicks = []  # clear player clicks
                else:
                    sqSelected = (row, col)
                    playerClicks.append(sqSelected)  # append for both 1st and 2nd clicks
                if len(playerClicks) == 1:  # after 2nd click
                    if i_board[row, col] == "F":
                        i_board[row, col] = "#"
                    elif i_board[row, col] == "#":
                        i_board[row, col] = "F"

                    sqSelected = ()  # reset user clicks
                    playerClicks = []

            elif left:
                location = p.mouse.get_pos()  # (x ,y) location of mouse
                col = location[0] // SQ_SIZE
                row = location[1] // SQ_SIZE
                if sqSelected == (row, col):  # the user clicked the same square twice
                    sqSelected = ()  # deselect
                    playerClicks = []  # clear player clicks
                else:
                    sqSelected = (row, col)
                    playerClicks.append(sqSelected)  # append for both 1st and 2nd clicks
                if len(playerClicks) == 1:  # after 2nd click
                    if i_board[row, col] == "#":
                        if stop:
                            g_board = board(row, col, DIMENSION)
                            ge = gameEngine(g_board)
                            stop = False
                        ge.openSquare(row, col)
                        i_board = ge.ib

                    sqSelected = ()  # reset user clicks
                    playerClicks = []

        drawGameState(screen, i_board)
        clock.tick(MAX_FPS)
        p.display.flip()



"""
Responsible for all the graphics with a current game state.
"""


def drawGameState(screen, board):
    drawBoard(screen)  # draw square on th board
    # add in piece highlighting or move suggestions (later)
    drawPieces(screen, board)  # draw piece on top of these square


"""
Draw the squares on the board. The top left square is always light.
"""


def drawBoard(screen):
    colors = [p.Color("white"), p.Color("gray")]
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            color = colors[((r + c) % 2)]
            p.draw.rect(screen, color, p.Rect(c * SQ_SIZE, r * SQ_SIZE, SQ_SIZE, SQ_SIZE))


"""
Draw the pieces on the board using the current GameState.board.
"""


def drawPieces(screen, board):
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            piece = board[r, c]
            if piece != "#":  # not empty square
                screen.blit(IMAGES[piece], p.Rect(c * SQ_SIZE, r * SQ_SIZE, SQ_SIZE, SQ_SIZE))


if __name__ == "__main__":
    main()
