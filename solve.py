def read_input(filename):
    left_list = []
    right_list = []
    
    with open(filename, 'r') as f:
        for line in f:
            # Split each line into two numbers and convert to integers
            left, right = map(int, line.strip().split())
            left_list.append(left)
            right_list.append(right)
    
    return left_list, right_list

def calculate_total_distance(left_list, right_list):
    # Sort both lists independently
    sorted_left = sorted(left_list)
    sorted_right = sorted(right_list)
    
    # Calculate absolute differences between corresponding positions
    total_distance = sum(abs(l - r) for l, r in zip(sorted_left, sorted_right))
    
    return total_distance

def main():
    # Read input and calculate result
    left_list, right_list = read_input('input.dat')
    result = calculate_total_distance(left_list, right_list)
    print("=" * 50)
    print(f"The total distance between the lists is: {result}")
    print("=" * 50)

if __name__ == "__main__":
    main()
