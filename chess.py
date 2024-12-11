import tkinter as tk

window = tk.Tk()
window.title("Chess Game")


BOARD_SIZE = 8
SQUARE_SIZE = 60
LIGHT_SQUARE_COLOR = "#f0d9b5"
DARK_SQUARE_COLOR = "#b58863"


PIECES = {
    "R": "♖", "N": "♘", "B": "♗", "Q": "♕", "K": "♔", "P": "♙",
    "r": "♖", "n": "♘", "b": "♗", "q": "♕", "k": "♔", "p": "♙"
}

# Chessboard setup: empty squares and starting pieces
initial_board = [
    ["r", "n", "b", "q", "k", "b", "n", "r"],
    ["p", "p", "p", "p", "p", "p", "p", "p"],
    ["", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", ""],
    ["P", "P", "P", "P", "P", "P", "P", "P"],
    ["R", "N", "B", "Q", "K", "B", "N", "R"]
]

# Current board (copy of initial)
board = [row[:] for row in initial_board]

# Functions


def draw_board():
    """Draw the chessboard with alternating colors."""
    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            color = LIGHT_SQUARE_COLOR if (
                row + col) % 2 == 0 else DARK_SQUARE_COLOR
            square = tk.Canvas(root, width=SQUARE_SIZE,
                               height=SQUARE_SIZE, bg=color)
            square.grid(row=row, column=col)

            piece = board[row][col]
            if piece:
                square.create_text(SQUARE_SIZE // 2, SQUARE_SIZE //
                                   2, text=PIECES[piece], font=("Arial", 24))


def move_piece(start_row, start_col, end_row, end_col):
    """Move a piece from start to end coordinates."""
    if board[start_row][start_col]:
        # Move the piece
        board[end_row][end_col] = board[start_row][start_col]
        board[start_row][start_col] = ""
        redraw_board()


def redraw_board():
    """Redraw the chessboard with updated pieces."""
    for widget in root.winfo_children():
        widget.destroy()
    draw_board()


def square_click(event):
    """Handle clicks on squares (for moving pieces)."""
    global start_row, start_col
    row, col = event.widget.grid_info()["row"], event.widget.grid_info()[
        "column"]
    row, col = int(row), int(col)

    if start_row is None:
        start_row, start_col = row, col
    else:
        move_piece(start_row, start_col, row, col)
        start_row, start_col = None, None


# Add event listeners for clicking squares
start_row, start_col = None, None
root.bind("<Button-1>", square_click)

# Draw initial board
draw_board()

# Run the Tkinter event loop
root.mainloop()
