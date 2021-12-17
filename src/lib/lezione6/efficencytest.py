import time 
I=list(range(1000000))
V=list(range(10000000))

T1=time.time()

s=I+V
T2=time.time()
print(T2-T1)

m=[]

T1=time.time()
for i in I:
  m.append(i)
for v in V: 
  m.append(v)

T2=time.time()

print(T2-T1)