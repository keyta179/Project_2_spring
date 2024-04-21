import change
import arrangement
import random

head = """
<html>
<body>
<script src="http://ajax.googleapis.com/ajax/libs/jquery/1.3.2/jquery.min.js"></script>
<script src="springy.js"></script>
<script src="springyui.js"></script>
<script>
var graph = new Springy.Graph();
"""

tail = """
jQuery(function(){
var springy = jQuery('#springydemo').springy({
    graph: graph
});
});
</script>

<canvas id="springydemo" width="1800" height="900" />
</body>
</html>
"""
def fileout_nodes(w_list, file_path, d):
    with open(file_path, mode='a', encoding='UTF-8') as file:
        if w_list!=[]:
            file.write("graph.addNodes(\n")
            node_str=""
            for word in w_list:
                word = word.split(',')
                if word[1]=="名詞" or word[1]=="セリフ" or word[1]=="キーワード":
                    if not (word[2] == "非自立" or word[2] == "代名詞"):
                        node_str = node_str + "'" + word[0] +  "'," +  "\n"
            node_str = node_str.rstrip(",")
            file.write(node_str+")\n")

def fileout_links(w_list, file_path, d):
    with open(file_path, mode='a', encoding='UTF-8') as file:
        n_list = []
        if w_list!=[]:
            file.write("graph.addEdges(\n")
            node_str=""
            for i in range(len(w_list)):
                word1 = None
                word2 = None
                color =  '#000000'
                label = " "
                wordA = w_list[i].split(',')
                if wordA[1] == "名詞" or wordA[1] == "セリフ" or wordA[1] == "キーワード":
                    if not (wordA[2] == "非自立" or wordA[2] == "代名詞"):
                        word1 = wordA[0]
                        for j in range(i+1, len(w_list)):
                            wordB = w_list[j].split(',')
                            if wordB[1] == "動詞" or wordB[1] == "副詞":
                                verb = wordB[0]
                                label = verb
                            if wordB[1] == "助詞":
                                particle = wordB
                                color = change.color(particle)
                            if word1 != None and (wordB[1] == "名詞" or wordB[1] == "セリフ" or wordB[1] == "キーワード"):
                                if not (wordB[2] == "非自立" or wordB[2] == "代名詞"):
                                    word2 = wordB[0]
                                    node_str = node_str + "['" + word1 + "'," + "'" + word2 + "'," + "{ color:" + "'"+color +"'" + ","+  "label:" + "'"+label +"'," + "}" +"]," + "\n"
                                    word1 = None
            node_str = node_str.rstrip(",")
            file.write(node_str+")\n")

def fileout_network(w_lists, file_path, d):
    with open(file_path, mode='w', encoding='UTF-8') as file:
        file.write(head)
    
    for w_list in w_lists:
        fileout_nodes(w_list, file_path, d)
        fileout_links(w_list, file_path, d)

    with open(file_path, mode='a', encoding='UTF-8') as file:
        file.write(tail)