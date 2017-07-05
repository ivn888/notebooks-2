
To begin, a basic import of NumPy is made to make it available.  Generally, NumPy is imported and given the notation 'np'.  This isn't a rule, but if followed, it will just be easier for you to repurpose code obtained elsewhere.


```python
import numpy as np
```

We can construct a basic array using some very simple methods.  A small 2D array of sequential values can be constructed using 'arange' which produces numbers of a certain type in a certain range.  

**Definition :** arange([start,] stop[, step,], dtype=None)
**Type :** Function of numpy.core.multiarray module


```python
a = np.arange(9).reshape(3, 3)
print("Array ... \n{}".format(a))
```

    Array ... 
    [[0 1 2]
     [3 4 5]
     [6 7 8]]
    

A slightly more complex example entails constructing an array or random integers within a specified range of values with a prescribe array shape.  The random in NumPy is exploited and the Mersenne Twister random number generator.  There are a variety of distributions that can be created, and in this example random integers in the range 0 up to 10 are created with a shape of 9 rows and 12 columns.  RandomState is used to ensure that the same pattern is generated each time the array is created so that there is a random generations only once, then the values are fixed.


```python
# ---- construct a repeatable array of 2D integers with a shape of 9 rows by 12 columns. ----
import numpy as np
a = np.random.mtrand.RandomState(1).randint(0, 10, size=(9, 12))
print("2D array ... {} rows {} cols\n{}".format(*a.shape, a))
```

    2D array ... 9 rows 12 cols
    [[5 8 9 5 0 0 1 7 6 9 2 4]
     [5 2 4 2 4 7 7 9 1 7 0 6]
     [9 9 7 6 9 1 0 1 8 8 3 9]
     [8 7 3 6 5 1 9 3 4 8 1 4]
     [0 3 9 2 0 4 9 2 7 7 9 8]
     [6 9 3 7 7 4 5 9 3 6 8 0]
     [2 7 7 9 7 3 0 8 7 7 1 1]
     [3 0 8 6 4 5 6 2 5 7 8 4]
     [4 7 7 4 9 0 2 0 7 1 7 9]]
    
