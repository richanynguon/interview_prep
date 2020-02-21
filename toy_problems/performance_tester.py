import time
import matplotlib.pyplot as plt
import random
from graph_helper import colors


def performance_tester(funcs, inputs, n=100000):
    total_performance = []
    for func in funcs:
        input_length = []
        performance = []
        color = colors[random.randrange(len(colors))-1]
        function_name = func.__name__
        for input in inputs:
            total_duration = 0
            for i in range(n):
                start = time.time()
                func(input)
                end = time.time()
                duration = end - start
                total_duration += duration
            average_duration = total_duration/n
            performance.append(average_duration*10000)
            if type(input) != list and type(input) != dict:
                if type(input) == str:
                    input_length.append(len(input))
                else:
                    input_length.append(input)
            else:
                input_length.append(len(input))
        total_performance.append({func.__name__: performance})
        plt.plot(input_length, performance, color=color,
                 linewidth=5, label=function_name)
        print("debugging reasons",color)
    plt.ylabel('Seconds')
    if type(input) != list and type(input) != dict:
        plt.xlabel(
            'Dyanmic Input Units - Numbers will show - Words will show by how many characters')
    else:
        plt.xlabel('Amount of Elements')
    plt.ylim([0, 1])
    plt.legend()
    plt.show()
    return total_performance
