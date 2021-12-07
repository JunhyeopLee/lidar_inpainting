# LiDAR Inpainting Dataset
This dataset is generated based on <a href="http://www.cvlibs.net/datasets/kitti/index.php" target="_blank">KITTI</a> dataset.  
This dataset is published under the <a href="https://creativecommons.org/licenses/by-nc-sa/3.0/" target="_blank">Creative Commons Attribution-NonCommercial-ShareAlike 3.0 License</a> following the KITTI.


## Download Link
You can download our dataset through below **link**.
https://drive.google.com/file/d/1ll5WiriTP6izHhhS0J5O1QR4MbuLP4nz/view?usp=sharing


## Dataset Folder Structure
This LiDAR inpainting dataset contains 3 folders and bin files are stored in each folder.
Each bin file has 512 width and 64 height.
Bin files in ```train``` and ```gt``` folder have 5 channels: depth, x, y, z, intensity.
And mask bin files has only one channel, which is zero or one.

```bash
├── dataset
    ├── training
    │   ├── train
    │   │   ├── *.bin
    │   ├── gt
    │   │   ├── *.bin
    │   └── mask
    │       └── *.bin
    └── testing
        ├── train
        │   ├── *.bin
        ├── gt
        │   ├── *.bin
        └── mask
            └── *.bin
```


## How to read LiDAR Inpainting dataset
Please loacate this file into the dataset folder to execute viewer example file with below command.
```
python dataloader_example.py
```


## Info
Our paper will be published soon with the detailed information on this dataset.

For more information about this dataset, please send an email to us.
-- mvp.research.yonsei@gmail.com


## Citation

@article{lee2021sam,
  title={SAM-Net: LiDAR Depth Inpainting for 3D Static Map Generation},
  author={Lee, Junhyeop and Hwang, Sangwon and Kim, Woo Jin and Lee, Sangyoun},
  journal={IEEE Transactions on Intelligent Transportation Systems},
  year={2021},
  publisher={IEEE}
}

