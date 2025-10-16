import plotly.express as px
import numpy as np


N = 500
x = []
y = []
value = 0.5


for r in np.arange(3.5, 4, 0.001):
    for i in range(2 * N):
        if i > 0:
            value = r * value * (1 - value)

    for i in range(N):
        x.append(r)
        value = r * value * (1 - value)
        y.append(value)


# print(y[(N - 2) : N])

fig = px.scatter(x=x, y=y)
fig.update_traces(marker=dict(size=1))

fig.show()
