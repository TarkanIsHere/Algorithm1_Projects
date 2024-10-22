
PLAYOFF_SIRALAMA_SARTI = 8
TAKIM_SAYISI = 14
NORMAL_SEZON_OYNANAN_MAC_SAYISI = (TAKIM_SAYISI-1)*2
#yukarıdaki constant değişkenlerle bir takımın normal sezonda oynadığı maç sayısını gösteren denklem ve değişken tanımlanmıştır.
yas = int(input("Lütfen yaşınızı giriniz:"))
aldigi_son_yil_ucret = int(input("Lütfen son yıllık ücretinizi giriniz:"))
normal_sezon_sira = int(input("Lütfen takımınızın normal sezondaki sırasını giriniz:"))
#Yukarıdaki kodlarla programı kullanan kullanıcıdan değerler alınmıştır.
if normal_sezon_sira <= PLAYOFF_SIRALAMA_SARTI:
    playoff_sayisi = int(input("Lütfen takımınızın playoff sezonunda oynadığı maç sayısını giriniz:"))
    toplam_mac_sayisi = playoff_sayisi + NORMAL_SEZON_OYNANAN_MAC_SAYISI
    mac_basi_maliyet = aldigi_son_yil_ucret/(toplam_mac_sayisi)
else:
    toplam_mac_sayisi = NORMAL_SEZON_OYNANAN_MAC_SAYISI
    mac_basi_maliyet = aldigi_son_yil_ucret / toplam_mac_sayisi
#yukarıdaki if else bloğunda takımın sıralamasına göre bir sezonda oynadığı toplam maç sayısı hesaplanıp, maç başı maliyet bulunmuştur.
if yas == 22:
    serbest_kalma_bedeli = aldigi_son_yil_ucret*2
elif yas == 23:
    serbest_kalma_bedeli = aldigi_son_yil_ucret
elif yas == 24:
    serbest_kalma_bedeli = aldigi_son_yil_ucret / 2
elif yas > 24:
    serbest_kalma_bedeli = 0
#Yukarıdaki if else bloğunda ise oyuncunun yaşına göre serbest kalma bedeli var mı, varsa kaç tl olduğu hesaplanmıştır.
if yas >= 22 and yas <=24:
    print(f"Takımınıza maç başı maliyetiniz: {mac_basi_maliyet:.2f} TL \nSerbest kalma hakkınız vardır, serbest kalma bedeliniz: {serbest_kalma_bedeli:.2f} TL")
elif yas > 24:
    print(f"Takımınıza maç başı maliyetiniz:{mac_basi_maliyet:.2f} TL \nSerbest kalma hakkınız vardır, serbest kalma bedeliniz: {serbest_kalma_bedeli:.2f} TL")
else:
    print(f"Takımınıza maç başı maliyetiniz:{mac_basi_maliyet:.2f} TL \nSerbest kalma hakkınız yoktur.")
#Yukarıdaki if elif else bloğu ise gerekli ve doğru çıktıların verilmesi için yapılmıştır.