import ruby

def read():
    file_path = input("読み込むテキスト:")
    file_path = ruby.remove(file_path)
    with open(file_path, mode='r', encoding="UTF-8") as file:
        text = file.read()
    return text