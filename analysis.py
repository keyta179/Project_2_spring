from janome.tokenizer import Tokenizer
from janome.tokenfilter import CompoundNounFilter
import relaiton
import node

def create_node(text):        
    t = Tokenizer()
    file_path = input("表示するhtml:")

    part_list = []
    new_part_list = []
    n_line = []
    n_lists = []
    w_line = []
    w_lists = []

    d = {}
    
    for token in t.tokenize(text):
        if token.part_of_speech.split(',')[0]=="記号":
            part_list.append([token.surface, token.part_of_speech.split(',')[1],token.part_of_speech.split(',')[0]])
        else:
            part_list.append([token.surface, token.part_of_speech.split(',')[0],token.part_of_speech.split(',')[1]])
    
    
    with open("part_list.txt",mode="w", encoding="UTF-8") as file:
        for part in part_list:
            file.write(f"{part[0]},{part[1]},{part[2]}"+"\n")
            
    part_list = relaiton.connection(part_list)
    
    for part in part_list:
        if not part[1] == "空白":
            new_part_list += [part]

    for word in new_part_list:
        if word[1]=="名詞":
            n_line.append(word[0])
            if word[0] in d:
                d[word[0]] += 1
            else:
                d[word[0]] = 1
        elif word[1]=="句点":
            n_lists.append(n_line)
            n_line = []

    for word in new_part_list:
        if not (word[1] == "読点" or word[1] == "句点"):
                w_line+=["{},{},{}".format(word[0],word[1],word[2])]
        if word[0] in d:
            d[word[0]] += 1
        else:
            d[word[0]] = 1
        if word[1]=="句点":
            w_lists.append(w_line)
            w_line = []

    with open("word_list.txt",mode="w",encoding="UTF-8") as file:
        for w_list in w_lists:
            for word in w_list:
                word = word.split(',')
                file.write(f"{word[0]},{word[1]},{word[2]}"+"\n")  
            file.write("\n")  
    
    with open("dictionary.txt", mode="w",encoding="UTF-8") as file:
        for k,v in d.items():
            file.write(f"key:{k},value:{v}"+"\n")
            
    node.fileout_network(w_lists, file_path, d)
    
    return new_part_list

