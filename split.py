import winsound
dur=1000
inp = "1000101001110110"
e=6
c = inp[:e]+str(1-eval(inp[e]))+inp[e+1:]

l1=list(c)
l = [eval(i) for i in l1]
print(l)
# got a list with ints

from functools import reduce
import operator as op
p=reduce(op.xor, [i for i,bit in enumerate(l) if bit])
redundant_string=bin(p)[2:]
for i in range(6-len(redundant_string)):
    redundant_string="0"+redundant_string
#final_string = redundant_string + c 
n=len(inp)
x = (n%3 != 0)
lt=[]
for i in range(n//3 + x):
    if(3*i+3 > n):
        lt.append(int(inp[3*i:],2))
    else:
        lt.append(int(inp[3*i:3*i+3],2))
lt.append(int(redundant_string[0:3],2))
lt.append(int(redundant_string[3:],2))

sentinal_freq =800
f0=50    
fl=(n+13)*25
winsound.Beep(sentinal_freq, dur)
winsound.Beep(fl,dur)
for i in lt:
    fs = f0*(8+i)
    winsound.Beep(fs,dur)