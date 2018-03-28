s = input('Please write an integer:')
try:
    if int(s)>=0:
        print("odd numbers:")
        for i in range(int(s),0,-1):
            if i%2 != 0:
                print(i)
        print("ok!")
except:
    print("please write a number")