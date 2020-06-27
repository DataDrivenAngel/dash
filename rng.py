from numpy.random import default_rng
from scipy.stats import genlogistic
import plotly.express as px

size = 500
rng = default_rng()

x = genlogistic.stats(,)
y = 2*rng.random(size)
z = 2*rng.random(size)


fix = px.scatter_3d(x = x, y=y, z=z)
fix.show()