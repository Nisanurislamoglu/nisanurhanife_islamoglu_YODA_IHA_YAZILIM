class BankaHesabi:
    def __init__(self, hesap_sahibi, hesap_numarasi, bakiye): #init nesne olusturulduğunda başlangıç degrlerini atar, self ise nesneyi temsil eder
        self.hesap_sahibi = hesap_sahibi
        self.hesap_numarasi = hesap_numarasi
        self.bakiye = bakiye

    def para_yatir(self, miktar): #para yatırmak için olan komut
        if miktar > 0:
            self.bakiye += miktar
            print(f"{miktar} TL yatırıldı. ")
        else:
            print("geçersiz miktar. ")

    def para_cek(self, miktar): #para çekmek için olan komut
        if 0 < miktar <= self.bakiye:
            self.bakiye -= miktar
            print(f"{miktar} TL çekildi. ")
        else:
            print("Yetersiz bakiye veya geçersiz miktar.") 

    def bakiye_goruntule(self): #bakiye görüntülemek için olan komut
        print(f"Hesap Sahibi: {self.hesap_sahibi}")
        print(f"Hesap No: {self.hesap_numarasi}")
        print(f"Bakiye: {self.bakiye} TL")

Bankahesabi1 = BankaHesabi("nisa", "08", 1000)  # hesaplarımızı tanımladık
Bankahesabi2 = BankaHesabi("ayşe", "09", 2000)
Bankahesabi3 = BankaHesabi("ahsen", "39", 30000)
Bankahesabi4 = BankaHesabi("asli", "41", 4000)
Bankahesabi5 = BankaHesabi("elif", "44", 5000)

sahip = input("Hesap sahibinin adı giriniz: ")   #hangi hesap için işem yapmamz gerektiğini seçtirdik
hesap_no = input("Hesap numarasını giriniz: ")

if sahip == Bankahesabi1.hesap_sahibi and hesap_no == Bankahesabi1.hesap_numarasi:   #hangi işlem yapıldı ve sonuçlarını yazdırdık
    
    islem = input("Yapmak istediğiniz işlem (yatır/çek/bakiye): ")
    miktar = float(input("Miktar: "))
    if islem == "yatır":
        Bankahesabi1.para_yatir(miktar)
    elif islem == "çek":
        Bankahesabi1.para_cek(miktar)
    elif islem == "bakiye":
        Bankahesabi1.bakiye_goruntule()
    else:
        print("Geçersiz işlem.")
    Bankahesabi1.bakiye_goruntule()

if sahip == Bankahesabi2.hesap_sahibi and hesap_no == Bankahesabi2.hesap_numarasi:
   
    islem = input("Yapmak istediğiniz işlem (yatır/çek/bakiye): ")
    miktar = float(input("Miktar: "))
    if islem == "yatır":
        Bankahesabi2.para_yatir(miktar)
    elif islem == "çek":
        Bankahesabi2.para_cek(miktar)
    elif islem == "bakiye":
        Bankahesabi2.bakiye_goruntule()
    else:
        print("Geçersiz işlem.")     
    Bankahesabi2.bakiye_goruntule()

if sahip == Bankahesabi3.hesap_sahibi and hesap_no == Bankahesabi3.hesap_numarasi:
    
    islem = input("Yapmak istediğiniz işlem (yatır/çek/bakiye): ")
    miktar = float(input("Miktar: "))
    if islem == "yatır":
        Bankahesabi3.para_yatir(miktar)
    elif islem == "çek":
        Bankahesabi3.para_cek(miktar)
    elif islem == "bakiye":
        Bankahesabi3.bakiye_goruntule()
    else:
        print("Geçersiz işlem.")
    Bankahesabi3.bakiye_goruntule()

if sahip == Bankahesabi4.hesap_sahibi and hesap_no == Bankahesabi4.hesap_numarasi:
    
    islem = input("Yapmak istediğiniz işlem (yatır/çek/bakiye): ")
    miktar = float(input("Miktar: "))
    if islem == "yatır":
        Bankahesabi4.para_yatir(miktar)
    elif islem == "çek":
        Bankahesabi4.para_cek(miktar)
    elif islem == "bakiye":
        Bankahesabi4.bakiye_goruntule()
    else:
        print("Geçersiz işlem.")
    Bankahesabi4.bakiye_goruntule()

if sahip == Bankahesabi5.hesap_sahibi and hesap_no == Bankahesabi5.hesap_numarasi:
    
    islem = input("Yapmak istediğiniz işlem (yatır/çek/bakiye): ")
    miktar = float(input("Miktar: "))
    if islem == "yatır":
        Bankahesabi5.para_yatir(miktar)
    elif islem == "çek":
        Bankahesabi5.para_cek(miktar)
    elif islem == "bakiye":
        Bankahesabi5.bakiye_goruntule()
    else:
        print("Geçersiz işlem.")               
    Bankahesabi5.bakiye_goruntule()                
