
KUTUDAKI_OLMASI_GEREKEN_MIN_BILYE = 10 # Kutunun değerlendirilmeye alınabilmesi için tanımlanmış constant değişkendir
BILYE_AGIRLIK_MINIMUM = 0 # Bilye ağırlığının 0'dan büyük olması gerekmekte bunun için tanımlanmış constant değişkendir
secim = "e"  # Buradaki "secim" degiskeni while'a en az bir kere girerek kullanıcıya kutudaki bilye sayısını sorması için "e" olarak tanımlanmıştır.
bilye_agirlik = 0
# Aşağıdaki 5 değişken, bizden en sonda istenilen çıktıların hesaplanmasında gerekli olan verileri tutacaktır.
tum_kutu_sayisi = 0
hatali_kutu_sayisi = 0
hafif_kutu_sayisi = 0
agir_kutu_sayisi = 0
hepsi_esit_kutu_sayisi = 0
# Aşağıdaki iki değişken, aşağıdaki işlemlerdeki hesaplamalardan sonra toplam ve iade edilen bilye sayısını tutacaktır.
iade_edilen_bilye_sayisi = 0
toplam_bilye_sayisi = 0
# Aşağıdaki değişken, bütün bilye ağırlıklarının eşit olduğu kutular arasından maksimum bilye sayısını içeren kutudaki bilye sayısını tutacaktır.
hepsi_esit_kutudaki_max_bilye_sayisi = 0
# Aşağıdaki değişken, bütün bilye ağırlıklarının eşit olduğu kutular arasından maksimum bilye sayısını içeren kutudaki bir bilyenin ağırlığını tutacaktır.
hepsi_esit_kutu_max_bilye_sayisindaki_agirlik = 0
# Aşağıdaki değişken, bütün bilye ağırlıklarının eşit olduğu kutular arasından maksimum bilye ağırlığına sahip olan kutudaki bilye sayısını tutacaktır.
hepsi_esit_kutudaki_max_bilye_agirligindaki_bilye_sayisi = 0
# Aşağıdaki değişken, bütün bilye ağırlıklarının eşit olduğu kutular arasından maksimum bilye ağırlığına sahip olan kutudaki bir bilyenin ağırlığını tutacaktır.
hepsi_esit_kutudaki_max_bilye_agirligi = 0
# Aşağıdaki değişken, bir bilyenin diğerlerinden daha ağır olduğu kutulardaki bilyeler arasındaki ağırlık farklarının toplamını tutacaktır.
agir_kutulardaki_toplam_fark = 0
# Aşağıdaki değişken, bir bilyenin diğerlerinden daha ağır olduğu kutulardaki bilyeler arasındaki ağırlık farkları yüzdelerinin toplamını tutacaktır
agir_kutulardaki_toplam_yuzde = 0
# Aşağıdaki değişken, bir bilyenin diğerlerinden daha hafif olduğu kutulardaki bilyeler arasındaki ağırlık farklarının toplamını tutacaktır.
hafif_kutulardaki_toplam_fark = 0
# Aşağıdaki değişken, bir bilyenin diğerlerinden daha hafif olduğu kutulardaki bilyeler arasındaki ağırlık farkları yüzdelerinin toplamını tutacaktır.
hafif_kutulardaki_toplam_yuzde = 0
# Aşağıdaki üç değişken, farklı bilye ağırlığının olduğu kutulardaki farklı olan bilyenin ağırlığının kutudaki diğer bilyelerin
# ağırlığıyla arasındaki farkın değerinin en büyük olduğu ağırlık farkının değerini, yüzdesini ve işaretini tutacaktır.
max_aradaki_fark = 0
max_aradaki_fark_yuzde = 0
max_aradaki_fark_isaret = ""
# Aşağıdaki üç değişken, farklı bilye ağırlığının olduğu kutulardaki farklı olan bilyenin ağırlığının kutudaki diğer
# bilyelerin ağırlığıyla arasındaki yüzdesinin en küçük olduğu ağırlık farkının değerini, yüzdesini ve işaretini tutacaktır.
min_aradaki_yuzde = 999999999999999999999999999999999999999999999 # Bu değişken en az 1 kere hesaplanması için çok yüksek bir değer atanmıştır.
min_aradaki_yuzde_fark = 0
min_aradaki_yuzde_isaret = ""
# Aşağıdaki while döngüsünün en az bir kere çalışması için "secim" değişkeni yukarıda "e" olarak atanmıştır.
# Aşağıdaki while döngüsü kullanıcı işleme devam ettikçe kutunun hatalı olup olmadığını, hatalı değilse kutu hakkında
# bilgi vermesini sağlamaktadır bunların yanı sıra en sonda istenilen çıktılar için gerekli verileri de hesaplamaktadır.
while secim == "e" or secim == "E":
    # Aşağıdaki değişken while'a her girildiğinde toplam kutu sayısını bir arttırmaktadır.
    tum_kutu_sayisi += 1
    # Aşağıdaki 6 değişken, while döngüsünde kullanılan değişkenleri tanımlamakla birlikte, bir sonraki kutu hakkında
    # hatalı yorum ve hesaplama yapılmaması için while döngüsüne her girildiğinde sıfırlanmaktadır.
    aradaki_fark = 0
    aradaki_fark_yuzde = 0
    referans = 0
    gercek_toplam = 0
    beklenen_toplam = 0
    hatali_bilye = 0
    # Aşağıdaki 3 satır kod kullanıcıdan bilye sayısını hatasız bir şekilde almak için yazılmıştır.
    # Kullanıcı, bilye sayısını 10'dan daha az girdikçe while döngüsü sayesinde soru tekrar sorulacaktır.
    bilye_sayi = int(input("Lütfen kutudaki bilye sayısını giriniz[Kutudaki bilye sayısı en az 10 olmalıdır!]:"))
    while bilye_sayi < KUTUDAKI_OLMASI_GEREKEN_MIN_BILYE:
        bilye_sayi = int(input("Lütfen kutudaki bilye sayısını 10 veya daha yüksek bir değer giriniz!:"))
    # Aşağıdaki satırda, kullanıcıdan alınan hatasız bilye sayısı toplam bilye sayısının üzerine ekleniyor.
    toplam_bilye_sayisi += bilye_sayi
    # Aşağıda, ilk üç bilyenin ağırlığı manuel bir şekilde alınmıştır. Burada ilk üç bilyenin manuel şekilde alınmasının
    # amacı: üç bilyenin durumu birbiriyle kıyaslanarak referans bir bilye değerini atamaktır, böylece daha sonraki
    # bilyelerin ağırlığı alınırken referanstan daha farklı bir bilye ağırlığı girilirse hatalı bilye sayısını bir
    # arttırmaktır. Hatalı bilye sayısı 2'ye ulaşınca kullanıcıya daha fazla ağırlık sormadan koddan çıkılacaktır.
    bilye1 = int(input("Kutudaki 1. bilyenin ağırlığını miligram cinsinden giriniz:"))
    while bilye1 <= BILYE_AGIRLIK_MINIMUM:
        bilye1 = int(input("Lütfen kutudaki 1. bilyenin ağırlığını pozitif bir değer giriniz:"))
    bilye2 = int(input("Kutudaki 2. bilyenin ağırlığını miligram cinsinden giriniz:"))
    while bilye2 <= BILYE_AGIRLIK_MINIMUM:
        bilye2 = int(input("Lütfen kutudaki 2. bilyenin ağırlığını pozitif bir değer giriniz:"))
    bilye3 = int(input("Kutudaki 3. bilyenin ağırlığını miligram cinsinden giriniz:"))
    while bilye3 <= BILYE_AGIRLIK_MINIMUM:
        bilye3 = int(input("Lütfen kutudaki 3. bilyenin ağırlığını pozitif bir değer giriniz:"))
    # Aşağıdaki if bloğunda girilen ilk 3 bilyenin birbirinden farklı olması durumunda kutunun iade edileceği ifadesinin
    # kullanıcıya bildirilmesi ve koddan direkt çıkılması sağlanmıştır.
    if bilye1 != bilye2 and bilye2 != bilye3 and bilye1 != bilye3:
        hatali_kutu_sayisi += 1
        iade_edilen_bilye_sayisi += bilye_sayi
        hatali_bilye = 2
        print("Bu kutudaki hatalı bilye sayısı 1'den fazla, bu nedenle kutu iade edilecektir!")
    # Aşağıdaki else bloğunda bilyelerin durumlarına göre farklı değerdeki referanslar atanmıştır. Burada atanan
    # referansa göre bir sonraki girilen bilyenin ağırlığı karşılaştırılacaktır.
    else:
        if bilye1 == bilye2 and bilye2 == bilye3:
            # Burada ilk 3 bilye birbiriyle eşit olduğu için hatalı bilye sayısı arttırılmamıştır ancak aşağıdaki
            # elif bloklarında bir bilyenin diğer 2 bilyeden farklı olması durumu hesaplandığı için hatalı bilye sayisi
            # bir arttırılmıştır.
            referans = bilye1
        elif bilye1 != bilye2 and bilye2 == bilye3:
            referans = bilye2
            hatali_bilye += 1
        elif bilye1 != bilye2 and bilye1 == bilye3:
            referans = bilye3
            hatali_bilye += 1
        elif bilye1 == bilye2 and bilye2 != bilye3:
            referans = bilye1
            hatali_bilye += 1
        # Aşağıdaki hesaplama, kutuda 1 adet farklı bilye ağırlığı olması durumunda farklı olan bilyenin hafif mi veya
        # ağır mı olduğunu tespit edilmesinde kullanılmak için yapılmıştır.
        beklenen_toplam = bilye_sayi * referans
        # Aşağıda kullanıcıdan alınan toplam bilyelerin gerçek toplamının hesaplanması için manuel olarak alınan 3
        # bilyenin toplamı "gercek_toplam" değişkenine atanmıştır. Aşağıda da for döngüsüyle alınan bilye ağırlıkları
        # "gercek_toplam" değişkenin üzerine her for döngüsünde eklenerek kullanıcının girdiği toplamı bulmuş oluruz.
        gercek_toplam = bilye1 + bilye2 + bilye3
        # Bu for döngüsü kalan bilye ağırlıklarını otomatik olarak almaktadır.
        for x in range(4, bilye_sayi+1):
            bilye_agirlik = int(input(f"Kutudaki {x}. bilyenin ağırlığını miligram cinsinden giriniz:"))
            # Bilye ağırlığı sıfır veya negatif girilmesi durumunda buradaki while döngüsü soruyu tekrar sormaktadır.
            while bilye_agirlik <= 0:
                bilye_agirlik = int(input(f"Lütfen kutudaki {x}. bilyenin ağırlığını pozitif bir değer giriniz:"))
            # Buradaki if ve bloğu, referans değer ile girilen değer birbirinden farklıysa hatalı bilyeyi bir arttırıyor
            if bilye_agirlik != referans:
                hatali_bilye += 1
            gercek_toplam += bilye_agirlik
            # Buradaki if bloğu hatalı bilye sayısının 2'ye ulaştığında kullanıcıya kutunun iade edileceğini bildirmekle
            # beraber hatalı kutu sayısını arttırmaktadır. Aynı zamanda döngüden çıkarak gereksiz soru sorulmasını da
            # engellemektedir.
            if hatali_bilye == 2:
                hatali_kutu_sayisi += 1
                iade_edilen_bilye_sayisi += bilye_sayi
                print("Bu kutudaki hatalı bilye sayısı 1'den fazla, bu nedenle kutu iade edilecektir!")
                break
    # for döngüsünden çıkılmasından sonra en sonda istenen çıktılar için gerekli veriler hesaplanmıştır.
    # Aşağıdaki if ve elif bloklarında içerisinde 1 adet bilyenin farklı olduğu kutulardaki bilyenin ağır mı hafif
    # mi ya da bütün bilyelerin eşit mi olduğu hesaplanmıştır. Buna göre hafif veya ağır kutu sayısı arttırılıp ağır
    # veya hafif olan bilyenin normal bilyelerden farkı hesaplanmış bu farkın da yüzdesi hesaplanmıştır. Bu çıktıların
    # kullanıcıya bildirilmesi gerektiği için print ile kutu hakkındaki bilgiler kullanıcıya gösterilmiştir. Kutu ağırsa
    # ağır kutulardaki toplam fark ve toplam yüzde arttırılmış, hafifse hafif kutulardaki toplam fark hesaplanmıştır.
    if gercek_toplam > beklenen_toplam and hatali_bilye == 1:
        agir_kutu_sayisi += 1
        aradaki_fark = (gercek_toplam - beklenen_toplam)
        aradaki_fark_yuzde = (aradaki_fark * 100) / referans
        agir_kutulardaki_toplam_fark += aradaki_fark
        agir_kutulardaki_toplam_yuzde += aradaki_fark_yuzde
        print("Bu kutuda bir hata yoktur ve bu kutudaki bir bilye diğerlerinden daha ağırdır!")
        print(f"Daha ağır olan bilye ile normal bilyeler arasındaki fark: {aradaki_fark}mg'dır.")
        print(f"Daha ağır olan bilye normal bilyelerden %{aradaki_fark_yuzde:.2f} daha ağırdır!")
    elif gercek_toplam < beklenen_toplam and hatali_bilye == 1:
        hafif_kutu_sayisi += 1
        aradaki_fark = (beklenen_toplam - gercek_toplam)
        aradaki_fark_yuzde = (aradaki_fark * 100) / referans
        hafif_kutulardaki_toplam_fark += aradaki_fark
        hafif_kutulardaki_toplam_yuzde += aradaki_fark_yuzde
        print("Bu kutuda bir hata yoktur ve bu kutudaki bir bilye diğerlerinden daha hafiftir!")
        print(f"Daha hafif olan bilye ile normal bilyeler arasındaki fark: {aradaki_fark}mg'dır.")
        print(f"Daha hafif olan bilye normal bilyelerden %{aradaki_fark_yuzde:.2f} daha hafiftir!")
    # Aşağıdaki elif bloğunda bilyelerin ağırlığının hepsinin eşit olduğu kutu durumu ele alınmıştır. Bilyelerin ağırlık
    # ları eşitse kullanıcıya bildirilmiş, bütün bilyelerin eşit ağırlıkta olduğu kutu sayısı arttırılmıştır.
    elif gercek_toplam == beklenen_toplam and hatali_bilye == 0:
        hepsi_esit_kutu_sayisi += 1
        print("Bu kutuda bir hata yok ve bu kutudaki bilyelerin hepsi eşittir!")
        # Buradaki if bloğunda bütün bilye ağırlıklarının eşit olduğu kutular arasındaki maksimum bilye sayısını içeren
        # kutudaki bilye sayısı ve o kutudaki bir bilyenin ağırlığı hesaplanmıştır.
        if hepsi_esit_kutudaki_max_bilye_sayisi < bilye_sayi:
            hepsi_esit_kutudaki_max_bilye_sayisi = bilye_sayi
            hepsi_esit_kutu_max_bilye_sayisindaki_agirlik = bilye_agirlik
        # Buradaki if bloğunda bütün bilye ağırlıklarının eşit olduğu kutular arasındaki maksimum bilye ağırlığına sahip
        # kutudaki bir bilyenin ağırlığı ve o kutudaki bilye sayisi hesaplanmıştır.
        if hepsi_esit_kutudaki_max_bilye_agirligi < (gercek_toplam / bilye_sayi):
            hepsi_esit_kutudaki_max_bilye_agirligi = (gercek_toplam / bilye_sayi)
            hepsi_esit_kutudaki_max_bilye_agirligindaki_bilye_sayisi = bilye_sayi
    # Buradaki if bloğu, sadece bir bilyenin diğerlerinden farklı olduğu kutuların bu bloğa girilmesi için yazılmıştır
    if gercek_toplam != beklenen_toplam and hatali_bilye == 1:
        # Aşağıdaki if ve elif bloklarında sadece bir bilyenin diğerlerinden farklı olduğu kutular içerisindeki ağır
        # veya hafif bilye ile normal bir bilyenin arasındaki farkın maksimum olduğu kutudaki bilyeler arasındaki fark,
        # farkın yüzdesi ve farklı olan bilyenin hafif mi yoksa daha ağır mı olduğu hesaplanmıştır.
        if (gercek_toplam - beklenen_toplam) < 0 and max_aradaki_fark < aradaki_fark:
            max_aradaki_fark = aradaki_fark
            max_aradaki_fark_yuzde = aradaki_fark_yuzde
            max_aradaki_fark_isaret = "Hafif"
        elif (gercek_toplam - beklenen_toplam) > 0 and max_aradaki_fark < aradaki_fark:
            max_aradaki_fark = aradaki_fark
            max_aradaki_fark_yuzde = aradaki_fark_yuzde
            max_aradaki_fark_isaret = "Ağır"
        # Aşağıdaki if ve elif bloklarında sadece bir bilyenin diğerlerinden farklı olduğu kutular içerisindeki ağır
        # veya hafif bilye ile normal bir bilyenin arasındaki farkın yüzdesinin minimum olduğu kutudaki bilyeler
        # arasındaki fark, farkın yüzdesi, farklı olan bilyenin hafif mi yoksa daha ağır mı olduğu hesaplanmıştır.
        if (gercek_toplam - beklenen_toplam) < 0 and min_aradaki_yuzde > aradaki_fark_yuzde:
            min_aradaki_yuzde = aradaki_fark_yuzde
            min_aradaki_yuzde_fark = aradaki_fark
            min_aradaki_yuzde_isaret = "Hafif"
        elif (gercek_toplam - beklenen_toplam) > 0 and min_aradaki_yuzde > aradaki_fark_yuzde:
            min_aradaki_yuzde = aradaki_fark_yuzde
            min_aradaki_yuzde_fark = aradaki_fark
            min_aradaki_yuzde_isaret = "Ağır"
    # Aşağıda "secim" değişkeninin değerini kullanıcıdan e/E/H/h alarak bu değere göre while'a tekrar girip
    # girmeyeceğini(kullanıcının kutuyu kontrol etmeye devam edip etmeyeceği) belirliyoruz. Hatalı veri girişine göre
    # ekstra bir while ile kontol edilerek soru tekrar sorulmuştur.
    secim = input("Kutu girmeye devam etmek istiyor musunuz? Devam etmek istiyorsanız e veya E, istemiyorsanız h veya H harflerinden birini tuşlayınız: ")
    while secim != "e" and secim != "E" and secim != "H" and secim != "h":
        secim = input("Lütfen sadece e/E veya h/H giriniz. Devam etmek istiyorsanız 'e' veya 'E', istemiyorsanız 'h' veya 'H'yi tuşlayınız:")
# Kutu girişi bittikten sonra en sonda istenilen çıktıların hesaplanması için aşağıda bir dizi hesaplama yapılmıştır.
# Aşağıdaki hesaplama, bir bilyenin diğerlerinden daha ağır olduğu kutulardaki ağır olan bilyelerin ağırlık farkı
# değerlerinin ortalamalasını hesaplamak için yapılmıştır.
agir_kutu_toplam_fark_ort = agir_kutulardaki_toplam_fark / agir_kutu_sayisi
# Aşağıdaki hesaplama, bir bilyenin diğerlerinden daha ağır olduğu kutulardaki ağır olan bilyelerin ağırlık farkı
# yüzdelerinin ortalamalasını hesaplamak için yapılmıştır.
agir_kutu_toplam_fark_yuzdesi = agir_kutulardaki_toplam_yuzde / agir_kutu_sayisi
# Aşağıdaki hesaplama, bir bilyenin diğerlerinden daha hafif olduğu kutulardaki hafif olan bilyelerin ağırlık farkı
# değerlerinin ortalamalasını hesaplamak için yapılmıştır.
hafif_kutu_toplam_fark_ort = hafif_kutulardaki_toplam_fark / hafif_kutu_sayisi
# Aşağıdaki hesaplama, Bir bilyenin diğerlerinden daha hafif olduğu kutulardaki hafif olan bilyelerin ağırlık farkı
#  yüzdelerinin ortalamalasını hesaplamak için yapılmıştır.
hafif_kutu_toplam_fark_yuzdesi = hafif_kutulardaki_toplam_yuzde / hafif_kutu_sayisi
# Aşağıdaki hesaplama, üretim hatası olmayan kutu sayısını toplam kutudan iade edilen kutuyu çıkararak bulmuştur.
uretim_hatasiz_kutu_sayisi = tum_kutu_sayisi - hatali_kutu_sayisi
# Aşağıdaki hesaplamalar, içerisindeki tüm bilyelerin eşit ağırlıkta olduğu kutu sayısının, bir adet ağır bilye ve bir
# adet hafif bilye içeren kutu sayısının üretim hatası olmayan kutular içerisindeki yüzdesini hesaplama amacıyla
# yapılmıştır.
hepsi_esit_kutu_yuzdesi = (hepsi_esit_kutu_sayisi * 100) / uretim_hatasiz_kutu_sayisi
agir_kutu_yuzdesi = (agir_kutu_sayisi * 100) / uretim_hatasiz_kutu_sayisi
hafif_kutu_yuzdesi = (hafif_kutu_sayisi * 100) / uretim_hatasiz_kutu_sayisi
# Aşağıdaki hesaplama, hatalı kutu sayısının tüm kutu sayısı içerisindeki yüzdesini bulma amacıyla yapılmıştır.
hatali_kutu_sayisi_yuzdesi = (hatali_kutu_sayisi * 100) / tum_kutu_sayisi
# Aşağıdaki hesaplama, kabul edilen bilye sayısını toplam bilye sayısından çıkararak bulmuştur.
kabul_edilen_bilye_sayisi = toplam_bilye_sayisi - iade_edilen_bilye_sayisi
# Aşağıda bizden istenilen çıktılar, print ile yazdırılmıştır.
print(f"Toplam hatalı kutu sayısı: {hatali_kutu_sayisi}")
print(f"Toplam hatalı kutu sayısının tüm kutular içerisindeki yüzdesi: %{hatali_kutu_sayisi_yuzdesi:.2f}")
print(f"Toplam kabul edilen bilye sayısı: {kabul_edilen_bilye_sayisi}")
print(f"Toplam iade edilen bilye sayısı: {iade_edilen_bilye_sayisi}")
print(f"İçerisindeki tüm bilyelerin eşit ağırlıkta olduğu kutu sayısı: {hepsi_esit_kutu_sayisi}")
print(f"İçerisindeki tüm bilyelerin eşit ağırlıkta olduğu kutu sayısının üretim hatası olmayan kutular içerisindeki yüzdesi: %{hepsi_esit_kutu_yuzdesi:.2f}")
print(f"Bir bilyenin diğerlerinden daha ağır olduğu kutu sayısı: {agir_kutu_sayisi}")
print(f"Bir bilyenin diğerlerinden daha ağır olduğu kutu sayısının üretim hatası olmayan kutular içerisindeki yüzdesi: %{agir_kutu_yuzdesi:.2f}")
print(f"Bir bilyenin diğerlerinden daha hafif olduğu kutu sayısı: {hafif_kutu_sayisi}")
print(f"Bir bilyenin diğerlerinden daha hafif olduğu kutu sayısının üretim hatası olmayan kutular içerisindeki yüzdesi: %{hafif_kutu_yuzdesi:.2f}")
print(f"Bir bilyenin diğerlerinden daha ağır olduğu kutulardaki ağır olan bilyelerin ağırlık farkı değerlerinin ortalamalası: {agir_kutu_toplam_fark_ort:.2f}mg")
print(f"Bir bilyenin diğerlerinden daha ağır olduğu kutulardaki ağır olan bilyelerin ağırlık farkı yüzdelerinin ortalamalası: %{agir_kutu_toplam_fark_yuzdesi:.2f}")
print(f"Bir bilyenin diğerlerinden daha hafif olduğu kutulardaki hafif olan bilyelerin ağırlık farkı değerlerinin ortalamalası: {hafif_kutu_toplam_fark_ort:.2f}mg")
print(f"Bir bilyenin diğerlerinden daha hafif olduğu kutulardaki hafif olan bilyelerin ağırlık farkı yüzdelerinin ortalamalası: %{hafif_kutu_toplam_fark_yuzdesi:.2f}")
print(f"Tüm bilyelerin eşit ağırlıkta olduğu kutular arasında, içinde en çok sayıda bilye olan kutudaki bilye sayısı: {hepsi_esit_kutudaki_max_bilye_sayisi}")
print(f"Tüm bilyelerin eşit ağırlıkta olduğu kutular arasında, içinde en çok sayıda bilye olan kutudaki bir bilyenin ağırlığı: {hepsi_esit_kutu_max_bilye_sayisindaki_agirlik}mg")
print(f"Tüm bilyelerin eşit ağırlıkta olduğu kutular arasında, içinde en ağır bilyeler olan kutudaki bilye sayısı: {hepsi_esit_kutudaki_max_bilye_agirligindaki_bilye_sayisi}")
print(f"Tüm bilyelerin eşit ağırlıkta olduğu kutular arasında, içinde en ağır bilyeler olan kutudaki bir bilyenin ağırlığı: {hepsi_esit_kutudaki_max_bilye_agirligi}mg")
print(f"Farklı olan bilyenin ağırlığının kutudaki diğer bilyelerin ağırlığıyla arasındaki farkın değerinin en büyük olduğu ağırlık farkının değeri: {max_aradaki_fark}mg")
print(f"Farklı olan bilyenin ağırlığının kutudaki diğer bilyelerin ağırlığıyla arasındaki farkın değerinin en büyük olduğu ağırlık farkının yüzdesi: %{max_aradaki_fark_yuzde:.2f}")
print(f"Farklı olan bilyenin ağırlığının kutudaki diğer bilyelerin ağırlığıyla arasındaki farkın değerinin en büyük olduğu ağırlık farkının işareti: {max_aradaki_fark_isaret}")
print(f"Farklı olan bilyenin ağırlığının kutudaki diğer bilyelerin ağırlığıyla arasındaki farkın yüzdesinin en küçük olduğu ağırlık farkının değeri: {min_aradaki_yuzde_fark}mg")
print(f"Farklı olan bilyenin ağırlığının kutudaki diğer bilyelerin ağırlığıyla arasındaki farkın yüzdesinin en küçük olduğu ağırlık farkının yüzdesi: %{min_aradaki_yuzde:.2f}")
print(f"Farklı olan bilyenin ağırlığının kutudaki diğer bilyelerin ağırlığıyla arasındaki farkın yüzdesinin en küçük olduğu ağırlık farkının işareti: {min_aradaki_yuzde_isaret}")
