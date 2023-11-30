import math


'''def dosya_birlestir(dosya1, dosya2, hedef_dosya):
    try:
        # İlk dosyayı oku
        with open(dosya1, 'r', encoding='utf-8') as file1:
            icerik1 = file1.read()

        # İkinci dosyayı oku
        with open(dosya2, 'r', encoding='utf-8') as file2:
            icerik2 = file2.read()

        # Dosyaları birleştir
        birlesik_icerik = icerik1 + '\n' + icerik2

        # Birleştirilmiş içerikleri hedef dosyaya yaz
        with open(hedef_dosya, 'w', encoding='utf-8') as hedef:
            hedef.write(birlesik_icerik)

        print("Dosyalar başarıyla birleştirildi.")

    except Exception as e:
        print("Bir hata oluştu:", str(e))


# Kullanım örneği
dosya_birlestir('C:\\Users\\emirh\\PycharmProjects\\Goruntu\\Cevirme\\F_Cevir\\Deney\\resolution.txt', 'C:\\Users\\emirh\\PycharmProjects\\Goruntu\\Cevirme\\F_Cevir\\Deney\\Sonuclar.txt', 'C:\\Users\\emirh\\PycharmProjects\\Goruntu\\Cevirme\\F_Cevir\\Deney\\birlesik_dosya.txt')

# Giriş dosyası adını ve yolu belirtin
giris_dosya_adi = "C:\\Users\\emirh\\PycharmProjects\\Goruntu\\Cevirme\\F_Cevir\\Deney\\birlesik_dosya.txt"
# Çıkış dosyası adını ve yolu belirtin
cikis_dosya_adi = "C:\\Users\\emirh\\PycharmProjects\\Goruntu\\Cevirme\\F_Cevir\\Deney\\cikis.txt"


# Dosyadan okuma ve köşeli parantezleri kaldırma işlemi
with open(giris_dosya_adi, 'r') as giris_dosya, open(cikis_dosya_adi, 'w') as cikis_dosya:
    for satir in giris_dosya:
        # Satırdaki köşeli parantezleri kaldır
        satir_kaldirilmis = satir.replace("[", "").replace("]", "")
        # Kaldırılmış satırı çıkış dosyasına yaz
        cikis_dosya.write(satir_kaldirilmis)

print("Köşeli parantezler kaldırıldı ve çıkış dosyası oluşturuldu:", cikis_dosya_adi)
'''


def elemanyolla():
    # Dosya adını ve yolu belirtin
    dosya_adı = "C:\\Users\\emirh\\PycharmProjects\\Goruntu\\Cevirme\\F_Cevir\\Deney\\cikis.txt"



    # Dosyayı oku ve satırları bir listeye kaydet
    with open(dosya_adı, 'r') as dosya:
        satırlar = dosya.readlines()

    # Her bir satırın ilk elemanını içerecek liste
    ilk_elemanlar = []

    # Her bir satırı işle
    for satır in satırlar:
        # Satırdaki elemanları boşluklara göre ayır
        elemanlar = satır.split(",")

        # Eğer satırda en az bir eleman varsa, ilk elemanı listeye ekle
        if elemanlar:
            ilk_elemanlar.append(elemanlar[0])


    ilk= list(map(float, ilk_elemanlar))
    # İlk elemanları ekrana yazdır
    print(ilk)
    AciHesapla(ilk[0],ilk[1],ilk[2],ilk[3],ilk[4],ilk[5])

def AciHesapla(X,Y,L0X,L0Y,L1X,L1Y,):



    Birinci_Nokta=[X*L0X,abs((Y*L0Y)-Y)]
    x1=Birinci_Nokta[0]
    y1=Birinci_Nokta[1]
    Ikinci_Nokta=[X*L1X,abs((Y*L1Y-Y))]
    x2=Ikinci_Nokta[0]
    y2=Ikinci_Nokta[1]
    print(Birinci_Nokta)
    a=abs(x2-x1)
    c=math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2))
    print(c)
    aci=math.acos(a/c)
    print("Aci:",aci)

elemanyolla()
