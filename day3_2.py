import re

def solve():
    # Read the input file
    with open('input_day3.dat', 'r') as file:
        data = file.read()

    # Track whether multiplications are enabled (True by default)
    enabled = True
    
    # Find all control instructions and multiplications in order
    # Using non-capturing group (?:) for the alternation
    pattern = r'(?:do\(\)|don\'t\(\)|mul\((\d{1,3}),(\d{1,3})\))'
    
    # Find all matches
    matches = re.finditer(pattern, data)
    
    total = 0
    print("Processing instructions:")
    for match in matches:
        instruction = match.group(0)
        
        if instruction == 'do()':
            enabled = True
            print("Enabling multiplications")
        elif instruction == "don't()":
            enabled = False
            print("Disabling multiplications")
        else:
            # It's a multiplication instruction
            if enabled:
                x = int(match.group(1))
                y = int(match.group(2))
                result = x * y
                total += result
                print(f"mul({x},{y}) = {result} (enabled)")
            else:
                x = match.group(1)
                y = match.group(2)
                print(f"mul({x},{y}) skipped (disabled)")
    
    return total

if __name__ == "__main__":
    result = solve()
    print(f"\nThe sum of all enabled multiplication results is: {result}")
