import re

def remove(file_path):
    # ファイルの読み込み
    with open(file_path, encoding="UTF-8") as file:
        text = file.read()
    
    # ルビなどの削除
    # ( )で囲まれた文字を削除
    text = re.sub("（[^）]+）","",text)
    # 【 】で囲まれた文字を削除
    text = re.sub("【[^】]+】","",text)
    # ◆から始まる文を削除
    lines = text.split('\n')
    text = '\n'.join(line for line in lines if not line.startswith('◆'))
    # 実験用
    # text = re.sub("<[^>]+>","",text)
    
    #ファイルの書き込み
    file_path = input("書き込むテキスト:")
    with open(file_path,encoding="UTF-8", mode = 'w' ) as file:
        for line in text:
            if not line.isspace():
                file.write(line)
                if line == '。':
                    file.write('\n')
  
    return file_path