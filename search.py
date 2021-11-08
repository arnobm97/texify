import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
img = cv2.imread('testing.png')
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

Q = input("Which letter do you want to find? : ")

#Detecting Characters

hImg,wImg,_ = img.shape
boxes = pytesseract.image_to_boxes(img)

search = []
result = []
count = 0

for b in boxes.splitlines():
    # print(b)
    b = b.split(' ')
    #print(b)
    x,y,w,h,= int(b[1]),int(b[2]),int(b[3]),int(b[4],)
    s = b[0]
    search.append(s)

print(search)

for i in range(len(search)):
    if search[i] == Q:
        result.append(search[i])
        count += 1
    # else:
    #     print("Your desired letter is not found")

print(result)
print("Your desired letter which is", Q , "is found", count , "times")

#     cv2.rectangle(img,(x,hImg-y),(w,hImg-h),(0,0,255),1)
#     cv2.putText(img,b[0],(x,hImg-y+20),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,255),1)
#
# cv2.imshow('Result',img)
# cv2.waitKey(0)