def find_difference(numbers):
    """
    Finds the difference between the largest and smallest numbers in the list.

    Args:
        numbers: the list of integers

    Returns:
        the difference between the largest and smallest numbers
    """
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list")
    
    if len(numbers) == 0:
        raise ValueError("Input list cannot be empty")
    
    sorted_numbers = sorted(numbers)
    if sorted_numbers:
        return sorted_numbers[-1] - sorted_numbers[0]
    

if __name__ == '__main__':
    sample_list = [10, 3, 5, 6, 20, -2]
    difference = find_difference(sample_list)
    print(difference)  # 22 should be printed