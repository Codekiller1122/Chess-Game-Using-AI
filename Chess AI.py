import random

# Define the chess pieces and their symbols
pieces = {
    'K': 'King', 'Q': 'Queen', 'R': 'Rook', 'B': 'Bishop', 'N': 'Knight', 'P': 'Pawn',
    'k': 'King', 'q': 'Queen', 'r': 'Rook', 'b': 'Bishop', 'n': 'Knight', 'p': 'Pawn'
}

# Initialize the chessboard
def initialize_board():
    board = [
        ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'],
        ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
        ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']
    ]
    return board

# Print the chessboard
def print_board(board):
    print("  a b c d e f g h")
    for i, row in enumerate(board):
        print(f"{8-i} {' '.join(row)} {8-i}")
    print("  a b c d e f g h")

# Check if a move is valid (basic validation)
def is_valid_move(board, move, player):
    start_pos, end_pos = move[:2], move[2:]
    start_x, start_y = 8-int(start_pos[1]), ord(start_pos[0]) - ord('a')
    end_x, end_y = 8-int(end_pos[1]), ord(end_pos[0]) - ord('a')
    
    # Check if start and end positions are within bounds
    if not (0 <= start_x < 8 and 0 <= start_y < 8 and 0 <= end_x < 8 and 0 <= end_y < 8):
        return False
    
    piece = board[start_x][start_y]
    if piece == ' ':
        return False
    
    if piece.islower() and player == 'white' or piece.isupper() and player == 'black':
        return False
    
    return True

# Move a piece on the board
def make_move(board, move):
    start_pos, end_pos = move[:2], move[2:]
    start_x, start_y = 8-int(start_pos[1]), ord(start_pos[0]) - ord('a')
    end_x, end_y = 8-int(end_pos[1]), ord(end_pos[0]) - ord('a')
    
    board[end_x][end_y] = board[start_x][start_y]
    board[start_x][start_y] = ' '

# Generate a random move for the AI
def ai_move(board):
    valid_moves = []
    for x in range(8):
        for y in range(8):
            piece = board[x][y]
            if piece == ' ' or piece.isupper():  # AI only controls lowercase pieces
                continue
            for dx in range(-1, 2):
                for dy in range(-1, 2):
                    if dx == 0 and dy == 0:
                        continue
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < 8 and 0 <= ny < 8 and board[nx][ny] == ' ':
                        valid_moves.append((x, y, nx, ny))
    
    if valid_moves:
        move = random.choice(valid_moves)
        start_pos = chr(move[1] + ord('a')) + str(8 - move[0])
        end_pos = chr(move[3] + ord('a')) + str(8 - move[2])
        return start_pos + end_pos
    return None

def main():
    board = initialize_board()
    print_board(board)
    
    player = 'white'
    
    while True:
        if player == 'white':
            print(f"{player.capitalize()}'s turn")
            move = input("Enter your move (e.g., e2e4): ").strip()
            
            if not is_valid_move(board, move, player):
                print("Invalid move. Try again.")
                continue
            
            make_move(board, move)
        
        else:
            print("AI's turn")
            move = ai_move(board)
            if move:
                print(f"AI moves: {move}")
                make_move(board, move)
            else:
                print("AI has no valid moves.")
        
        print_board(board)
        
        # Toggle player
        player = 'black' if player == 'white' else 'white'

if __name__ == "__main__":
    main()
