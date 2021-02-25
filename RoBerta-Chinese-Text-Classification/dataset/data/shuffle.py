#coding =utf8
import os
import random
out = open("dev.txt",'w',encoding='utf-8')
lines=[]
with open("dw.txt", 'r', encoding='utf-8') as infile:
	for line in infile:
		lines.append(line)
random.shuffle(lines)
for line in lines:
	out.write(line)
