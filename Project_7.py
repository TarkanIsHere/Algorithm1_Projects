
VOLEYBOL_SET_ADET = 5
toplam_kazanilan_sayi = 0
toplam_kaybedilen_sayi = 0
maximum_fark = 0
toplam_kazanilan_set = 0
toplam_kaybedilen_set = 0
kazanilan_mac = 0
kaybedilen_mac = 0
toplam_mac_adet = 0
set_kaybetmeden_kazanilan_mac = 0
bes_set_suren_mac = 0
maximum_farktaki_takim_adi = ""
# Yukarıda aşağıda kullanılacak değişkenler tanımlanmıştır.
sezon_oynanan_mac = int(input("Lütfen sezon boyunca oynadığınız toplam maç adetini giriniz:"))
for mac_no in range(1, sezon_oynanan_mac+1):
    macta_oynanan_set = 0
    macta_kazanilan_sayi = 0
    macta_kaybedilen_sayi = 0
    macta_kazanilan_set = 0
    macta_kaybedilen_set = 0
    toplam_mac_adet += 1
    rakip_takim_adi = input(f"Lütfen {mac_no}. maçta oynadığınız rakibin adını yazınız:")
    for set_no in range(1, VOLEYBOL_SET_ADET+1):
        sette_kazanilan_sayi = int(input(f"Lütfen {set_no}. sette kazandığınız sayı adetini giriniz:"))
        sette_kaybedilen_sayi = int(input(f"Lütfen {set_no}. sette kaybettiğiniz sayı adetini giriniz:"))
        toplam_kaybedilen_sayi += sette_kaybedilen_sayi
        toplam_kazanilan_sayi += sette_kazanilan_sayi
        # Alttaki if bloğu maçta kazanılan set sayısı ve maçta oynanan set sayısını hesaplamak için yapılmıştır.
        if sette_kazanilan_sayi > sette_kaybedilen_sayi:
            macta_kazanilan_set += 1
            toplam_kazanilan_set += 1
            macta_oynanan_set += 1
        elif sette_kaybedilen_sayi > sette_kazanilan_sayi:
            macta_kaybedilen_set += 1
            toplam_kaybedilen_set += 1
            macta_oynanan_set += 1
        # Aşağıda maçta kazanılan toplam sayıyı bulmak için sette kazanılan sayılar maçta kazanılan sayılara atanmıştır.
        macta_kazanilan_sayi += sette_kazanilan_sayi
        macta_kaybedilen_sayi += sette_kaybedilen_sayi
        # Aşağıdaki if bloğu en sonda kullanacağımız beş set süren maç sayısı ve set kaybedilmeden kazanılan maç sayısını bulmak için yazılmıştır.
        if macta_kazanilan_set + macta_kaybedilen_set == 5:
            bes_set_suren_mac += 1
        elif macta_kazanilan_set - macta_kaybedilen_set == 3:
            set_kaybetmeden_kazanilan_mac += 1
        # Aşağıdaki if bloğu herhangi bir takımın 3 sete ulaşınca for bloğunun tekrardan boş yere dönmemesi için yapılmıştır.
        if macta_kazanilan_set == 3 or macta_kaybedilen_set == 3:
            break
    if macta_kazanilan_set > macta_kaybedilen_set:  # Buradaki if bloğu kazanılan maç ve kaybedilen maç sayısını hesaplamak için yapılmıştır.
        kazanilan_mac += 1
    elif macta_kaybedilen_set > macta_kazanilan_set:
        kaybedilen_mac += 1
    fark = macta_kazanilan_sayi - macta_kaybedilen_sayi  # Buradaki değişken ve hemen bir altındaki if bloğu maksimum farkı ve maksimum farkın olduğu maçtaki rakip takımın adını bulmak için yapılmıştır.
    if fark < 0:
        fark *= -1
    if maximum_fark < fark:
        maximum_fark = fark
        maximum_farktaki_takim_adi = rakip_takim_adi
    # Aşağıda oynanan maç için yazılması istenilen değerler yazdırılmıştır.
    print(f"Bu maçta kazandığınız toplam sayı adeti: {macta_kazanilan_sayi}")
    print(f"Bu maçta kaybettiğiniz toplam sayı adeti: {macta_kaybedilen_sayi}")
    print(f"Bu maçta kazandığınız set sayısı: {macta_kazanilan_set}")
    print(f"Bu maçta kaybettiğiniz set sayısı: {macta_kaybedilen_set}")
    print(f"Bu maçta set başına kazandığınız sayı ortalaması: {macta_kazanilan_sayi/(macta_kaybedilen_set + macta_kazanilan_set):.2f}")
    print(f"Bu maçta set başına kaybettiğiniz sayı ortalaması: {macta_kaybedilen_sayi/(macta_kaybedilen_set + macta_kazanilan_set):.2f}")
# Aşağıdaki değişkenler en sonunda bizden istenilen değerlerin daha okunaklı bir şekilde print içerisinde yazılması için yapılmıştır.
mac_basi_kazanilan_sayi = toplam_kazanilan_sayi/toplam_mac_adet
set_kaybetmeden_kazanilan_mac_oran = (set_kaybetmeden_kazanilan_mac/kazanilan_mac)*100
bes_set_suren_mac_oran = (bes_set_suren_mac/toplam_mac_adet)*100
# Aşağıda bizden istenilen değerler yazdırılmıştır.
print(f"Bütün maçlarda toplam kazandığınız sayı adeti: {toplam_kazanilan_sayi}, maç başına kazandığınız sayı adeti: {mac_basi_kazanilan_sayi}")
print(f"Toplam kazandığınız maç adeti: {kazanilan_mac}, toplam kaybettiğiniz maç adeti: {kaybedilen_mac} ")
print(f"Set kaybetmeden kazandığınız maçların adeti:{set_kaybetmeden_kazanilan_mac}, tüm kazandığı maçlar içerisindeki oranı: %{set_kaybetmeden_kazanilan_mac_oran:.2f}")
print(f"5 set süren maçların sayısı:{bes_set_suren_mac}, tüm maçlar içerisindeki oranı: %{bes_set_suren_mac_oran:.2f}")
print(f"Kazandığı toplam sayı ile kaybettiği toplam sayı arasındaki farkın en yüksek olduğu maçtaki kazandığı toplam sayı ile kaybettiği toplam sayı arasındaki fark: {maximum_fark}")
print(f"Kazandığı toplam sayı ile kaybettiği toplam sayı arasındaki farkın en yüksek olduğu maçtaki rakibin adı: {maximum_farktaki_takim_adi}")
