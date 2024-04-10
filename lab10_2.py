class EmptyFileError(Exception):
    def __init__(self, message):
        self.message = message


def read_file(file_name):
    with open(file_name, mode="r", encoding="utf-8") as file:
        content = file.readlines()
        if len(content) > 0:
            print(f"Cодержимое файла '{file_name}':")
            for line in content:
                print(line.strip())
        else:
            raise EmptyFileError(f"Файл '{file_name}' пустой\n")


for file in ['lab10_2_text.txt', 'lab10_2_empty.txt']:
    try:
        read_file(file)
    except Exception as e:
        print(e)
