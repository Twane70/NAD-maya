import nibabel as nib
import matplotlib.pyplot as plt
import os

img = nib.load("scan_example_files/structures_HIGH_RES.nii")

data = img.get_fdata()
data = (data - data.min()) / (data.max() - data.min())
print(f"Data shape: {data.shape}")

# visualize the middle slice of a given time point
time_point = 0  # change this index to view different time points
middle_slice_index = data.shape[2] // 2

plt.figure(figsize=(10, 5))
plt.imshow(data[:, :, middle_slice_index], cmap='gray')
plt.title(f'Middle Slice of Volume at Time Point {time_point}')
plt.axis('off')
plt.colorbar()
plt.show()