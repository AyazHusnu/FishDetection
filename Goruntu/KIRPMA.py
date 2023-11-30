import os
from PIL import Image
import math

def cikart():

    def koordinat():
        klasor_yolu = "C:\\Users\\emirh\\Desktop\\Deney\\Cikart"  # Klasör yolunu değiştirin

        # Çıktı dosyasının adını belirtin
        cikti_dosyasi = "C:\\Users\\emirh\\Desktop\\Deney\\Cikart\\Cikartilmis\\Sonuclar.txt"

        # Değişkenleri tanımlayın
        L0X = []
        L0Y = []
        L0W = []
        L0H = []



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
                        if değerler[0] == '7':
                            L0X.append(float(değerler[1]))
                            L0Y.append(float(değerler[2]))
                            L0W.append(float(değerler[3]))
                            L0H.append(float(değerler[4]))
        # Sonuçları çıktı dosyasına yazın
        with open(cikti_dosyasi, 'w') as cikti_dosya:
            cikti_dosya.write("{}".format(L0X))
            cikti_dosya.write("\n{}".format(L0Y))
            cikti_dosya.write("\n{}".format(L0W))
            cikti_dosya.write("\n{}".format(L0H))

        print("Sonuçlar {} dosyasına kaydedildi.".format(cikti_dosyasi))


    def cozunurlukal():
        def get_image_resolution(image_path):
            try:
                with Image.open(image_path) as img:
                    width, height = img.size
                    return width, height
            except Exception as e:
                print(f"Hata: {e}")
                return None

        def process_images_in_folder(folder_path):
            x_values = []
            y_values = []

            for filename in os.listdir(folder_path):
                if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
                    image_path = os.path.join(folder_path, filename)
                    resolution = get_image_resolution(image_path)

                    if resolution:
                        x_value, y_value = resolution
                        x_values.append(x_value)
                        y_values.append(y_value)
                    else:
                        print(f"{image_path} için çözünürlük alınamadığı için kayıt yapılamadı.")

            return x_values, y_values

        def write_coordinates_array_to_txt(x_values, y_values,
                                              output_file="C:\\Users\\emirh\\Desktop\\Deney\\Cikart\\Cikartilmis\\resolution.txt"):
            try:
                with open(output_file, "w") as file:
                    file.write(f"{x_values} \n{y_values}")
                    print(f"X ve Y değerleri {output_file} adlı dosyaya yazıldı.")
            except Exception as e:
                print(f"Hata: {e}")

        # Kullanım örneği
        folder_path = "C:\\Users\\emirh\\Desktop\\Deney\\foto"  # Klasör yolunu belirtin
        x_values, y_values = process_images_in_folder(folder_path)
        write_coordinates_array_to_txt(x_values, y_values)


    def birlestir():
        def dosya_birlestir(dosya1, dosya2, hedef_dosya):
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
        dosya_birlestir('C:\\Users\\emirh\\Desktop\\Deney\\Cikart\\Cikartilmis\\resolution.txt',
                        'C:\\Users\\emirh\\Desktop\\Deney\\Cikart\\Cikartilmis\\Sonuclar.txt',
                        'C:\\Users\\emirh\\Desktop\\Deney\\Cikart\\Cikartilmis\\birlesik_dosya.txt')

        # Giriş dosyası adını ve yolu belirtin
        giris_dosya_adi = "C:\\Users\\emirh\\Desktop\\Deney\\Koy\\birlesik_dosya.txt"
        # Çıkış dosyası adını ve yolu belirtin
        cikis_dosya_adi = "C:\\Users\\emirh\\Desktop\\Deney\\Koy\\cikis.txt"

        # Dosyadan okuma ve köşeli parantezleri kaldırma işlemi
        with open(giris_dosya_adi, 'r') as giris_dosya, open(cikis_dosya_adi, 'w') as cikis_dosya:
            for satir in giris_dosya:
                # Satırdaki köşeli parantezleri kaldır
                satir_kaldirilmis = satir.replace("[", "").replace("]", "")
                # Kaldırılmış satırı çıkış dosyasına yaz
                cikis_dosya.write(satir_kaldirilmis)

        print("Köşeli parantezler kaldırıldı ve çıkış dosyası oluşturuldu:", cikis_dosya_adi)


    def parantez_kaldir():
        # Giriş dosyası adını ve yolu belirtin
        giris_dosya_adi = "C:\\Users\\emirh\\Desktop\\Deney\\Cikart\\Cikartilmis\\birlesik_dosya.txt"
        # Çıkış dosyası adını ve yolu belirtin
        cikis_dosya_adi = "C:\\Users\\emirh\\Desktop\\Deney\\Cikart\\Cikartilmis\\cikis.txt"


        # Dosyadan okuma ve köşeli parantezleri kaldırma işlemi
        with open(giris_dosya_adi, 'r') as giris_dosya, open(cikis_dosya_adi, 'w') as cikis_dosya:
            for satir in giris_dosya:
                # Satırdaki köşeli parantezleri kaldır
                satir_kaldirilmis = satir.replace("[", "").replace("]", "")
                # Kaldırılmış satırı çıkış dosyasına yaz
                cikis_dosya.write(satir_kaldirilmis)

        print("Köşeli parantezler kaldırıldı ve çıkış dosyası oluşturuldu:", cikis_dosya_adi)



    def elemanyolla():
        # Dosya adını ve yolu belirtin
        dosya_adı = "C:\\Users\\emirh\\Desktop\\Deney\\Cikart\\Cikartilmis\\cikis.txt"



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
        kes(ilk[0],ilk[1],ilk[2],ilk[3],ilk[4],ilk[5])


    def kes(CozX,CozY,X,Y,W,H):

        def crop_image(input_path, output_path, x, y, width, height):
            # Görüntüyü aç
            image = Image.open(input_path)

            # Belirtilen koordinatlar, genişlik ve yükseklik kullanılarak bölgeyi kes
            cropped_image = image.crop((x, y, x + width, y + height))

            # Kesilen bölgeyi kaydet
            cropped_image.save(output_path)

        # Kullanım örneği
        input_image_path = "C:\\Users\\emirh\\Desktop\\Deney\\foto\\adnan3.jpg"
        output_image_path = "C:\\Users\\emirh\\Desktop\\Deney\\Cikart\\Balik2.jpg"
        crop_width =CozX*W
        crop_height =CozY*H
        x_coordinate = (X*CozX) - (crop_width/2)
        y_coordinate = (Y*CozY) - (crop_height/2)

        crop_image(input_image_path, output_image_path, x_coordinate, y_coordinate, crop_width, crop_height)

    koordinat()
    cozunurlukal()
    birlestir()
    parantez_kaldir()
    elemanyolla()


cikart()