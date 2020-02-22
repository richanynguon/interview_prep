from performance_tester import performance_tester
import random

# o(n)
def chunking_array(arr, chonk_size=4):
    results = []
    temp_array = []
    for idx, element in enumerate(arr):
        if len(temp_array) < chonk_size:
            temp_array.append(element)
            if idx == (len(arr)-1):
                results.append(temp_array)
        else:
            results.append(temp_array)
            temp_array = []
    return results

# o(n) faster
def chunking_arr(arr, chonk_size=4):
    results = []
    if len(arr) % chonk_size is 0:
        for idx in range(len(arr)//chonk_size):
            results.append(
                [arr[(((idx+1)*chonk_size)-chonk_size):((idx+1)*chonk_size)]])
        return results
    else:
        remainders = (len(arr)-(len(arr) % chonk_size))-1
        for idx in range((len(arr)//chonk_size)+1):
            if idx < remainders:
                results.append(
                    [arr[(((idx+1)*chonk_size)-chonk_size):((idx+1)*chonk_size)]])
            else:
                results.append([arr[remainders:]])
        return results


sample1 = random.sample(range(200), 10)
sample2 = random.sample(range(200), 60)
sample3 = random.sample(range(200), 80)


performance_tester([chunking_array, chunking_arr], [sample1, sample2, sample3])
