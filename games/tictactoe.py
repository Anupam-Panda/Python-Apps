##!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 20 20:40:37 2020

@author: anupampanda
"""
import sys
VALID_CELL = [1,2,3,4,5,6,7,8,9]

class TicTacToeBoard:
    def __init__(self):
        self.cells = []
        self.win_cells = []
        for idx in VALID_CELL:
            self.cells.append(Cell(idx))
            #print(self.cells[idx - 1].index)
    def set_win_cells(self,win_cells: list):
        self.win_cells = win_cells
    def __del__(self):
        self.cells = None
        self.win_cells = None

class Cell:
    def __init__(self,index):
        self.index = index
        self.mark = None
    def set_mark(self, mark: str):
        self.mark = mark

def get_move(board: TicTacToeBoard):
    cell = int (input('Enter your next move cell: '))
    while((cell not in VALID_CELL) or (board.cells[cell - 1].mark is not None)):
        print('You entered a wrong cell. Please put the correct cell info')
        cell = int (input('Enter your next move cell: '))
    print()    
    return cell

def check_win(board: TicTacToeBoard):
    # Check row wise, columnwise and diagonalwise marks
    cell = 1
    for row in range (1,4):
        if (row == 1):
            #check row
            if ((board.cells[cell - 1].mark is not None) and \
                (board.cells[cell].mark is not None) and \
                (board.cells[cell + 1].mark is not None) and \
                (board.cells[cell - 1].mark == board.cells[cell].mark) and \
                (board.cells[cell - 1].mark == board.cells[cell + 1].mark)):
                board.set_win_cells([cell - 1, cell, cell + 1])
                return True
            elif ((board.cells[cell - 1].mark is not None) and \
                (board.cells[cell + 2].mark is not None) and \
                (board.cells[cell + 5].mark is not None) and \
                (board.cells[cell - 1].mark == board.cells[cell + 2].mark) and \
                (board.cells[cell - 1].mark == board.cells[cell + 5].mark)):
                board.set_win_cells([cell - 1, cell + 2, cell + 5])
                return True
            elif ((board.cells[cell - 1].mark is not None) and \
                (board.cells[cell + 3].mark is not None) and \
                (board.cells[cell + 7].mark is not None) and \
                (board.cells[cell - 1].mark == board.cells[cell + 3].mark) and \
                (board.cells[cell - 1].mark == board.cells[cell + 7].mark)):
                board.set_win_cells([cell - 1, cell + 3, cell + 7])
                return True
            elif ((board.cells[cell].mark is not None) and \
                (board.cells[cell + 3].mark is not None) and \
                (board.cells[cell + 6].mark is not None) and \
                (board.cells[cell].mark == board.cells[cell + 3].mark) and \
                (board.cells[cell].mark == board.cells[cell + 6].mark)):
                board.set_win_cells([cell, cell + 3, cell + 6])
                return True
            elif ((board.cells[cell + 1].mark is not None) and \
                (board.cells[cell + 4].mark is not None) and \
                (board.cells[cell + 7].mark is not None) and \
                (board.cells[cell + 1].mark == board.cells[cell + 4].mark) and \
                (board.cells[cell + 1].mark == board.cells[cell + 7].mark)):
                board.set_win_cells([cell + 1, cell + 4, cell + 7])
                return True
            elif ((board.cells[cell + 1].mark is not None) and \
                (board.cells[cell + 3].mark is not None) and \
                (board.cells[cell + 5].mark is not None) and \
                (board.cells[cell + 1].mark == board.cells[cell + 3].mark) and \
                (board.cells[cell + 1].mark == board.cells[cell + 5].mark)):
                board.set_win_cells([cell + 1, cell + 3, cell + 5])
                return True
            cell = 4
        elif (row == 2):
            #check row
            if ((board.cells[cell - 1].mark is not None) and \
                (board.cells[cell].mark is not None) and \
                (board.cells[cell + 1].mark is not None) and \
                (board.cells[cell - 1].mark == board.cells[cell].mark) and \
                (board.cells[cell - 1].mark == board.cells[cell + 1].mark)):
                board.set_win_cells([cell - 1, cell, cell + 1])
                return True
            cell = 7
        elif (row == 3):
            #check row
            if ((board.cells[cell - 1].mark is not None) and \
                (board.cells[cell].mark is not None) and \
                (board.cells[cell + 1].mark is not None) and \
                (board.cells[cell - 1].mark == board.cells[cell].mark) and \
                (board.cells[cell - 1].mark == board.cells[cell + 1].mark)):
                board.set_win_cells([cell - 1, cell, cell + 1])
                return True
    return False
    

def display_board(board: TicTacToeBoard):
    cell = 1
    for row in range (1,4):
        while (cell <= row * 3):
            if(cell % 3 == 0):
                if (board.cells[cell - 1].mark is None):
                    print (board.cells[cell - 1].index, end=" ")
                else:
                    print (board.cells[cell - 1].mark, end=" ")   
            else:
                if (board.cells[cell - 1].mark is None):
                    disp = f"{board.cells[cell - 1].index} | "
                    print (disp, end=" ")
                else:
                    disp = f"{board.cells[cell - 1].mark} | "
                    print (disp, end=" ")
            cell += 1
        if (row != 3):
            print('\n-----------')
        else:
            print()
            
def win_display_board(board: TicTacToeBoard, win_cells: list):
    cell = 1
    for row in range (1,4):
        while (cell <= row * 3):
            if(cell % 3 == 0):
                if (board.cells[cell - 1].mark is None):
                    print (board.cells[cell - 1].index, end=" ")
                elif ((cell - 1) in win_cells):
                    print ("("+board.cells[cell - 1].mark+")", end=" ") 
                else:
                    print (board.cells[cell - 1].mark, end=" ")   
            else:
                if (board.cells[cell - 1].mark is None):
                    disp = f"{board.cells[cell - 1].index} | "
                    print (disp, end=" ")
                elif ((cell - 1) in win_cells):
                    disp = f"({board.cells[cell - 1].mark}) | "
                    print (disp, end=" ") 
                else:
                    disp = f"{board.cells[cell - 1].mark} | "
                    print (disp, end=" ")
            cell += 1
        if (row != 3):
            print('\n-----------')
        else:
            if (board.cells[win_cells[0]].mark == 'X'):
                win_player = "PlayerA"
            else:
                win_player = "PlayerB"
            print(f'\n\n{win_player} has won the game!\n')

if __name__ == '__main__':
    player = ('PlayerA', 'PlayerB')
    while(True):
        #print('Do you want to start a new game?[y/N]')
        ans = input('Do you want to start a new game?[y/N]:')
        if (ans in ('n', 'N')):
            break
        if (ans not in ('y', 'Y')):
            print('You entered a wrong value. Exiting the game. Restart the game again')
            sys.exit()
        max_terms = 9
        term = 1
        board = TicTacToeBoard()
        while ((term <= max_terms) and not(check_win(board))):
            if (term % 2 == 0):
                print('PlayerB will enter\n\n')
                display_board(board)
                cell = get_move(board)
                board.cells[cell - 1].set_mark('O')
            else:
                print('PlayerA will enter\n\n')
                display_board(board)
                cell = get_move(board)
                board.cells[cell - 1].set_mark('X')
            term += 1
        win_display_board(board, board.win_cells)
        del board
