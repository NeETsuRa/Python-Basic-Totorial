import statistics as s

# dooing statistic on a list. The class is/can be used in the PythonExampleCode.
def someStatistic(list):
    x = s.mean(list)
    print(x)

    y = s.median(list)
    print(y)

    z = s.mode(list)
    print(z)

    a = s.stdev(list)
    print(a)

    b = s.variance(list)
    print(b)

    print(abs(list[1]))

    largest = max(list)
    print(largest)

    smallest = min(list)
    print(smallest)

    x = 5.622
    x = round(x)
    print(x)