import os

# Prepare dataset
os.system("python ./prepare_dataset.py --inputs_dir ../data/ImageNet/original --output_dir ../data/ImageNet/SRGAN --image_size 96")

# Split train and valid
os.system("python ./split_train_valid_dataset.py --inputs_dir ../data/ImageNet/SRGAN --valid_samples_ratio 0.1")

# Create LMDB database file
os.system("python ./create_lmdb_dataset.py --inputs_dir ../data/ImageNet/SRGAN/train --lmdb_path ../data/train_lmdb/SRGAN/ImageNet_HR_lmdb --upscale_factor 1")
os.system("python ./create_lmdb_dataset.py --inputs_dir ../data/ImageNet/SRGAN/train --lmdb_path ../data/train_lmdb/SRGAN/ImageNet_LRbicx4_lmdb --upscale_factor 4")

os.system("python ./create_lmdb_dataset.py --inputs_dir ../data/ImageNet/SRGAN/valid --lmdb_path ../data/valid_lmdb/SRGAN/ImageNet_HR_lmdb --upscale_factor 1")
os.system("python ./create_lmdb_dataset.py --inputs_dir ../data/ImageNet/SRGAN/valid --lmdb_path ../data/valid_lmdb/SRGAN/ImageNet_LRbicx4_lmdb --upscale_factor 4")
