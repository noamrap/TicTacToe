
import tkinter as tk
from tkinter import messagebox
import random

class TicTacToeGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("TicTacToeboard")
        self.master.geometry("800x800")
        self.master.config(bg="light blue")
        self.board = [["", "", ""],
                      ["", "", ""],
                      ["", "", ""]]
        self.player_turn = "X"

        self.cell_buttons = []
        for row in range(3):
            cell_row = []
            for col in range(3):
                button = tk.Button(master, text="", width=10, height=5, command=lambda r=row, c=col: self.handle_button_click(r, c))
                button.grid(row=row, column=col, padx=10, pady=10)
                cell_row.append(button)
            self.cell_buttons.append(cell_row)

    def handle_button_click(self, row, col):
        if self.board[row][col] == "" and self.player_turn == "X":
            self.board[row][col] = "X"
            self.cell_buttons[row][col].config(text="X")
            self.player_turn = "O"
            if not self.check_winner(row, col):
                self.computer_move()

    def check_winner(self, row, col):
        current_player = self.board[row][col]

        if self.board[row][0] == self.board[row][1] == self.board[row][2] == current_player != "":
            self.display_winner(current_player)
            return True

    
        if self.board[0][col] == self.board[1][col] == self.board[2][col] == current_player != "":
            self.display_winner(current_player)
            return True

      
        if self.board[0][0] == self.board[1][1] == self.board[2][2] == current_player != "":
            self.display_winner(current_player)
            return True

        if self.board[0][2] == self.board[1][1] == self.board[2][0] == current_player != "":
            self.display_winner(current_player)
            return True

        if self.is_board_full():
            self.display_tie()
            return True

        return False

    def display_winner(self, player):
        messagebox.showinfo("Winner", f"Player {player} wins!")
        self.reset_board()

    def display_tie(self):
        messagebox.showinfo("Game Over", "It's a tie!")
        self.reset_board()

    def reset_board(self):
        for row in range(3):
            for col in range(3):
                self.board[row][col] = ""
                self.cell_buttons[row][col].config(text="")
        self.player_turn = "X"

    def computer_move(self):
        available_moves = []
        for row in range(3):
            for col in range(3):
                if self.board[row][col] == "":
                    available_moves.append((row, col)) # לצרף לפנויים

        if available_moves: # אם יש פנוי
            row, col = random.choice(available_moves)
            self.board[row][col] = "O"
            self.cell_buttons[row][col].config(text="O")
            self.player_turn = "X"
            self.check_winner(row, col)

    def is_board_full(self):
        for row in range(3):
            for col in range(3):
                if self.board[row][col] == "":
                    return False
        return True

root = tk.Tk()
tic_tac_toe = TicTacToeGUI(root)
root.mainloop()