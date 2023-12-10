# Data preprocessing

Notes and projects of Data Preprocessing course of the Faculty of Information Technology CTU in Prague.

## Projects

1. Data validation and cleaning
2. Class balancing and discretization (binning)
3. Data transformation and dimensionality reduction

## TODO

* google charts

## References

* Hastie, T.; Tibshirani, R.; Friedman, J. The Elements of Statistical Learning. Springer. 2013.
* Kuhn, M.; Johnson, K. Feature Engineering and Selection: A Practical Approach for Predictive Models. [online version](http://www.feat.engineering/intro-intro.html)
* Zheng, A.; Casari, A. Feature Engineering for Machine Learning: Principles and Techniques for Data Scientists. O'Reilly. 2018.

## KDDM, CRISP-DM, DM software

### Knowledge discovery (DIKW) model

### Definitions

- data mining (DM)
- knowledge discovery (KD)
- knowledge discovery in databases (KDD)
- knowledge discovery and data mining (KDDM)

### Data preprocessing types

- human centric model (experts)
- data centric model

### CRISP-DM

1. Domain understanding     (10%)
2. Data understanding       (20%)
3. Data preparation         (45%)
4. DM                       (10%)
5. Evaluation of results    (10%)
6. Deployment of results    ( 5%)

**Predictive model markup lanuage (PMML)**

## Feature Types

* Dimensionality
  * Scalar
  * Multidimensional
* Categorical
  * Number
    * Binary
    * Multi
  * Order
    * Ordered
    * Unordered
* Numeric
  * Discrete
  * Continuous

## Visualization and data exploration

### Visualization

- basic charts for visualisation
    + column / bar chart
        * 2D / 3d
        * simple / cumulated
    + box and whiskers
    + line chart
    + scatter plot
    + XY chart
    + pie chart
    + radar chart
    + sankey chart
    + tree visualisation
        * plain / circular
    + map visualisation
    + sphagetti chart
    + infographics
    + cloud of words
- Vector field visualization
    + static / dynamic
    + 2D / 3D
    + array field of arrows
- high dimensional data visualisation
    + chart of parallel coordinates
    + glyphs
    + radviz
- Visualizaton of volume data
    + photorealistic visualisation
- Dedicated infrastructure

## Dimensionality reduction - feature ranking and selection

Feature selection based on its quality, by its information value.

Feature selection by number of considered features at a time:

- Univariate method
- Multivariate method

Feature selection methods:

1. Filter method:
  - ranks features or feature subsets independently of the predictor (classifier).
2. Wrapper method:
  - uses a classifier to assess features or feature subsets.
3. Embedded method:
  - like wrapper, the search is controlled by the algorithm constructing classifier

### Filter methods

- T-test to determine whether the mean values differ significantly.
- Correlation methods (Pearson, Spearman)
- Entropy
- Univariate dependence
- Consistency

### Wrapper methods

- classifier error rate

### Search approaches

- Exhaustive
- Heuristic
- Random
- Evolutionary

## Problems in data, data cleaning

### Problem types

- Noisy
- Incomplete
- Inconsistent
- Invalid
- Non-representative
- Unbalanced

### Cleaning steps

- Data Understanding
- Data Validation
- Data Cleaning
  - Metadata
  - Missing Values
  - Unified Date Format
  - Nominal to Numeric
  - Discretization
- Field Selection and “False Predictors”
- Unbalanced Target Distribution
- Data Transformation
- Data Reduction
- Sample Selection

#### Missing values

Record missing values:

- Missing value should be of the same type.
- Always keep in mind, the datatype (overflows).

Fill missing values:

- Random
- Mean, median
- kNN

#### KSP Date format

```
# YYYY.year_portion
year + (day_from_jan_1 - 0.5) / (365 + is_leap_year)
```

- [All you want to know about preprocessing: Data preparation](https://towardsdatascience.com/all-you-want-to-know-about-preprocessing-data-preparation-b6c2866071d4)

## Data Cleaning: Discretization

### Binning

- Equal width
- Equal depth

### Outliers

Cluster analysis
- K-Means
- Hierarchical clustering

### Field selection

Remove features with little or no variance, does not help with anything.

### False predictors, information leakers

Prediction based on only one feature, if the accuracy is too high, then be careful.

Number of samples should be proportionally higher than number of features. Else there will be found dependencies, based only on the small number of samples.

### Balancing

- Balancing samples by attributes (man/female)
- balancing samples by target variable (healthy/ill)

### Data transformation

1. smoothing
  - remove noise
2. standardization
  - z-score normalization
  - min-max
  - softmax
  - normalization by decimal scaling
  - transformation to different distribution (uniform perhaps)
3. Feature construction

### Dimensionality reduction

1. Feature selection
2. Heuristics
  - step-wise forward selection (feature by feature replaced with mean, tested)
  - step-wise backward selection (all features except one replaced with mean)

### Data compression

- Principal component analysis
- Independent component analysis

### Sampling

- Stratified sample (choose representative subset)
- During addition or removal of a few samples (10) check density and distribution functions if they changes with samples then the addition/removal was significant.

## Data reduction

- picking quality samples
- removing noised samples

### Nearest neighbor

Sub-sample data with kNN and then use exact nearest neighbor.

- Voronoi diagram - divide space by the class representatives.
- Decision boundary consistent - sub-samples boundary equal to the original one.
- Minimum consistent set - Minimum samples subset that classifies all samples correctly (not consistent decision boundary).

### Condensing (picking samples)

#### Condensed nearest neighbor

- Randomly pick samples until reaching minimum consistent set.

#### Proximity graph

Pick only samples at the decision boundary.

Neighbour defintions:

- DT = Delaunay Triangulation
- GG = Gabriel Graph
- RNG = Relative Neighbourhood Graph
- MST = Minimum Spanning Tree
- NNG = Nearest Neighbour Graph

$NNG \subset MST \subset RNG \subset GG \subset DT$

### Editing (removing samples)

#### Wilson editing

kNN removes minority samples.

#### Multi-edit

Repeatedly used Wilson editing to subset of samples classifying samples with samples from the next set. 

### Condensing and Editing

- Combination of condensing and editing methods.

### Methods overview

Selective algorithms:
- CNN – selects instances near the decision boundary
- RNN – subset selected by CNN is further reduced
- IB3 – similar to CNN, statistical reduction (confidence)
- DROP3 – deletes instances, that will not change the classification of other instances
Adaptive algorithms:
- Prototype – creates new strategic data points
- Chen – new instances as centroids of original data
- RSP1 – Chen including class ballancing

Balancing aware reduction methods
- Baseline Methods
  - Random over-sampling
  - Random under-sampling
- Under-sampling Methods
  - Tomek links
  - Condensed Nearest Neighbor Rule
  - One-sided selection
  - CNN + Tomek links
  - Neighborhood Cleaning Rule
- Over-sampling Methods
  - Smote
- Combination of Over-sampling method with Under-sampling method
  - Smote + Tomek links
  - Smote + ENN

## Data Projections (dimensionality reduction)

Linear

- Random mapping
- PCA
- ICA
- LDA

Non-linear

- MDS
- Sammon mapping

## Feature extraction from time series

- filtering vs querying
- signal distance

### Comparison

- offset
- normalization
- trend removal
- noise removal

### Euclidean distance

- Clustering
- Wedge

### non-Euclidean distance

- Dynamic time wrapping (DTW)
- Longest Common Subsequence (LCS)
- Landmarks

Piecewise Aggregate Approximation (PAA)
- Segment the time series into equal parts, store the average value for each part.
Adaptive Piecewise Constant Approximation (APCA)
- Parts are of adaptive length

## Feature extraction from text

Basic
- Representative words
- Indexing
- Weighting Model
- Dimensionality Reduction
Linguistic
- Part-of-speech tagging
- Syntactic parsing

### Intelligent Miner for Text

### Natural Language Processing

1. Sentence splitting
2. Tokenization
3. Lemmatisation
4. Part-of-speech tagging (POS tagging)
5. Shallow parsing
6. Named entity recognition
7. Syntactic parsing
8. (Semantic Role Labeling)

## Image preprocessing

Representation of image information - levels
1. level - matrix of numbers (values of brightness, grayscale values)
  - for preprocessing, e.g. filtering, sharpening, etc.
2. level - segmented images, edge/area segmentation
  - a priori information is used
3. level - geometric representations
  - knowledge of 2D, 3D shapes, influence of e.g. lighting
4. level - relational models
  - semantic networks, derivation

Shapes/types of filters (convolution kernels)
- Filtration by averaging
- Median filtration

### Edge detection

Gradient methods and edge detection
- Roberts’ operator - approximation of the 1st partial derivative
- Sobel's operator - approximation of the 1st partial derivative (more
precise)
- Laplace's operator - approximation of the 2nd partial derivative
(invariant to rotation)

Smoothing
- Gaussian filter

LoG filter („Laplacian of Gaussian“).
- Combination of the first two steps is called

### Corner detection

### Fourier transform

- Fast Fourier transform (FFT)
- Discrete Fourier transform (DFT)

### Image segmentation

- Thresholding methods (single/double threshold)
- Otsu's method, Adaptive thresholding
- Watershed segmentation
- Mean-shift segmentation

### Border representation

### Object detection and tracking based on a model
