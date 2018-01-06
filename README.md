# 484_project

The repository has three folders. First folder is position_and_orientation_learning which is a ros package that has the modified gazebo launch files in “launch”  and kinect snapshot code in “src”. Second is the snapshots folder where all the data is located. The final data collection I did is located in pcd_png_372/9862, and the processed images are located in reduced_png. The folder also has the codes for auto generating data, processing the images, and converting pcd into png formats. The third folder in the project is called “training” and has everything related to tensorflow learning. The processed images from the data folder are copied here and sorted according to their orientation between 0 and 1.4 radians. Also it includes the label.txt folder which lists the names of all the categories. The folder also includes the following:
Output folder: for saving and restoring tensorboard graph. 
Resized_image folder: copies of the data set but in JEPG format and different labelling.
Build_image_data.py: for creating tfrecord from the data and the labels.
Dir_traversal_tfrecord: for locating and traversing tfrecord files.
Read_tfrecord.py: for recreating the JPEG images with the new lable and saving it in “resized image” folder.
Orientation_train_cnn.py: for training and evaluating the neural network using tensorflow.
