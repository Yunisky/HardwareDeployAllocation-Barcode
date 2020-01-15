import pyzbar.pyzbar as pyzbar
import os
from PIL import Image,ImageEnhance
def barec():
    img = Image.open(jpg)
    mac = 0
    sn = 0
    ponsn = 0
    twodbar = 0
    tsn = 0
    pn = 0
    qty = 0
    loc = 0
    #img = ImageEnhance.Brightness(img).enhance(2.0)#增加亮度
    #img = ImageEnhance.Sharpness(img).enhance(17.0)#锐利化
    img = ImageEnhance.Contrast(img).enhance(4.0)#增加对比度
    img = img.convert('L')#灰度化
    barcodes = pyzbar.decode(img)
    for barcode in barcodes:
        barcodedata = barcode.data.decode("utf-8")
        if len(barcodedata) == 12 :
            mac=barcodedata
        elif len(barcodedata) == 20 and barcodedata[0:1] =="2":
            sn=barcodedata
        elif len(barcodedata) == 16 :
            ponsn=barcodedata
        elif barcodedata[0:3] =="[)>" :
            twodbar=barcodedata
        elif barcodedata[0:2] == "AP" or barcodedata[0:2] == "S" or barcodedata[0:2] == "EG" :
            tsn=barcodedata
        elif barcodedata[:1].isdigit() and len(barcodedata) == 8 :
            pn=barcodedata
        elif barcodedata[-3:] == "PCS" :
            qty=barcodedata.rstrip("PCS")
        elif barcodedata[0:2] == "L-" :
            loc=barcodedata.strip("L-")
    print(str(jpg)+","+str(pn)+","+str(tsn)+","+str(sn)+","+str(mac)+","+str(ponsn)+","+str(twodbar)+","+str(qty)+","+str(loc)+",")
path = "E:\coding\prodece"
jpg = "0"
fnames = os.listdir(path)
print("文件名,生产PN,设备型号,序列号,MAC地址,PONSN,QR信息,数量,安装位置")
for fname in fnames :
    if fname.endswith('.jpg'):
        jpg = path+'\\'+fname
        barec()