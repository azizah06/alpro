num = int(input("Masukkan number : "))
num2 = int(input("Masukkan number2 :"))
if num < 10 :
    if num2 == 5:
        print("ini kurang dari sepuluh")
    else:
        print("ini kurang dari sepuluh tapi bukan 5")

elif num > 10:
    print("ini lebih dari sepuluh")

else:
    print("ini else")