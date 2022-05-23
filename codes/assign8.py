import numpy as np
from scipy.stats import binom
from scipy import ndimage as nd
A=[1,2,3]
B=[1,2,3,4,5]
#clearly A is subset of B
for i in range (10):
#Randomly generate the parameters
  n = np.random.randint(1, 10)
  for j in range (5):
    if j<3:
      if A[j]==n :
        a+=1
    if B[j]==n :
      b+=1
#P(A)=a/10,P(B)=b/10
#verifying whether P(A) <= P(B)
if a/10 <= b/10 :
  print ("Verified")
else :
  print ("Error")
