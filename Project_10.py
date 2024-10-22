
def main():
    # Bu fonksiyon diğer fonksiyonların çalışması için tanımlanmıştır.
    bilgiler = kullanicidan_bilgileri_al() # Kullanıcıdan bilgiler fonksiyon aracılığı ile alınmıştır.
    gerekli = puanlari_al_ve_gerekli_listeleri_olustur(bilgiler[0], bilgiler[1])
    # Gerekli işlemler kullanıcıdan alınan değerlere göre yukarıdaki fonksiyonla yaptırılıp değişkene atanmıştır.
    yazdir(bilgiler[0], gerekli[0], gerekli[1], gerekli[2], gerekli[3], gerekli[4])
    # İstenilen çıktılar yukarıdaki fonksiyona gerekli argümanlar gönderilerek yazdırılmıştır.


def kullanicidan_bilgileri_al():
    # Bu fonksiyon kullanıcıdan gelen bilgileri hata kontrolü yaparak alıp, alınan değerleri tutmuştur.
    while True:
        try:
            okcu_sayisi = int(input("Lütfen yarışmadaki okçu sayısını giriniz[en az 10]:"))
            while okcu_sayisi < 10:
                okcu_sayisi = int(input("Lütfen okçu sayısını en az 10 giriniz:"))
        except ValueError:
            print("Yanlış veri girdiniz, lütfen doğru veri giriniz!")
        else:
            break
    while True:
        try:
            atis_hakki = int(input("Lütfen her yarışmacının atacağı ok sayısını giriniz:"))
            while atis_hakki <= 0:
                atis_hakki = int(input("Atış hakkı 0'dan küçük veya 0'a eşit olamaz, lütfen sporcuların atış hakkını "
                                       "tekrar giriniz:"))
        except ValueError:
            print("Yanlış veri girdiniz, lütfen doğru veri giriniz!")
        else:
            break
    return okcu_sayisi, atis_hakki


def puanlari_al_ve_gerekli_listeleri_olustur(okcu_sayisi, atis_hakki):
    # Argüman olarak gelen bilgiler, bu fonksiyonla beraber gerekli adımlarla işlenerek fonksiyonla tutulmuştur.
    TOPLAM_PUAN_ADETI = 11
    RUZGAR_SORMA_PUANI = 0
    # Yukarıda "constant" değişkenler tanımlanmıştır. Herhangi bir kural değişikliğinde kolaylıkla değiştirilebilir.
    ruzgarlar = ["Yıldız", "Poyraz", "Gündoğusu", "Keşişleme", "Kıble", "Lodos", "Günbatısı", "Karayel"]
    # Yukarıdaki liste, rüzgar isimlerinin doğru yazılıp yazılmadığını kontrol etmek için yazılmıştır.
    toplam_sayi_adet = 0
    puanlar_toplami_listesi = [0] * okcu_sayisi
    ondan_sifira_indexe_bagli_adet_listesi = [0] * TOPLAM_PUAN_ADETI
    ruzgar_ismi_sozlugu = {}
    adete_gore_oran_listesi = [0] * TOPLAM_PUAN_ADETI
    tum_sayi_adetleri = []
    # Yukarıda tanımlanan değişkenler aşağıda kullanılacaktır.
    for a in range(okcu_sayisi):
        bir_okcu_icin_adet = [0] * TOPLAM_PUAN_ADETI
        tum_sayi_adetleri.append(bir_okcu_icin_adet)
    for tur_sayisi in range(atis_hakki):
        for yarismaci_sirasi in range(okcu_sayisi):
            # Okçu tarafından alınan puanlar aşağıda hata kontrolü yapılarak alınmıştır.
            while True:
                try:
                    puan = int(input(f"Lütfen {yarismaci_sirasi + 1}. yarışmacının {tur_sayisi + 1}. turda aldığı "
                                     f"puanı giriniz[0-10]:"))
                    while puan < 0:
                        puan = int(input(f"Lütfen {yarismaci_sirasi + 1}. yarışmacının {tur_sayisi + 1}. turda aldığı "
                                         f"puanı 0 veya 0'dan yüksek bir değer giriniz:"))
                except ValueError:
                    print("Yanlış veri girdiniz, lütfen doğru veri giriniz!")
                else:
                    break
            puanlar_toplami_listesi[yarismaci_sirasi] += puan
            toplam_sayi_adet += 1
            if puan == RUZGAR_SORMA_PUANI:
                # Puan 0 olması durumunda kullanıcıdan gelen hatalı veri kontrol edilerek rüzgarın ismi alınmıştır.
                ruzgar = input(f"Lütfen {yarismaci_sirasi + 1}. yarışmacının {tur_sayisi + 1}. turda ıskaladığı "
                               f"atıştaki rüzgarın ismini giriniz[Rüzgarın ismini eksiksiz yazınız]:")
                while ruzgar not in ruzgarlar:
                    print(f"Lütfen {yarismaci_sirasi + 1}. yarışmacının {tur_sayisi + 1}. turda ıskaladığı atıştaki "
                          f"rüzgarın ismini yanlış girdiniz! [rüzgarın ismi büyük harfle başlamalıdır!]")
                    ruzgar = input(
                        f"Lütfen {yarismaci_sirasi + 1}. yarışmacının {tur_sayisi + 1}. turda ıskaladığı atıştaki "
                        f"rüzgarın ismini tekrar giriniz[Rüzgarın ismini eksiksiz yazınız]:")
                tum_sayi_adetleri[yarismaci_sirasi][10] += 1
                ondan_sifira_indexe_bagli_adet_listesi[10] += 1
                if ruzgar in ruzgar_ismi_sozlugu:
                    ruzgar_ismi_sozlugu[ruzgar] += 1
                else:
                    ruzgar_ismi_sozlugu[ruzgar] = 1
            # Aşağıdaki bloklarda puanın farklı olması durumunda farklı senaryolar hesaplanmıştır.
            elif puan == 10:
                tum_sayi_adetleri[yarismaci_sirasi][0] += 1
                ondan_sifira_indexe_bagli_adet_listesi[0] += 1
            elif puan == 9:
                tum_sayi_adetleri[yarismaci_sirasi][1] += 1
                ondan_sifira_indexe_bagli_adet_listesi[1] += 1
            elif puan == 8:
                tum_sayi_adetleri[yarismaci_sirasi][2] += 1
                ondan_sifira_indexe_bagli_adet_listesi[2] += 1
            elif puan == 7:
                tum_sayi_adetleri[yarismaci_sirasi][3] += 1
                ondan_sifira_indexe_bagli_adet_listesi[3] += 1
            elif puan == 6:
                tum_sayi_adetleri[yarismaci_sirasi][4] += 1
                ondan_sifira_indexe_bagli_adet_listesi[4] += 1
            elif puan == 5:
                tum_sayi_adetleri[yarismaci_sirasi][5] += 1
                ondan_sifira_indexe_bagli_adet_listesi[5] += 1
            elif puan == 4:
                tum_sayi_adetleri[yarismaci_sirasi][6] += 1
                ondan_sifira_indexe_bagli_adet_listesi[6] += 1
            elif puan == 3:
                tum_sayi_adetleri[yarismaci_sirasi][7] += 1
                ondan_sifira_indexe_bagli_adet_listesi[7] += 1
            elif puan == 2:
                tum_sayi_adetleri[yarismaci_sirasi][8] += 1
                ondan_sifira_indexe_bagli_adet_listesi[8] += 1
            elif puan == 1:
                tum_sayi_adetleri[yarismaci_sirasi][9] += 1
                ondan_sifira_indexe_bagli_adet_listesi[9] += 1
    # Aşağıdaki forda tüm okçuların yaptıkları atışların puanlara göre oransal dağılımı (%) hesaplanmıştır.
    for y in range(len(ondan_sifira_indexe_bagli_adet_listesi)):
        oran = (ondan_sifira_indexe_bagli_adet_listesi[y] / toplam_sayi_adet) * 100
        adete_gore_oran_listesi[y] = float(f"{oran:.2f}")
    # Aşağıdaki kodlarda tüm ıska atışların rüzgar türlerine göre oransal dağılımı (%) hesaplanmıştır.
    ruzgar_ismi_listesi = list(ruzgar_ismi_sozlugu.keys())
    ruzgar_ismi_adet_listesi = list(ruzgar_ismi_sozlugu.values())
    toplam_iska_sayisi = sum(ruzgar_ismi_adet_listesi)
    iska_atis_oranlari_listesi = [0] * len(ruzgar_ismi_listesi)
    for y in range(len(ruzgar_ismi_listesi)):
        oran = (ruzgar_ismi_adet_listesi[y] / toplam_iska_sayisi) * 100
        iska_atis_oranlari_listesi[y] = float(f"{oran:.2f}")
    # Aşağıda return ile gerekli veriler tutulmuştur.
    return tum_sayi_adetleri, puanlar_toplami_listesi, ruzgar_ismi_listesi, iska_atis_oranlari_listesi, \
        adete_gore_oran_listesi


def yazdir(okcu_sayisi, tum_sayi_adetleri, puanlar_toplami_listesi, ruzgar_ismi_listesi, iska_atis_oranlari_listesi,
           adete_gore_oran_listesi):
    # Bu fonksiyonla gelen argümanlar işlenerek ekrana yazdırılmıştır.
    print("Okçu Kayıt No   10 P    9 P     8 P     7 P     6 P     5 P     4 P     3P      2P      1P      0P     "
          "Toplam Puan")
    print("-------------   -----   -----   -----   -----   -----   -----   -----   -----   -----   -----   -----  "
          "------------")
    for x in range(okcu_sayisi):
        print()
        print(f"{x + 1:<13}", end="   ")
        for b in range(11):
            print(f"{tum_sayi_adetleri[x][b]:<5}", end="   ")
        print(f"{puanlar_toplami_listesi[x]:<12}", end="")
    print()
    print("Tüm Okçular(%)", end="  ")
    for x in range(len(adete_gore_oran_listesi)):
        print(f"%{adete_gore_oran_listesi[x]:<5}", end="  ")
    print()
    print()
    print("Rüzgar Adı", end="      ")
    print("Iska Atış Oranı(%)")
    print("----------", end="      ")
    print("------------------")
    for x in range(len(ruzgar_ismi_listesi)):
        print(f"{ruzgar_ismi_listesi[x]:<10}", end="      %")
        print(f"{iska_atis_oranlari_listesi[x]:<16}")


main()
