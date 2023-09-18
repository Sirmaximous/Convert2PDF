import img2pdf
import os
from PIL import Image
from tqdm import tqdm

Image.MAX_IMAGE_PIXELS = None

print("Please input directory path to tif files.")
dirname = input()

print("Converting files to PDF...")
tif_files = [fname for fname in os.listdir(dirname) if fname.endswith("tif")]
for fname in tqdm(tif_files):
    path = os.path.join(dirname, fname)
    if os.path.isdir(path):
        continue
    with open(fname.replace("tif", "pdf"), "wb") as f:
        f.write(img2pdf.convert(path))