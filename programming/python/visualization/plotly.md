# Plotly

## Content

- [Content](#content)
- [Line](#line)
  - [Line style - color, width, dash](#line-style---color-width-dash)
- [Histogram](#histogram)
  - [Number of bins](#number-of-bins)
  - [Range of x axis](#range-of-x-axis)
- [Subplots](#subplots)
- [X axis tics](#x-axis-tics)
- [Show grid](#show-grid)
- [Two Y axis](#two-y-axis)
- [Save plot as image](#save-plot-as-image)

## Line

```py
import plotly.express as px

df = px.data.gapminder().query("country=='Canada'")
fig = px.line(df, x="year", y="lifeExp", title='Life expectancy in Canada')
fig.show()
```

### Line style - color, width, dash

```py
fig = go.Figure()
# Create and style traces
fig.add_trace(go.Scatter(x=month, y=high_2014, name='High 2014',
                         line=dict(color='firebrick', width=4)))
fig.add_trace(go.Scatter(x=month, y=low_2014, name = 'Low 2014',
                         line=dict(color='royalblue', width=4)))
fig.add_trace(go.Scatter(x=month, y=high_2007, name='High 2007',
                         line=dict(color='firebrick', width=4,
                              dash='dash') # dash options include 'dash', 'dot', and 'dashdot'
))
```

[line source](https://plotly.com/python/line-charts/)

## Histogram

```py
import plotly.express as px
df = px.data.tips()
fig = px.histogram(df, x="total_bill")
fig.show()
```

[histogram link](https://plotly.com/python/histograms/)
[histogram documentation](https://plotly.com/python/reference/histogram/)

### Number of bins

```py
fig.add_trace(go.Histogram(
    x=x1,
    histnorm='percent',
    name='experimental',
    xbins=dict(
        start=-3.0,
        end=4,
        size=0.5
    ),
    marker_color='#330C73',
    opacity=0.75
))
```

### Range of x axis

```py
fig = go.Figure()
fig.add_trace(go.Histogram(
    x = pred_prob, # numpy.ndarray
    xbins = dict(
        start = 0.0,
        end = 1.0,
        size = 1/8,
    )
))

fig.update_layout(
    title_text = 'Sampled Results',
    xaxis_title_text = 'Probability Range',
    yaxis_title_text = 'Count',
    xaxis_range = [0, 1]
)
fig.show()
```

[source](https://github.com/plotly/plotly.js/issues/1229)

## Subplots

```py
from plotly.subplots import make_subplots
import plotly.graph_objects as go

fig = make_subplots(rows=1, cols=2)

fig.add_trace(
    go.Scatter(x=[1, 2, 3], y=[4, 5, 6]),
    row=1, col=1
)

fig.add_trace(
    go.Scatter(x=[20, 30, 40], y=[50, 60, 70]),
    row=1, col=2
)

fig.update_layout(height=600, width=800, title_text="Side By Side Subplots")
fig.show()
```
[subplots link](https://plotly.com/python/subplots/)

## X axis tics

```py
import plotly.graph_objects as go

fig = go.Figure(go.Scatter(
    x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
    y = [28.8, 28.5, 37, 56.8, 69.7, 79.7, 78.5, 77.8, 74.1, 62.6, 45.3, 39.9]
))

fig.update_layout(
    xaxis = dict(
        tickmode = 'linear',
        tick0 = 0.5,
        dtick = 0.75
    )
)

fig.show()
```
[ticks](https://plotly.com/python/tick-formatting/)

## Show grid

```py
go.Layout(
    xaxis = {
        'showgrid': False
    },
    yaxis = {
       'showgrid': True
    }
)
```
[grids source](https://community.plotly.com/t/how-do-i-hide-the-grid-lines-that-appear-on-dcc-graph-by-default/30762)

## Two Y axis

```py
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Create figure with secondary y-axis
fig = make_subplots(specs=[[{"secondary_y": True}]])

# Add traces
fig.add_trace(
    go.Scatter(x=[1, 2, 3], y=[40, 50, 60], name="yaxis data"),
    secondary_y=False,
)

fig.add_trace(
    go.Scatter(x=[2, 3, 4], y=[4, 5, 6], name="yaxis2 data"),
    secondary_y=True,
)

# Add figure title
fig.update_layout(
    title_text="Double Y Axis Example"
)

# Set x-axis title
fig.update_xaxes(title_text="xaxis title")

# Set y-axes titles
fig.update_yaxes(title_text="<b>primary</b> yaxis title", secondary_y=False)
fig.update_yaxes(title_text="<b>secondary</b> yaxis title", secondary_y=True)

fig.show()
```
[multiple axis](https://plotly.com/python/multiple-axes/)

## Save plot as image

```py
import os

if not os.path.exists("images"):
    os.mkdir("images")

fig.write_image("images/fig1.png")
```

[static image export](https://plotly.com/python/static-image-export/)