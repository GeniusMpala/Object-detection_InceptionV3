from threading import local
import numpy as np
import tensorflow as tf
from tensorflow.keras import layers
from tensorflow.keras.optimizers import RMSprop
from tensorflow.keras import Model
import os
import shutil
import cv2


import cv2
import numpy as np
import os
from Model import *
import shutil



def extract_frames(vid_path, outputpath):
    # set video file path of input video with name and extension
    vid = cv2.VideoCapture(vid_path)


    if not os.path.exists('images'):
        os.makedirs('images')
    else:
        shutil.rmtree('images')
        os.makedirs('images')
    #identify frame
    index = 0
    while(True):
        
        # Extract images
        ret, frame = vid.read()
        # end of frames
        if not ret: 
            break
        # Saves images
        name = outputpath+'/frame' + str(index) + '.jpg'
        # print ('Creating... ' + name)
        cv2.imwrite(name, frame)

        # next frame
        index += 1
    vid.release()

def label_frames(inputpath, outputpath, videoFile):

    if not os.path.exists('encoded_images'):
        os.makedirs('encoded_images')
    else:
        shutil.rmtree('encoded_images')
        os.makedirs('encoded_images')

    count = 0
    cap = cv2.VideoCapture(videoFile)   # capturing the video from the given path
    frameRate = cap.get(5) #frame rate
    font_scale = 3
    font = cv2.FONT_HERSHEY_PLAIN
    obj_detected = []


    while(cap.isOpened()):
        ret, frame = cap.read()
        if (ret != True):
            break
        filename =inputpath+"/frame"+str(count)+".jpg"
        p = tf.keras.applications.imagenet_utils.decode_predictions(identify_frames(filename))
        label = p[0][0][1]
        threshold = p[0][0][2]
        if threshold >= 0.5:
            if (label not in obj_detected):
                obj_detected.append(label)
            cv2.putText(frame, "[*Object Detected] : "+str(label), (25, 60), font, fontScale=font_scale,color=(0,255,0), thickness=3)
            print ('Enconded... ' + str(label) + "... " + str(count))
        cv2.imwrite(outputpath+ str(label) + " " + str(count)+".jpg", frame)
        count += 1
    cap.release()
    print ("[**Frame Encoding] - Done")


def build_video(inputpath,outputpath,fps):
    if not os.path.exists('videos'):
        os.makedirs('videos')
    else:
        shutil.rmtree('videos')
        os.makedirs('videos')

    image_array = []
    files = [f for f in os.listdir(inputpath) if os.path.isfile(os.path.join(inputpath, f))]
    files.sort(key = lambda x: int(x.split()[1][:-4]))

    
    for i in range(len(files)):
        img = cv2.imread(inputpath + files[i])
      
        size = (img.shape[1], img.shape[1])
        img  = cv2.resize(img,size)
        image_array.append(img)
       
        

    fourcc = cv2.VideoWriter_fourcc(*'X264')
    out  =cv2.VideoWriter(outputpath, fourcc, fps, (224,224), True)

    for i in range(len(image_array)):
        out.write(image_array[i])
        return out

    out.release()