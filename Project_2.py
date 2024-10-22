ogr_no=input("Öğrenci numarınızı giriniz:")
ad_soyad= input("Adınızı ve soyadınızı giriniz:")
ilkders_teorik = float(input("Aldığınız ilk dersin haftalık teorik ders saatini giriniz:"))
ilkders_uygulama = float(input("Aldığınız ilk dersinizin haftalık uygulama ders saatini giriniz:"))
ilkders_akts = float(input("Aldığınız ilk dersinizin haftalık AKTS kredisini giriniz:"))
ilkders_not = float(input("Aldığınız ilk dersin dönem sonu notunu giriniz:"))
ikinciders_teorik = float(input("Aldığınız ikinci dersinizin haftalık teorik ders saatini giriniz:"))
ikinciders_uygulama = float(input("Aldığınız ikinci dersinizin haftalık uygulama ders saatini giriniz:"))
ikinciders_akts= float(input("Aldığınız ikinci dersinzin haftalık AKTS kresini giriniz:"))
ikinciders_not = float(input("Aldığınız ikinci dersin dönem sonu notunu giriniz."))
ilkders_yerelkredi = ilkders_teorik + ilkders_uygulama/2
ikinciders_yerelkredi = ikinciders_teorik + ikinciders_uygulama/2
toplam_yerelkredi = ilkders_yerelkredi+ikinciders_yerelkredi
toplam_akts = ilkders_akts + ikinciders_akts
akts_agno = ((ilkders_not*ilkders_akts +ikinciders_akts*ikinciders_not) / (ilkders_akts+ikinciders_akts) )
yerelkredi_agno =((ilkders_not*ilkders_yerelkredi+ikinciders_not*ikinciders_yerelkredi)/(ilkders_yerelkredi+ikinciders_yerelkredi))
print(f"Ögrenci numarası: {ogr_no}")
print(f"Ad ve Soyad: {ad_soyad}")
print(f"Bu dönem aldığı toplam yerel kredi miktarı {toplam_yerelkredi}")
print(f"Bu dönem aldıgı toplam AKTS kredi miktarı {toplam_akts}")
print(f"Yerel krediye göre bu dönem sonu AGNO {yerelkredi_agno}")
print(f"AKTS'ye göre bu dönem sonu AGNO {akts_agno}")




