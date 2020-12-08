import sqlite3
import copy

def dfs(synset_tree):
    for synset_root in synset_tree:

        #上位語を検索
        cur = conn.execute("select synset1 from synlink where synset2='%s' and link='hypo'" % synset_root[len(synset_root)-1])
        synsets = []
        for result in cur:
            synsets.append(result[0])

        #上位語が一つもないとき
        if len(synsets) == 0:
            return

        #上位語が一つの場合
        elif len(synsets) == 1:
            synset_root.append(synsets[0])
            dfs(synset_tree)

        #上位語が複数の場合
        elif len(synsets) > 1:
            #現在の道を(上位語の数-1)コ複製する
            for i in range(len(synsets)-1):
                synset_tree.append(copy.deepcopy(synset_root))

            #それぞれ複製した道に複数ある上位語を一つずつ割り当てる
            tree_index = 0
            for hypernym in synsets:
                synset_tree[tree_index].append(hypernym)
                tree_index += 1

            dfs(synset_tree)

if __name__ == '__main__':
    #データベースに接続
    conn = sqlite3.connect("wnjpn.db")

    #単語からそのWordIDを取得
    word = "犬"
    cur = conn.execute("select wordid from word where lemma='%s'" % word)
    word_id = 99999999 #temp
    for row in cur:
        word_id = row[0]

    #WordNetに存在する語であるかの判定
    if word_id==99999999:
        print("[%s]は，WordNetに存在しない単語です．" % word)

    else:
        #WordIDからsynsetIDを取得
        cur = conn.execute("select synset from sense where wordid='%s'" % word_id)
        synset=[]
        for row in cur:
            synset.append(row[0])

        #synsetIDから全ての上位語を検索し，synsetIDのリストとして返す．
        #一つの単語に風数の意味がある場合，synsetは複数になりますが，今回は始めに格納されているものを使います
        synset_roots=[]
        synset_roots.append([synset[0]])
        dfs(synset_roots)

        #概念に含まれる単語を検索して画面に出力する
        no = 1
        for root in synset_roots:
            for synsetID in root:
                cur1 = conn.execute("select name from synset where synset='%s'" % synsetID)
                for row1 in cur1:
                    print("%sつめの概念：%s" %(no, row1[0]))

                cur2 = conn.execute("select def from synset_def where (synset='%s' and lang='jpn')" % synsetID)
                sub_no = 1
                for row2 in cur2:
                    print("意味%s：%s" %(sub_no, row2[0]))
                    sub_no += 1

                no += 1
                print("")