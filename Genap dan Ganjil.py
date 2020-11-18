a=int(input("Masukkan nilai integer : "))
if a>=0:
    if a%2==0:
        print(a," adalah bilangan positif genap")
    else:
        print(a," adalah bilangan positif ganjil")
else:
    print(a," adalah bilangan negatif")