import os
import uuid

def clear_directory(directory):
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
        except Exception as e:
            print(f"Failed to delete {file_path}. Reason: {e}")

def split_text_into_chunks(text, chunk_size):
    chunks = []
    for i in range(0, len(text), chunk_size):
        chunks.append(text[i:i+chunk_size])
    return chunks

def save_chunks_to_files(chunks, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    for chunk in chunks:
        chunk_filename = str(uuid.uuid4()) + '.txt'
        with open(os.path.join(output_dir, chunk_filename), 'w', encoding='utf-8') as file:
            file.write(chunk)

def create_dataset_for_author(source_dir_name, out_dir_name, chunk_size):
    clear_directory(out_dir_name)
    for filename in os.listdir(source_dir_name):
        input_file = os.path.join(source_dir_name, filename)
        with open(input_file, 'r', encoding='utf-8') as file:
            text = file.read()
        chunks = split_text_into_chunks(text, chunk_size)
        save_chunks_to_files(chunks, out_dir_name)
        print(f'Файл "{filename}" успешно разбит на {len(chunks)} кусков и сохранен в директории "{out_dir_name}".')
