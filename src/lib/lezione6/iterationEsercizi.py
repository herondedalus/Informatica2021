import random
import numpy as np



val_alpha=np.random.randint(0,9,10)
count=1
print(val_alpha)

for i in val_alpha:
 print(i)
 if i==count:
   print("GOTTA STOP NOWWW")
   break
 count+=1
else:
  print("seems like there was no problem")

count=1

while i<len(val_alpha):
 print(i)
 if i==count:
  print("GOTTA STOP NOWWW")
  break
 count+=1
else:
   print("seems like there was no problem")


