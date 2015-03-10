import numpy


def fs(x, r):
    """Function mapping in single precision"""
    x = numpy.float32(x)
    r = numpy.float32(r)
    return r * x * (numpy.float32(1) - x)


def fd(x, r):
    """Function mapping in double precision"""
    x = numpy.float64(x)
    r = numpy.float64(r)
    return r * x * (numpy.float64(1) - x)


yss = []  # Single precision pairs
ysd = []  # Double precision pairs
rs = numpy.linspace(3.75, 3.8, 10)

rss = rs.astype(numpy.float32)  # Casting linear space array into single...
rsd = rs.astype(numpy.float64)  # ... and double precision as well.

for r in rss:  # For each r iterate 1k times in floats
    x = 0.5
    for i in range(1000):
        x = fs(x, r)
    yss.append([r, x])

yss = numpy.array(yss)

print(yss)

for r in rsd:  # For each r iterate 1k times in doubles
    x = 0.5
    for i in range(1000):
        x = fd(x, r)
    ysd.append([r, x])

ysd = numpy.array(ysd)
print(ysd)

diff = numpy.subtract(yss[:, 1], ysd[:, 1])  # Find difference

print(diff)