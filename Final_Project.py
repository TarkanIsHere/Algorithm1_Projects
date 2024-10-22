
def oyun_bilgilerini_al():
    # Bu fonksiyon kullanıcıdan oyun bilgilerini almak için yapılmıştır.
    birinci_oyuncu_karakter = ""
    ikinci_oyuncu_karakter = ""
    satir_sutun_sayisi = 0
    # Yukarıda 3 adet değişken tanımlanmıştır, bu değişkenler isimlerinden de anlaşılabileceği gibi oyun hakkındaki
    # bilgileri tutacaktır.
    while birinci_oyuncu_karakter == "":
        birinci_oyuncu_karakter = input("1. oyuncuyu temsil etmek için bir karakter giriniz:")
        while len(birinci_oyuncu_karakter) != 1:
            birinci_oyuncu_karakter = input("1. oyuncuyu temsil etmek için bir adet karakter giriniz:")
    while ikinci_oyuncu_karakter == "":
        ikinci_oyuncu_karakter = input("2. oyuncuyu temsil etmek için bir karakter giriniz:")
        while len(ikinci_oyuncu_karakter) != 1:
            ikinci_oyuncu_karakter = input("2. oyuncuyu temsil etmek için bir adet karakter giriniz:")
        while birinci_oyuncu_karakter == ikinci_oyuncu_karakter:
            ikinci_oyuncu_karakter = input("2. oyuncuyu temsil etmek için, 1. oyuncudan farklı bir karakter giriniz:")
    # Yukarıdaki 2 while döngüsü kullanıcının oyunda temsil ettiği karakterleri kontrollü bir şekilde almaktadır.
    # Kullanıcı boş bir girdi girerse veya bir karakterden fazla bir girdi girerse kullanıcıda hatası bildirilip
    # doğru girdi alınana kadar tekrar tekrar karakter bilgisi alınacaktır.
    while satir_sutun_sayisi == 0:
        try:
            satir_sutun_sayisi = int(input("Oyun alanının satır/sütun sayısını giriniz(4-8):"))
            while not( satir_sutun_sayisi >= 4 and satir_sutun_sayisi <= 8):
                satir_sutun_sayisi = int(input("Oyun alanının satır/sütun sayısını 4 ile 8 arasında bir tam sayı giriniz:"))
        except ValueError:
            print("Lütfen oyun alanının satır/sütun sayısına sadece 4 ile 8 arasında pozitif bir tam sayı giriniz")
            satir_sutun_sayisi = 0
    # Yukarıdaki while döngüsü ve try-except, kullanıcıdan oyunun satir ve sutun bilgisini düzgün alma amacıyla yapılmıştır.
    return birinci_oyuncu_karakter, ikinci_oyuncu_karakter, satir_sutun_sayisi
    # Alınan bilgiler geri döndürülmüştür.

    # Yukarıdaki while'ın içerisine try ve except eklenmiştir. Kullanıcı satir sutun sayısına  8'den fazla bir
    # değer girdikçe veya 4 'ten az bir değer girdikçe oyundaki satır ve sütun sayısını tekrar tekrar alacaktır.
    # Satır ve sütun sayısına yanlış bir değer girilmesi durumunda ise except sayesinde kullanıcıya hatası bildirilecek


def oyun_alanini_olustur(birinci_oyuncu_karakter, ikinci_oyuncu_karakter, satir_sutun_sayisi):
    # Bu fonksiyon, oyunun oynanacağı oyun alanını iki boyutlu liste şeklinde oluşturmak amacıyla yazılmıştır.
    iki_boyut_listesi = []
    for satir_no in range(satir_sutun_sayisi):
        satir_listesi = [""] * satir_sutun_sayisi
        for sutun_no in range(satir_sutun_sayisi):
            if satir_no == 0:
                satir_listesi[sutun_no] = ikinci_oyuncu_karakter
            elif satir_no == satir_sutun_sayisi - 1:
                satir_listesi[sutun_no] = birinci_oyuncu_karakter
            else:
                satir_listesi[sutun_no] = ""
        iki_boyut_listesi.append(satir_listesi)
    # Yukarıdaki for döngüsü ile başlangıçta girilen karakterler uygun pozisyonlara if-else koşulları kullanılarak
    # yerleştirilmiştir.
    return iki_boyut_listesi
    # Oluşturulan oyun alanı main fonksiyonunda kullanılmak üzere, bu fonksiyonun sonunda geri döndürülmüştür.


def oyun_alanini_yazdir(satir_sutun_sayisi, sutun_listesi, iki_boyut_listesi):
    # Bu fonksiyon, oyun alanının ödevde istenilen görsel şekilde yazdırması amacıyla tanımlanmıştır.
    print("   ", end="")
    for satir in range(satir_sutun_sayisi):
        if satir <= satir_sutun_sayisi - 2:
            print(f"{sutun_listesi[satir]:^3}", end=" ")
        elif satir > satir_sutun_sayisi - 2:
            print(f"{sutun_listesi[satir]:^3}")
    print("  ", end="")
    print("----" * satir_sutun_sayisi + "-")
    for sutun in range(satir_sutun_sayisi):
        print(sutun + 1, end=" ")
        print("|", end="")
        for satir in range(satir_sutun_sayisi):
            print(f"{iki_boyut_listesi[sutun][satir]:^3}", end="")
            if satir > satir_sutun_sayisi - 2:
                print(f"| {sutun+1}")
            else:
                print("|", end="")

        print("  ", end="")
        print("----" * satir_sutun_sayisi + "-")
    print("   ", end="")
    for satir in range(satir_sutun_sayisi):
        if satir <= satir_sutun_sayisi - 2:
            print(f"{sutun_listesi[satir]:^3}", end=" ")
        elif satir > satir_sutun_sayisi - 2:
            print(f"{sutun_listesi[satir]:^3}")


def oyuncunun_hareketini_al_ve_kontrol_et(birinci_oyuncu_karakter, ikinci_oyuncu_karakter, kontrol_sayisi,
                                          sutun_listesi, iki_boyut_listesi, satir_sutun_sayisi):
    # Bu fonksiyon, kullanıcıdan o anda taşının sahip olduğu konumu ve hedef konumunu doğru bir şekilde alması amacıyla
    # yazılmıştır.
    baskasinin_tasini_hareket_ettirme = True
    capraz_hareket = True
    tas_olan_yere_hareket = True
    tas_olmayan_yer_secimi = True
    tas_ustunden_atlama = True
    yanlis_konum_girme = True
    # Yukarıda kullanıcının yanlış bir konum ve hedef konum girmesi durumunda, konum ve hedef bilgisinin tekrar alınması
    # için tanımlanmıştır.
    while capraz_hareket is True or tas_olan_yere_hareket is True or tas_olmayan_yer_secimi is True or \
            baskasinin_tasini_hareket_ettirme is True or tas_ustunden_atlama is True or yanlis_konum_girme is True:
        # Bu while, yanlış girilme durumundan herhangi biri bile sağlansa tekrardan kullanıcıdan konum ve hedef bilgisini
        # almak için yazılmıştır.
        tas_ustunden_atlama = False
        yanlis_konum_girme = False
        # Aşağıda kontrol sayısı tek sayılarda 1. oyuncu için konum ve hedef konum bilgisi girmesini sağlarken
        # çift sayılarda 2. oyuncunun konum ve hedef bilgisinin alınmasını sağlamıştır.
        if kontrol_sayisi % 2 == 1:
            oyuncunun_hareketi = input(f"Oyuncu {birinci_oyuncu_karakter}, lütfen hareket ettirmek istediğiniz kendi "
                                       f"taşınızın "f"konumunu ve hedef konumu giriniz:")
            while oyuncunun_hareketi == "" or len(oyuncunun_hareketi) != 5 or oyuncunun_hareketi[2] != " ":
                # Yukarıdaki while döngüsü oyuncunun konum bilgisini doğru almak amacıyla yazılmıştır.
                # Yukarıdaki while döngüsü oyuncunun konum bilgisini doğru almak amacıyla yazılmıştır. Kullanıcı konum
                # bilgisine boş bir girdi, 5'ten fazla uzunluğa sahip bir girdi, ve taşın konum bilgisi ile hedef konumu
                # arasında boşluk girilmemesi durumunda tekrar tekrar oyuncunun hareket bilgisini alacaktır Aynısı
                # ikinci oyuncu için de aşağıda bir while döngüsü ile kontrol edilmiştir.
                print("Yanlış konum girdiniz! Lütfen tekrar giriniz.")
                oyuncunun_hareketi = input(
                    f"Oyuncu {birinci_oyuncu_karakter}, lütfen hareket ettirmek istediğiniz kendi "
                    f"taşınızın konumunu ve hedef konumunu tekrar giriniz:")

        elif kontrol_sayisi % 2 == 0:
            oyuncunun_hareketi = input(f"Oyuncu {ikinci_oyuncu_karakter}, lütfen hareket ettirmek istediğiniz kendi "
                                       f"taşınızın "f"konumunu ve hedef konumu giriniz:")
            while oyuncunun_hareketi == "" or len(oyuncunun_hareketi) != 5 or oyuncunun_hareketi[2] != " ":
                # Yukarıdaki while döngüsü oyuncunun konum bilgisini doğru almak amacıyla yazılmıştır.
                print("Yanlış konum girdiniz! Lütfen tekrar giriniz.")
                oyuncunun_hareketi = input(
                    f"Oyuncu {ikinci_oyuncu_karakter}, lütfen hareket ettirmek istediğiniz kendi "
                    f"taşınızın konumunu ve hedef konumunu tekrar giriniz:")

        oyuncunun_konum_sutunu = oyuncunun_hareketi[1]
        oyuncunun_konum_satiri = int(oyuncunun_hareketi[0]) - 1
        oyuncunun_hedef_sutunu = oyuncunun_hareketi[4]
        oyuncunun_hedef_satiri = int(oyuncunun_hareketi[3]) - 1
        sutun_listesi_kontrol = [""] * satir_sutun_sayisi
        kontrol_listesi = []
        for x in range(satir_sutun_sayisi):
            kontrol_listesi.append(x)
            sutun_listesi_kontrol[x] = sutun_listesi[x]

        if oyuncunun_konum_satiri not in kontrol_listesi or oyuncunun_hedef_satiri not in kontrol_listesi or \
                oyuncunun_konum_sutunu not in sutun_listesi_kontrol or oyuncunun_hedef_sutunu not in \
                sutun_listesi_kontrol:
            print("Yanlış bir konum girdiniz! Lütfen tekrar giriniz.")
            yanlis_konum_girme = True
        # Yukarıda düzgün bir konum bilgisi girildiğinde oyuncunun oyun alanında bir konum ve hedef konumu girdiği
        # tespit edilmesi amacıyla yazılmıştır.

        for satir in sutun_listesi:
            if satir == oyuncunun_hedef_sutunu:
                oyuncunun_hedef_sutunu = int(sutun_listesi.index(satir))
            if satir == oyuncunun_konum_sutunu:
                oyuncunun_konum_sutunu = int(sutun_listesi.index(satir))
        # Aşağıda düzgün bir konum girilmesi durumunda konum ve hedef konum bilgilerinin doğru olup olmadığı hiyerarşik
        # bir sıraya göre kontrol edilmiştir. Böylece gereksiz işlemlerden kaçınılmıştır.

        # Bu hiyerarşik sıra sayesinde gereksiz işlemden kaçınılacaktır.
        # Öncelikle kullanıcı doğru bir konum ve hedef konum bilgisi girdi mi? Doğru konumu ve hedefi doğru formatta
        # girdiyse taşının olmadığı bir nokta girdi mi? Doğru girdiyse başkasının taşını mı hareket ettirmeye çalışıyor
        # başkasının taşını hareket ettirmeye çalışmıyorsa, çapraz mı hareket ettirmeye çalışıyor, çapraz hareket ettir-
        # meye çalışmıyorsa, taşın olduğu bir yere mi taşını hareket ettirmek istiyor, istemiyorsa  bir taşın üzerinden
        # mi atlıyor bunlar kontrol edilmiştir.

        if yanlis_konum_girme is False:
            if iki_boyut_listesi[oyuncunun_konum_satiri][oyuncunun_konum_sutunu] == '':
                tas_olmayan_yer_secimi = True
                print("Karakterinizin olmadığı bir yer seçtiniz! Lütfen tekrar giriniz.")
            else:
                tas_olmayan_yer_secimi = False

            if tas_olmayan_yer_secimi is False:
                if kontrol_sayisi % 2 == 1:
                    if iki_boyut_listesi[oyuncunun_konum_satiri][oyuncunun_konum_sutunu] != birinci_oyuncu_karakter:
                        baskasinin_tasini_hareket_ettirme = True
                        print(
                            f"Oyuncu {birinci_oyuncu_karakter}"
                            f" sadece kendi taşınızı hareket ettirebilirsiniz! Lütfen tekrar giriniz.")
                    else:
                        baskasinin_tasini_hareket_ettirme = False
                elif kontrol_sayisi % 2 == 0:
                    if iki_boyut_listesi[oyuncunun_konum_satiri][oyuncunun_konum_sutunu] != ikinci_oyuncu_karakter:
                        baskasinin_tasini_hareket_ettirme = True
                        print(
                            f"Oyuncu {ikinci_oyuncu_karakter}"
                            f" sadece kendi taşınızı hareket ettirebilirsiniz! Lütfen tekrar giriniz.")
                    else:
                        baskasinin_tasini_hareket_ettirme = False

            if baskasinin_tasini_hareket_ettirme is False:
                if oyuncunun_konum_sutunu != oyuncunun_hedef_sutunu and \
                        oyuncunun_konum_satiri != oyuncunun_hedef_satiri:
                    capraz_hareket = True
                    print("Karakterini çapraz hareket ettiremezsiniz! Lütfen tekrar giriniz.")
                else:
                    capraz_hareket = False

            if capraz_hareket is False:
                if iki_boyut_listesi[oyuncunun_hedef_satiri][oyuncunun_hedef_sutunu] != '':
                    tas_olan_yere_hareket = True
                    print(
                        "Karakterinizi başka bir karakterin olduğu yere hareket ettiremezsiniz! Lütfen tekrar giriniz.")
                else:
                    tas_olan_yere_hareket = False

            if tas_olan_yere_hareket is False:
                if oyuncunun_konum_satiri > oyuncunun_hedef_satiri:
                    for x in range(oyuncunun_konum_satiri - oyuncunun_hedef_satiri):
                        if iki_boyut_listesi[oyuncunun_konum_satiri - x - 1][oyuncunun_konum_sutunu] != "":
                            print("Bir taşın üzerinden atlayamazsınız!")
                            tas_ustunden_atlama = True

                elif oyuncunun_konum_satiri < oyuncunun_hedef_satiri:
                    for x in range(oyuncunun_hedef_satiri - oyuncunun_konum_satiri):
                        if iki_boyut_listesi[oyuncunun_konum_satiri + x + 1][oyuncunun_konum_sutunu] != "":
                            print("Bir taşın üzerinden atlayamazsınız!")
                            tas_ustunden_atlama = True

                if oyuncunun_konum_sutunu > oyuncunun_hedef_sutunu:
                    for x in range(oyuncunun_konum_sutunu - oyuncunun_hedef_sutunu):
                        if iki_boyut_listesi[oyuncunun_konum_satiri][oyuncunun_konum_sutunu - x - 1] != "":
                            print("Bir taşın üzerinden atlayamazsınız!")
                            tas_ustunden_atlama = True

                elif oyuncunun_konum_sutunu < oyuncunun_hedef_sutunu:
                    for x in range(oyuncunun_hedef_sutunu - oyuncunun_konum_sutunu):
                        if iki_boyut_listesi[oyuncunun_konum_satiri][oyuncunun_konum_sutunu + x + 1] != "":
                            print("Bir taşın üzerinden atlayamazsınız!")
                            tas_ustunden_atlama = True

    if kontrol_sayisi % 2 == 1:
        iki_boyut_listesi[oyuncunun_konum_satiri][oyuncunun_konum_sutunu] = ""
        iki_boyut_listesi[oyuncunun_hedef_satiri][oyuncunun_hedef_sutunu] = birinci_oyuncu_karakter
    elif kontrol_sayisi % 1 == 0:
        iki_boyut_listesi[oyuncunun_konum_satiri][oyuncunun_konum_sutunu] = ""
        iki_boyut_listesi[oyuncunun_hedef_satiri][oyuncunun_hedef_sutunu] = ikinci_oyuncu_karakter
    # Başarılı bir şekilde konum bilgisi girilirse yukarıdaki işlemler oyun alanında gerekli değişikliği yapacaktır.

    return iki_boyut_listesi, oyuncunun_hedef_satiri, oyuncunun_hedef_sutunu
    # Başarılı konum girilmesi durumunda yeni oyun alanı, oyuncunun hedef satiri ve oyuncunun hedef sutunu
    # bu fonksiyonla geriye döndürülecektir.


def tas_cikarilip_cikarilmama_kontrol(birinci_oyuncu_karakter, ikinci_oyuncu_karakter, satir_sutun_sayisi,
                                      iki_boyut_listesi, oyuncunun_hedef_satiri, oyuncunun_hedef_sutunu):
    # Bu fonksiyon başarılı bir şekilde gelen konum bilgisi sonucunda herhangi bir taşın çıkıp çıkmaması durumunu
    # kontrol edecek, eğer bir karakterin çıkması gerekiyorsa doğru konumdan taşı çıkarıp oyuncuya bilgi verecektir.
    sutun_listesi_sozlugu = {0: "A", 1: "B", 2: "C", 3: "D", 4: "E", 5: "F", 6: "G", 7: "H"}

    # Aşağıdaki nested if blokları, köşeler hariç bir noktada herhangi bir taş çıkarma durumu olduğunu kontrol edecektir
    # Bu if birinci karakter için köşeler haricinde bir çıkarma durumu varsa kontrol edip taşı çıkaracaktır.
    if iki_boyut_listesi[oyuncunun_hedef_satiri][oyuncunun_hedef_sutunu] == birinci_oyuncu_karakter:
        if oyuncunun_hedef_sutunu - 1 >= 0:
            if iki_boyut_listesi[oyuncunun_hedef_satiri][oyuncunun_hedef_sutunu - 1] == ikinci_oyuncu_karakter:
                if oyuncunun_hedef_sutunu - 2 >= 0:
                    if iki_boyut_listesi[oyuncunun_hedef_satiri][oyuncunun_hedef_sutunu - 2] == birinci_oyuncu_karakter:
                        iki_boyut_listesi[oyuncunun_hedef_satiri][oyuncunun_hedef_sutunu - 1] = ""
                        print(
                            f"{oyuncunun_hedef_satiri + 1}{sutun_listesi_sozlugu[oyuncunun_hedef_sutunu - 1]}"
                            f" konumundaki taş çıkarıldı!")

        if oyuncunun_hedef_sutunu + 1 <= satir_sutun_sayisi - 1:
            if iki_boyut_listesi[oyuncunun_hedef_satiri][oyuncunun_hedef_sutunu + 1] == ikinci_oyuncu_karakter:
                if oyuncunun_hedef_sutunu + 2 <= satir_sutun_sayisi - 1:
                    if iki_boyut_listesi[oyuncunun_hedef_satiri][oyuncunun_hedef_sutunu + 2] == birinci_oyuncu_karakter:
                        iki_boyut_listesi[oyuncunun_hedef_satiri][oyuncunun_hedef_sutunu + 1] = ""
                        print(
                            f"{oyuncunun_hedef_satiri + 1}{sutun_listesi_sozlugu[oyuncunun_hedef_sutunu + 1]}"
                            f" konumundaki taş çıkarıldı!")
        if oyuncunun_hedef_satiri - 1 >= 0:
            if iki_boyut_listesi[oyuncunun_hedef_satiri - 1][oyuncunun_hedef_sutunu] == ikinci_oyuncu_karakter:
                if oyuncunun_hedef_satiri - 2 >= 0:
                    if iki_boyut_listesi[oyuncunun_hedef_satiri - 2][oyuncunun_hedef_sutunu] == birinci_oyuncu_karakter:
                        iki_boyut_listesi[oyuncunun_hedef_satiri - 1][oyuncunun_hedef_sutunu] = ""
                        print(
                            f"{oyuncunun_hedef_satiri}{sutun_listesi_sozlugu[oyuncunun_hedef_sutunu]}"
                            f" konumundaki taş çıkarıldı!")
        if oyuncunun_hedef_satiri + 1 <= satir_sutun_sayisi - 1:
            if iki_boyut_listesi[oyuncunun_hedef_satiri + 1][oyuncunun_hedef_sutunu] == ikinci_oyuncu_karakter:
                if oyuncunun_hedef_satiri + 2 <= satir_sutun_sayisi - 1:
                    if iki_boyut_listesi[oyuncunun_hedef_satiri + 2][oyuncunun_hedef_sutunu] == birinci_oyuncu_karakter:
                        iki_boyut_listesi[oyuncunun_hedef_satiri + 1][oyuncunun_hedef_sutunu] = ""
                        print(
                            f"{oyuncunun_hedef_satiri + 2}{sutun_listesi_sozlugu[oyuncunun_hedef_sutunu]}"
                            f" konumundaki taş çıkarıldı!")
    # Bu if ikinci karakter için köşeler haricinde bir çıkarma durumu varsa kontrol edip taşı çıkaracaktır.
    if iki_boyut_listesi[oyuncunun_hedef_satiri][oyuncunun_hedef_sutunu] == ikinci_oyuncu_karakter:
        if oyuncunun_hedef_sutunu - 1 >= 0:
            if iki_boyut_listesi[oyuncunun_hedef_satiri][oyuncunun_hedef_sutunu - 1] == birinci_oyuncu_karakter:
                if oyuncunun_hedef_sutunu - 2 >= 0:
                    if iki_boyut_listesi[oyuncunun_hedef_satiri][oyuncunun_hedef_sutunu - 2] == ikinci_oyuncu_karakter:
                        iki_boyut_listesi[oyuncunun_hedef_satiri][oyuncunun_hedef_sutunu - 1] = ""
                        print(
                            f"{oyuncunun_hedef_satiri + 1}{sutun_listesi_sozlugu[oyuncunun_hedef_sutunu - 1]}"
                            f" konumundaki taş çıkarıldı!")
        if oyuncunun_hedef_sutunu + 1 <= satir_sutun_sayisi - 1:
            if iki_boyut_listesi[oyuncunun_hedef_satiri][oyuncunun_hedef_sutunu + 1] == birinci_oyuncu_karakter:
                if oyuncunun_hedef_sutunu + 2 <= satir_sutun_sayisi - 1:
                    if iki_boyut_listesi[oyuncunun_hedef_satiri][oyuncunun_hedef_sutunu + 2] == ikinci_oyuncu_karakter:
                        iki_boyut_listesi[oyuncunun_hedef_satiri][oyuncunun_hedef_sutunu + 1] = ""
                        print(
                            f"{oyuncunun_hedef_satiri + 1}{sutun_listesi_sozlugu[oyuncunun_hedef_sutunu + 1]}"
                            f" konumundaki taş çıkarıldı!")
        if oyuncunun_hedef_satiri - 1 >= 0:
            if iki_boyut_listesi[oyuncunun_hedef_satiri - 1][oyuncunun_hedef_sutunu] == birinci_oyuncu_karakter:
                if oyuncunun_hedef_satiri - 2 >= 0:
                    if iki_boyut_listesi[oyuncunun_hedef_satiri - 2][oyuncunun_hedef_sutunu] == ikinci_oyuncu_karakter:
                        iki_boyut_listesi[oyuncunun_hedef_satiri - 1][oyuncunun_hedef_sutunu] = ""
                        print(
                            f"{oyuncunun_hedef_satiri}{sutun_listesi_sozlugu[oyuncunun_hedef_sutunu]}"
                            f" konumundaki taş çıkarıldı!")
        if oyuncunun_hedef_satiri + 1 <= satir_sutun_sayisi - 1:
            if iki_boyut_listesi[oyuncunun_hedef_satiri + 1][oyuncunun_hedef_sutunu] == birinci_oyuncu_karakter:
                if oyuncunun_hedef_satiri + 2 <= satir_sutun_sayisi - 1:
                    if iki_boyut_listesi[oyuncunun_hedef_satiri + 2][oyuncunun_hedef_sutunu] == ikinci_oyuncu_karakter:
                        iki_boyut_listesi[oyuncunun_hedef_satiri + 1][oyuncunun_hedef_sutunu] = ""
                        print(
                            f"{oyuncunun_hedef_satiri + 2}{sutun_listesi_sozlugu[oyuncunun_hedef_sutunu]}"
                            f" konumundaki taş sıkıştırıldı ve çıkarıldı!")

    # Aşağıdaki for döngüsü köşelerde bir taşın sıkışma durumu olup olmadığını var ise taşı çıkararak kullancıya bilgi
    # verecektir.
    for satir in range(satir_sutun_sayisi):
        for sutun in range(satir_sutun_sayisi):
            if sutun == 0 and satir == 0:  # sol üst
                if iki_boyut_listesi[satir][sutun] != '' and iki_boyut_listesi[satir + 1][sutun] != '' and \
                        iki_boyut_listesi[satir][sutun + 1] != '':
                    if iki_boyut_listesi[satir][sutun] != iki_boyut_listesi[satir + 1][sutun] and \
                            iki_boyut_listesi[satir][sutun] != iki_boyut_listesi[satir][sutun + 1]:
                        iki_boyut_listesi[satir][sutun] = ""
                        print(f"{satir + 1}{sutun_listesi_sozlugu[sutun]}"
                              f" konumundaki taş köşeye sıkıştırıldı ve çıkarıldı!")

            elif sutun == (satir_sutun_sayisi - 1) and satir == 0:  # sağ üst köşe
                if iki_boyut_listesi[satir][sutun] != '' and iki_boyut_listesi[satir][sutun - 1] != '' and \
                        iki_boyut_listesi[satir + 1][sutun] != '':
                    if iki_boyut_listesi[satir][sutun] != iki_boyut_listesi[satir][sutun - 1] and \
                            iki_boyut_listesi[satir + 1][sutun] != iki_boyut_listesi[satir][sutun]:
                        iki_boyut_listesi[satir][sutun] = ""
                        print(f"{satir + 1}{sutun_listesi_sozlugu[sutun]}"
                              f" konumundaki taş köşeye sıkıştırıldı ve çıkarıldı!")

            elif sutun == 0 and satir == (satir_sutun_sayisi - 1):  # sol alt köşe
                if iki_boyut_listesi[satir][sutun] != '' and iki_boyut_listesi[satir - 1][sutun] != '' and \
                        iki_boyut_listesi[satir][sutun + 1] != '':
                    if iki_boyut_listesi[satir][sutun] != iki_boyut_listesi[satir - 1][sutun] and \
                            iki_boyut_listesi[satir][sutun + 1] != iki_boyut_listesi[satir][sutun]:
                        iki_boyut_listesi[satir][sutun] = ""
                        print(f"{satir + 1}{sutun_listesi_sozlugu[sutun]}"
                              f" konumundaki taş köşeye sıkıştırıldı ve çıkarıldı!")

            elif sutun == (satir_sutun_sayisi - 1) and satir == (satir_sutun_sayisi - 1):  # sağ alt köşe
                if iki_boyut_listesi[satir][sutun] != '' and iki_boyut_listesi[satir][sutun - 1] != '' and \
                        iki_boyut_listesi[satir - 1][sutun] != '':
                    if iki_boyut_listesi[satir][sutun] != iki_boyut_listesi[satir][sutun - 1] and \
                            iki_boyut_listesi[satir][sutun] != iki_boyut_listesi[satir - 1][sutun]:
                        iki_boyut_listesi[satir][sutun] = ""
                        print(f"{satir + 1}{sutun_listesi_sozlugu[sutun]}"
                              f" konumundaki taş köşeye sıkıştırıldı ve çıkarıldı!")


    return iki_boyut_listesi
    # Bu fonksiyon bir çıkarılma durumu olup olmadığını kontrol edip yeni oyun alanını geriye döndürecektir.


def main():
    # Bu fonksiyon, oyunun oynanmasını sağlayan fonksiyonların bir araya doğru şekilde getirilmesi amacıyla oluşturulmuştur.
    sutun_listesi = ["A", "B", "C", "D", "E", "F", "G", "H"]
    MIN_KARAKTER_SAYISI = 1

    tekrar_oynama = "E"  # En az bir kere girmesi için "E" olarak tanımlanmıştır.
    while tekrar_oynama == "E":
        # Oyun tekrar oynanmak istenirse bilgiler tekrardan fonksiyonlar yardımıyla alınacak, geriye döndürülen değerler
        # indexlerine göre değişkenlere atanacaktır.
        alinmis_bilgiler = oyun_bilgilerini_al()
        birinci_oyuncu_karakter = alinmis_bilgiler[0]
        ikinci_oyuncu_karakter = alinmis_bilgiler[1]
        satir_sutun_sayisi = alinmis_bilgiler[2]
        # Yukarıda oyun bilgileri alındıktan sonra isimlerinden de anlaşılacağı gibi geriye döndürülen değerler
        # indexlere göre çeşitli değişkenlere atanmıştır.
        oyun_alani = oyun_alanini_olustur(birinci_oyuncu_karakter, ikinci_oyuncu_karakter, satir_sutun_sayisi)
        # Yukarıda oyun alanı, oyun_alanini_olustur fonksiyonuna gerekli argümanlar doğru sırada gönderilerek oluşturulmuştur.
        kontrol_sayisi = 0
        # Yukarıdaki değişken, tek sayılarda 1. oyuncuya, çift sayılarda ise 2. oyuncuya hareket bilgilerini sorması
        # amacıyla oluşturulmuştur. Program, her while döngüsüne girdiğinde ise 1 adet arttırılmıştır.
        birinci_karakter_sayisi = 2
        ikinci_karakter_sayisi = 2
        # Yukarıdaki değişkenler 0'dan farklı oldukça oyun oynanmaya devam edecektir. Hamleler sonucunda ikisinden
        # birisi 0'a inerse yani herhangi bir oyuncunun bir taşı kalmaz ise oyunu sonlandıracaktır.
        while birinci_karakter_sayisi > MIN_KARAKTER_SAYISI and ikinci_karakter_sayisi > MIN_KARAKTER_SAYISI:
            kontrol_sayisi += 1
            birinci_karakter_sayisi = 0
            ikinci_karakter_sayisi = 0
            # Aşağıda başlangıç oyun alanı gerekli argümanlar oyun_alanina_yazdir fonksiyonuna gönderilerek yazdirilmistir.
            oyun_alanini_yazdir(satir_sutun_sayisi, sutun_listesi, oyun_alani)
            # Aşağıda oyuncunun_hareketini_al_ve_kontrol_et fonksiyonuna gerekli argümanlar gönderilerek oyuncunun hareketi
            # düzgün bir şekilde alınmış, geriye döndürdüğü bilgiler bir değişkene atılmıştır.
            hareket_sonrasi_bilgiler = oyuncunun_hareketini_al_ve_kontrol_et(birinci_oyuncu_karakter, ikinci_oyuncu_karakter, kontrol_sayisi, sutun_listesi, oyun_alani, satir_sutun_sayisi)
            # Hareket sonrasında fonksiyonla döndürülen ilgili değerler indexlerine göre ilgili değişkenlere atanmıştır.
            yeni_iki_boyut_listesi = hareket_sonrasi_bilgiler[0]
            oyuncunun_hedef_satiri = hareket_sonrasi_bilgiler[1]
            oyuncunun_hedef_sutunu = hareket_sonrasi_bilgiler[2]
            # Hareket sonrası yeni oluşturulan yeni oyun alani, oyun alanina atanmıştır.
            oyun_alani = yeni_iki_boyut_listesi
            # Aşağıdaki fonksiyona gerekli argümanlar gönderilerek hareket sonrasında herhangi bir taşın çıkması gerek-
            # kiyor mu gerekiyorsa çıkartılarak yeni oyun alanı geriye döndürülmüştür.
            tas_cikarilip_cikarilmama_kontrol_sonrasi_yeni_oyun_alani = tas_cikarilip_cikarilmama_kontrol(
                birinci_oyuncu_karakter, ikinci_oyuncu_karakter, satir_sutun_sayisi, oyun_alani, oyuncunun_hedef_satiri,
                oyuncunun_hedef_sutunu)
            # Çıkması gereken taş çıkarıldıktan sonra yeni oyun alanı tekrardan oyun_alani değişkenine atanmıştır.
            oyun_alani = tas_cikarilip_cikarilmama_kontrol_sonrasi_yeni_oyun_alani
            # Aşağıda for döngüsüyle yeni oyun alanında kalan oyuncu taşlarının sayısı hesaplanmıştır.
            for satir in range(satir_sutun_sayisi):
                for sutun in range(satir_sutun_sayisi):
                    if birinci_oyuncu_karakter == oyun_alani[satir][sutun]:
                        birinci_karakter_sayisi += 1
                    if ikinci_oyuncu_karakter == oyun_alani[satir][sutun]:
                        ikinci_karakter_sayisi += 1
            # Oyuncu taşlarından hangisi sıfırlandıysa oyunculara oyunu kazanan ters bir şekilde bildirilmiştir.
            if birinci_karakter_sayisi <= MIN_KARAKTER_SAYISI :
                oyun_alanini_yazdir(satir_sutun_sayisi, sutun_listesi, oyun_alani)
                print(f"Oyuncu {ikinci_oyuncu_karakter} oyunu kazandı.")
            elif ikinci_karakter_sayisi <= MIN_KARAKTER_SAYISI:
                oyun_alanini_yazdir(satir_sutun_sayisi, sutun_listesi, oyun_alani)
                print(f"Oyuncu {birinci_oyuncu_karakter} oyunu kazandı.")
            # Aşağıdaki if bloğunda, oyuncu taşlarından herhangi biri sıfırlandığında oyunculara tekrar oynayıp oynamamak istediği sorulmuştur.
            if birinci_karakter_sayisi <= MIN_KARAKTER_SAYISI or ikinci_karakter_sayisi <= MIN_KARAKTER_SAYISI:
                tekrar_oynama = input("Tekrar oynamak ister misiniz(E/H)?:")
                while tekrar_oynama not in ["E", "H"]:
                    tekrar_oynama = input("Lütfen tekrar oynamak istiyorsanız 'E'yi istemiyorsanız 'H'yi tuşlayınız:")


main()

# Yukarıda main fonksiyonu çağırılarak oyunun oynanması sağlanmıştır.
