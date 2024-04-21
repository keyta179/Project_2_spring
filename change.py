
def color(word):
    # 「格助詞」
    if word[2]=="格助詞":
        # 前の単語が主語→赤
        if word[0] == ("が" or "は" or "も"):
            color = '#FF0000'
        # 後ろに動詞
        elif word[0] == "で":
            color = '#00000F'
        # 後ろに動詞→青
        elif word[0] == ("に" or "から" or "へ"):
            color = '#0000FF'
        elif word[0] == "を":
            color = '#FF00FF'
        else:
            color = '#0F0000'
    # 「連体化」→緑
    elif word[2]== "連体化":
        color = '#00FF00'
    # 「係助詞」
    elif word[2]== "係助詞":
        color = '#FF0000'
    else:
        color = '#000000'
    return color