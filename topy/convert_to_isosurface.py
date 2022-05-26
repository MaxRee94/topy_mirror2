import os
from sys import argv
import numpy as np
import mcubes

# voldata_file = argv[1]
# if not os.path.exists(argv[1]):
#     print("file", argv[1], "does not exist. Aborting iso conversion.")

#X, Y, Z = np.mgrid[:6, :6, :6]
#u = (X-3)**2 + (Y-3)**2 + (Z-3)**2 - 2**2

voldata_file = r"E:\Development\Generative_Design_Research\topy\iterations\mbb_beam_3d_exp_gsf_050.npy"

#print("u:\n", u)
#exit()

voldata = np.load(voldata_file)
voldata = np.pad(voldata, 1, mode="constant")
voldata = voldata * -100 + 100

# Extract the 0-isosurface
vertices, triangles = mcubes.marching_cubes(voldata, 50)

# Export the result to sphere.dae
mcubes.export_mesh(
    vertices, 
    triangles, 
    r"E:/Development/Generative_Design_Research/topy/iterations/" + os.path.basename(voldata_file).replace(".npy", ".dae"), 
    "Test"
)

print("exported to : ", r"E:/Development/Generative_Design_Research/topy/iterations/{}".format(os.path.basename(voldata_file).replace(".npy", ".dae")))
