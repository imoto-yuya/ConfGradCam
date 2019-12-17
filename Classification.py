import glob
import os
import re
import shutil

imgDirPath = '/Users/yuya/Downloads/cam23456_block5_conv3_test/'
fileNamePattern = re.compile(r'\d+_\d+_cam_L(\d)_P(\d).jpg')

for filePath in glob.glob(imgDirPath + '*'):
    fileName = os.path.split(filePath)[1]
    fileNameMatch = fileNamePattern.search(fileName)
    if fileNameMatch:
        fileNameGroups = fileNameMatch.groups()
        # print(fileName, fileNameGroups[0], fileNameGroups[1])
        dirPath = imgDirPath
        classID = fileNameGroups[1]
        if fileNameGroups[0] == fileNameGroups[1]:
            dirPath += 'L' + classID + 'P' + classID + '/'
        else:
            dirPath += 'L*P' + classID + '/'
        if not os.path.exists(dirPath):
            os.makedirs(dirPath)
        if not os.path.exists(dirPath + fileName):
            shutil.copy(filePath, dirPath)
    else:
        print('error')
        print(fileName)
        exit()