# String awal
s = 'Hey there! what should this string be?'

# Modifikasi string sesuai dengan permintaan
s = s[:20]
print(s)
s = s.replace('Hey ','Strey')
s = s.replace('there','moka')
s = s.replace('what','play')
s = s.replace('shou','ome!')

# String hasil modifikasi
print("------------------")
print(s)
print("------------------")

# Panjang s harusnya 20
print('\npanjang dari s = %d' % len(s))
print("------------------")

# huruf pertama 'a' harusnya di index no 8
print('\nkemunculan pertama a = %d' % s.index('a'))
print("------------------")

# jumlah huruf a harusnya 2
print('\na muncul sebanyak %d' % s.count('a'), 'kali')
print("------------------")

# memotong string berdasarkan index
print("Lima karakter pertama adalah '%s'" % s[:5])
print("Lima karakter berikutnya adalah '%s'" % s[5:10])
print("Karakter ketiga belas adalah '%s'" % s[12])
print("Karakter dengan indeks ganjil adalah '%s'" %s[1::2])
print("Lima karakter terakhir adalah '%s'" % s[-5:])
print("------------------")

# konversi ke uppercase
print('\nString dalam huruf besar : %s' % s.upper())
print("------------------")

# konversei ke lowercase
print('\nString dalam huruf kecil : %s' % s.lower())
print("------------------")

# cek bagaimana string dimulai
if s.startswith("Str"):
    print('\nString dimulai dengan "Str". Good!')
    print("------------------")

# cek bagaimana string diakhiri
if s.endswith("ome!"):
    print('\nString dikahiri dengan "ome!". Good!')
    print("------------------")

# Pisahkan string menjadi tiga string yang berbeda

# masing-masing hanya berisi satu kata
print(s)
print('pisahkan kata-kata dari string tersebut: %s' % s.split(' '))
print("------------------")