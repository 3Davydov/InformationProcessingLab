import os


def get_texts_from_dir(files_dir):

    test_files = os.listdir(files_dir)

    test_texts = []
    for file_name in test_files:
        file_path = os.path.join(files_dir, file_name)
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
            test_texts.append(text)
    return test_texts