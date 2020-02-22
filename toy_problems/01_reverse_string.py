from performance_tester import performance_tester
import random

sample1 = random.sample(range(200), 10)
sample2 = random.sample(range(200), 20)
sample3 = random.sample(range(200), 50)
sample4 = random.sample(range(200), 150)
sample5 = random.sample(range(200), 200)

#o(1)?
def reverse(arr):
    # uses slices start start step
    # performs almost at constant
    return arr[::-1]

#o(N)
def reverse_extended(arr):
    for i in range(len(arr)//2):
        arr[i], arr[len(arr) - i - 1] = arr[len(arr) - i - 1], arr[i]

#o(N)
def reverse_extended_append(arr):
    reversed = []
    for element in arr:
        reversed = [element].append(reverse)
    return reversed



print(performance_tester([reverse, reverse_extended, reverse_extended_append], [
      sample1, sample2, sample3, sample4, sample5], 100000))
