import matplotlib.pyplot as plt
import numpy as np

a = np.array([0.313660827978, 0.365348418405, 0.423733120134,
              0.365348418405, 0.439599930621, 0.525083754405,
              0.423733120134, 0.525083754405, 0.651536351379]).reshape(3,3)

plt.imshow(a,interpolation="nearest",cmap="bone",origin="upper") # 亦可寫成cmap=plt.cm.bone。origin代表选择的原点的位置。

# interpolation 出图方式
# for the value of "interpolation", check this:
# http://matplotlib.org/examples/images_contours_and_fields/interpolation_methods.html
###
# for the value of "origin"= ['upper', 'lower'], check this:
# http://matplotlib.org/examples/pylab_examples/image_origin.html
###

plt.colorbar(shrink=0.92)

plt.xticks(())
plt.yticks(())

plt.show()