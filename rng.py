from numpy.random import default_rng
from scipy.stats import genlogistic
import plotly.express as px
import numpy as np

###

size = 500
c = 0.4

###

rng = default_rng()

x = np.linspace(genlogistic.ppf(0.01, c),
                genlogistic.ppf(0.99, c), size)
y = 2*rng.random(size)
z = 2*rng.random(size)

###

print (len(x),len(y), len(z))

fix = px.scatter_3d(x = x, y = y, z = z)
fix.show()