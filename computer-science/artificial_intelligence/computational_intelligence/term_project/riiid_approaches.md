# Approaches

## Contents

## Introduction

There are already multiple solutions on Kaggle utilizing many different approaches with similar results. I list here the best result for every approach of the open notebooks.

- [Decision Trees ~ 0.783](https://lightgbm.readthedocs.io/en/latest/)
    - [0.783 Fork of Riiid LGBM bagging2.1 471152](https://www.kaggle.com/julianguo/fork-of-riiid-lgbm-bagging2-1-471152)
- Logistic regression ~ 0.754
    - [0.754 Mike simple predictor](https://www.kaggle.com/mikel1/mike-simple-predictor)
- [Feed Forward Neural Network (FFN) ~ 0.767](https://docs.fast.ai/tabular.learner.html)
    - [0.767 Fastai Tabular with State](https://www.kaggle.com/gannonreynolds/fastai-tabular-with-state)
- [Attention ~ 0.771](https://pytorch.org/docs/stable/generated/torch.nn.MultiheadAttention.html)
    - [0.771 SAKT with Randomization & State Updates](https://www.kaggle.com/leadbest/sakt-with-randomization-state-updates)
- [Ensemble: Attention + Trees ~ 0.781](https://www.kaggle.com/satorushibata/optimized-lightgbm-with-optuna-adding-sakt-model)

## RNN

Start with a simple RNN time series prediction of `(student_id, task_id, was_correct)`.
This approach was published in paper [Deep Knowledge Tracing](https://proceedings.neurips.cc/paper/2015/file/bac9162b47c56fc8a4d2a519803d51b3-Paper.pdf), this is their lua implementation: [DeepKnowledgeTracing (github)](https://github.com/chrispiech/DeepKnowledgeTracing). For my purpose more handy was the tensorflow implementation [dkt git project](https://github.com/mmkhajah/dkt/blob/master/dkt.py) published in paper [How Deep is Knowledge Tracing?](https://arxiv.org/pdf/1604.02416.pdf).

