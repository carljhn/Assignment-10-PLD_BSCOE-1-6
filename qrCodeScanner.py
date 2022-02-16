# Assignment 10

# Contact Tracing App
# 	- Create a python program that will read QRCode using your webcam
# 	- You may use any online QRCode generator to create QRCode
# 	- All personal data are in QRCode 
# 	- You may decide which personal data to include
# 	- All data read from QRCode should be stored in a text file including the date and time it was read

# Note: 
# 	- Search how to generate QRCode
# 	- Search how to read QRCode using webcam
# 	- Search how to create and write to text file
# 	- Your source code should be in github before Feb 19
# 	- Create a demo of your program (1-2 min) and send it directly to my messenger.

#import the modules to be used:
import cv2
import webbrowser
import datetime

capture=cv2.VideoCapture(0)
detect=cv2.QRCodeDetector()
time_date=datetime.datetime.now()

while True: 
    _, img=capture.read()

    data, BBOX, _=detect.detectAndDecode(img)

    if data: 
        d=data
        qr_data=open("QRData.txt", "w")
        qr_data.write("Result: ")
        qr_data.write("\n")
        qr_data.write("" +str(d))
        qr_data.write("\n")
        qr_data.write("Date and Time: " +str(time_date))
        break

    cv2.imshow("qrcode_scanner", img)
    if cv2.waitKey(1)==ord("q"):
        break

b=webbrowser.open(str(d))
capture.release()
cv2.destroyAllWindows()