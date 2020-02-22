from performance_tester import performance_tester
import random

def reverse_int(num):
  if num > 0:
    return int(str(num)[::-1])
  else:
    string=str(num)[::-1]
    return int(string[:-1]) * -1

print(reverse_int(-1213213213))
performance_tester([reverse_int],[1111,32135,123543])