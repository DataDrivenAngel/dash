import plotly.express as px
import numpy as np

print("starting")
n = 5000
x = np.random.standard_normal(n)
y = np.random.standard_normal(n)
print("data generated.... plotting")


fig = px.scatter(x=x, y=y)
fig.show()