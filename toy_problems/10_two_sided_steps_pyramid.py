from performance_tester import performance_tester

#o(n)
def pyramid(n):
    stairs = ''
    for i in range(n):
        stairs = stairs+(((n-i)*" ")+(i*"#")+((n-i)*" ")+"\n")
    return stairs

#o(n^2)
def pyramid_loop(n):
    midpoint = ((2*n)-1)//2
    i = 0
    pyramid = ""
    while i < n:
        level = ''
        j = 0
        while j < ((2*n)-1):
            if midpoint - i <= j and midpoint + i >= j:
                level += "#"
            else:
                level += " "
            j += 1
        i += 1
        pyramid = pyramid+(level + "\n")
    return pyramid


performance_tester([pyramid, pyramid_loop], [5,10,20])
