# scikit-learn

Machine Learning in Python

<!-- TOC GFM -->

* [Dataset](#dataset)
    * [Split dataset into train set and test set](#split-dataset-into-train-set-and-test-set)
    * [Data Preprocessing](#data-preprocessing)
    * [Discretize High Cardinality Features](#discretize-high-cardinality-features)
* [Classifiers](#classifiers)
    * [Decision Tree](#decision-tree)
    * [Clustering Methods](#clustering-methods)
    * [K-Means](#k-means)
    * [k-Nearest Neighbors (KNN)](#k-nearest-neighbors-knn)
    * [Naive Bayes](#naive-bayes)
    * [Linear Regression](#linear-regression)
    * [Logistic Regression](#logistic-regression)
    * [Neural Networks](#neural-networks)
        * [Multilayer Perceptron](#multilayer-perceptron)
    * [Support Vector Machine](#support-vector-machine)
    * [Parameters and Training](#parameters-and-training)
* [Metrics](#metrics)
    * [Accuracy](#accuracy)
    * [Confusion Matrix](#confusion-matrix)
    * [Balanced Accuracy](#balanced-accuracy)
    * [Precision, Recall, F-measures](#precision-recall-f-measures)
        * [Precision](#precision)
        * [Recall](#recall)
        * [F-measure](#f-measure)
    * [ROC AUC](#roc-auc)
    * [F1 Score](#f1-score)
    * [Log loss (Cross entropy loss)](#log-loss-cross-entropy-loss)
* [Regression metrics](#regression-metrics)
    * [Preprocessing](#preprocessing)
    * [Scalers](#scalers)
    * [Feature selection](#feature-selection)
    * [Dimensionality reduction](#dimensionality-reduction)

<!-- /TOC -->

```py
import sklearn as skit
```

## Dataset

### Split dataset into train set and test set

```py
from sklearn.model_selection import train_test_split

train_x, test_x, train_y, test_y = train_test_split(
    x, y, test_size=0.20, random_state=42)
```

- [train_test_set](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html)

### Data Preprocessing

- [data preprocessing](https://scikit-learn.org/stable/modules/preprocessing.html)

### Discretize High Cardinality Features

- [KBinsDiscretizer](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.KBinsDiscretizer.html#sklearn.preprocessing.KBinsDiscretizer)

## Classifiers

- [Classifiers comparison](https://scikit-learn.org/stable/auto_examples/classification/plot_classifier_comparison.html)

### Decision Tree

```py
from sklearn.tree import DecisionTreeClassifier

dtc = DecisionTreeClassifier(random_state=SEED)
y_pred_dtc = dtc.fit(train_ds.X, train_ds.y).predict(test_ds.X)
```

- [DecisionTreeClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html)

### Clustering Methods

- [Clustering](https://scikit-learn.org/stable/modules/clustering.html)

### K-Means

```py
from sklearn.cluster import KMeans

km = KMeans(n_clusters=2, random_state=SEED)
y_pred_km = km.fit(train_ds.X, train_ds.y).predict(test_ds.X)
```

- [KMeans](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html)

### k-Nearest Neighbors (KNN)

```py
from sklearn.neighbors import KNeighborsClassifier

knn = KNeighborsClassifier()
y_pred_knn = knn.fit(train_ds.X, train_ds.y).predict(test_ds.X)
```

- [k-nearest neighbors](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html)

### Naive Bayes

```py
from sklearn.naive_bayes import GaussianNB

gnb = GaussianNB()
# Train the model and make prediction
y_pred_gnb = gnb.fit(train_ds.X, train_ds.y).predict(test_ds.X)
```

- [Naive Bayes (Scikit learn documentation)](https://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.GaussianNB.html)

### Linear Regression

```py
from sklearn.linear_model import LinearRegression
```

- [LinearRegression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html)

### Logistic Regression

```py
lr = LogisticRegression(max_iter=1000, random_state=SEED)
y_pred_lr = lr.fit(train_ds.X, train_ds.y).predict(test_ds.X)
```

- [LogisticRegression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html)

### Neural Networks

#### Multilayer Perceptron

```py
from sklearn.neural_network import MLPClassifier

mlp = MLPClassifier(hidden_layer_sizes=(100, ), alpha=1, max_iter=1000, random_state=SEED)
mlp = MLPClassifier(hidden_layer_sizes=(75, 75), alpha=1, max_iter=1000, random_state=SEED)
mlp = MLPClassifier(hidden_layer_sizes=(50, 50, 50, 50, 50), alpha=1, max_iter=1000, random_state=SEED)

y_pred_mlp = mlp.fit(train_ds.X, train_ds.y).predict(test_ds.X)
```

- [MLPClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.neural_network.MLPClassifier.html#sklearn.neural_network.MLPClassifier)
- [L2 penalty (alpha parameter)](https://scikit-learn.org/stable/auto_examples/neural_networks/plot_mlp_alpha.html)

### Support Vector Machine

```py
from sklearn.svm import SVC

# Linear SVM
clf = SVC(kernel="linear", C=0.025)
# Radial Basis Function SVM
clf = SVC(gamma=2, C=1) # by default kernel="rbf"

# Train the classifier and make prediction
y_pred_svc = svc.fit(train_ds.X, train_ds.y).predict(test_ds.X)
```

- [SVM (Scikit learn documentation)](https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html)

### Parameters and Training

```py
# Exhaustive search over specified parameters optimized by Cross Validation.
searcher = GridSearchCV(estimator, parameters)
searcher.fit(train.X, train.y)

# Get parameters
params_dict = estimator.get_params()

# Set parameters
estimator.set_params(alpha=1)
estimator.set_params(**params_dict)
```

- [Exhaustive search over specified parameter values](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html)
- [scikit tools api and description](https://scikit-learn.org/stable/developers/develop.html)

## Metrics

- [model_evaluation (scikit)](https://scikit-learn.org/stable/modules/model_evaluation.html)
- [Multiclass vs multilabel (stackoverflow)](https://stats.stackexchange.com/questions/11859/what-is-the-difference-between-multiclass-and-multilabel-problem)
- [f1-score-accuracy-roc-auc-pr-auc (neptune.ai)](https://neptune.ai/blog/f1-score-accuracy-roc-auc-pr-auc)

### Accuracy

$$
Accuracy
= \frac{1}{n}\sum_{0}^{n-1} 1 (\hat{y}_1=y_1)
= \frac{TP+TN}{TP+TN+FP+FN}
$$

```py
from sklearn.metrics import accuracy_score
```

### Confusion Matrix

| Actual \ Predicted | 0   | 1   |
| ---                | --- | --- |
| 0                  | TN  | FP  |
| 1                  | FN  | TP  |


```py
tn, fp, fn, tp = confusion_matrix(y_true, y_pred).ravel()
```

### Balanced Accuracy

$$
\frac{1}{2}
\left(
  \frac{TP}{TP+FN} + \frac{TN}{TN+FP}
\right)
$$

```py
from sklearn.metrics import balanced_accuracy_score
```

### Precision, Recall, F-measures

- **Precision**: How many selected items are relevant?
- **Recall**: How many relevant items are selected?

- [Precision_and_recall (wikipedia)](https://en.wikipedia.org/wiki/Precision_and_recall)
- [Precision_and_recall (scikit)](https://scikit-learn.org/stable/auto_examples/model_selection/plot_precision_recall.html#sphx-glr-auto-examples-model-selection-plot-precision-recall-py)

#### Precision

- **Precision = Positive predictive value (PPV)**

$$
precision = \frac{retrieved \cap relevant}{retrieved}
$$
$$
precision = \frac{TP}{TP+FP}
$$


#### Recall

- **Recall = sensitivity = hit rate = True Positive Rate (TPR)**

$$
recall = \frac{retrieved \cap relevant}{relevant}
$$
$$
recall = \frac{TP}{TP+FN}
$$

#### F-measure

$$
F_1 = 2 \cdot \frac{precision \cdot recall}{precision + recall}
$$

### ROC AUC

$$
AUC
= \frac{1}{2} \left(TPR + 1 - FPR \right)
= \frac{1}{2} \left(TPR + TNR \right)
$$

- [ROC AUC explained](https://towardsdatascience.com/understanding-auc-roc-curve-68b2303cc9c5)

```py
from sklearn.metrics import roc_curve, auc

# pos_label is positive class label
fpr, tpr, thresholds = roc_curve(y, scores, pos_label=1)

print(metrics.auc(fpr, tpr))
```

```py
from sklearn.metrics import roc_auc_score

print(roc_auc_score(y_test, y_predicted))
```

- [roc_curve](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.roc_curve.html)
- [roc_auc_score](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.roc_auc_score.html#sklearn.metrics.roc_auc_score)

### F1 Score

```py
from sklearn.metrics import f1_score
```

### Log loss (Cross entropy loss)

Can be used to evaluate the probability outputs of a classifier instead of its discrete predictions.

$y \in \{0, 1\}$ and $p = Pr(y = 1)$

$$L_{log}(y,p) = - log(Pr(y | p)) = -\right(y log(p) + (1 - y) log (1 - p)\left)$$

$$L_{log}(Y,P) = - log(Pr(Y | P)) = -\frac{1}{N} \sum_{i=0}^{N-1} \sum_{k=0}^{K-1} y_{i,k} log(p_{i,k})$$

- [log_loss (scikit)](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.log_loss.html)

## Regression metrics

- [mean_squared_log_error (RMSLE)](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.mean_squared_log_error.html)

### Preprocessing

- [scikit preprocessing](https://scikit-learn.org/stable/modules/preprocessing.html)

### Scalers

- [**Compare different scalers**](https://scikit-learn.org/stable/auto_examples/preprocessing/plot_all_scaling.html)
    - [MaxAbsScaler](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.MaxAbsScaler.html)
    - [MinMaxScaler](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.MinMaxScaler.html)
    - [PowerTransformer](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.PowerTransformer.html)
    - [QuantileTransformer](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.QuantileTransformer.html)
    - [RobustScaler](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.RobustScaler.html)
    - [StandardScaler](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html)

### Feature selection

- [feature_selection](https://scikit-learn.org/stable/modules/feature_selection.html)
- [recursive feature elimination](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.RFE.html)
- [SelectFromModel](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.SelectFromModel.html)

### Dimensionality reduction

- [Principal component analysis](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html)
