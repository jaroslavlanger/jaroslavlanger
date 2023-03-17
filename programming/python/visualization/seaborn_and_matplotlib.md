# Seaborn and Matplotlib

Python libraries for making visualizations.

`2021 Feb 12, Jaroslav Langer`

Libraries:  seaborn [0.11.0], matplotlib [3.3.3]

## Contents

<!-- TOC GFM -->

* [Seaborn](#seaborn)
    * [Introduction](#introduction)
    * [Basics](#basics)
        * [Import](#import)
    * [Plotting Functions](#plotting-functions)
    * [Bar Chart (barplot)](#bar-chart-barplot)
        * [Percentages Over Bars](#percentages-over-bars)
    * [Histogram (histplot, countplot)](#histogram-histplot-countplot)
    * [Box Plot (boxplot)](#box-plot-boxplot)
    * [Line Chart (lineplot)](#line-chart-lineplot)
    * [Scatter Plot (scatterplot)](#scatter-plot-scatterplot)
    * [Heat Map (heatmap)](#heat-map-heatmap)
    * [Multi-plot Grids (pairplot, PairGrid, FacetGrid)](#multi-plot-grids-pairplot-pairgrid-facetgrid)
        * [pairplot](#pairplot)
        * [PairGrid](#pairgrid)
        * [FacetGrid](#facetgrid)
    * [Plot aesthetics (set_style, color_pallete, dash styles)](#plot-aesthetics-set_style-color_pallete-dash-styles)
        * [Set style](#set-style)
        * [Color palettes](#color-palettes)
        * [Dash styles](#dash-styles)
* [Matplotlib](#matplotlib)
    * [Basics](#basics-1)
        * [pyplot](#pyplot)
        * [The Axes Class](#the-axes-class)
        * [Figure Class](#figure-class)
    * [Set title](#set-title)
    * [Plot Multiple Graphs (subplots, subplot)](#plot-multiple-graphs-subplots-subplot)
        * [subplots](#subplots)
        * [subplot](#subplot)
    * [Set Figure Size](#set-figure-size)
    * [Legend](#legend)
    * [Colors](#colors)
    * [Save Image](#save-image)
    * [Ticks (xtics, yticks)](#ticks-xtics-yticks)
        * [Format time from seconds](#format-time-from-seconds)
* [TODO](#todo)

<!-- /TOC -->

## Seaborn

Seaborn is a Python data visualization library based on matplotlib.
This is a quick overview of what is possible with seaborn and how to do it.

### Introduction

Seaborn has a beautiful [documentation](https://seaborn.pydata.org/) so you can either start with their [tutorial](https://seaborn.pydata.org/tutorial.html) or (more likely) browse their [gallery](https://seaborn.pydata.org/examples/index.html) and dive into what you want to accomplish.
This document covers 
  (a) the absolute basics you are good to go with,
  (b) some handy stuff that are easy to imagine but harder to do.

### Basics

#### Import

```py
import seaborn as sns
```

### Plotting Functions

Plotting functions return matplotlib Axes object.

### Bar Chart (barplot)

```py
# Two barplots mean bars in front of the max bars
sns.barplot(x="n", y=f"{feature}_max", data=df, color="firebrick", order=self.values[-1], label="max")
sns.barplot(x="n", y=f"{feature}_mean", data=df, color="tab:blue", order=self.values[-1], label="mean")
plt.legend()
```

```py
# Horizontal barplot
sns.barplot(y="name", x="f1_score", hue="model_name", data=eval_df, orient="h")
```

- [barplot](https://seaborn.pydata.org/generated/seaborn.barplot.html)
- [multiple bars](https://stackoverflow.com/questions/14270391/python-matplotlib-multiple-bars)

#### Percentages Over Bars

```py
for p in ax.patches:
    percentage = '{:.1f}%'.format((p.get_height()/df.shape[0]) * 100)
    x = p.get_x() + p.get_width()/10
    y = int((p.get_y() + p.get_height()) + df.shape[0] * 0.005)
    ax.annotate(percentage, (x, y))
```

- [Barplot Percentages (stackoverflow)](https://datascience.stackexchange.com/questions/48035/how-to-show-percentage-text-next-to-the-horizontal-bars-in-matplotlib)

### Histogram (histplot, countplot)

```py
# Plot histogram (discrete=True for discrete values)
sns.histplot(x="age", data=df, discrete=False)

# Plot categories sizes
ax = sns.countplot(x=feature, data=df, ax=ax)
```

- [histplot](https://seaborn.pydata.org/generated/seaborn.histplot.html#seaborn.histplot)
- [countplot](https://seaborn.pydata.org/generated/seaborn.countplot.html)
- [Distributions (pandas)](https://seaborn.pydata.org/tutorial/distributions.html)

### Box Plot (boxplot)

```py
meanprops={"marker":"o", "markerfacecolor":"white", 
    "markeredgecolor":"black","markersize":"10"}


sns.boxplot( self.params[-1], feature, order=self.values[-1], showmeans=True, meanprops=meanprops)
```

- [boxplot](https://seaborn.pydata.org/generated/seaborn.boxplot.html)

### Line Chart (lineplot)

```py
g = sns.relplot(x="time", y="value", kind="line", data=df)
# Legend full to see present values in legend, not approximative
g2 = sns.lineplot(hue="something", legend="full" sort=False)
```

- [relplot](https://seaborn.pydata.org/generated/seaborn.relplot.html)

### Scatter Plot (scatterplot)

```py
# Stripplot, hue - survived group
- sns.stripplot(x="Pclass", y="Age", hue="Survived", data=data, palette= ['black','green']) #, jitter=False) 
# Swarmplot
- sns.swarmplot(x='Rok', hue='Kandidátní listina - název', y='Věk', data=candidates)

# Scatterplot s - size of dots
ax = sns.scatterplot(x="weight", y="value", data=df, s=10)
```

- [scatterplot](https://seaborn.pydata.org/generated/seaborn.scatterplot.html)

### Heat Map (heatmap)

```py
# heatmap from correlation matrix
sns.heatmap(cor_matrix, annot=True)
```

### Multi-plot Grids (pairplot, PairGrid, FacetGrid)

#### pairplot

Plot pairwise relationships in dataset.

```py
sns.pairplot(data, hue='Survived', palette=['red', 'green']) #, diag_kind='hist'
```

- [pairplot](https://seaborn.pydata.org/generated/seaborn.pairplot.html)


#### PairGrid

```py
g = sns.PairGrid(df, x_vars=["accuracy", "auc", "f1_score"], y_vars=["model_name"], height=4)
_ = g.map(sns.barplot)
```

- [PairGrid](https://seaborn.pydata.org/generated/seaborn.PairGrid.html#seaborn.PairGrid)

#### FacetGrid

```py
# Create a grid
g = sns.FacetGrid(col="method", row="dataset", data=df, hue="score",
        sharey=False, sharex=False, height=3.5) # aspect=2
# Map the plots onto the gird
g.map(sns.boxplot, self.params[-1], feature, order=self.values[-1])

# Rotate x tics labels
g.set_xticklabels(rotation=90)
# Rotate y tick labels
for ax in g.axes.flat:
    for label in ax.get_yticklabels():
        label.set_rotation(0)
```

- [FacetGrid](https://seaborn.pydata.org/generated/seaborn.FacetGrid.html)
- [Rotate the y (x) labels](https://github.com/mwaskom/seaborn/issues/867)

### Plot aesthetics (set_style, color_pallete, dash styles)

- [Seaborn aesthetics](https://seaborn.pydata.org/tutorial/aesthetics.html)

#### Set style

```py
sns.set_style("dark")
```

#### Color palettes

```py
# Create the palette
pall = sns.color_palette("hls", 8)
# See the palette
sns.palplot(pall)
```

- [palettes](https://seaborn.pydata.org/tutorial/color_palettes.html)

#### Dash styles

It is not possible to plot more than 6 values with different style.

In case it needed, the styles can be defined.

```py
dash_styles = ["",
               (4, 1.5),
               (1, 1),
               (3, 1, 1.5, 1),
               (5, 1, 1, 1),
               (5, 1, 2, 1, 2, 1),
               (2, 2, 3, 1.5),
               (1, 2.5, 3, 1.2)]
sns.relplot(...,  dashes=dash_styles,...)
```

- [dash_styles](https://github.com/mwaskom/seaborn/issues/1513)

## Matplotlib

Module for ploting of all the graphs you can imagine.

`2020/11/08, Jaroslav Langer`

### Basics

```py
import matplotlib
%matplotlib inline # Without this matplotlib sometimes doesn't work correctly in jupyter notebooks.
matplotlib.style.use('ggplot')
```

#### pyplot

Provides a MATLAB-like plotting framework.

```py
import matplotlib.pyplot as plt
```

- [pyplot](https://matplotlib.org/api/pyplot_api.html)

#### The Axes Class

The Axes contains most of the figure elements: Axis, Tick, Line2D, Text, Polygon, etc., and sets the coordinate system.

- [Axes](https://matplotlib.org/3.3.3/api/axes_api.html)

#### Figure Class

The top level container for all the plot elements.

- [Figure](https://matplotlib.org/3.3.3/api/_as_gen/matplotlib.figure.Figure.html)

### Set title

```py
feature = "age"
ax = sns.distplot(df[feature], kde=False)
ax.set_title(f"{feature.capitalize()} distribution")

# Add a centered title to the figure.
plt.subplots_adjust(top=0.7) # Otherwise the figure will collide with the title 
fig.suptitle('All the Beautiful Charts')
```

### Plot Multiple Graphs (subplots, subplot)

#### subplots

```py
fig, (ax1, ax2) = plt.subplots(1, 2)
# Or
fig, axes = plt.subplots(nrows=1, ncols=2)

# Plot using specified ax
survived['Sex'].apply(lambda x: 1 if x == 'female' else 0).plot.hist(color='Green', ax=ax1)
not_survived['Sex'].plot.hist(color='Black', ax=ax2)
```

#### subplot

```py
# Examples of six ploted graphs
# Next graph will be plotted to pos 1 in grid 3 rows 2 columns
plt.subplot(121)
survived['Sex'].apply(lambda x: 1 if x == 'female' else 0).plot.hist(color='Green')
plt.subplot(122)
not_survived['Sex'].apply(lambda x: 1 if x == 'female' else 0).plot.hist(color='Black')
```

### Set Figure Size

```py
# Set size of figures in inches
plt.figure(figsize=(10,18))
# Or
fig.set_size_inches(11.7, 8.27)
# Or
fig, ax = plt.subplots(figsize=(16, 10))
```

### Legend

```py
# Show legend
ax.legend()
# Move legend out from graph
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
```

- [link](https://stackoverflow.com/questions/30490740/move-legend-outside-figure-in-seaborn-tsplot)

### Colors

```py
# Named colors such as
color="tab:blue"
```

- [Names colors (matplotlib)](https://matplotlib.org/3.1.0/gallery/color/named_colors.html)

### Save Image

**Save figure as png**

```py
fig = sns.boxplot(x="time" y="n", orient="h", data=df)

fig.savefig(f"{project_path}/figures/n_time_boxplot.png")
```

**Save matrix as png**

```py
plt.imsave(file_name, array)
```

* [imsave (matplotlib.org)](https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.imsave.html)

### Ticks (xtics, yticks)

```py
# Show only x ticks values that are present in the data
ax.set(xticks=df["x_column"].nunique(), xticklabels=df["x_column"].nunique())

# Rotate x ticks (handy if the ticks are too long)
plt.xticks(rotation=45)

# Rotate x ticks by given ax
ax.set_xticklabels(ax.get_xticklabels(), rotation=70)

# Rotate y tick labels
for label in ax.get_yticklabels():
    label.set_rotation(0)
```

#### Format time from seconds

Prepare formater function.

```py
from matplotlib.ticker import FuncFormatter

def format_func(x, pos):
    hours = int(x//3600)
    minutes = int((x%3600)//60)
    seconds = int(x%60)

    return "{:d}:{:02d}".format(hours, minutes)
    # return "{:d}:{:02d}:{:02d}".format(hours, minutes, seconds)

formatter = FuncFormatter(format_func)
```

Format y axis tickers.

```py
ax.yaxis.set_major_formatter(formatter)
# this locates y-ticks at the hours
ax.yaxis.set_major_locator(matplotlib.ticker.MultipleLocator(base=3600))
# this ensures each bar has a 'date' label
ax.xaxis.set_major_locator(matplotlib.ticker.MultipleLocator(base=1))
```

- [Format time y axis (stackoverflow)](https://stackoverflow.com/questions/48294332/plot-datetime-timedelta-using-matplotlib-and-python)

## TODO

- plt.show()
- fig.show()
