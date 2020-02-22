from performance_tester import performance_tester
import random

# o(1)? faster
def reverse_int(num):
    if num > 0:
        return int(str(num)[::-1])
    else:
        string = str(num)[::-1]
        return int(string[:-1]) * -1

# o(1)?
def reverse_int_second(num):
    reverse = 0
    while num > 0:
        reminder = num % 10
        reverse = (reverse * 10) + reminder
        num = num // 10
    return reverse


performance_tester([reverse_int, reverse_int_second],
                   [-121, 1111, 32135, 123543, ], 100000, False)
