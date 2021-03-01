
import numpy as np
import open3d as o3d
from matplotlib import pyplot as plt


def read_depth_image(filename, im_size):
	# print(type(filename))
	A = np.fromfile(filename, dtype='float32', sep="")
	A = A.reshape(im_size)

	# print(A.shape[0])
	img = np.zeros((im_size[0], im_size[2], im_size[1]), dtype=float)
	for ch in range(A.shape[0]):
		img_data = A[ch, :, :]
		img[ch, :, :] = img_data.transpose()

	return img

def read_gt_image(filename, im_size):
	# print(type(filename))
	A = np.fromfile(filename, dtype='float32', sep="")
	A = A.reshape(im_size)

	img = A.transpose()

	return img

def read_mask_image(filename, im_size):
	# print(type(filename))
	A = np.fromfile(filename, dtype='float32', sep="")
	A = A.reshape(im_size)

	img = A.transpose()
	img = (img != 0)

	return img



if __name__ == "__main__":

	######################
	##  Read Bin Files  ##
	######################
	train_fname = './training/train/00019_05.bin'
	gt_fnames = train_fname.replace("/train/", "/gt/")
	mask_fnames = train_fname.replace("/train/", "/mask/")

	image = read_depth_image(train_fname, [5, 512, 64])
	gt_image = read_depth_image(gt_fnames, [5, 512, 64])
	mask_image = read_mask_image(mask_fnames, [1, 512, 64])

	
	######################
	## 2D Visualization ##
	######################
	## 5 channels: Depth, X, Y, Z, Intensity
	img_d = image[0,:,:]
	img_d_gt = gt_image[0,:,:]

	# plt.figure(1)
	plt.figure(num='2D Visualization')
	plt.subplot(511)
	plt.imshow(image[0,:,:])
	# plt.axis('off')
	plt.ylabel('Depth')
	plt.yticks([])
	plt.xticks([])

	plt.subplot(512)
	plt.imshow(image[1,:,:])
	# plt.axis('off')
	plt.ylabel('X')
	plt.yticks([])
	plt.xticks([])

	plt.subplot(513)
	plt.imshow(image[2,:,:])
	# plt.axis('off')
	plt.ylabel('Y')
	plt.yticks([])
	plt.xticks([])

	plt.subplot(514)
	plt.imshow(image[3,:,:])
	plt.ylabel('Z')
	# plt.axis('off')
	plt.yticks([])
	plt.xticks([])

	plt.subplot(515)
	plt.imshow(image[4,:,:])
	# plt.axis('off')
	plt.ylabel('Intensity')
	plt.yticks([])
	plt.xticks([])
	plt.show()

	######################
	## 3D Visualization ##
	######################
	x = image[1,:,:].reshape(1,-1)
	y = image[2,:,:].reshape(1,-1)
	z = image[3,:,:].reshape(1,-1)

	x_gt = gt_image[1,:,:].reshape(1,-1)
	y_gt = gt_image[2,:,:].reshape(1,-1)
	z_gt = gt_image[3,:,:].reshape(1,-1)

	xyz = np.concatenate((x,y,z)).transpose()
	pcd = o3d.geometry.PointCloud()
	pcd.points = o3d.utility.Vector3dVector(xyz[:,:3])
	o3d.visualization.draw_geometries([pcd], window_name='3D Object-visible Scene')

	xyz_gt = np.concatenate((x_gt,y_gt,z_gt)).transpose()
	pcd = o3d.geometry.PointCloud()
	pcd.points = o3d.utility.Vector3dVector(xyz_gt[:,:3])
	o3d.visualization.draw_geometries([pcd], window_name='3D Static Background Scene')


