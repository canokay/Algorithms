sesli_harfler = "aeıioöuü"
sessiz_harfler = "bcçdfgğhjklmnprsştvyz"
sesliler = ""
sessizler = ""
karakter = ""
kelime = input("Kelime girin: ")
for i in kelime:
    if i in sesli_harfler:
        sesliler += i
    elif i in sessiz_harfler:
        sessizler += i
    else:
        karakter += i
print("sesli harfler: ", sesliler)
print("sessiz harfler: ", sessizler)
if karakter:
    print("Karakter harfler: ", karakter)
