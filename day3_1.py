import re

def solve():
    # Read the input file
    with open('input_day3.dat', 'r') as file:
        data = file.read()

    # Pattern to match mul(X,Y) where X and Y are 1-3 digit numbers
    # Using positive lookahead (?=\)) to ensure the pattern ends with a closing parenthesis
    pattern = r'mul\((\d{1,3}),(\d{1,3})\)'
    
    # Find all matches
    matches = re.finditer(pattern, data)
    
    total = 0
    print("Found multiplications:")
    for match in matches:
        x = int(match.group(1))
        y = int(match.group(2))
        result = x * y
        total += result
        print(f"mul({x},{y}) = {result}")
    
    return total

if __name__ == "__main__":
    result = solve()
    print(f"\nThe sum of all multiplication results is: {result}")
