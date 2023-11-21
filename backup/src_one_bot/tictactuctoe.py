import arcade

# Constants
CELL_SIZE = 100
GRID_SIZE = 4
NUM_LAYERS = 4
SCREEN_WIDTH = CELL_SIZE * GRID_SIZE
SCREEN_HEIGHT = CELL_SIZE * GRID_SIZE*NUM_LAYERS
WINNING_LENGTH = 4

# Colors
BACKGROUND_COLOR = (51, 51, 51)
LINE_COLOR = (255, 255, 255)
X_COLOR = (252, 163, 17)
O_COLOR = (12, 146, 113)

# Initialize the game board
board = [[[' ' for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
current_player = 'X'
winner = None

# Function to check for a win
def check_for_win():
    global winner
    for x in range(GRID_SIZE):
        for y in range(GRID_SIZE):
            for z in range(NUM_LAYERS):
                if board[x][y][z] != ' ':
                    # Check rows, columns, and diagonals for a win
                    for i in range(-1, 2):
                        if (0 <= x + i < GRID_SIZE and
                            0 <= y + i < GRID_SIZE and
                            0 <= z + i < NUM_LAYERS and
                            board[x][y][z] == board[x + i][y + i][z + i] and
                            board[x][y][z] == board[x - i][y + i][z - i] and
                            board[x][y][z] == board[x + i][y - i][z - i] and
                            board[x][y][z] == board[x - i][y - i][z + i]):
                            winner = current_player
                            return True
    return False

# Function to handle mouse click
def on_mouse_press(x, y, button, modifiers):
    print(x,y)
    global current_player

    if winner is not None:
        return

    cell_x = x // CELL_SIZE
    cell_y = y // CELL_SIZE

    if cell_x < GRID_SIZE and cell_y < GRID_SIZE:
        for z in range(NUM_LAYERS):
            if board[cell_x][cell_y][z] == ' ':
                board[cell_x][cell_y][z] = current_player
                if check_for_win():
                    print(f"Player {current_player} wins!")
                current_player = 'O' if current_player == 'X' else 'X'

def on_draw(delta_time):
    arcade.start_render()

    # Draw the grid lines
    for i in range(GRID_SIZE + 1):
        x = i * CELL_SIZE
        arcade.draw_line(x, 0, x, SCREEN_HEIGHT, LINE_COLOR)
        arcade.draw_line(0, x, SCREEN_WIDTH, x, LINE_COLOR)
    # Draw X and O symbols
    for x in range(GRID_SIZE):
        for y in range(GRID_SIZE):
            for z in range(NUM_LAYERS):
                cell_value = board[x][y][z]
                print(cell_value)
                print(z)
                if cell_value == 'X':
                    arcade.draw_text("X", x * CELL_SIZE + CELL_SIZE // 3, y * CELL_SIZE + CELL_SIZE // 3, X_COLOR, font_size=50)
                elif cell_value == 'O':
                    arcade.draw_text("O", x * CELL_SIZE + CELL_SIZE // 3, y * CELL_SIZE + CELL_SIZE // 3, O_COLOR, font_size=50)

def main():
    window = arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "3D Tic-Tac-Toe")
    arcade.set_background_color(BACKGROUND_COLOR)
    
    # Register the mouse press event
    window.on_mouse_press = on_mouse_press
    
    arcade.schedule(on_draw, 1/60)
    arcade.run()

if __name__ == "__main__":
    main()
