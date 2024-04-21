import file
import analysis

# ファイルの読み込み
text = file.read()

# 接続、単語のノード化(node.js)
word_list = analysis.create_node(text)