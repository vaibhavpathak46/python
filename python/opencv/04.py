import cv2

# create a cascadeclassifier object
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# reading the image
img = cv2.imread(r"C:\Users\vaibh\OneDrive\Pictures\New folder\86752.jpg")

# reading the image as gray scale image
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# search the co-ordinates of image
faces = face_cascade.detectMultiScale(gray_img, scaleFactor=1.05, minNeighbors=5)

print(type(faces))
print(faces)

for x, y, w, h in faces:
    img = cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 3)

resized = cv2.resize(img, (int(img.shape[1]), int(img.shape[0])))
cv2.imshow("Gray", resized)
cv2.waitKey(0)
cv2.destroyAllWindows()
