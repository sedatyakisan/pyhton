sayilar =[100,200,300,400,"Merhaba"]

#programci saymaya sifirdan baslanir 0 inci index de 100 degeri gelir
print(sayilar[1])
print(sayilar)

sayilar.append(600)
print(sayilar) #listenin soluna eklenen veriyi yazar
sayilar.remove("Merhaba") #degere gore silme islemi gerceklestirir
sayilar.pop() #index e gore deger siler
print(sayilar)

sayilar.extend([10,2030]) # coklu veri ekleme

sayilar.clear()
print(sayilar)