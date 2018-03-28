s = input('Please write an integer:')
try:
    if int(s)>=0:
        f = 1
        a = int(s)
        while (a>=2):
            f = f * a
            a -= 1
        print("%s!=%d" % (s,f))
except:
    print("please write a number")