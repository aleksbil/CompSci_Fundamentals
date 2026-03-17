"""
Algorithm Showcase: Bubble Sort & Binary Search
A demonstration of algorithmic efficiency with fair performance comparison.
"""

def bubble_sort(data):
    """Sorts a list of numbers using the Bubble Sort algorithm."""
    n = len(data)
    steps = 0
    print(f'\n[Sorting] Starting with: {data}')
    
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
                swapped = True
                steps += 1
                print(f'Step {steps}: Swapping {data[j+1]} & {data[j]} -> {data}')
        if not swapped:
            break
            
    print(f'Sorting complete in {steps} swaps.\n')
    return data

def binary_search(data, target):
    """Efficiently finds a value in a sorted list using Binary Search."""
    low = 0
    high = len(data) - 1
    attempts = 0
    
    print(f'[Search] Hunting for: {target}')
    
    while low <= high:
        attempts += 1
        mid = (low + high) // 2
        print(f'Attempt {attempts}: Checking index {mid} (Value: {data[mid]})')
        
        if data[mid] == target:
            return mid, attempts
        
        if data[mid] < target:
            print('Target is HIGHER, discarding the left half.')
            low = mid + 1
        else:
            print('Target is LOWER, discarding the right half.')
            high = mid - 1
            
    return None, attempts

def get_validated_input(prompt):
    """Asks for input until the user provides a valid list of integers."""
    while True:
        user_input = input(prompt)
        try:
            numbers = [int(x) for x in user_input.split()]
            if not numbers:
                print('The list cannot be empty.')
                continue
            return numbers
        except ValueError:
            print('Invalid format! Please enter only NUMBERS separated by spaces.')

def main():
    print('='*45)
    print('   ALGORITHM SHOWCASE: SORTING & EFFICIENCY   ')
    print('='*45)
    
    numbers = get_validated_input('Enter a list of numbers (e.g., 42 7 12 3): ')
    sorted_list = bubble_sort(numbers.copy())
    
    target = None
    while target is None:
        try:
            target = int(input('Enter the number you want to find: '))
        except ValueError:
            print('Please enter a single valid integer.')

    # Execute searches
    index, bin_attempts = binary_search(sorted_list, target)
    
    # Linear search attempts simulation
    if target in sorted_list:
        lin_attempts = sorted_list.index(target) + 1
    else:
        lin_attempts = len(sorted_list)
    
    print('\n' + '='*30)
    print('--- EFFICIENCY BATTLE ---')
    print(f'Linear Search (Brute-force): {lin_attempts} steps')
    print(f'Binary Search (Logarithmic): {bin_attempts} steps')
    
    if index is not None:
        print(f'RESULT: Found at index {index}.')
        if bin_attempts < lin_attempts:
            print(f'WINNER: Binary Search (saved {lin_attempts - bin_attempts} steps)')
        elif lin_attempts < bin_attempts:
            print(f'WINNER: Linear Search (saved {bin_attempts - lin_attempts} steps)')
        else:
            print("WINNER: It's a tie! Both took the same number of steps.")
    else:
        print('RESULT: Value not found in the list.')
    print('='*30)

if __name__ == '__main__':
    main()