import cv2 as cv
import pickle
import cvzone
import numpy as np
import tensorflow as tf

new_model = tf.keras.models.load_model('staticfiles/CNN/saved_model/my_model.h5')
# vcap = cv.imread('test_images/20220616_094946.png')

# frame = vcap

with open('staticfiles/CNN/CarParkPos', 'rb') as f:
    posList = pickle.load(f)

import pandas as pd
xy = pd.read_csv("staticfiles/CNN/coordenadassvg.csv", sep=" ", header=None).rename(columns={0:"x", 1:"y"})
a = xy.values.tolist()


def mkprediction():
    vcap = cv.VideoCapture(
        "rtsp://teste:teste123@10.22.22.50:554/cam/realmonitor?channel=1&subtype=0")
    ret, frame = vcap.read()
    predresult = []
    for count, pos in enumerate(posList):
        coordinates = np.array(pos)
        # coordinates.append(pos)
        coordinatesarray = np.array(coordinates)
        pts_dst = np.array([[0, 0], [32, 0], [32, 32], [0, 32]])
        h, status = cv.findHomography(coordinatesarray, pts_dst)
        im_out = cv.warpPerspective(frame, h, (32, 32))
        rect = cv.boundingRect(coordinates)
        imgCrop = frame[rect[1]: rect[1] + rect[3], rect[0]: rect[0] + rect[2]]
        inter = cv.INTER_AREA
        resized = cv.resize(imgCrop, (32, 32), interpolation=inter)
        res = im_out.reshape(1, 32, 32, 3)
        result = new_model.predict(res)
        # cv.imshow(str(rect[1]), im_out)
        #cvzone.putTextRect(frame, str(np.argmax(result)),(rect[0], rect[1] + rect[3]), 1, 1,)
        predresult.append([a[count], (np.argmax(result))])
    return predresult
