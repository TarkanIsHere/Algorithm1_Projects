ilk_takim_isim = input("Lütfen ilk takımın adını giriniz:")
ilk_takim_set = int(input("Lütfen ilk takımın kazandığı set sayısını giriniz:"))
ikinci_takim_isim = input("Lütfen ikinci takımın adını giriniz:")
ikinci_takim_set = int(input("Lütfen ikinci takımın kazandığı set sayısını giriniz:"))
puan0=0
puan1=1
puan2=2
puan3=3
if ilk_takim_set > ikinci_takim_set and ilk_takim_set-ikinci_takim_set >=2:
    print(f"Kazanan takım: {ilk_takim_isim}, kazandığı puan: {puan3}")
    print(f"Kaybeden takım: {ikinci_takim_isim}, kazandığı puan: {puan0}")
if ilk_takim_set > ikinci_takim_set and ilk_takim_set-ikinci_takim_set<2:
    print(f"Kazanan takım: {ilk_takim_isim}, kazandığı puan:{puan2} ")
    print(f"Kaybeden takım: {ikinci_takim_isim}, kazandığı puan: {puan1}")
if ikinci_takim_set > ilk_takim_set and ikinci_takim_set- ilk_takim_set >=2:
    print(f"Kazanan takım: {ikinci_takim_isim}, kazandığı puan: {puan3}")
    print(f"Kaybeden takım: {ilk_takim_isim}, kazandığı puan: {puan0}")
if ikinci_takim_set > ilk_takim_set and ikinci_takim_set-ilk_takim_set <2:
    print(f"Kazanan takım: {ikinci_takim_isim}, kazandığı puan: {puan2}")
    print(f"Kaybeden takım: {ilk_takim_isim}, kazandığı puan: {puan1}")
