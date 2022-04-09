import os
import re

FOLDER_NAME = r'./potter/'
PATTERN = r'(?<=Chapter )([\d]*): ([^?=,<]*)'

def get_harry_potter_names(folder_name: str, title_pattern: str):
    for file in os.listdir(folder_name):
        with open(os.path.join(folder_name, file), mode='r', encoding='utf-8') as html_file:
            regex_result = re.search(title_pattern, html_file.read())
        index = regex_result.group(1).zfill(3)
        chapter_name = regex_result.group(2)
        new_file_name = f"{index} {chapter_name}.html".replace(":", "")
        os.rename(os.path.join(folder_name, file), os.path.join(folder_name, new_file_name))
