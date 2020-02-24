from performance_tester import performance_tester


#o(N) faster
def print_steps(n):
    stairs = ""
    for i in range(n):
        stairs = stairs+(i*"#")+"\n"

#o(n^2) using the grid method of rows and columns 
def print_steps_nested(n):
    all_stairs = ""
    for i in range(n):
        stairs = ""
        for j in range(n):
            if j <= i:
                stairs += "#"
            else:
                stairs += ""
        all_stairs = all_stairs+stairs+"\n"
    return all_stairs


performance_tester([print_steps, print_steps_nested], [5,10,20])
