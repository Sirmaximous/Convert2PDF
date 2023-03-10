import img2pdf
import os
from PIL import Image

Image.MAX_IMAGE_PIXELS = None

dirname = "C:\\Users\\TyrellJohnson\\Downloads\\PDF Convert\\Input"
imgs = []


for fname in os.listdir(dirname):
    if not fname.endswith("tif"):
        continue
    path = os.path.join(dirname, fname)
    if os.path.isdir(path):
        continue
    imgs.append(path)
    with open ("name.pdf","wb") as f:
        f.write(img2pdf.convert(imgs))
