import random
import numpy as np

a=range(10)
b=[el*2 for el in a]
I=[1,2]
I2=['a','b']
I3=[4,5]
f=[(e1,e2,e3) for e1 in I for e2 in I2 for e3 in I3]
print(f)
f2=[]
for e1 in I:
  for e2 in I2:
    for e3 in I3:
      f2.append((e1,e2,e3))
f3=[]
for i in f:
  for j in i:
   print(j)


#val_alpha=np.random.randint(0,9,10)
#print(val_alpha)
#alpha=[(a1,a2,a3,a4) for a1 in val_alpha for a2 in random.sample(val_alpha, len(val_alpha)) for a3 in random.sample(val_alpha, len(val_alpha)) for a4 in random.sample(val_alpha, len(val_alpha)) ]
