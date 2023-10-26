# Pillow: redimensionando imagens com Python
# Essa biblioteca é o Photoshop do Python 😂
from PIL import Image

from pathlib import Path

ROOT_FOLDER = Path(__file__).parent
ORIGINAL = ROOT_FOLDER / 'clooney-batman.jpg'
NEW_IMAGE = ROOT_FOLDER / 'new-batima.jpg'

pil_image = Image.open(ORIGINAL)

width, height = pil_image.size
# exif = pil_image.info['exif']

new_width = 1920
new_height = round(height * new_width / width)

print(new_width, new_height)

new_image = pil_image.resize((new_width, new_height))

new_image.save(
    NEW_IMAGE,
    optimize=True,
    quality=70,
)
