a=input("bir metin veya paragraf giriniz: ") #girdi aldık
toplam_karakter=len(a) #boşlukları dahil ederek toplam karakteri saydık len komutu ile
print("toplam karakter sayısı:", toplam_karakter) 
toplam_kelime=len(a.split()) # .split() komutu ile boşluklardan ayırarak toplam kelime sayısını bulduk
print("toplam kelime sayısı:", toplam_kelime)
en_uzun_kelime=max(a.split(), key=len) # key=len fonksiyonu ile max'ın neye göre sıralaması gerektiğini belirttik
print("en uzun kelime:", en_uzun_kelime)
kelimeler=a.split() # .split() komutu ile boşluklardan ayırarak kelimeleri listeledik
sayaç = {} #kelime sayısı için boş bir sözlük açtık
for kelime in kelimeler: #kelimeler listesindeki her bir kelimeyi tek tek dolaşmak için for döngüsü kullandık
    sayaç[kelime] = sayaç.get(kelime, 0) + 1 #sayaç sözlüğünde kelimenin sayısını bir artırdık, eğer kelime yoksa 0 ile başlatır
for kelime, sayi in sayaç.items(): #sayaç sözlüğündeki her bir kelime ve sayısını dolaşmak için for döngüsü kullandık    
    print(f"{kelime}: {sayi}") #her bir kelime ve sayısını ekrana yazdırdık