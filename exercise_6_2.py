KEYBOARD_LINES = [{'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'},
                  {'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l'},
                  {'z', 'x', 'c', 'v', 'b', 'n', 'm'}]


def is_word_built_with_characters(state: str, lines: str):
    """
    :param state: string that we check if include specific characters
    :param lines: the lines which check for match
    :return: boolean status of the results
    """
    for line in lines:
        if all(character in line for character in state):
            return True
    return False


def get_one_keyboard_line_words(path: str, keyboard_lines: list[set]):
    """
    :param path: wanted path to check for match
    :param keyboard_lines: wanted keyboard lines
    :return: list of words which is only one keyboard line
    """
    with open(path, mode='r') as current_file:
        words = current_file.read().split()
    return [word for word in words if is_word_built_with_characters(word, keyboard_lines)]
