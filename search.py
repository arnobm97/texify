import cv2
import pytesseract
import os

targetfile = input('Enter the filename accurately with extension: ')
if os.path.isfile(targetfile) == True:
    print("found")
else:
    print("There are no files named", targetfile , "in this directory")
    print("Please enter a valid file with extension. e.g texify.png")
    quit()
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
img = cv2.imread(targetfile)
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

R = input("Type 1 for Letter and 2 for Word : ")

if R=="1":
    print ("Letter")

    Q = input("Which letter do you want to find? (Case Sensitive) : ")
    hImg, wImg, _ = img.shape
    boxes = pytesseract.image_to_boxes(img)

    search = []
    result = []
    count = 0
    sCount = 0

    for b in boxes.splitlines():
        s = b[0]
        search.append(s)
        sCount += 1

    for i in range(len(search)):
        if search[i] == Q:
            result.append(search[i])
            count += 1

    print(result)
    print("Your desired letter which is", Q, "is found", count, "times")

    for b in boxes.splitlines():
        if (b[0] == Q):
            b = b.split(' ')
            x, y, w, h = int(b[1]), int(b[2]), int(b[3]), int(b[4])
            cv2.rectangle(img, (x, hImg - y), (w, hImg - h), (0, 0, 255), 1)
            cv2.putText(img, b[0], (x, hImg - y + 20), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 255), 1)

    cv2.imshow('Result', img)
    cv2.waitKey(0)
    exit(0)
elif R=="2":
    print ("Word")
    L = input("Which word do you want to find? (Case Sensitive) : ")

    hImg, wImg, _ = img.shape
    boxes = pytesseract.image_to_data(img)

    for o, b in enumerate(boxes.splitlines()):
        if o != 0:
            print(b)
            b = b.split()
            print(b)
            if len(b) == 12:
                if b[11] == L:
                    x, y, w, h = int(b[6]), int(b[7]), int(b[8]), int(b[9])
                    cv2.rectangle(img, (x, y), (w + x, h + y), (0, 0, 255), 1)
                    cv2.putText(img, b[11], (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 255), 1)

    cv2.imshow('Result', img)
    cv2.waitKey(0)
    exit(0)