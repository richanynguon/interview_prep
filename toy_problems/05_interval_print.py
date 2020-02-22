'''
For each multiple of three print multiple of three
For each multipleof five print multiple of five
'''
from performance_tester import performance_tester

def interval_print(n):
    results=[]
    for i in range(n):
        if (i+1) % 3 == 0:
            results.append("Multiple of Three")
        elif (i+1) % 5 == 0:
            results.append("Multiple of Five")
        else:
            results.append(i+1)
    return results


performance_tester([interval_print],[10,52,325])
