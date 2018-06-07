from matplotlib.pyplot import scatter, show, plot
import numpy

x = numpy.array([1, 2, 3, 4, 5])
y = [1, 4, 9, 16, 25]
z = x*2

plot(x, z)
plot(x, y)

show()