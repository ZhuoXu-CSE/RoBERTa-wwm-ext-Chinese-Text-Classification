import numpy as np
import linecache

n = np.load('outputs.txt.npy')
f = open('eval.txt', 'r', encoding = 'utf-8')
fw = open('wrong_result.txt', 'w', encoding= 'utf-8')
print(n[123])
wrong = []
for i in range(n.shape[0]):
    if n[i] == 0:
        wrong.append(i)

line = f.readline()
fw.write('Lines should be 0 but get 1.\n')
for i in wrong:
    the_line = linecache.getline('eval.txt', i)
    fw.write(the_line[:-2] +'\n')