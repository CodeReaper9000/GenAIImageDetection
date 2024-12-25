1) download.py was used to download specific images from source for real camera images
2) extract_ela.py was used to extract the ela map and save them for real and ai images
3) ela_tester.h5 is final model for now


Dataset
Midjourney from GenImage dataset
Selected images from VISION dataset

ELA extracted and resized and stored for training, testing

for tensorflow
https://youtu.be/QUjtDIalh0k?si=Li5YYUX98S6x5kwU
1. conda create -n py37 python=3.7
2. conda activate py37
3. conda install -c conda-forge cudatoolkit=11.2 cudnn=8.1.0
4. python -m pip install "tensorflow"
5. Test GPU
   import tensorflow as tf
   tf.config.list_physical_devices('GPU')
   tf.test.is_gpu_available()
