

def pickup_manyword(lists, d):
    word_list = []
    for i in range(len(lists)-1):
        # 頻出度によって残す単語を決める
        if d[lists[i]]>=20:
            word_list.append(lists[i])
    return word_list

def connection(lists, d):
    arrange_list = []
    for i in range(len(lists)-1):
        if i==0:
            now_word = lists[i].split(',')
            after_word = lists[i+1].split(',')
            if now_word[1] == "名詞":
                if after_word[0] == "の" or after_word[0] == "な":
                    arrange_list += [[now_word[0], 1]]
                elif after_word[0] == "と":
                    arrange_list += [[now_word[0], 2]]
                elif after_word[0] == "を":
                    arrange_list += [[now_word[0], 3]]
                else:
                    arrange_list += [[now_word[0], 0]]
            
        else:
            previous_word = lists[i-1].split(',')
            now_word = lists[i].split(',')
            after_word = lists[i+1].split(',')
            if previous_word[1] == "名詞":
                if now_word[0] == "の":
                    arrange_list += [[now_word[0], 1]]
                elif now_word[0] == "と":
                    arrange_list += [[now_word[0], 2]]
                elif now_word[0] == "を":
                    arrange_list += [[now_word[0], 3]]
                else:
                    arrange_list += [[now_word[0], 0]]
            elif previous_word[1] == "動詞":
                arrange_list += [[now_word[0], 0]]
                
    # print(arrange_list)
    return arrange_list