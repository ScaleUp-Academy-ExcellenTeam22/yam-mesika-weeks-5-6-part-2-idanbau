def get_perfect(first_number: int):
    """
    :param first_number: first number to check for matching
    """
    current_num = 1
    while True:
        if sum([num for num in range(first_number, current_num // 2 + 1) if current_num % num == 0]) == current_num:
            yield current_num
        current_num += 1
