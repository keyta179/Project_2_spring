

def connection(lists):
    for i in range(1,len(lists)-1):
        #「名詞」「名詞」、あるいは「接頭詞」「名詞」ならセットにして名詞にする=複合名詞
        if lists[i-1][1] == lists[i][1] == "名詞"\
        or (lists[i-1][1] ==  "接頭詞" and lists[i][1] == "名詞"):
            # 「名詞」が自立ならつなげる
            if not lists[i-1][2] == "非自立":
                twoToNoun(lists, i)
        #「名詞」「アルファベット」ならセットにして名詞にする=複合名詞
        if lists[i-1][1] == "名詞" and lists[i][1] == "アルファベット":
            twoToNoun(lists, i)
        #「動詞」「動詞」ならセットにして動詞にする=複合動詞
        if lists[i-1][1] == lists[i][1] == "動詞":
            twoToVerb(lists, i)
        # 「動詞」「助動詞」ならセットにして動詞にする
        if lists[i-1][1] == "動詞" and lists[i][1] == "助動詞":
            twoToVerb(lists, i)
        # 「名詞」「動詞」ならセットにして動詞にする
        if lists[i-1][1] == "名詞" and lists[i][1] == "動詞":
            twoToVerb(lists, i)
        #「形容詞」「名詞」ならセットにして名詞にする
        if lists[i-1][1] == "形容詞" and lists[i][1] == "名詞":
            twoToNoun(lists, i)
        #「動詞」「助詞」「動詞」ならセットにして動詞にする
        if lists[i-1][1] == "動詞" and lists[i][1] == "助詞" and lists[i+1][1] == "動詞":
            threeToVerb(lists, i)
        # 「名詞」「する」ならセットにして動詞にする
        if lists[i-1][1] == "名詞" and lists[i][0] == "する":
            twoToVerb(lists, i)
        # 「名詞」「助詞(副詞化)」ならセットにして副詞にする
        if lists[i-1][1] == "名詞" and lists[i][1] == "助詞" and lists[i][2]=="副詞化":
            twoToAdverb(lists, i)
        # 「助詞」「助詞」ならセットにして助詞にする
        if lists[i-1][1] == "助詞" and lists[i][1] == "助詞":
            twoToParticle(lists, i)
        # 「助動詞」「助動詞」ならセットにして助動詞にする
        if lists[i-1][1] == "助動詞" and lists[i][1] == "助動詞":
            twoToAuxiliaryVerb(lists, i)
        # 「名詞」+「・」+「名詞」ならセットにして名詞にする
        if lists[i-1][1] == "名詞" and lists[i][0] == "・" and lists[i+1][1] == "名詞":
            threeToNoun(lists, i)
        # 「動詞」+「助詞」
        if lists[i-1][1] == "動詞" and lists[i][1] == "助詞":
            # 助詞が接続助詞ならセットにして動詞にする
            if lists[i][2] == "接続助詞":
                twoToVerb(lists, i)
        # セリフ(「　」で囲まれた文)ならまとめて、セリフにする
        if lists[i][1] == "括弧開":
            sentence(lists,i)
    return lists


def twoToNoun(lists, i):
    tmp = lists[i-1][0]+lists[i][0]
    lists[i-1][0] = ""
    lists[i][0] = tmp
    lists[i-1][1] = "空白"
    lists[i][1] = "名詞"
    lists[i][2] = "一般"
    return lists

def twoToVerb(lists, i):
    tmp = lists[i-1][0]+lists[i][0]
    lists[i-1][0] = ""
    lists[i][0] = tmp
    lists[i-1][1] = "空白"
    lists[i][1] = "動詞"
    lists[i][2] = "自立"
    return lists

def twoToAdverb(lists, i):
    tmp = lists[i-1][0]+lists[i][0]
    lists[i-1][0] = ""
    lists[i][0] = tmp
    lists[i-1][1] = "空白"
    lists[i][1] = "副詞"
    lists[i][2] = "一般"
    return lists

def twoToParticle(lists, i):
    tmp = lists[i-1][0]+lists[i][0]
    lists[i-1][0] = ""
    lists[i][0] = tmp
    lists[i-1][1] = "空白"
    lists[i][1] = "助詞"
    return lists

def twoToAuxiliaryVerb(lists, i):
    tmp = lists[i-1][0]+lists[i][0]
    lists[i-1][0] = ""
    lists[i][0] = tmp
    lists[i-1][1] = "空白"
    lists[i][1] = "助動詞"
    return lists

def threeToNoun(lists, i):
    tmp = lists[i-1][0]+lists[i][0]+lists[i+1][0]
    lists[i-1][0] = ""
    lists[i][0] = ""
    lists[i+1][0] = tmp
    lists[i-1][1] = "空白"
    lists[i][1] = "空白"
    lists[i+1][1] = "名詞"
    lists[i+1][2] = "一般"
    return lists

def threeToVerb(lists, i):
    tmp = lists[i-1][0]+lists[i][0]+lists[i+1][0]
    lists[i-1][0] = ""
    lists[i][0] = ""
    lists[i+1][0] = tmp
    lists[i-1][1] = "空白"
    lists[i][1] = "空白"
    lists[i+1][1] = "動詞"
    lists[i+1][2] = "自立"
    return lists

def sentence(lists, i):
    flag = True
    tmp = lists[i][0]
    lists[i][0] = ""
    lists[i][1] = "空白"
    lists[i][2] = "空白"
    while lists[i+1][1] != "括弧閉":
        if lists[i+1][1] != "空白":
            tmp += lists[i+1][0]
            if lists[i+1][0] == "。":
                lists[i+1][0] = tmp + "」"
                lists[i+1][1] = "セリフ"
                lists[i+1][2] = "セリフ"
                tmp = "「".rstrip('\n')
                flag = False
            else:
                lists[i+1][0] = ""
                lists[i+1][1] = "空白"
                lists[i+1][2] = "空白"
        i += 1
    if flag:
        lists[i+1][0] = tmp + "」"
        lists[i+1][1] = "キーワード"
        lists[i+1][2] = "キーワード"
    else:
        lists[i+1][0] = tmp + "」"
        lists[i+1][1] = "空白"
        lists[i+1][2] = "空白"
    return lists