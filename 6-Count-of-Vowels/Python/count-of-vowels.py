s = input()
sesli_harf = 'aeıioöuü'
x = 0
for i in s:
    if i in sesli_harf:
        x += 1
print("%s count of vowels:%d" % (s,x))