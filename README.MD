# Blur-vs-Resnet
### Contributors: Jessica Huang & Diane Park

Summary: We aim to investigate the impacts that blurred training data have on a Resnet50's classification accuracy.
We initially use transfer learning to train our ResNet50 model for 20 epochs on the Stanford Dogs Dataset. We also use the same images with gaussian and median blur to train our model. 
We observe the impacts that this has on how the model is able to classify blurred AND unblurred images. 

More detail here: [final paper]

## To use our code:

FILE PATHING WILL BE DIFFERENT IF NOT RUN FROM THE CS SERVER FROM "/cs/cs153/projects/diane-jessica". CHANGE PATHING ACCORDINGLY.

We have two directories: "data" & "resnet" 

### Data

Our data directory holds many subdirectories and also a "split_creation.py" file.

The "split_creation.py" file contains functions to create our blurred training and validation splits.
In order to use this file:

First, create a copy of the "Images" subdirectory which contains the original images from the Stanford Dogs Dataset, already separated into a 80/10/10 train/val/test split. (If downloading a new dataset without pre-made splits, the "make_splits()" function can do that for you)

Second, run either the gaussian_blur_images() or median_blur_images() on the copy of "Images" to blur all of the images. Alter the kernel size as needed. 

Lastly, to create a subdirectory with blurred training set and unblurred validation set, copy and paste directly from the original "Images" subdirectory.


### Resnet

Our Resnet holds our "resnet50.py" file which does most of our heavy lifting.

Simply running the file in ipython will begin the training and validating process. 
To change which data directory you're using or number of training epochs, make adjustments to the code past line 295 according to instructions in the comments. 

Accuracies per epoch will appear in the terminal as training occurs.
  
