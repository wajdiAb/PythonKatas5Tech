def count_true_values(array):
    """
    Counts the number of True values in the given boolean list.

    Args:
        array: the boolean list to check

    Returns:
        the count of True values in the list
    """
    count = 0
    for value in array:
        if value is True:
            count += 1
    return count


if __name__ == '__main__':
    sample_array = [True, False, True, True, False]
    true_count = count_true_values(sample_array)
    print(true_count)  # 3 should be printed