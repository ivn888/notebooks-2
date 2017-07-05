
# coding: utf-8
"""
To begin, a basic import of NumPy is made to make it available.  Generally, NumPy is imported and given the notation 'np'.
This isn't a rule, but if followed, it will just be easier for you to repurpose code obtained elsewhere.
"""
# In[1]:

import numpy as np

"""
 We can construct a basic array using some very simple methods.  A small 2D array of sequential values can be constructed
 using 'arange' which produces numbers of a certain type in a certain range.   
 **Definition :** arange([start,] stop[, step,], dtype=None)
 **Type :** Function of numpy.core.multiarray module
"""
# In[2]:

a = np.arange(9).reshape(3, 3)
print("Array ... \n{}".format(a))

"""
A slightly more complex example entails constructing an array or random integers within a specified range of values
with a prescribe array shape.  The random in NumPy is exploited and the Mersenne Twister random number generator.  
There are a variety of distributions that can be created, and in this example random integers in the range 0 up to 10 are 
created with a shape of 9 rows and 12 columns.  RandomState is used to ensure that the same pattern is generated each time 
the array is created so that there is a random generations only once, then the values are fixed.
"""
# In[3]:

# ---- construct a repeatable array of 2D integers with a shape of 9 rows by 12 columns. ----
import numpy as np
a = np.random.mtrand.RandomState(1).randint(0, 10, size=(9, 12))
print("2D array ... {} rows {} cols\n{}".format(*a.shape, a))

# We can make a 'map' from a 2D array using MatPlotLib. Two variants are produced by reshaping 256 sequential integers 
# into a 16x16 array (map).  An RGB image is produced from the 3 'bands' of information and 'stacked together 
# 

# In[4]:


# num_92 gray scale image from rgb
def num_92():
    """num_92... gray-scale image from rgb
    :Essentially gray = 0.2989 * r + 0.5870 * g + 0.1140 * b
    : http://stackoverflow.com/questions/12201577/how-can-i-convert
    :       -an-rgb-image-into-grayscale-in-python
    : https://en.m.wikipedia.org/wiki/Grayscale#Converting_color_to_grayscale
    : see https://en.m.wikipedia.org/wiki/HSL_and_HSV
    """
    import numpy as np
    import matplotlib.pyplot as plt
    a = np.arange(256).reshape(16, 16)
    b = a[::-1]
    c = np.ones_like(a)*128
    rgb = np.dstack((a, b, c))
    gray = np.dot(rgb[..., :3], [0.2989, 0.5870, 0.1140])
    plt.imshow(gray, cmap=plt.get_cmap('gray'))
    plt.show()
    plt.imshow(rgb, cmap=plt.get_cmap('spectral'))
    plt.show()

# ----- Call the function ----
num_92() # produce the gray image

# That is just some of the basics you can do with the packages that are available to you through numpy and ArcMap and ArcGIS Pro.
