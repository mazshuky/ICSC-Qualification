import sys
import random


def create_crossword(words: list) -> list:
    """
    Generate a 10x10 word search puzzle containing the given words.

    Args:
        words: A list of words to include in the puzzle.

    Returns:
        A 2D array (list of lists) representing the word search puzzle.
    """
    # Validate input: all words must be alphabetic and at most 10 characters
    if not words or any(not word.isalpha() or len(word) > 10 for word in words):
        raise ValueError("All words must be alphabetic and at most 10 characters long.")
    # Convert all words to uppercase
    words = [word.upper() for word in words]
    grid_size = 10
    # Initialize empty grid
    grid = [[' ' for _ in range(grid_size)] for _ in range(grid_size)]
    # Define all 8 possible directions (horizontal, vertical, diagonal)
    directions = [(0, 1), (1, 0), (1, 1), (0, -1), (-1, 0), (-1, -1), (1, -1), (-1, 1)]
    # Shuffle words to randomize placement order
    random.shuffle(words)
    for word in words:
        placed = False
        attempts = 0
        # Try up to 100 times to place the word
        while not placed and attempts < 100:
            attempts += 1
            direction = random.choice(directions)
            start_row = random.randint(0, grid_size - 1)
            start_col = random.randint(0, grid_size - 1)
            end_row = start_row + direction[0] * (len(word) - 1)
            end_col = start_col + direction[1] * (len(word) - 1)
            # Check if the word fits within the grid boundaries
            if 0 <= end_row < grid_size and 0 <= end_col < grid_size:
                can_place = True
                # Check for conflicts with existing letters
                for i in range(len(word)):
                    r = start_row + direction[0] * i
                    c = start_col + direction[1] * i
                    if grid[r][c] not in (' ', word[i]):
                        can_place = False
                        break
                # Place the word if possible
                if can_place:
                    for i in range(len(word)):
                        r = start_row + direction[0] * i
                        c = start_col + direction[1] * i
                        grid[r][c] = word[i]
                    placed = True
        # If unable to place the word, raise an error
        if not placed:
            raise ValueError(f"Could not place the word: {word}")
    # Fill remaining empty spaces with random letters
    for r in range(grid_size):
        for c in range(grid_size):
            if grid[r][c] == ' ':
                grid[r][c] = random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    return grid


# --- Main execution block. DO NOT MODIFY.  ---
if __name__ == "__main__":
    try:
        # Read words from first line (comma-separated)
        words_input = input().strip()
        words = [word.strip() for word in words_input.split(',')]

        # Generate the word search puzzle
        puzzle = create_crossword(words)

        # Print the result as a 2D grid
        for row in puzzle:
            print(''.join(row))

    except ValueError as e:
        print(f"Input Error: {e}", file=sys.stderr)
        sys.exit(1)
    except EOFError:
        print("Error: Not enough input lines provided.", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)
        sys.exit(1)