# Tensorflow and Keras

```
Author:     Jaroslav Langer
Software:
    TensorFlow 2.4.0
Date:       2021 Jan 09
```

## Contents

- [Introduction](#introduction)
- [References](#references)
- [TODO](#todo)
- [Tensorflow](#tensorflow)
  - [Tensor](#tensor)
- [Keras](#keras)
- [Model](#model)
  - [Sequential](#sequential)
  - [Model training](#model-training)
  - [Compile](#compile)
  - [Fit](#fit)
  - [Evaluate](#evaluate)
  - [Different loss values fit() vs. evaluate()](#different-loss-values-fit-vs-evaluate)
  - [predict](#predict)
  - [model.layers](#modellayers)
- [Layers](#layers)
  - [Layer](#layer)
  - [Flatten](#flatten)
  - [Dense](#dense)
  - [Embedding](#embedding)
  - [Masking](#masking)
  - [SimpleRNN](#simplernn)
  - [RNN](#rnn)
  - [LSTM](#lstm)
  - [TimeDistributed](#timedistributed)
- [Model training APIs](#model-training-apis)
- [Activations](#activations)
- [Losses](#losses)
  - [BinaryCrossentropy](#binarycrossentropy)
  - [CategoricalCrossentropy](#categoricalcrossentropy)
  - [Optimizers](#optimizers)
- [Metrics](#metrics)
  - [BinaryAccuracy](#binaryaccuracy)
- [Utils](#utils)
- [Theano](#theano)

## Introduction

Tensorflow - An end-to-end open source machine learning platform.
Keras - Keras is an API designed for human beings, not machines. 

- [Keras vs. tf.keras: What’s the difference in TensorFlow 2.0?](https://www.pyimagesearch.com/2019/10/21/keras-vs-tf-keras-whats-the-difference-in-tensorflow-2-0/)

## References

The keras documentation at [keras.io] and [tensorflow.org] are sometimes the same. I like better the structure and appearance of the doc at [tensorflow.org] and that is why I will refer to the [tensorflow.org] doc even though the same one could be found at [keras.io].

- [Guide (tensorflow.org)](https://www.tensorflow.org/guide)
    - [Guide sequential_model (tensorflow.org)](https://www.tensorflow.org/guide/keras/sequential_model)
    - [Guide RNN (tensorflow.org)](https://www.tensorflow.org/guide/keras/rnn)
- [Tutorials (tensorflow.org)](https://www.tensorflow.org/tutorials/)

## TODO

- [tensorboard (tensorflow.org)](https://www.tensorflow.org/tensorboard)
- [save_and_serialize](https://www.tensorflow.org/guide/keras/save_and_serialize)
    - It seems to me, Keras does not support saving state of stateful layers. 

## Tensorflow

- [Time series forecasting (TensorFlow Core Tutorials)](https://www.tensorflow.org/tutorials/structured_data/time_series)

```py
import tensorflow as tf
```

### Tensor

```py
# Convert EagerTensor to numpy
tens.numpy()
```

AttributeError: 'Tensor' object has no attribute 'numpy'

```py
# Eager is the way
import tensorflow as tf
tf.enable_eager_execution()
# or/and
model.compile(loss=loss_function, optimizer='rmsprop', run_eagerly=True)
```

- [Tensor](https://www.tensorflow.org/api_docs/python/tf/Tensor)
- [no attribute numpy (stackoverflow)](https://stackoverflow.com/questions/52357542/attributeerror-tensor-object-has-no-attribute-numpy)

## Keras

Keras supports multiple backends such as Theano, CNTK, etc.

- [Time Series Prediction with LSTM Recurrent Neural Networks in Python with Keras](https://machinelearningmastery.com/time-series-prediction-lstm-recurrent-neural-networks-python-keras/)

## Model

- [Model](https://www.tensorflow.org/api_docs/python/tf/keras/Model)

### Sequential

```py
from tf.keras import Sequential

model = Sequential(layers=None, name=None)

model.add(layer)
```

- [Sequantial (tensorflow.org)](https://www.tensorflow.org/api_docs/python/tf/keras/Sequential)
- [Sequential (keras.io)](https://keras.io/api/models/sequential/)

### Model training

- compile
- fit
- evaluate
- predict
- save_weights
- load_weights
- train_on_batch
- test_on_batch 
- predict_on_batch 
- run_eagerly

- [train_and_evaluate (tensorflow.org)](https://www.tensorflow.org/guide/keras/train_and_evaluate)
- [model_training_apis](https://keras.io/api/models/model_training_apis/)

### Compile

| Arguments           | Default   | Description |
| ---                 | :---:     | ---         |
| optimizer           | 'rmsprop' |             |
| loss                | None      | String (name of objective function), objective function or tf.keras.losses.Loss instance. |
| metrics             | None      |             |
| loss_weights        | None      |             |
| weighted_metrics    | None      |             |
| run_eagerly         | None      |             |
| steps_per_execution | None      |             |
| `**kwargs`          |           |             |

### Fit

In verbose mode, model.fit() shows loss value. The value is always shown before the weights update i.e. the last loss is not the loss of the last prediction because the weights were updated afterwards.

| Arguments             | Def.  | Description |
| ---                   | :---: | ---         |
| x                     | None  |
| y                     | None  |
| batch_size            | None  | Number of samples per gradient update. If unspecified, batch_size will default to 32 |
| epochs                | 1     | Number of epochs to train the model. An epoch is an iteration over the entire x and y data provided. |
| verbose               | 1     |
| callbacks             | None  |
| **validation_split**  | 0.0   | Float between 0 and 1. Fraction of the training data to be used as validation data. |
| validation_data       | None  |
| shuffle               | True  | Boolean (whether to shuffle the training data before each epoch) or str (for 'batch'). |
| class_weight          | None  |
| sample_weight         | None  |
| initial_epoch         | 0     |
| steps_per_epoch       | None  |
| validation_steps      | None  |
| validation_batch_size | None  |
| validation_freq       | 1     |
| max_queue_size        | 10    |
| workers               | 1     |
| use_multiprocessing   | False |

- [Model fit (tensorflow.org)](https://www.tensorflow.org/api_docs/python/tf/keras/Model#fit)

#### fit_generator?

### Evaluate

Evaluate shows average loss of all the batches of one epoch.

### Different loss values fit() vs. evaluate()

The model.evaluate() loss value can be very different from the model.fit() loss. Besides the fact, that the last value of the model.fit() loss is not the loss of the last prediction (the difference would not be that significant), the main difference is that the fit function shows losses for every batch before the weight update (for every epoch the number changes until the last batch). That means the last fit loss is the loss just before the last weight update. On the other hand the evaluate function averages all the losses of all the batches of given epoch. This is especially visible with series predictions where the first predictions are much worse than the later ones. The fit() loss value ends up pretty small but the evaluate() loss will be drastically higher because of the averaging of the first large losses.

- [why-is-my-training-loss-much-higher-than-my-testing-loss (keras.io)](https://keras.io/getting_started/faq/#why-is-my-training-loss-much-higher-than-my-testing-loss)
- [model.evaluate() gives a different loss on training data from the one in training process (github.com)](https://github.com/keras-team/keras/issues/6977)

### predict

### model.layers

```py
model.layers
```

## Layers

- [layers (tensorflow.org](https://www.tensorflow.org/api_docs/python/tf/keras/layers)

### Layer

```py
layer.get_config()  # Returns the config of the layer.
layer.get_weights() # Returns the current weights of the layer.
layer.set_weights() # Set layer weights.
```

- [Layer (tensorflow.org)](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Layer#attributes_1)

### Flatten

Flattens the input. Does not affect the batch size.

- [keras flatten](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Flatten)

### Dense

```py
from tf.keras.layers import Dense
```

| Arguments            | Default          | Description                       |
| :---                 | ---              | ---                               |
| units                |                  | Positive integer, dimensionality of the output space. |
| activation           | None             | Activation function to use. If you don't specify anything, no activation is applied (ie. "linear" activation: a(x) = x).|
| use_bias             | True             | Boolean, whether the layer uses a bias vector. |
| kernel_initializer   | 'glorot_uniform' | Initializer for the kernel weights matrix. |
| bias_initializer     | 'zeros'          | Initializer for the bias vector.  |
| kernel_regularizer   | None             | Regularizer function applied to the kernel weights matrix. |
| bias_regularizer     | None             | Regularizer function applied to the bias vector. |
| activity_regularizer | None             | Regularizer function applied to the output of the layer (its "activation"). |
| kernel_constraint    | None             | Constraint function applied to the kernel weights matrix. |
| bias_constraint      | None             | Constraint function applied to the bias vector.  |
| `**kwargs`           |                  |                                   |

- [Dense (tensorflow.org)](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Dense)

### Embedding

- [Embedding (tensorflow)](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Embedding)
- [embdedding (keras)](https://keras.io/api/layers/core_layers/embedding/)

### Masking

```py
from tf.keras.layers import Masking

Masking(mask_value=0.0, **kwargs)
```

- [Masking](https://keras.io/api/layers/core_layers/masking/)

### SimpleRNN

```py
from tensorflow.keras.layers import SimpleRNN
```

- [SimpleRNN (tensorflow.org)](https://www.tensorflow.org/api_docs/python/tf/keras/layers/SimpleRNN)

### RNN

```py
from tf.keras.layers import RNN
```

| Arguments        | Def   | Description |
| :---             | ---   | ---         |
| cell             |       | A RNN cell instance or a list of RNN cell instances. A RNN cell is a class that has: |
| return_sequences | False |
| return_state     | False |
| go_backwards     | False |
| stateful         | False | Boolean (default False). If True, the last state for each sample at index i in a batch will be used as initial state for the sample of index i in the following batch. |
| unroll           | False |
| time_major       | False |
| `**kwargs`       |       |

**To enable statefulness**:

- Specify `stateful=True` in the layer constructor.
- Specify a fixed batch size for your model, by passing
  If sequential model:
    `batch_input_shape=(batch_size, timesteps, data_dim)` to the first layer in your model.
  Else for functional model with 1 or more Input layers:
    `batch_shape=(...)` to all the first layers in your model.
  This is the expected shape of your inputs
  *including the batch size*.
  It should be a tuple of integers, e.g. `(32, 10, 100)`.
- Specify `shuffle=False` when calling `fit()`

- [keras RNN (tensorflow.org)](https://www.tensorflow.org/api_docs/python/tf/keras/layers/RNN)

### LSTM

```py
from tf.keras.layers import LSTM
```

| Arguments             | Defaults         |
| :---:                 | :---:            |
| units                 |                  |
| activation            | 'tanh'           |
| recurrent_activation  | 'sigmoid'        |
| use_bias              | True             |
| kernel_initializer    | 'glorot_uniform' |
| recurrent_initializer | 'orthogonal'     |
| bias_initializer      | 'zeros'          |
| unit_forget_bias      | True             |
| kernel_regularizer    | None             |
| recurrent_regularizer | None             |
| bias_regularizer      | None             |
| activity_regularizer  | None             |
| kernel_constraint     | None             |
| recurrent_constraint  | None             |
| bias_constraint       | None             |
| dropout               | 0.0              |
| recurrent_dropout     | 0.0              |
| return_sequences      | False            |
| return_state          | False            |
| go_backwards          | False            |
| stateful              | False            |
| time_major            | False            |
| unroll                | False            |
| `**kwargs`            |                  |

- [keras LSTM (tensorflow.org)](https://www.tensorflow.org/api_docs/python/tf/keras/layers/LSTM)

### TimeDistributed

```py
from tf.keras.layers import TimeDistributed

TimeDistributed(Dense)
```

- [TimeDistributed](https://keras.io/api/layers/recurrent_layers/time_distributed/)

## Model training APIs

- [Model training APIs](https://keras.io/api/models/model_training_apis/)

## Activations

| Activation func.  | Description                                                              |
| :---              | ---                                                                      |
| elu(...)          | Exponential Linear Unit.                                                 |
| exponential(...)  | Exponential activation function.                                         |
| gelu(...)         | Applies the Gaussian error linear unit (GELU) activation function.       |
| hard_sigmoid(...) | Hard sigmoid activation function.                                        |
| linear(...)       | Linear activation function (pass-through).                               |
| relu(...)         | Applies the rectified linear unit activation function.                   |
| selu(...)         | Scaled Exponential Linear Unit (SELU).                                   |
| sigmoid(...)      | Sigmoid activation function, sigmoid(x) = 1 / (1 + exp(-x)).             |
| softmax(...)      | Softmax converts a real vector to a vector of categorical probabilities. |
| softplus(...)     | Softplus activation function, softplus(x) = log(exp(x) + 1).             |
| softsign(...)     | Softsign activation function, softsign(x) = x / (abs(x) + 1).            |
| swish(...)        | Swish activation function, swish(x) = x * sigmoid(x).                    |
| tanh(...)         | Hyperbolic tangent activation function.                                  |

- [Activations (tensorflow.org)](https://www.tensorflow.org/api_docs/python/tf/keras/activations)
- [What is the Softmax Function? (deepai.org)](https://deepai.org/machine-learning-glossary-and-terms/softmax-layer#:~:text=The%20softmax%20function%20is%20a,can%20be%20interpreted%20as%20probabilities.)

## Losses

- MeanSquaredError()
- KLDivergence()
- CosineSimilarity()
- ...

- [losses (tensorflow.org)](https://www.tensorflow.org/api_docs/python/tf/keras/losses)
- [losses (keras)](https://keras.io/api/losses/)
    - [probabilistic_losses (keras)](https://keras.io/api/losses/probabilistic_losses/)

### BinaryCrossentropy

Suitable for binary classification, or multi-label classification.

**Label smoothing**

e.g. [0, 1, 0] -> [0.01, 0.98, 0.01]

A way to overcome overfitting (not be so sure about the prediction).

- [binary_crossentropy (tensorflow.org)](https://www.tensorflow.org/api_docs/python/tf/keras/losses/binary_crossentropy)
- [BinaryCrossentropy (tensorflow.org)](https://www.tensorflow.org/api_docs/python/tf/keras/losses/BinaryCrossentropy)
- [label-smoothing (pyimagesearch.com)](https://www.pyimagesearch.com/2019/12/30/label-smoothing-with-keras-tensorflow-and-deep-learning/)
- [tf.keras.backend.binary_crossentropy](http://man.hubwiz.com/docset/TensorFlow.docset/Contents/Resources/Documents/api_docs/python/tf/keras/backend/binary_crossentropy.html)

### CategoricalCrossentropy

Suitable for multi-class classification.

- [CategoricalCrossentropy (tensorflow.org)](https://www.tensorflow.org/api_docs/python/tf/keras/losses/CategoricalCrossentropy)

### Optimizers

| Optimizer | Description                                       |
| :---:     | ---                                               |
| Adadelta  | Optimizer that implements the Adadelta algorithm. |
| Adagrad   | Optimizer that implements the Adagrad algorithm.  |
| Adam      | Optimizer that implements the Adam algorithm.     |
| Adamax    | Optimizer that implements the Adamax algorithm.   |
| Ftrl      | Optimizer that implements the FTRL algorithm.     |
| Nadam     | Optimizer that implements the NAdam algorithm.    |
| RMSprop   | Optimizer that implements the RMSprop algorithm.  |
| SGD       | Gradient descent (with momentum) optimizer.       |

- [optimizers (tensorflow.org)](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers)
- [optimizers](https://keras.io/api/optimizers/)

## Metrics

- AUC()
- BinaryAccuracy()
- Precision()
- Recall()
- ...

```py
model.compile(metrics=[keras.metrics.SparseCategoricalAccuracy()])
```

- [metrics (tensorflow.org)](https://www.tensorflow.org/api_docs/python/tf/keras/metrics)

### BinaryAccuracy

| Arguments | Def               | Description                         |
| :---      | ---               | ---                                 |
| name      | 'binary_accuracy' | String name of the metric instance. |
| dtype     | None              | Data type of the metric result.     |
| threshold | 0.5               | Float representing the threshold for deciding whether prediction values are 1 or 0. |

- [BinaryAccuracy](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/BinaryAccuracy)

## Utils

```py
int_labels = [1,0,2]
cat = keras.utils.to_categorical(int_labels, num_classes=3)

cat # array([[0., 1., 0.], [1., 0., 0.], [0., 0., 1.]], dtype=float32)
```

- [to_categorical](https://www.tensorflow.org/api_docs/python/tf/keras/utils/to_categorical)

## Theano

- [basic (theano)](https://theano.readthedocs.io/en/rel-0.6rc3/library/tensor/basic.html)

```py
tf.executing_eagerly()
model.compile(loss=loss_function, optimizer='rmsprop', run_eagerly=True)

# Sum dot product of two vectors, convert the result to numpy array
np.array(Th.sum((y_pred * skill).numpy(), axis=2, acc_dtype='float32', dtype='float32'))
```

