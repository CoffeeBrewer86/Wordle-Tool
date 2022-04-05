dict0 = {}
set0 = set()
from math import log
def cut(obj, sec):
    return [obj[i:i+sec] for i in range(0,len(obj),sec)]

dict_word = {}

with open("Wordle库数据表.txt","r") as f:
    for line in f.readlines():
        str0 = line
        str0 = cut(str0,5*2315)
print(len(str0))
with open("Wordle猜词库.txt", "r") as h:
    for line in h.readlines():
        line = line.strip('\n')
        dict0[len(dict0)] = line

set0 = set(list(range(0,2315)))

while 1:
    a = input("请输入一个5字母单词，它需要在Wordle的猜词库中")
    b = str(input("请用0，1，2的方式输入反馈的结果，它们分别代表灰色，黄色和绿色")).split()
    dict_word[a] = b
    for w in dict_word:
        set_test = set()
        for i in range(0,12978):
            if dict0[i] == w:
                print(w,dict_word[w],i)
                str_test = cut(str0[i],5)
                for j in range(0,2315):
                    if str_test[j] == "".join(list(map(str, dict_word[w]))):
                        set_test.add(j)
        set0 = set0 & set_test

    print(len(set0),log(len(set0),2))
    list_ans = []
    for i in set0:
        list_ans.append(dict0[i])
    print(list_ans)
    if len(set0) == 1:
        break
    K = input("请选择搜索广度。0不搜索，1在可能的答案中搜索，2在答案库中搜索，3在猜词库中搜索")
    if K == "1":
        k = set0.copy()
    elif K == "2":
        k = range(0,2315)
    elif K == "3":
        k = range(0,12978)
    else:
        continue
    dict_ans = {}
    for i in k:     ##猜词备选词
        m = 0
        str_test = cut(str0[i],5)
        list_test = []
        for j in set0:
            list_test.append(str_test[j])
        set_test = set(list_test)
        for j in set_test:     ##假设的答案
            m += list_test.count(j)**2

        dict_ans[dict0[i]] = log(len(set0)**2/m,2)

    list2= sorted(dict_ans.items(),key=lambda x:x[1],reverse = True)
    for x in range(0,min(len(list2),20)):
        print(list2[x])
        