import matplotlib.pyplot as plt
import numpy

f = lambda x, r: r * x * (1 - x)

ys = []
rs = numpy.linspace(2.5, 4, 800)

# Loop thorough r in rs
for r in rs:
    x = 0.5
    # As we wish to see quite many iterations. However, we do not
    # want to see all of the points as the important picture
    # is seen as x -> infinity
    for i in range(1000):
        x = f(x, r)

    # This is the important, visible part
    for i in range(500):
        x = f(x, r)
        # Save the point (r, x) in the list ys
        ys.append([r, x])

# ys is a list of lists.
# It could be thought as pairs of values - points.
# Function below converts ys into array of n times 2 size
ys = numpy.array(ys)

# ys[:,0] is a 1D array of r values (: means 'whatever what')
# ys[:, 1] is a 1D array of x values
# This draws a scatter plot of (r, x) points.
plt.plot(ys[:, 0], ys[:, 1], '.')
plt.axis([2.5, 4, 0, 1])
plt.show()