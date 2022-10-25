#soal nomor 1
user = int(input("Masukkan umur : "))

if user >= 17:
    print("anda cukup usia")
else:
    print("sek bocil")
    
#soal nomor 3
bb = float(input("Masukkan berat badan anda :"))
tb = float(input("Masukkan tinggi badan anda :"))
tbm = tb/100
bmi = bb / (tbm*tbm)

if bmi < 18.5 :
    print("anda kurus")
elif bmi >= 18.5 and bmi <= 24.9:
    print("anda ideal")
elif bmi >= 25 and bmi <= 29.9:
    print("anda gemuk")
else:
    print("obesitas")