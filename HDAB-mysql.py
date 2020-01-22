import pyzbar.pyzbar as pyzbar
import os
import mysql.connector
from PIL import Image,ImageEnhance
print(" __     __          _     _ ")         
print(" \ \   / /         (_)   | |         ")
print("  \ \_/ /   _ _ __  _ ___| | ___   _ ")
print("   \   / | | | '_ \| / __| |/ / | | |")
print("    | || |_| | | | | \__ \   <| |_| |")
print("    |_| \__,_|_| |_|_|___/_|\_\\\__  |")
print("                                __/ /")
print("                               |___/ ")
print()
print("Copyright © 2019 Jinan Yunisky Infotech Co.,Ltd. All rights reserved.  ")
print()
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
        elif barcodedata[0:2] == "AP" or barcodedata[0:1] == "S" or barcodedata[0:2] == "EG" or barcodedata[0:1] == "H" :
            tsn=barcodedata
        elif barcodedata[:1].isdigit() and len(barcodedata) == 8 :
            pn=barcodedata
        elif barcodedata[-3:] == "PCS" :
            qty=barcodedata.rstrip("PCS")
        elif barcodedata[0:2] == "L-" :
            loc=barcodedata.strip("L-")
    sql = "INSERT INTO " + dbtname + "(id, mac, sn, ponsn, twodbar, tsn, qty, loc, fname) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
    val = (id, mac, sn, ponsn, twodbar, tsn, qty, loc, fname)
    cursor.execute(sql, val)
    conn.commit()
print('欢迎使用ICT产品批量安装统计终端')
print()
print()
dbtname = input("请输入项目代码:")
print()
print()
path = "E:\coding\prodece"
jpg = "0"
global id 
id = 0
fnames = os.listdir(path)
conn = mysql.connector.connect(host='xxx.xxx.xxx.xxx' , user='username', password='password', database='databasename', use_unicode=True)
cursor = conn.cursor()
dbcr='create table '+ dbtname 
cursor.execute(dbcr+'(id varchar(20) primary key, mac varchar(40), sn  varchar(80), ponsn varchar(80), twodbar varchar(100), tsn varchar(40), qty varchar(10), loc varchar(80), fname varchar(100))')
for fname in fnames :
    if fname.endswith('.jpg'):
        jpg = path+'\\'+fname
        id = id + 1
        barec()
cursor.execute("SELECT fname FROM "+ dbtname)
result = cursor.fetchall()
for x in result:
  print(x)
print()
print()
print("以上记录已被处理，导入装维管理系统。工具将自动退出。")
