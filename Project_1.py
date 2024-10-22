LAB_KATSAYISI = 0.2
ARASINAV_KATSAYISI = 0.3
FINAL_KATSAYISI = 0.5
ogr_no = input("Lütfen öğrenci numarınızı giriniz:")
ad_soyad = input("Lütfen adınızı ve soyadınızı giriniz:")
lab_notu= int(input("Lütfen lab notunuzu giriniz:"))
arasinav_notu = int(input("Lütfen ara sınav notunuzu giriniz:"))
final_notu = int(input("Lütfen final notunuzu giriniz:"))
donemsonu_notu = lab_notu*LAB_KATSAYISI + arasinav_notu*ARASINAV_KATSAYISI + final_notu*FINAL_KATSAYISI
print("Sayın", ogr_no, "ogrneci Nolu", ad_soyad, "Donem sonu notunuz:", str(round((donemsonu_notu))))
if donemsonu_notu >= 70:
    print("Tebrıkler gectiniz.")
else:
    print("Geçemediniz.")
devam = input("Tekrar yapmak istiyorsanız 1i tuslayınız.")
print(f"merhaba {ad_soyad}")









ilk_ay = int(input("Lütfen ürünün ilk ayki fiyatını giriniz:"))
ikinci_ay = int(input("Lütfen ürünün ikinci aydaki fiyatını giriniz:"))
degisim = ikinci_ay-ilk_ay
degisim_yuzde = ikinci_ay/ilk_ay*100
fiyat_degisim_oran= degisim/ilk_ay*100
print(f"üründeki fiyat farkı {degisim} üründeki yüzdelik degisim artıs miktarı {degisim_yuzde-100} degisim oranı {fiyat_degisim_oran}")












