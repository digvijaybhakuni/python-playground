from PIL import Image

var_image1 = Image.open(r'temp/img1.jpg')
var_image2 = Image.open(r'temp/img2.jpg')
var_image3 = Image.open(r'temp/img3.jpg')
var_image4 = Image.open(r'temp/img4.jpg')

pil_img1 = var_image1.convert('RGB')
pil_img2 = var_image2.convert('RGB')
pil_img3 = var_image3.convert('RGB')
pil_img4 = var_image4.convert('RGB')


imgList = [pil_img2, pil_img3, pil_img4];

pil_img1.save(r'temp/testList.pdf', save_all=True, append_images=imgList);
