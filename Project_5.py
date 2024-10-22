
DUSUK_SINIR = 10000
ORTA_SINIR = 25000
COK_YUKSEK_SINIR = 50000
DUSUK_VERGI_ORAN = 0.15
ORTA_VERGI_ORAN = 0.20
YUKSEK_VERGI_ORAN = 0.25
brut_maas = 1
dusuk_kisi = 0
orta_kisi = 0
yuksek_kisi = 0
cok_yuksek_kisi = 0
toplam_net_maas = 0
toplam_vergi = 0
toplam_brut = 0
#yukarıda aşağıdaki işlemler kullanılması için gerekli constant ve farklı türlerde değişkenler tanımlanmıştır.
brut_maas = int(input("Satış temsilcisinin brüt maaş tutarını giriniz:"))
#yukarıdaki kodda while girmek için gerekli ilk brüt maaş alınmıştır.
while brut_maas >= 1:
    if brut_maas <= DUSUK_SINIR:
        vergi = (brut_maas * DUSUK_VERGI_ORAN)
        net_maas = brut_maas - vergi
        dusuk_kisi += 1
        print(f"Devlete ödenecek vergi tutarı: {vergi} TL'dir.")
        print(f"Satış temsilcisine ödenecek net maaş tutarı: {net_maas} TL'dir.")
    elif brut_maas > DUSUK_SINIR and brut_maas < ORTA_SINIR:
        vergi = (brut_maas * ORTA_VERGI_ORAN)
        net_maas = brut_maas - vergi
        orta_kisi += 1
        print(f"Devlete ödenecek vergi tutarı: {vergi} TL'dir.")
        print(f"Satış temsilcisine ödenecek net maaş tutarı: {net_maas} TL'dir.")
    else:
        vergi = (brut_maas * YUKSEK_VERGI_ORAN)
        net_maas = brut_maas - vergi
        yuksek_kisi += 1
        if brut_maas > COK_YUKSEK_SINIR:
            cok_yuksek_kisi += 1
        print(f"Devlete ödenecek vergi tutarı: {vergi} TL'dir.")
        print(f"Satış temsilcisine ödenecek net miktar: {net_maas} TL'dir.")
    #yukarıdaki kodda programın sonunda kullanılması gereken gerekli ve doğru ifadelerin alınabilmesi için if blokları kullanılmıştır.
    #buradaki if blokları sayesinde gerekli arttırımlar yapılmıştır
    toplam_brut +=  brut_maas
    toplam_net_maas += net_maas
    toplam_vergi += vergi
    #yukarıdaki kodda ise while döngüsünden çıkmadan aşağıda kullanılacak olan ifadeler atanmıştır.

    brut_maas = int(input("Devam etmek istiyorsanız sıradaki satış temsilcisinin brüt maaş tutarını giriniz:"))
    #buraki kod while döngüsünü devam ettirmek için gereklidir. Böylece brüt maaş 0'dan farklı ve 0'dan büyük oldukça while döngüsü çaşlışmaya devam edecektir.
toplam_kisi = orta_kisi + dusuk_kisi + yuksek_kisi
cok_yukseklerin_orani = (cok_yuksek_kisi / yuksek_kisi) * 100
tüm_kisilerin_net_maas_ortalamasi = toplam_net_maas / toplam_kisi
devlete_odenen_vergi_orani = toplam_vergi / toplam_brut * 100
#yukarıdaki kodlarda aşağıdaki print çıktılarında kullanılacak değişkenler tanımlanmıştır.
print(f"Bürüt maaş seviyesi düşük seviye olan temsilci sayısı: {dusuk_kisi} \nBürüt maaş seviyesi orta seviye olan temsilci sayısı: {orta_kisi}  \nBürüt maaş seviyesi yüksek seviye olan temsilci sayısı: {yuksek_kisi}")
print(f"Brüt maaş tutarı 50000 TL’den çok olan satış temsilcilerinin, brüt maaş seviyesi yüksek olan satış temsilcileri içindeki yüzdesi: %{cok_yukseklerin_orani:.2f}")
print(f"Tüm satış temsilcilerinin net maaş tutarı ortalaması: {tüm_kisilerin_net_maas_ortalamasi:.2f}")
print(f"Devlete ödenecek toplam gelir vergisi tutarı: {toplam_vergi:.2f} \nDevlete ödenecek toplam gelir vergisi tutarının toplam brüt maaşı tutarı içindeki yüzdesi: %{devlete_odenen_vergi_orani:.2f}")
#yukarıdaki kodlarda istenilen çıktılar basılmıştır.



