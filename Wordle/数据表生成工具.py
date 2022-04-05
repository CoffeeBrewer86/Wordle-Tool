##该程序用于生成所需的数据库，默认生成官方版wordle的数据库。如需生成其他wordle的数据库需要固定格式的对应单词表文件。
##文件字节数大约为单词长度乘以词库单词数的平方。
from copy import deepcopy
list1 = []
list0 = []
dict0 = {}
for u in "abcdefghijklmnopqrstuvwxyz":
    dict0[u] = 0

list1 = ["ioate"]

with open("Wordle答案库.txt", "r") as h:
    for line in h.readlines():
        line = line.strip('\n')
        list0.append(line)      ##创建一个包含整个答案库的list

with open("Wordle库数据表的副本.txt","a") as f:
    for x in list1:     ##list0[x] 是猜测
        for y in list0:     ##list0[y] 是假设的答案
            list_test = []
            dict_x = deepcopy(dict0)
            dict_y = deepcopy(dict0)
            list_test
            ##此规则为官方wordle规则
            for i in range(0,5):
                dict_y[y[i]] += 1
                if x[i] == y[i]:
                    list_test += "2"
                    dict_x[x[i]] += 1
                else:
                    list_test += "0"
            for j in range(0,5):
                if list_test[j] == "0":
                    if x[j] in y:
                        if dict_y[x[j]] > dict_x[x[j]]:
                            list_test[j] = "1"
                            dict_x[x[j]] += 1

            f.write("".join(list_test))
