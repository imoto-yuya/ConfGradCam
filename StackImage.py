import cv2
import glob
import os
import re
import shutil
import matplotlib.pyplot as plt
import numpy as np

imgDirPath = '/Users/yuya/Downloads/cam23456_block5_conv3_test/'
fileNamePattern = re.compile(r'\d+_\d+_cam_L(\d)_P(\d).jpg')

imgShape = [256, 256, 3]
# cv2.imshow('imgArray', imgArray)

for filePath in glob.glob(imgDirPath + '*'):
    if os.path.isdir(filePath):
        # print(filePath)
        imgArray = np.zeros(imgShape, np.int)
        aveImg = np.zeros(imgShape, np.uint8)
        sumBrightness = 0
        counter = 0
        brightnessHistArray = [0 for _ in range(256)]
        # 画像1枚ずつ処理する
        for filePath2 in glob.glob(filePath + '/*'):
            # print(filePath2)
            img = cv2.imread(filePath2)
            for width in range(imgShape[0]):
                for height in range(imgShape[1]):
                    for pixel in range(imgShape[2]):
                        imgArray[width][height][pixel] += int(img[width][height][pixel])
                    brightness = 0.114*int(img[width][height][0]) + 0.587*int(img[width][height][1]) + 0.299*int(img[width][height][2])
                    sumBrightness += brightness
                    brightnessHistArray[int(brightness)] += 1
            counter += 1
        print(os.path.basename(filePath), sumBrightness/256/256/counter)
        for width in range(imgShape[0]):
            for height in range(imgShape[1]):
                for pixel in range(imgShape[2]):
                    aveImg[width][height][pixel] = np.uint8(imgArray[width][height][pixel]/counter)
        cv2.imwrite(filePath + '.png', aveImg)
        brightnessHistRange = range(len(brightnessHistArray))
        for index in brightnessHistRange:
            brightnessHistArray[index] /= counter
        plt.plot(brightnessHistRange, brightnessHistArray)
        plt.savefig(filePath + '_hist.png')
        plt.close()
        
