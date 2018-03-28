s = input('Please write an integer:')
try:
    if int(s)>=0:
        i = 0
        total = 0
        while (i<=int(s)):
            total = total + i
            i = i + 1
    print("Sum of the numbers between 0 to {0}={1}".format(s,total))
except:
    print("please write a number")