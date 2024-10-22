
def kullanicidan_bilgileri_al():  # Bu fonksiyon kullanıcıdan bilgileri alması için tanımlanmıştır.
    # Aşağıda kodda kullanılacak 'Constant' değişkenler tanımlanmıştır. İleride oyunun kuralı değişirse kolaylıkla
    # programa da müdahale edilebilir.
    MINIMUM_SPORCU_SAYISI = 8
    MIN_PUAN_ALMA_SINIRI = 5
    X_BOLGESI_SORMA_SINIRI = 10
    while True:  # Burada hem kata kontrolü yapılıp kullanıcıya söylenmiş hem de doğru değer alınmıştır.
        try:
            sporcu_sayisi = int(input("Lütfen sporcu sayısını giriniz[en az 8 olmalıdır]:"))
            while sporcu_sayisi < MINIMUM_SPORCU_SAYISI:
                sporcu_sayisi = int(input("Lütfen sporcu sayısını 8 veya 8'den fazla giriniz:"))
        except ValueError:
            print("Hatalı veri girdiniz! Lütfen sporcu sayısını tekrar giriniz!")
        else:
            break
    # Aşağıda sporcu sayısına bağlı olarak kullanılacak listeler oluşturulmuştur.
    isim_listesi = [""] * sporcu_sayisi
    puan_listesi = [0] * sporcu_sayisi
    x_sayisi_listesi = [0] * sporcu_sayisi
    onpuan_sayisi_listesi = [0] * sporcu_sayisi
    while True:  # Burada hem kata kontrolü yapılıp kullanıcıya söylenmiş hem de doğru değer alınmıştır.
        try:
            atis_hakki = int(input("Lütfen yarışmacıların yarışmada yapacağı atış hakkını giriniz:"))
        except ValueError:
            print("Hatalı veri girdiniz! Lütfen sporcu sayısını tekrar giriniz!")
        else:
            break
    for yarismaci_sirasi in range(1, sporcu_sayisi+1):
        # Aşağıda for döngüsünde çeşitli değerler alan değişkenler hata çıkmaması için sıfırlanmıştır
        toplam_puan = 0
        on_puan_sayisi = 0
        x_sayisi = 0
        # Aşağıda kullanıcıdan yarışmacının adı alınmıştır.
        isim = input(f"Lütfen {yarismaci_sirasi}. yarışmacının ad ve soyadını giriniz:")
        isim_listesi[yarismaci_sirasi-1] = isim  # Alınan isim isim listesine indexe bağlı olarak eklenmiştir.
        for atis_sirasi in range(atis_hakki):  # Bu for döngüsü her yarışmacının atışlarını sormak için yazılmıştır.
            while True:  # Burada hem kata kontrolü yapılıp kullanıcıya söylenmiş hem de doğru değer alınmıştır.
                try:
                    puan = int(input(f"Lütfen {isim} isimli yarışmacının {atis_sirasi + 1}. atışında aldığı puanı giriniz[0 veya 5-10]:"))
                    while puan not in [0, 5, 6, 7, 8, 9, 10]:
                        puan = int(input(f"Lütfen {isim} isimli yarışmacının {atis_sirasi + 1}. atışında aldığı puanı 0 veya 5 ile 10 arasında giriniz:"))
                except ValueError:
                    print(f"Hatalı veri girdiniz! Lütfen {isim} isimli yarışmacının {atis_sirasi + 1}. atışında aldığı puanı tekar giriniz!")
                else:
                    break
            if puan >= MIN_PUAN_ALMA_SINIRI:  # puan 5 ve 5'ten büyükse toplam puana ekleniyor.
                toplam_puan += puan
            if puan == X_BOLGESI_SORMA_SINIRI:  # puan 10'a eşitse xe vurup vurmaması için açılmış bir if
                on_puan_sayisi += 1  # Bu if bloğuna girilirse on puan sayısı arttırılıyor.
                x_durumu = input(f"{isim} isimli oyuncu x bölgesine vurdu mu(e/h)?")  # x bölgesine vurulup vurulmadığı kontrollü bir şekilde sorulmuştur
                while x_durumu not in ["e", "h"]:
                    x_durumu = input(f"Yanlış veri girdiniz! Lütfen {isim} isimli oyuncu x bölgesine vurduysa 'e', vurmadıysa 'h' giriniz:")
                if x_durumu == "e":
                    x_sayisi += 1  # Eğer ki 'e' girilirse x sayisi bir arttırılmıştır.
        # Aşağıda hesaplanan değişkenler listelerde yarışmacıya ait indexlere eklenmiştir.
        puan_listesi[yarismaci_sirasi-1] = toplam_puan
        onpuan_sayisi_listesi[yarismaci_sirasi-1] = on_puan_sayisi
        x_sayisi_listesi[yarismaci_sirasi-1] = x_sayisi
    # Aşağıda verilen değerler döndürülmüştür.
    return isim_listesi, puan_listesi, onpuan_sayisi_listesi, x_sayisi_listesi


def siralama_yap_ve_yazdir(kullanicidan_gelen_bilgiler):  # Bu fonksiyon sıralama yapması ve ekrana bastırması için yapılmıştır.
    # Aşağıda istenen çıktı formatının başlangıcı yazdırılmıştır.
    print("Sıra   Ad Soyad                        Puan    10 Sayısı    X Sayısı")
    print("----   --------                        ----    ---------    --------")
    # Aşağıda argümanla gelen listeler fonksiyonda kullanılacak listelere atanmıştır.
    isim_listesi = kullanicidan_gelen_bilgiler[0]
    puan_listesi = kullanicidan_gelen_bilgiler[1]
    on_puan_sayisi_listesi = kullanicidan_gelen_bilgiler[2]
    x_sayisi_listesi = kullanicidan_gelen_bilgiler[3]
    # Aşağıdaki for döngüsü her seferinde listedeki puana, 10 sayısına, x sayısına göre en yüksek puanı
    # hesaplıyor, ekrana yazdırıyor bunu yaptıktan sonra da en yüksek değeri listeden atarak tekrarlıyor.
    for y in range(len(isim_listesi)):
        maksimum_puan = -1
        maksimum_puan_on_sayisi = 0
        maksimum_puan_x_sayisi = 0
        for i in range(len(puan_listesi)):
            if maksimum_puan < puan_listesi[i]:
                maksimum_puan = puan_listesi[i]
                maksimum_puan_on_sayisi = on_puan_sayisi_listesi[i]
                maksimum_puan_x_sayisi = x_sayisi_listesi[i]
                sira = puan_listesi.index(maksimum_puan)
            elif maksimum_puan == puan_listesi[i]:
                if maksimum_puan_on_sayisi < on_puan_sayisi_listesi[i]:
                    maksimum_puan = puan_listesi[i]
                    maksimum_puan_on_sayisi = on_puan_sayisi_listesi[i]
                    maksimum_puan_x_sayisi = x_sayisi_listesi[i]
                    sira = on_puan_sayisi_listesi.index(maksimum_puan_on_sayisi)
                elif maksimum_puan_on_sayisi == on_puan_sayisi_listesi[i]:
                    if maksimum_puan_x_sayisi < x_sayisi_listesi[i]:
                        maksimum_puan = puan_listesi[i]
                        maksimum_puan_on_sayisi = on_puan_sayisi_listesi[i]
                        maksimum_puan_x_sayisi = x_sayisi_listesi[i]
                        sira = x_sayisi_listesi.index(maksimum_puan_x_sayisi)
        print(f"{y+1:4d}", end="   ")
        print(f"{isim_listesi[sira]:<32}", end="")
        print(f"{puan_listesi[sira]:4d}", end="    ")
        print(f"{on_puan_sayisi_listesi[sira]:9d}", end="    ")
        print(f"{x_sayisi_listesi[sira]:8d}")
        puan_listesi.pop(sira)
        on_puan_sayisi_listesi.pop(sira)
        x_sayisi_listesi.pop(sira)
        isim_listesi.pop(sira)


# Aşağıda bir ana fonksiyon tanımlanmıştır.
def main():
    bilgiler = kullanicidan_bilgileri_al()  # Kullanıcıdan alınan değerler bilgiler adlı bir değişkene atanmıştır.
    siralama_yap_ve_yazdir(bilgiler)  # bilgiler değişkeni fonksiyona argüman olarak gönderilmiştir.


# Ana fonksiyon çağırılarak program çıktıları alınmıştır.
main()
# Hocam verileri tek tek girince yapı bozulmuyor ama toplu girince sıra, ad soyad, puan, 10 sayısı, x sayısı yazan yer sağa kayıyor.
