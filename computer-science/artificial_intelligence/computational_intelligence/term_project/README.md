# Riiid! Answer Correctness Prediction

`2021 Jan 09, Jaroslav Langer`

## Contents

- [Competition](#competition)
  - [Rules](#rules)
  - [Evaluation](#evaluation)
  - [Code requirements](#code-requirements)
  - [Data description](#data-description)
  - [Competition API Detailed Introduction](#competition-api-detailed-introduction)
  - [Winning Model Documentation Guidelines](#winning-model-documentation-guidelines)
- [References](#references)
- [Literature](#literature)
- [Terminology](#terminology)
- [Exploratory Data Analysis](#exploratory-data-analysis)
- [Models](#models)
  - [Decision Tree](#decision-tree)
  - [Boosting](#boosting)
  - [Logistic regression](#logistic-regression)
  - [Feed Forward Neural Network (FFN)](#feed-forward-neural-network-ffn)
  - [Recurrent Neural Network (RNN)](#recurrent-neural-network-rnn)
  - [Attention](#attention)

## Competition

### Rules

- [riiid rules](https://www.kaggle.com/c/riiid-test-answer-prediction/rules)

### Evaluation

- AOC

### Code requirements

- CPU Notebook <= 9 hours run-time
- GPU Notebook <= 9 hours run-time
- TPU Notebook <= 3 hours run-time
- Freely & publicly available external data is allowed, including pre-trained models
- Submission file must be named submission.csv

### Data description

- [Dataset](https://www.kaggle.com/c/riiid-test-answer-prediction/data)
    - [Parts](https://www.iibc-global.org/english/toeic/test/lr/about/format.html)

### Competition API Detailed Introduction

- [API introduction notebook](https://www.kaggle.com/sohier/competition-api-detailed-introduction)

### Winning Model Documentation Guidelines

- [Winning Model Documentation Guidelines](https://www.kaggle.com/WinningModelDocumentationGuidelines)

## References

- [Pytorch NN](https://pytorch.org/docs/stable/nn.html)
- [masking_and_padding (keras)](https://www.tensorflow.org/guide/keras/masking_and_padding)
    - [masking input shape](https://stackoverflow.com/questions/46982616/batch-input-shape-tuple-on-keras-lstm)
- [Our implementation of the LSTM version of Deep Knowledge Tracing (DKT)](https://github.com/mmkhajah/dkt)
- [deep knowledge tracing / tensorflow implement](https://github.com/jiangxinyang227/dkt)
- [An implementation of the Deep Knowledge Tracing (DKT) using Tensorflow 2.0](https://github.com/lccasagrande/Deep-Knowledge-Tracing)
- [Olszewski & Otmianowski: How to efficiently model learner’s knowledge with... | PyData Warsaw 2019](https://www.youtube.com/watch?v=CzRmRZNpB1Y)

## Literature

- [2013 ad-click-prediction (FTRL)](https://www.eecs.tufts.edu/~dsculley/papers/ad-click-prediction.pdf)
- [2015 Deep Knowledge Tracing](https://papers.nips.cc/paper/2015/hash/bac9162b47c56fc8a4d2a519803d51b3-Abstract.html)
- [2016 How Deep is Knowledge Tracing?](https://arxiv.org/pdf/1604.02416.pdf)
    - [Deep Knowledge Tracing Implementation (github)](https://github.com/mmkhajah/dkt)
- [2019 LSTM Optimizer Choice ? (LSTM Optimizer Choice ?)](https://deepdatascience.wordpress.com/2016/11/18/which-lstm-optimizer-to-use/)
- [2017 How to Update LSTM Networks During Training for Time Series Forecasting (machinelearningmastery.com)](https://machinelearningmastery.com/update-lstm-networks-training-time-series-forecasting/)
- [2017 How to use Different Batch Sizes when Training and Predicting with LSTMs (machinelearningmastery.com)](https://machinelearningmastery.com/use-different-batch-sizes-training-predicting-python-keras/)
- [2017 Attention Is All You Need](https://arxiv.org/pdf/1706.03762.pdf)
- [2018 Does Deep Knowledge Tracing Model Interactions Among Skills?](https://par.nsf.gov/biblio/10157351)
- [2018 Deep Knowledge Tracing and Dynamic Student Classification for Knowledge Tracing](https://arxiv.org/pdf/1809.08713.pdf)
- [2018 SAINT+: Integrating Temporal Features for EdNet Correctness Prediction](https://arxiv.org/pdf/2010.12042.pdf)
- [2019 Understand the Impact of Learning Rate on Neural Network Performance (machinelearningmastery.com)](https://machinelearningmastery.com/understand-the-dynamics-of-learning-rate-on-deep-learning-neural-networks/)
- [2019 A Self-Attentive model for Knowledge Tracing](https://arxiv.org/abs/1907.06837)
- [2019 Why Deep Knowledge Tracing Has Less Depth than Anticipated](https://eric.ed.gov/?id=ED599227)
- [2019 settings Open AccessArticle Predicting Student Achievement Based on Temporal Learning Behavior in MOOCs](https://www.mdpi.com/2076-3417/9/24/5539/htm)
- [2020 Time Series Forecasting with Deep Learning and Attention Mechanism](https://towardsdatascience.com/time-series-forecasting-with-deep-learning-and-attention-mechanism-2d001fc871fc)
- [2020 RNN-based Online Learning: An Efficient First-Order Optimization Algorithm with a Convergence Guarantee](https://arxiv.org/pdf/2003.03601v1.pdf)
- [2020 A Novel Approach for Knowledge State Representation and Prediction](https://dl.acm.org/doi/10.1145/3386527.3406745)
- [2020 Interpretable Personalized Knowledge Tracing and Next Learning Activity Recommendation](https://dl.acm.org/doi/10.1145/3386527.3406739)
- [2020 Cold Start Knowledge Tracing with Attentive Neural Turing Machine](https://assets.amazon.science/99/cf/0737f44b4de2bf41e7a8767a0858/cold-start-knowledge-tracing-with-attentive-neural-turing-machine.pdf)

## Terminology

| Abbr. | Name                                         | Description                |
| :---: | ---                                          | ---                        |
| EDM   | Educational Data Mining                      |                            | 
| KT    | Knowledge Tracing                            |                            |
| BKT   | Bayesian Knowledge Tracing                   |                            |
| DKT   | Deep Knowledge Tracing                       |                            |
| KC    | Knowledge Concept                            |                            |
|       | Knowledge state                              |                            |
|       |                                              | $X = (x_1, x_2, ..., x_t)$ |
|       |                                              | $x_t = (e_t, r_t)$         |
|       |                                              | $p(r_{t+1}=1|e_{t+1}, X)$  |
| DKVMN | Dynamic Key-value Memory Network             |                            |
| SAKT  | A self-Attentive model for Knowledge Tracing |                            |
| DSP   | discriminative sequential pattern            |                            |
| CCS   | Computing Classification System              |                            |

## Exploratory Data Analysis

- [Tutorial on reading large datasets](https://www.kaggle.com/rohanrao/tutorial-on-reading-large-datasets)
- [comprehensive eda + baseline](https://www.kaggle.com/erikbruin/riiid-comprehensive-eda-baseline)

## Models

### Decision Tree

- [0.753 Expanding on Simple LGBM](https://www.kaggle.com/dwit392/expanding-on-simple-lgbm#Modeling)
    - [LightGBM](https://lightgbm.readthedocs.io/en/latest/)
- [0.758 Riiid! LGBM Starter](https://www.kaggle.com/shoheiazuma/riiid-lgbm-starter)
    - [LightGBM](https://lightgbm.readthedocs.io/en/latest/)
- [0.766 Riiid! Training and Prediction using a state](https://www.kaggle.com/markwijkhuizen/riiid-training-and-prediction-using-a-state)
    - [LightGBM](https://lightgbm.readthedocs.io/en/latest/)

### Boosting

- [0.704 Answer Correctness - RAPIDS crazy fast](https://www.kaggle.com/andradaolteanu/answer-correctness-rapids-crazy-fast)
    - [XGBoost](https://xgboost.readthedocs.io/en/latest/)

### Logistic regression

- [0.754 Mike simple predictor](https://www.kaggle.com/mikel1/mike-simple-predictor)
- [0.740 RIIID: FTRL FTW !](https://www.kaggle.com/rohanrao/riiid-ftrl-ftw)
    - [FTRL](https://datatable.readthedocs.io/en/v0.10.1/ftrl.html)

### Feed Forward Neural Network (FFN)

- [????? Riiid:Super Cool EDA and Pytorch Baseline](https://www.kaggle.com/maunish/riiid-super-cool-eda-and-pytorch-baseline#Pytorch-Baseline-Model-%F0%9F%94%A5)
    - [torch.nn.BatchNorm1d](https://pytorch.org/docs/stable/generated/torch.nn.BatchNorm1d.html)
    - [torch.nn.Linear](https://pytorch.org/docs/stable/generated/torch.nn.Linear.html)
- [0.751 Fastai Single NN](https://www.kaggle.com/gilfernandes/fastai-single-nn)
    - [Fastai Tabular learner](https://docs.fast.ai/tabular.learner.html)
- [0.767 Fastai Tabular with State](https://www.kaggle.com/gannonreynolds/fastai-tabular-with-state)
    - [Fastai Tabular learner](https://docs.fast.ai/tabular.learner.html)

### Recurrent Neural Network (RNN)

- Also called Feedback Neural Network (FNN)

- [Riid Answer Correctness with RNN](https://www.kaggle.com/gianzlupko/riid-answer-correctness-with-rnn)

### Attention

- [0.771 SAKT with Randomization & State Updates](https://www.kaggle.com/leadbest/sakt-with-randomization-state-updates)
- [0.765 A self-Attentive model for Knowledge Tracing](https://www.kaggle.com/wangsg/a-self-attentive-model-for-knowledge-tracing)
    - [torch.nn.Embedding](https://pytorch.org/docs/stable/generated/torch.nn.Embedding.html)
    - [torch.nn.MultiheadAttention](https://pytorch.org/docs/stable/generated/torch.nn.MultiheadAttention.html)
- [0.541 SAKT Self-Attentive Knowledge Tracing Submitter](https://www.kaggle.com/leadbest/sakt-self-attentive-knowledge-tracing-submitter/comments)

