s = input('Please write an integer:\n')
try:
    if int(s)>=0:
        print("Even numbers:")
        for i in range(int(s)):
            if i % 2 == 0:
                print(i)
        print("ok!")
except:
        print("please write a number")