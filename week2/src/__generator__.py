import random

cur_file = 1
f = open("dataset/source-" + str(cur_file) + ".txt", 'w')
l_cnt = 0
max_l_cnt = 500000
for n in range(1, 5000001):
    rand = max(int(random.random() * 30), 5)
    f.write(",".join([str(int(random.random() * 10)) for i in range(0, rand)]))
    f.write("\n")
    l_cnt = l_cnt + 1
    if l_cnt >= max_l_cnt and n < 5000000:
        cur_file = cur_file + 1
        f.close()
        f = open("dataset/source-" + str(cur_file) + ".txt", 'w')
        l_cnt = 0
f.close()