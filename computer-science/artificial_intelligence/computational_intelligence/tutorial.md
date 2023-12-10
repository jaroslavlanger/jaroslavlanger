# Computational Intelligence Tutorial

## Contents

## Study Links

- (machinelearningmastery)[https://machinelearningmastery.com/]
- (AI, ML, DL (Amidi, Stanford))[https://stanford.edu/~shervine/teaching/]
- (deeplearning.ai (coursera))[https://www.coursera.org/learn/convolutional-neural-networks?specialization=deep-learning]

## Environment

- [Kaggle vs Colab (towardsdatascience)](https://towardsdatascience.com/kaggle-vs-colab-faceoff-which-free-gpu-provider-is-tops-d4f0cd625029)
- [Google Colab vs Kaggle (analyticsindiamag)](https://analyticsindiamag.com/google-colab-vs-kaggle-kernels-which-of-the-two-platforms-should-you-go-for/)

### Google Colab

- gpu - tpu
- connect with drive
- open/push github
- [set tensorflow version](https://colab.research.google.com/notebooks/tensorflow_version.ipynb#scrollTo=-XbfkU7BeziQ)

### Kaggle

- Limits GPU and TPU usage to 30 hours/week [efficient-gpu-usage](https://www.kaggle.com/docs/efficient-gpu-usage).
    - [See GPU and TPU hours left](http://kaggle.com/me/account)
- [How to Use Kaggle](https://www.kaggle.com/docs/notebooks)
- [upload data example](https://www.youtube.com/watch?v=0jQwAp7po00&feature=youtu.be)
- [upload python scripts example](https://www.kaggle.com/rtatman/reproducing-research-men-also-like-shopping)
- [download data from kaggle output](https://www.kaggle.com/product-feedback/109715)

## Turorials

### 01 General

- Tensor
- Gradient descent for linear regression
- Logistic regression
- MLP
- Metrics

### 02 Dense Neural Network (DNN)

- checkpoint, early stopping
- save weights, load weights
- regularization (batch normalization)
- show the model
- custom loss function
- custom activation function

### 03 Convolutional Neural Network (CNN)

- conv2D
- Transfer learning
- save weights during learning
- conv1D

### 04 Recurrent Neural Network (RNN)

- transfer learning
    - cut last layer, change only the predicted classes, train only the last weights
    - use intermediate layer of trained model as output for your next layer
- tf.keras.layers.LSTM
- Bidirectional(LSTM(50,...))
- GRU 

