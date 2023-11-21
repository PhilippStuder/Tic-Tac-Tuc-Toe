import numpy as np

# Given array
arr = [ 0,  0,  0, -1, -1, -1,  0, -1,  0, -1,  1,  1,  1,  1,  0,  0,  0, -1,
  0,  0,  1,  1,  0,  0, -1,  0,  0, -1,  0,  0, -1,  1,  0, -1,  0,  1,
  0,  0,  1,  0,  0,  0,  0,  0, -1,  1,  0,  0,  0,  1,  0,  0,  0, -1,
 -1,  1, -1,  1,  1,  1,  1, -1,  1, -1,]

# Reshape the array to 4x4x4
arr_4x4x4 = np.addarray(arr).reshape(4, 4, 4)

print(arr_4x4x4)