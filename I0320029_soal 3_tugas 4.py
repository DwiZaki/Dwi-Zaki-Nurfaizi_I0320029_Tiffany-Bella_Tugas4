def koper():
    berat_koper = float(input("Masukkan berat koper(kg) : "))
    x = berat_koper <= 50*0.45
    if x == True:
        print(True, ". Diperbolehkan masuk")
    else:
        print(False, ". Tidak diperbolehkan masuk")

koper()