import random
import math

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

# Generate all possible moves for a piece (simplified)
def generate_moves(board, player):
    moves = []
    for x in range(8):
        for y in range(8):
            piece = board[x][y]
            if piece == ' ' or (piece.islower() and player == 'white') or (piece.isupper() and player == 'black'):
                continue
            for dx in range(-1, 2):
                for dy in range(-1, 2):
                    if dx == 0 and dy == 0:
                        continue
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < 8 and 0 <= ny < 8 and board[nx][ny] == ' ':
                        start_pos = chr(y + ord('a')) + str(8 - x)
                        end_pos = chr(ny + ord('a')) + str(8 - nx)
                        moves.append(start_pos + end_pos)
    return moves

# Evaluate the board (simplified evaluation)
def evaluate_board(board):
    piece_values = {'P': 1, 'N': 3, 'B': 3, 'R': 5, 'Q': 9, 'K': 0,
                    'p': -1, 'n': -3, 'b': -3, 'r': -5, 'q': -9, 'k': 0}
    value = 0
    for row in board:
        for piece in row:
            value += piece_values.get(piece, 0)
    return value

# Minimax algorithm with Alpha-Beta Pruning
def minimax(board, depth, alpha, beta, maximizing_player):
    if depth == 0:
        return evaluate_board(board)

    if maximizing_player:
        max_eval = -math.inf
        for move in generate_moves(board, 'black'):
            new_board = [row[:] for row in board]
            make_move(new_board, move)
            eval = minimax(new_board, depth - 1, alpha, beta, False)
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = math.inf
        for move in generate_moves(board, 'white'):
            new_board = [row[:] for row in board]
            make_move(new_board, move)
            eval = minimax(new_board, depth - 1, alpha, beta, True)
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval

# Choose the best move for the AI using Minimax
def ai_move(board):
    best_move = None
    best_value = -math.inf
    for move in generate_moves(board, 'black'):
        new_board = [row[:] for row in board]
        make_move(new_board, move)
        move_value = minimax(new_board, 3, -math.inf, math.inf, False)
        if move_value > best_value:
            best_value = move_value
            best_move = move
    if best_move:
        return best_move
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
