def read_input(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()
    # Each line is a row in the grid
    grid = []
    for line in lines:
        grid.append(list(line.strip()))
    return grid

def find_xmas(grid):
    rows = len(grid)
    cols = len(grid[0])
    count = 0
    
    def is_valid_pos(row, col):
        return 0 <= row < rows and 0 <= col < cols
    
    def check_mas(chars):
        # Check if the three characters form "MAS" forwards or backwards
        return ''.join(chars) in ['MAS', 'SAM']
    
    def check_x_pattern(row, col):
        # Check if we can form a valid X pattern centered at this position
        # Need to check both diagonals (top-left to bottom-right and top-right to bottom-left)
        # Each diagonal needs to be 3 characters forming "MAS" or "SAM"
        
        # First check if we have enough space for the X pattern
        if not all(is_valid_pos(row + dr, col + dc) for dr, dc in [(-1, -1), (-1, 1), (0, 0), (1, -1), (1, 1)]):
            return False
        
        # Get the characters for both diagonals
        diagonal1 = [
            grid[row - 1][col - 1],
            grid[row][col],
            grid[row + 1][col + 1]
        ]
        
        diagonal2 = [
            grid[row - 1][col + 1],
            grid[row][col],
            grid[row + 1][col - 1]
        ]
        
        # Check if either diagonal can form MAS/SAM in either direction
        return (check_mas(diagonal1) and check_mas(diagonal2))
    
    # Check each possible center position of an X pattern
    for row in range(1, rows - 1):  # Skip edges as we need space for the X
        for col in range(1, cols - 1):
            if check_x_pattern(row, col):
                count += 1
    
    return count

def main():
    grid = read_input('input_day4.dat')
    result = find_xmas(grid)
    print(f"X-MAS appears {result} times in the word search")

if __name__ == "__main__":
    main()
