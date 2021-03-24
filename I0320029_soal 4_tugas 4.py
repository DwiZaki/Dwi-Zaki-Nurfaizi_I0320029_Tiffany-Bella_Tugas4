def kursus():
    usia = float(input("berapa usiamu?\n: "))
    if usia >= 21:
        spesifikasi = str(input("Apakah anda lulus ujian kualifikasi? (Y/T) : "))
        if  spesifikasi == 'Y' or 'y' :
            print ("Anda dapat mendaftar")
        elif spesifikasi == 'T' or 't':
            print ("Anda tidak dapat mendaftar")
        else:
            print ("Ketik Y/T")
    else:
        print ("Anda tidak dapat mendaftar")
kursus()