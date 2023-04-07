import piexif
from PIL import ImageFont,ImageDraw,Image
import numpy as np
import cv2
import os
import imageio,rawpy

def test_imgdata(img_dir):
    exif_dict=piexif.load(img_dir)
    for tag in exif_dict["Exif"]:
        print(piexif.TAGS["Exif"][tag]["name"],exif_dict["Exif"][tag])

def raw2jpg(args,img_dir):

    filename=img_dir.split("/")[-1].split(".")[0]
    with rawpy.imread(img_dir) as rawfile:
        thumb=rawfile.extract_thumb()
    if thumb.format==rawpy.ThumbFormat.JPEG:
        with open(os.path.join(args.tmpdir,filename)+".jpg",'wb') as f:
            f.write(thumb.data)
    elif thumb.format==rawpy.Thumbformat.BITMAP:
        imageio.imsave(os.path.join(args.tmpdir,filename)+".jpg",thumb.data)

    
def modDatetime(rawstring):
    rawdatetime=rawstring
    rawdatetime=rawdatetime.replace(" ",":")
    dates=rawdatetime.split(":")
    datetime=".".join(dates[0:3])
    datetime+=" "
    datetime+=":".join(dates[3:])
    return datetime
        

def read_img_data(args):
    imgs=os.listdir(args.imgdir)
    exif_list=[]
    img_list=[]
    for item in imgs:
        if "jpg" in item.lower() or "jpeg" in item.lower():
            exif_dict=piexif.load(os.path.join(args.imgdir,item))
            exif_data=[]
            for tag in exif_dict["0th"]:
                if piexif.TAGS["0th"][tag]["name"]=="Make":
                    cam_factory=(exif_dict["0th"][tag].decode('utf-8'))
                elif piexif.TAGS["0th"][tag]["name"]=="Model":
                    cam_name=(exif_dict["0th"][tag].decode('utf-8'))
            for tag in exif_dict["Exif"]:
                if piexif.TAGS["Exif"][tag]["name"]=="ExposureTime":
                    shutter=list(exif_dict["Exif"][tag])
                if piexif.TAGS["Exif"][tag]["name"]=="FNumber":
                    aperture=str(round(exif_dict["Exif"][tag][0]/exif_dict["Exif"][tag][1],1))
                if piexif.TAGS["Exif"][tag]["name"]=="ISOSpeedRatings":
                    iso=str(int(exif_dict["Exif"][tag]))
                if piexif.TAGS["Exif"][tag]["name"]=="FocalLength":
                    focallength=str(int(exif_dict["Exif"][tag][0]/exif_dict["Exif"][tag][1]))
                if piexif.TAGS["Exif"][tag]["name"]=="DateTimeOriginal":
                    datetime=exif_dict["Exif"][tag].decode('utf-8')
            exif_data.append(cam_factory)
            exif_data.append(cam_name)
            exif_data.append(shutter)
            exif_data.append(aperture)
            exif_data.append(iso)
            exif_data.append(datetime)
            exif_data.append(focallength)
            exif_list.append(exif_data)
            img_list.append(os.path.join(args.imgdir,item))
        elif "nef" in item.lower() or "cr" in item.lower() or "arw" in item.lower():
            exif_dict=piexif.load(os.path.join(args.imgdir,item))
            exif_data=[]
            for tag in exif_dict["0th"]:
                if piexif.TAGS["0th"][tag]["name"]=="Make":
                    cam_factory=(exif_dict["0th"][tag].decode('utf-8'))
                elif piexif.TAGS["0th"][tag]["name"]=="Model":
                    cam_name=(exif_dict["0th"][tag].decode('utf-8'))
            for tag in exif_dict["Exif"]:
                if piexif.TAGS["Exif"][tag]["name"]=="ExposureTime":
                    shutter=list(exif_dict["Exif"][tag])
                if piexif.TAGS["Exif"][tag]["name"]=="FNumber":
                    aperture=str(round(exif_dict["Exif"][tag][0]/exif_dict["Exif"][tag][1],1))
                if piexif.TAGS["Exif"][tag]["name"]=="ISOSpeedRatings":
                    iso=str(int(exif_dict["Exif"][tag]))
                if piexif.TAGS["Exif"][tag]["name"]=="FocalLength":
                    focallength=str(int(exif_dict["Exif"][tag][0]/exif_dict["Exif"][tag][1]))
                if piexif.TAGS["Exif"][tag]["name"]=="DateTimeOriginal":
                    datetime=exif_dict["Exif"][tag].decode('utf-8')
            exif_data.append(cam_factory)
            exif_data.append(cam_name)
            exif_data.append(shutter)
            exif_data.append(aperture)
            exif_data.append(iso)
            exif_data.append(datetime)
            exif_data.append(focallength)
            exif_list.append(exif_data)
            img_list.append(os.path.join(args.tmpdir,item.split(".")[0])+".jpg")
            raw2jpg(args,os.path.join(args.imgdir,item))
     
    return exif_list,img_list


def addMark(args, exif_list, img_list):

    fontpath="C:\\Windows\\Fonts\\Microsoft YaHei UI\\msyhbd.ttc"
    font2path="C:\\Windows\\Fonts\\Microsoft YaHei UI\\msyh.ttc"

    for img,exif_data in zip(img_list,exif_list):
        src=cv2.imread(img)
        height,width,_=src.shape
        badge_width=int(max(height,width)/10)
        fontratio=[3.0/np.log2(max(height,width)),1.8/np.log2(max(height,width)),3.0/np.log2(max(height,width)),1.8/np.log2(max(height,width))]

        # make border
        src=cv2.copyMakeBorder(src,0,badge_width,0,0,cv2.BORDER_CONSTANT,value=[255,255,255])

        # add brand logo
        binfo=exif_data[0].lower()
        if "nikon" in binfo:
            brand=cv2.imread("./logo/nikon.jpeg")
        elif "canon" in binfo:
            brand=cv2.imread("./logo/canon.jpeg")
        elif "sony" in binfo:
            brand=cv2.imread("./logo/sony.jpg")
        else:
            raise ValueError("No camera brand found! Check the exif data!")
        bh,bw,_=brand.shape
        longboard=max(bh,bw)
        ratio=longboard/(badge_width*0.583)
        brand=cv2.resize(brand,(int(bh/ratio),int(bw/ratio)))
        bh,bw,_=brand.shape

        font3=ImageFont.truetype(fontpath,int(badge_width*fontratio[2]))
        shoot_params=exif_data[-1]+"mm f/"+exif_data[3]+" "+str(exif_data[2][0])+"/"+str(exif_data[2][1])+"s ISO"+exif_data[4]
        f3width,_=font3.getsize(shoot_params)
        
        np.copyto(src[height+badge_width//4:height+badge_width//4+bh,int(width-f3width-width//20-1.3*bw):int(width-f3width-width//20-1.3*bw)+bw,:],brand)
        
        
        # add exif text
        font1=ImageFont.truetype(fontpath,int(badge_width*fontratio[0]))
        img_pil=Image.fromarray(src)
        drawMat=ImageDraw.Draw(img_pil)
        drawMat.text((width/30,height+badge_width//3.5),exif_data[1],font=font1,fill=(0,0,0))
        _,f1height=font1.getsize(exif_data[1])
        font2=ImageFont.truetype(font2path,int(badge_width*fontratio[1]))
        drawMat.text((width/30,height+badge_width//3.5+int(1.*f1height)),exif_data[0],font=font2,fill=(120,120,120))
        
        drawMat.text((width-f3width-width//20,height+badge_width//3.5),shoot_params,font=font3,fill=(0,0,0))
        font4=ImageFont.truetype(font2path,int(badge_width*fontratio[3]))
        datetime=modDatetime(exif_data[-2])
        drawMat.text((width-f3width-width//20,height+badge_width//3.5+int(1.*f1height)),datetime,font=font4,fill=(120,120,120))

        # add seperate line
        sep_wid=(int(width-f3width-width//20)+int(width-f3width-width//20-1.3*bw)+bw)//2
        drawMat.line((sep_wid,height+badge_width*2//10,sep_wid,height+badge_width*9//10),fill=(20,20,20),width=badge_width//200)


        dst=np.array(img_pil)
        # cv2.namedWindow("add_text",cv2.WINDOW_FREERATIO)
        # cv2.imshow("add_text",dst)
        # cv2.waitKey(0)
        cv2.imwrite(args.svdir+"/"+img.split("/")[-1],dst)
        print("Image ",img.replace("\\","/").split("/")[-1]," has been processed!")
    return


def testraw(args):
    exif_list=[]
    for item in os.listdir(args.imgdir):
        exif_dict=piexif.load(os.path.join(args.imgdir,item))
        exif_data=[]
        for tag in exif_dict["0th"]:
            if piexif.TAGS["0th"][tag]["name"]=="Make":
                cam_factory=(exif_dict["0th"][tag].decode('utf-8'))
            elif piexif.TAGS["0th"][tag]["name"]=="Model":
                cam_name=(exif_dict["0th"][tag].decode('utf-8'))
        for tag in exif_dict["Exif"]:
            if piexif.TAGS["Exif"][tag]["name"]=="ExposureTime":
                shutter=list(exif_dict["Exif"][tag])
            if piexif.TAGS["Exif"][tag]["name"]=="FNumber":
                aperture=str(round(exif_dict["Exif"][tag][0]/exif_dict["Exif"][tag][1],1))
            if piexif.TAGS["Exif"][tag]["name"]=="ISOSpeedRatings":
                iso=str(int(exif_dict["Exif"][tag]))
            if piexif.TAGS["Exif"][tag]["name"]=="FocalLength":
                focallength=str(int(exif_dict["Exif"][tag][0]/exif_dict["Exif"][tag][1]))
            if piexif.TAGS["Exif"][tag]["name"]=="DateTimeOriginal":
                datetime=exif_dict["Exif"][tag].decode('utf-8')
        exif_data.append(cam_factory)
        exif_data.append(cam_name)
        exif_data.append(shutter)
        exif_data.append(aperture)
        exif_data.append(iso)
        exif_data.append(datetime)
        exif_data.append(focallength)
        exif_list.append(exif_data)
    for item in exif_list:
        print(item)
