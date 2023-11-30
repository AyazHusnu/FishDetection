import os
import cv2
from PIL import Image
import numpy as np
import KIRPMA






def CevirFoto(x):

    import numpy as np
    print(x)
    print(type(x))
    # Fotoğrafı yükleyin
    image_path = "C:\\Users\\emirh\\Desktop\\Deney\\3A5BBF764E8CCB55C12589930059DDD3.jpg"
    image = cv2.imread(image_path)

    # Döndürme açısını belirtin (örneğin, 22 derece)
    angle = x
    print((angle))

    # Döndürme matrisini oluşturun
    height, width = image.shape[:2]
    rotation_matrix = cv2.getRotationMatrix2D((width / 2, height / 2), angle, 1)

    # Fotoğrafı döndürün
    rotated_image = cv2.warpAffine(image, rotation_matrix, (width, height))

    # Döndürülmüş fotoğrafı gösterin
    cv2.imshow("Rotated Image", rotated_image)
    cv2.imwrite("C:\\Users\\emirh\\Desktop\\Deney\\adnan2.jpg", rotated_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def ayna():
    def mirror_image(image_path, output_path):
        print("aynnn")
        # Resmi oku
        original_image = cv2.imread(image_path)

        # Resmi yatay olarak simetrik olarak çevir
        mirrored_image = cv2.flip(original_image, 1)

        # Sadece ayna görüntüsünü kaydet
        cv2.imwrite(output_path, mirrored_image)

    # Kullanım örneği
    image_path = "C:\\Users\\emirh\\Desktop\\Deney\\adnan2.jpg"
    output_path = "C:\\Users\\emirh\\Desktop\\Deney\\foto\\adnan3.jpg"
    mirror_image(image_path, output_path)


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

def write_coordinates_array_to_txt(x_values, y_values, output_file="C:\\Users\\emirh\\Desktop\\Deney\\Koy\\resolution.txt"):
    try:
        with open(output_file, "w") as file:
            file.write(f"{x_values} \n{y_values}")
            print(f"X ve Y değerleri {output_file} adlı dosyaya yazıldı.")
    except Exception as e:
        print(f"Hata: {e}")

# Kullanım örneği
folder_path = "C:\\Users\\emirh\\Desktop\\Deney"  # Klasör yolunu belirtin
x_values, y_values = process_images_in_folder(folder_path)
write_coordinates_array_to_txt(x_values, y_values)



import os

# Klasör yolunu belirtin
klasor_yolu = "C:\\Users\\emirh\\Desktop\\Deney"  # Klasör yolunu değiştirin

# Çıktı dosyasının adını belirtin
cikti_dosyasi = "C:\\Users\\emirh\\Desktop\\Deney\\Koy\\Sonuclar.txt"

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
















import math


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
dosya_birlestir('C:\\Users\\emirh\\Desktop\\Deney\\Koy\\resolution.txt', 'C:\\Users\\emirh\\Desktop\\Deney\\Koy\\Sonuclar.txt', 'C:\\Users\\emirh\\Desktop\\Deney\\Koy\\birlesik_dosya.txt')

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





def elemanyolla():
    # Dosya adını ve yolu belirtin
    dosya_adı = "C:\\Users\\emirh\\Desktop\\Deney\\Koy\\cikis.txt"



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

    x11=L0X
    y11=L0Y
    x21=L1X
    y21=L1Y

    a=abs(x2-x1)
    c=math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2))
    aci=math.acos(a/c)

    def radian_to_degree(radian):
        degree = radian * (180 / math.pi)
        return degree
    aci=radian_to_degree(aci)
    print(aci)

    if x11-x21>0 and y11-y21<0:
        aci=-aci
        print("Burda1")
        CevirFoto(aci)
    if x11-x21<0 and y11-y21<0 :
        aci=aci
        print("Burda2")
        CevirFoto(aci)
        ayna()
    if x11-x21<0 and y11-y21>0:
        aci=-aci
        print("Burda3")
        CevirFoto(aci)
        ayna()
    if x11-x21>0 and y11-y21>0:
        aci=aci
        CevirFoto(aci)




    print("aci:",aci)
    CevirFoto(aci)

elemanyolla()
KIRPMA.cikart()