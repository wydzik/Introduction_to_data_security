import cv2
import numpy as np
import random

def random_pixel_generator():
    #0 - black pixel
    #1 - white pixel
    pix=(int)(random.uniform(0,2))
    if pix==0:
        return 0
    else:
        return 255
def random_pixel_value_changer():
    # pixels are as follows 1 3
    #                       2 4
    pix=(int)(random.uniform(1,4))
    return pix
img=cv2.imread('message.png',cv2.IMREAD_GRAYSCALE)

blank_image = np.zeros((len(img)*2,len(img[0])*2,1), np.uint8)
cv2.imwrite('bw.png',blank_image)

sec1=cv2.imread('bw.png',cv2.IMREAD_GRAYSCALE)
sec2=cv2.imread('bw.png',cv2.IMREAD_GRAYSCALE)
for i in range(0,len(img)):
    for j in range(0,len(img[i])):
        if(img[i][j]==0):
            sec1.itemset((i*2,j*2),random_pixel_generator())
            if(sec1[i*2,j*2]==255):
                sec2.itemset((i*2,j*2),0)
            else:
                sec2.itemset((i*2,j*2),255)
            sec1.itemset((i*2+1,j*2),random_pixel_generator())
            if (sec1[i * 2 + 1, j * 2] == 255):
                sec2.itemset((i * 2 + 1, j * 2), 0)
            else:
                sec2.itemset((i*2+1,j*2),255)
            sec1.itemset((i*2,j*2+1),random_pixel_generator())
            if (sec1[i * 2, j * 2 + 1] == 255):
                sec2.itemset((i * 2, j * 2 + 1), 0)
            else:
                sec2.itemset((i * 2, j * 2 + 1), 255)
            sec1.itemset((i*2+1,j*2+1),random_pixel_generator())
            if (sec1[i * 2 + 1, j * 2 + 1] == 255):
                sec2.itemset((i * 2 + 1, j * 2 + 1), 0)
            else:
                sec2.itemset((i * 2 + 1, j * 2 + 1), 255)
        if(img[i][j]==255):
            counter=False
            sec1.itemset((i * 2, j * 2), random_pixel_generator())
            if (sec1[i * 2, j * 2] == 255):
                counter=True
            sec1.itemset((i * 2 + 1, j * 2), random_pixel_generator())
            if (sec1[i * 2 + 1, j * 2] == 255):
                counter = True
            sec1.itemset((i * 2, j * 2 + 1), random_pixel_generator())
            if (sec1[i * 2, j * 2 + 1] == 255):
                counter = True
            sec1.itemset((i * 2 + 1, j * 2 + 1), random_pixel_generator())
            if (sec1[i * 2 + 1, j * 2 + 1] == 255):
                counter = True
            if counter==False:
                a=random_pixel_value_changer()
                if a==1:
                    sec1.itemset((i * 2, j * 2), 255)
                if a==2:
                    sec1.itemset((i * 2 + 1, j * 2),255)
                if a==3:
                    sec1.itemset((i * 2, j * 2 + 1),255)
                if a==4:
                    sec1.itemset((i * 2 + 1, j * 2 + 1),255)
            check=0
            sec2.itemset((i * 2, j * 2), random_pixel_generator())
            if(sec1[i * 2, j * 2] ==0 or sec2[i * 2, j * 2]==0):
                check+=1
            sec2.itemset((i * 2 + 1, j * 2), random_pixel_generator())
            if(sec1[i * 2 + 1, j * 2]==0 or sec2[i * 2 + 1, j * 2]==0):
                check+=1
            sec2.itemset((i * 2, j * 2 + 1), random_pixel_generator())
            if(sec1[i * 2, j * 2 + 1]==0 or sec2[i * 2, j * 2 + 1]==0):
                check+=1
            sec2.itemset((i * 2 + 1, j * 2 + 1), random_pixel_generator())
            if(sec1[i * 2 + 1, j * 2 + 1]==0 or sec2[i * 2 + 1, j * 2 + 1]==0):
                check+=1
            if check==4:
                if (sec1[i * 2, j * 2] == 255 and  sec2[i * 2, j * 2] == 0):
                    sec2.itemset((i*2,j*2),255)
                elif (sec1[i * 2 + 1, j * 2]==255 and sec2[i * 2 + 1, j * 2]==0):
                    sec2.itemset((i*2+1,j*2),255)
                elif (sec1[i * 2, j * 2 + 1]==255 and sec2[i * 2, j * 2 + 1]==0):
                    sec2.itemset((i*2,j*2+1),255)
                elif(sec1[i * 2 + 1, j * 2 + 1]==255 and sec2[i * 2 + 1, j * 2 + 1]==0):
                    sec2.itemset((i*2+1,j*2+1),255)
cv2.imwrite('secret1.png',sec1)
cv2.imwrite('secret2.png',sec2)
print("Message divided into sercet1.png an secret2.png")
blank_image2 = np.zeros(((int)(len(sec1)/2),(int)(len(sec1[0])/2),1), np.uint8)
cv2.imwrite('decryption.png',blank_image2)
dec=cv2.imread('decryption.png',cv2.IMREAD_GRAYSCALE)
for i in range(0,len(dec)):
    for j in range(0,len(dec[0])):
        check=0
        if (sec1[i * 2, j * 2] == 0 or sec2[i * 2, j * 2] == 0):
            check+=1
        if (sec1[i * 2 + 1, j * 2] == 0 or sec2[i * 2 + 1, j * 2] == 0):
            check+=1
        if (sec1[i * 2, j * 2 + 1] == 0 or sec2[i * 2, j * 2 + 1] == 0):
            check+=1
        if (sec1[i * 2 + 1, j * 2 + 1] ==0 or sec2[i * 2 + 1, j * 2 + 1] == 0):
            check+=1
        if check!=4:
            dec.itemset((i,j),255)
cv2.imwrite('decryption.png',dec)
print("Decrypted message stored in 'decryption.png'")
