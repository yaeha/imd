#-*- coding: utf-8 -*-
#encoding=utf-8

import sys
import argparse
import os

import cv2
print(cv2.__version__)

def extractImage(sourceFile, target_path):

    if not os.path.isdir(target_path):
        os.mkdir(target_path)
    else:
        pass

    cap = cv2.VideoCapture(sourceFile)
    count = 0
    while(cap.isOpened()):
        # Capture frame-by-frame
        ret, frame = cap.read()

        if ret == True:
            print('read %d frame: ' % count, ret)
            cv2.imwrite(os.path.join(target_path, "frame{:d}.jpg".format(count)), frame)  # save frame as JPEG file
            count += 1
        else:
            break

    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()


def parse_arguments(argv):
    parser = argparse.ArgumentParser()

    parser.add_argument('source_video', type=str,
                        help='Path to the source video directory.')
    parser.add_argument('target_dir', type=str,
                        help='Path to the data directory to be saved.')

    return parser.parse_args(argv)

def main(args):
    # extractImage(args[1], args[2])
    # extractImage('C:/Users/dojinKim/Desktop/VisionRecog/dataset/IU_TV_Palette_Album_Making_01.mp4',
    #              'C:/Users/dojinKim/Desktop/VisionRecog/dataset/001')
    # print(args.source_video + ' ' + args.target_dir)
    extractImage(args.source_video, args.target_dir)

if __name__ == '__main__':
    main(parse_arguments(sys.argv[1:]))