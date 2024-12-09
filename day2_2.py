def is_sequence_safe(nums):
    if len(nums) < 2:
        return True
        
    # Check if all differences are between 1 and 3 (inclusive)
    diffs = [nums[i+1] - nums[i] for i in range(len(nums)-1)]
    
    # Check if all differences are within 1-3 range
    valid_diffs = all(1 <= abs(diff) <= 3 for diff in diffs)
    if not valid_diffs:
        return False
    
    # Check if all numbers are either increasing or decreasing
    all_increasing = all(diff > 0 for diff in diffs)
    all_decreasing = all(diff < 0 for diff in diffs)
    
    return all_increasing or all_decreasing

def is_safe_with_dampener(levels):
    # Convert string numbers to integers
    nums = [int(x) for x in levels.split()]
    
    # First check if it's safe without removing any number
    if is_sequence_safe(nums):
        return True
    
    # If not safe, try removing each number one at a time
    for i in range(len(nums)):
        # Create new list without the current number
        dampened_nums = nums[:i] + nums[i+1:]
        if is_sequence_safe(dampened_nums):
            return True
            
    return False

def count_safe_reports(filename):
    safe_count = 0
    with open(filename, 'r') as f:
        for line in f:
            if is_safe_with_dampener(line.strip()):
                safe_count += 1
    return safe_count

def main():
    filename = 'input_day2.dat'
    result = count_safe_reports(filename)
    print(f"Number of safe reports with Problem Dampener: {result}")

if __name__ == "__main__":
    main()
