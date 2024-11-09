import cv2
import os
import time
import uuid
IMAGES_PATH='Tensorflow/workspace/images/collectedimages'
labels=['नमस्कार','नहीं','भाई','भैंस','सोचना','ठीक है','धन्यवाद','सूर्य']
number_imgs=15
for label in labels:
    os.makedirs(os.path.join(IMAGES_PATH, label), exist_ok=True)
    cap = cv2.VideoCapture(0)
    print('Collecting images for{}'.format(label))
    time.sleep(5)
    for imgnum in range(number_imgs):
        ret, frame = cap.read()
    imgname = os.path.join(IMAGES_PATH, label, '{}_{}.jpg'.format(label, imgnum))
    cv2.imwrite(imgname, frame)
    cv2.imshow('frame', frame)
    time.sleep(2)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    
    cap.release()
import cv2
import os
import time
import uuid

IMAGES_PATH = 'Tensorflow/workspace/images/collectedimages'
labels = ['नमस्कार', 'नहीं', 'भाई', 'भैंस', 'सोचना', 'ठीक है', 'धन्यवाद', 'सूर्य']
number_imgs = 15

for label in labels:
    os.makedirs(os.path.join(IMAGES_PATH, label), exist_ok=True)
    cap = cv2.VideoCapture(0)
    print('Collecting images for {}'.format(label))
    time.sleep(5)
    
    for imgnum in range(number_imgs):
        ret, frame = cap.read()
        if not ret:
            print("Failed to capture image")
            continue
        
        imgname = os.path.join(IMAGES_PATH, label, '{}_{}.jpg'.format(label, imgnum))
        cv2.imwrite(imgname, frame)
        print("Image saved:", imgname)
        cv2.imshow('frame', frame)
        time.sleep(2)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    cap.release()
    cv2.destroyAllWindows()
