def read_input(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
    
    left_list = []
    right_list = []
    
    for line in lines:
        left, right = line.strip().split()
        left_list.append(int(left))
        right_list.append(int(right))
    
    return left_list, right_list

def calculate_similarity_score(left_list, right_list):
    total_score = 0
    
    for num in left_list:
        # Count occurrences of this number in right list
        count = right_list.count(num)
        # Add to total score (num * count)
        score_for_num = num * count
        print(f"Number {num} appears {count} times in right list. Adding {score_for_num} to total.")
        total_score += score_for_num
    
    return total_score

def main():
    print("Reading input file...")
    left_list, right_list = read_input('input.dat')
    print(f"Found {len(left_list)} numbers in each list")
    print("\nCalculating similarity score...")
    score = calculate_similarity_score(left_list, right_list)
    print(f"\nFinal similarity score: {score}")

if __name__ == "__main__":
    main()
