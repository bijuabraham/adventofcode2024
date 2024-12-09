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
    
    # All 8 directions: right, down-right, down, down-left, left, up-left, up, up-right
    directions = [
        (0, 1), (1, 1), (1, 0), (1, -1),
        (0, -1), (-1, -1), (-1, 0), (-1, 1)
    ]
    
    def is_valid_pos(row, col):
        return 0 <= row < rows and 0 <= col < cols
    
    def check_direction(row, col, dx, dy):
        # First check if all positions needed are valid
        for i in range(4):
            new_row = row + i*dx
            new_col = col + i*dy
            if not is_valid_pos(new_row, new_col):
                return False
        
        # Now safely build the word
        word = ''
        for i in range(4):
            word += grid[row + i*dx][col + i*dy]
        return word == 'XMAS'
    
    for row in range(rows):
        for col in range(cols):
            for dx, dy in directions:
                if check_direction(row, col, dx, dy):
                    count += 1
    
    return count

def main():
    grid = read_input('input_day4.dat')
    result = find_xmas(grid)
    print(f"XMAS appears {result} times in the word search")

if __name__ == "__main__":
    main()
