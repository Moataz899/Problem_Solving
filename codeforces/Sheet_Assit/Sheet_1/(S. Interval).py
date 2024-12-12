X = float(input())

if 0 <= X <= 25:
    print("Interval [0,25]")
elif 25 < X <= 50:
    print("Interval (25,50]")
elif 50 < X <= 75:
    print("Interval (50,75]")
elif 75 < X <= 100:
    print("Interval (75,100]")
else:
    print("Out of Intervals")
    