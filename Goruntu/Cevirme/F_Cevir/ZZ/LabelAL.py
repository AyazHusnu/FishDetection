import os

# Klasör yolunu belirtin
klasor_yolu = "C:\\Users\\emirh\\PycharmProjects\\Goruntu\\Cevirme\\F_Cevir\\ZZ"  # Klasör yolunu değiştirin

# Çıktı dosyasının adını belirtin
cikti_dosyasi = "C:\\Users\\emirh\\PycharmProjects\\Goruntu\\Cevirme\\F_Cevir\\Deney\\Sonuclar.txt"

# Değişkenleri tanımlayın
L0X = []
L0Y = []
L0W = []
L0H = []

L1X = []
L1Y = []
L1W = []
L1H = []



# Klasördeki tüm dosyaları kontrol edin
for dosya_adı in os.listdir(klasor_yolu):
    if dosya_adı.endswith(".txt"):
        dosya_yolu = os.path.join(klasor_yolu, dosya_adı)

        # Dosyayı okuyun
        with open(dosya_yolu, 'r') as dosya:
            for satır in dosya:
                # Satırdaki değerleri boşluk karakteriyle ayırın
                değerler = satır.strip().split()

                # Label'ı kontrol edin
                if değerler[0] == '0':
                    L0X.append(float(değerler[1]))
                    L0Y.append(float(değerler[2]))
                    L0W.append(float(değerler[3]))
                    L0H.append(float(değerler[4]))
                elif değerler[0] == '1':
                    L1X.append(float(değerler[1]))
                    L1Y.append(float(değerler[2]))
                    L1W.append(float(değerler[3]))
                    L1H.append(float(değerler[4]))

# Sonuçları çıktı dosyasına yazın
with open(cikti_dosyasi, 'w') as cikti_dosya:
    cikti_dosya.write("{}".format(L0X))
    cikti_dosya.write("\n{}".format(L0Y))


    cikti_dosya.write("\n{}".format(L1X))
    cikti_dosya.write("\n{}".format(L1Y))




print("Sonuçlar {} dosyasına kaydedildi.".format(cikti_dosyasi))
