import numpy
import matplotlib.pyplot as plt

x = numpy.random.normal(100.0, 1.0, 100000)

plt.hist(x, 100)
plt.show()