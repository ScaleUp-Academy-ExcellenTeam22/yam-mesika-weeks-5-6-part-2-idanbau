import time


def get_list_set_by_words(file_path: str):
    """
    :param file_path: wanted path to open the words list
    :return: return list of file words and set of file words
    """
    with open(file_path, mode='r', encoding='utf-8') as words_file:
        words_list = [line[:-1] for line in words_file]
        words_set = {line[:-1] for line in words_file}
    return words_list, words_set


def average_runtime(words_list: list[str], words_set: set, tests_count: int, name_to_search: str):
    """
    :param words_list: wanted words list to check
    :param words_set: wanted words set to check
    :param tests_count: number of time to test to calculate average
    :param name_to_search: name to search in both files
    :return: time needed to calculate list search of name_to_search
     in tests_count average and set search of name_to_search in tests_count
    """
    list_start_time = time.time()
    for i in range(tests_count):
        if name_to_search in words_list:
            pass

    list_search_time = (time.time() - list_start_time) / tests_count
    set_start_time = time.time()
    for i in range(tests_count):
        if name_to_search in words_set:
            pass
    set_search_time = (time.time() - set_start_time) / tests_count
    return list_search_time, set_search_time
