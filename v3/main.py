from models.get_estatisc_espion import GetEstatiscEspion
import pytesseract
from PIL import Image
import easyocr
import tempfile
from PIL import Image
import pillow_avif


def search_images_and_extract_text(path_image):
    imagem = Image.open(path_image)
    width, height = imagem.size
    top = 0
    left = 0
    right = width
    bottom = int(height * 0.9)

    imagem_cortada = imagem.crop((left, top, right, bottom))
    with tempfile.NamedTemporaryFile(delete=False, suffix='.png') as temp_file:
        temp_path = temp_file.name
        imagem_cortada.save(temp_path)

    reader = easyocr.Reader(['pt'])
    resultado = reader.readtext(temp_path, detail=0)
    return " ".join(resultado)


if __name__ == '__main__':
    # tranformando imagam avif em png
    # img = Image.open('teste.avif')
    # img.save('output.png')
    search_images_and_extract_text("goias-x-america-mg.webp")
#     object = GetEstatiscEspion()
#     object.searchEstatisticEspion()




