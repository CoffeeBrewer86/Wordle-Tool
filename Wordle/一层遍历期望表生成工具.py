dict0 = {}
set0 = set()
dict_ans = {}
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
for i in range(0,12978):     ##猜词备选词
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
print(list2)
