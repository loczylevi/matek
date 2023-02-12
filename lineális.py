import plotly.express as px
import numpy as np

x = np.linspace(-10, 10, 100)
y1 = x**2
y2 = x

fig = px.line(x=x, y=y1)
fig.add_scatter(x=x, y=y2, mode='lines', name='y=x')
fig.show()
