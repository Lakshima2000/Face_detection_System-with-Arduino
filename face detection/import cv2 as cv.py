import cv2 as cv
import face_recognition as fr
import numpy as np
import os
import pyttsx3
import random as rd
import socket
import serial

#my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#my_socket.connect(('192.168.118.254', 8080))


port="COM6"
baudrate=9600
#ser=serial.Serial(port,baudrate,timeout=0.5)

path="C:\\Users\\MSI\\Desktop\\img"

images=[]
classnames=[]
mylist=os.listdir(path)
print(mylist)
for cls in mylist:
    cimage=cv.imread(f'{path}/{cls}')
    images.append(cimage)
    classnames.append(os.path.splitext(cls)[0])
print(classnames)

def findencodings(images):
    encodelist = []
    for img in images:
        img=cv.cvtColor(img, cv.COLOR_BGR2RGB)
        encode=fr.face_encodings(img)[0]
        encodelist.append(encode)
    return encodelist


encodeListKnown=findencodings(images)
print("encoding complete")
video=cv.VideoCapture(0)
address="http://192.168.118.254:8080/video"
video.open(address)


while True:
    success,imgc=video.read()
    imgS=cv.resize(imgc,(0,0),None,0.25,0.25)
    imgS=cv.cvtColor(imgc, cv.COLOR_BGR2RGB)

    faceloccam=fr.face_locations(imgS)
    encodecam=fr.face_encodings(imgS,faceloccam)      #encode camera image and image face locations

   

    for encodeface,facelocation in zip(encodecam,faceloccam):
        matches=fr.compare_faces(encodeListKnown,encodeface)
        facedis=fr.face_distance(encodeListKnown,encodeface)        #encodeface = encodecam
        print(facedis)
        matchindex=np.argmin(facedis)           #elon,me  ryan,me   bezoz,me me,me

        if facedis[matchindex]:
            name=classnames[matchindex].upper()
            print(name)
            y1,x2,y2,x1=facelocation
            #y1,x2,y2,x1=y1*4,x2*4,y2*4,x1*4
            cv.rectangle(imgc,(x1,y1),(x2,y2),(0,255,0),2)
            cv.rectangle(imgc,(x1,y2-35),(x2,y2),(0,255,255),cv.FILLED)
            cv.putText(imgc,name,(x1+6,y2-6),cv.FONT_HERSHEY_PLAIN,1,(255,255,0),2)
            cv.putText(imgc,str("Face Detected"),(10,20),cv.FONT_HERSHEY_PLAIN,1,(255,0,0),2)
      
            
            
      
            
            
        print(ser.readline().decode(),end='')
        
        mes1=" Good Morning"
        mes2=name
        msg=mes1.encode()
       
        msg1=mes2.encode()
        msg2=mes2.encode()
        
        #msg2=mes2.encode()
        ser.write(msg1)
        ser.write(msg)
       
        #ser.write(msg2)
                




    cv.imshow("imagec",imgc)
    cv.waitKey(1)




    