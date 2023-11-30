
import math
import os
from PIL import Image

import os
from PIL import Image

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

def write_coordinates_array_to_txt(x_values, y_values, output_file="C:\\Users\\emirh\\PycharmProjects\\Goruntu\\Cevirme\\F_Cevir\\Deney\\resolution.txt"):
    try:
        with open(output_file, "w") as file:
            file.write(f"X: {x_values} \nY: {y_values}")
            print(f"X ve Y değerleri {output_file} adlı dosyaya yazıldı.")
    except Exception as e:
        print(f"Hata: {e}")

# Kullanım örneği
folder_path = "C:\\Users\\emirh\\PycharmProjects\\Goruntu\\Cevirme\\F_Cevir\\Deney"  # Klasör yolunu belirtin
x_values, y_values = process_images_in_folder(folder_path)
write_coordinates_array_to_txt(x_values, y_values)








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



def read_resolution_from_txt(file_path="resolution.txt"):
    resolutions = []
    try:
        with open(file_path, "r") as file:
            lines = file.readlines()
            for line in lines:
                if "X değeri:" in line and "Y değeri:" in line:
                    # X ve Y değerlerini bul ve resolutions listesine ekle
                    x_value = int(line.split("X değeri:")[1].split("piksel")[0].strip())
                    y_value = int(line.split("Y değeri:")[1].split("piksel")[0].strip())
                    resolutions.append((x_value, y_value))
        return resolutions
    except FileNotFoundError:
        print(f"{file_path} dosyası bulunamadı.")
        return None
    except Exception as e:
        print(f"Hata: {e}")
        return None


# Kullanım örneği
resolutions = read_resolution_from_txt()

if resolutions:
    for x, y in resolutions:
        AciHesapla(x, y)











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
