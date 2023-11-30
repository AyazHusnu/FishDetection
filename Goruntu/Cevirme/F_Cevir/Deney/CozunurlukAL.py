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
            file.write(f"{x_values} \n{y_values}")
            print(f"X ve Y değerleri {output_file} adlı dosyaya yazıldı.")
    except Exception as e:
        print(f"Hata: {e}")

# Kullanım örneği
folder_path = "C:\\Users\\emirh\\PycharmProjects\\Goruntu\\Cevirme\\F_Cevir\\Deney"  # Klasör yolunu belirtin
x_values, y_values = process_images_in_folder(folder_path)
write_coordinates_array_to_txt(x_values, y_values)
