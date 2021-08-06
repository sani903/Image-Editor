import cv2 as cv
import sys
import os
import argparse
import numpy as np

parser = argparse.ArgumentParser(description='Load an image. Press Q to quit, R to draw with red, G to draw with green B to draw with blue')
parser.add_argument('image', metavar='image.jpg', nargs=1,
                    help='image to be edited')
parser.add_argument('-d', '-dimensions', metavar='', type=int, nargs=2,
                    help='custom dimensions of image, 2 values required')

args = parser.parse_args()
parent = cv.imread(sys.argv[1])
if parent is None:
    if len(sys.argv) < 3:
        img = np.ones([500 , 500, 3], dtype='uint8')
        img = img * 255
    else:
        a = sys.argv[3]
        b = sys.argv[4]
        img = np.ones([int(a), int(b), 3], dtype='uint8')
        img = img * 255
    cv.imshow('Image', img)
else:
    if len(sys.argv) < 3:
        img = parent
    else:
        a = sys.argv[3]
        b = sys.argv[4]
        img = cv.resize(parent, (int(a), int(b)), interpolation=cv.INTER_CUBIC)
    cv.imshow('Image', img)

print("Default color selected: Red")
color = 1


def main():
    while True:
        global color
        cv.setMouseCallback('Image', click_event)
        k = cv.waitKey(0) & 0xFF
        if k == ord('r'):
            color = 1
            print('Red')
        if k == ord('g'):
            color = 2
            print('Green')
        if k == ord('b'):
            color = 3
            print('Blue')
        if k == ord('q'):  # you can put any key here
            cv.destroyAllWindows()
            break


def click_event(event, x, y, flags, params):
    if event == cv.EVENT_LBUTTONDOWN:
        if color == 1:
            cv.circle(img, (x, y), 10, (0, 0, 255), thickness=-1)
        if color == 2:
            cv.circle(img, (x, y), 10, (0, 255, 0), thickness=-1)
        if color == 3:
            cv.circle(img, (x, y), 10, (255, 0, 0), thickness=-1)
        cv.imshow('Image', img)


main()
