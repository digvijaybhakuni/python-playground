from PIL import Image

var_image = Image.open(r'temp/test.png')

pil_img = var_image.convert('RGB')
pil_img.save(r'temp/test.pdf')

