import os


def get_texts_from_file():
    test_data_dir = "texts"

    test_files = os.listdir(test_data_dir)

    test_texts = []
    for file_name in test_files:
        file_path = os.path.join(test_data_dir, file_name)
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
            test_texts.append(text)
    return test_texts