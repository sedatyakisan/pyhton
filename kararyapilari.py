ortalamaNot = input("lutfen Ortalamanizi giriniz.")
print(type(ortalamaNot))
OrtalamaNotAsInteger = int(ortalamaNot)
print(type(OrtalamaNotAsInteger))

if OrtalamaNotAsInteger >80 :
    print("gectiniz")
    if OrtalamaNotAsInteger > 90:
        print("bravo gectiniz")
elif OrtalamaNotAsInteger >50:
print("basarili")

else:
    print("malesef kaldiniz")
