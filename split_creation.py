import os
import json
import cv2
import csv
import urllib
import pdb
import numpy as np 

# this variable should only change if no longer using the stanford dogs dataset
origin_data = "/cs/cs153/projects/diane-jessica/data/Images"

# change depending on what new folder you create (as described in the README)
gaussian_images = "/cs/cs153/projects/diane-jessica/data/gaussian_images"
median_images = "/cs/cs153/projects/diane-jessica/data/median11_images"

def make_splits(data = origin_data):
    """
    Takes a folder containing subdirectories with images for each class.
    Creates a 80/10/10 train/val/test split directories, each with subdirectories for each class
    """

    for __, dirs,__ in os.walk(data):
        for dir in dirs:
            if (dir[0] == "n"):
                for __,__,files in os.walk(data + "/" + dir):
                    class_size = len(files)
                    count = 0
                    for file in files:
                        if count < class_size//10:
                            if not os.path.exists(data+'/test/'+dir):
                                os.mkdir(data+'/test/'+dir)
                            os.rename(data+'/'+dir+'/'+file, data+'/test/'+dir+'/'+file)
                        elif count < class_size//5:
                            if not os.path.exists(data+'/val/'+dir):
                                os.mkdir(data+'/val/'+dir)
                            os.rename(data+'/'+dir+'/'+file, data+'/val/'+dir+'/'+file)
                        else:
                            if not os.path.exists(data+'/train/'+dir):
                                os.mkdir(data+'/train/'+dir)
                            os.rename(data+'/'+dir+'/'+file, data+'/train/'+dir+'/'+file)
                        
                        count += 1
                        

def gaussian_blur_images(data = gaussian_images, kernel_size):
    """
    Given a copy of the "Images" directory of unblurred images,
    applies the default cv2 gaussian blur with specified kernel size on all images.
    """
    for __, dirs,__ in os.walk(data):
        for dir in dirs:
            for _,subdirs,_ in os.walk(data + "/" + dir):
                for subdir in subdirs:
                    for __,__,files in os.walk(data + '/' + dir + "/" + subdir):
                        for file in files:
                            im_path = os.path.join(data, dir, subdir, file)

                            image = cv2.imread(im_path) 
                            
                            # Gaussian Blur 
                            Gaussian = cv2.GaussianBlur(image, (kernel_size, kernel_size), 0) 
                                   
                            os.remove(im_path)
                            cv2.imwrite(im_path, Gaussian)
    


def median_blur_images(data = median_images, kernel_size):
    """
    Given a copy of the "Images" directory of unblurred images,
    applies the default cv2 median blur with specified kernel size on all images.
    """
    for __, dirs,__ in os.walk(data):
        for dir in dirs:
            for _,subdirs,_ in os.walk(data + "/" + dir):
                for subdir in subdirs:
                    for __,__,files in os.walk(data + '/' + dir + "/" + subdir):
                        for file in files:
                            im_path = os.path.join(data, dir, subdir, file)

                            image = cv2.imread(im_path) 
                            
                            # Median Blur 
                            Median = cv2.medianBlur(image, kernel_size) 
                                   
                            os.remove(im_path)
                            cv2.imwrite(im_path, Median)
